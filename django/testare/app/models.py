from django.db import models
from django.contrib.auth.models import User

class Firma(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nume = models.CharField(max_length=100)

    def __str__(self):
        return self.nume

class Cont(models.Model):
    numar = models.CharField(max_length=20, unique=True)
    nume = models.CharField(max_length=255)  # redenumit din `denumire`

    def __str__(self):
        return f"{self.numar} - {self.nume}"

class Operatiune(models.Model):
    firma = models.ForeignKey(Firma, on_delete=models.CASCADE)
    data = models.DateField()
    descriere = models.TextField()
    cont_debit = models.ForeignKey(
        Cont, related_name='operatiuni_debit', on_delete=models.CASCADE
    )
    cont_credit = models.ForeignKey(
        Cont, related_name='operatiuni_credit', on_delete=models.CASCADE
    )
    suma = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.data} – {self.descriere}"













