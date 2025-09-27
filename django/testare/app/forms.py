from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Firma, Cont, Operatiune

class FirmaForm(forms.ModelForm):
    class Meta:
        model = Firma
        fields = ['nume']
        widgets = {
            'nume': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numele firmei'})
        }

class SignUpForm(forms.Form):
    username = forms.CharField(
        max_length=150, 
        required=True, 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Utilizator'
        })
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Parolă'
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        })
    )
    nume = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nume firmă'
        })
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("Acest username există deja.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Acest email este deja folosit.")
        return email

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email']
        )
        firma = Firma.objects.create(
            user=user, 
            nume=self.cleaned_data['nume']
        )
        return user

class OperatiuneForm(forms.ModelForm):
    class Meta:
        model = Operatiune
        fields = ['data', 'cont_debit', 'cont_credit', 'suma', 'descriere']
        widgets = {
            'data': forms.DateInput(attrs={
                'type': 'date', 
                'class': 'form-control',
                'placeholder': 'Selectează data'
            }),
            'descriere': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3,
                'placeholder': 'Descriere operațiune'
            }),
            'suma': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Suma (ex: 1000.00)'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cont_debit'] = forms.ModelChoiceField(
            queryset=Cont.objects.all().order_by('numar'),
            widget=forms.Select(attrs={'class': 'form-control'}),
            label="Cont Debit"
        )
        self.fields['cont_credit'] = forms.ModelChoiceField(
            queryset=Cont.objects.all().order_by('numar'),
            widget=forms.Select(attrs={'class': 'form-control'}),
            label="Cont Credit"
        )
        
        # Custom labels for accounts
        self.fields['cont_debit'].label_from_instance = lambda obj: f"{obj.numar} – {obj.nume}"
        self.fields['cont_credit'].label_from_instance = lambda obj: f"{obj.numar} – {obj.nume}"

