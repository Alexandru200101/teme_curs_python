from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import FirmaForm, SignUpForm, OperatiuneForm
from .models import Operatiune, Cont, Firma

# … restul view-urilor rămâne neschimbat …



def index(request):
    return render(request, 'app/index.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Contul a fost creat cu succes! Te poți autentifica.")
            return redirect('login_firma')
    else:
        form = SignUpForm()
    return render(request, 'app/signup.html', {'form': form})


def login_view(request):
    error = ''
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            if user.is_superuser:
                return redirect('dashboard_superuser')
            try:
                _ = user.firma
                return redirect('dashboard_firma')
            except ObjectDoesNotExist:
                error = 'Nu ai un rol asociat.'
        else:
            error = 'Utilizator sau parolă incorecte.'
    return render(request, 'app/login_firma.html', {'error': error})


@login_required
def dashboard_firma(request):
    if not hasattr(request.user, 'firma'):
        return redirect('login_firma')
    return render(request, 'app/dashboard_firma.html', {'firma': request.user.firma})


@login_required
def dashboard_superuser(request):
    if not request.user.is_superuser:
        return redirect('dashboard_firma')
    users = User.objects.all()
    return render(request, 'app/dashboard_superuser.html', {'users': users})


def logout_view(request):
    logout(request)
    return redirect('login_firma')


# -----------------------------
# Operațiuni contabile
# -----------------------------

@login_required
def adauga_operatiune(request):
    firma = request.user.firma
    if request.method == 'POST':
        form = OperatiuneForm(request.POST)
        if form.is_valid():
            operatiune = form.save(commit=False)
            operatiune.firma = firma
            operatiune.save()
            messages.success(request, "Operațiunea a fost adăugată.")
            return redirect('lista_operatiuni')
    else:
        form = OperatiuneForm()
    return render(request, 'app/adauga_operatiune.html', {'form': form})


@login_required
def lista_operatiuni(request):
    operatiuni = Operatiune.objects.filter(firma=request.user.firma).order_by('-data')
    return render(request, 'app/lista_operatiuni.html', {'operatiuni': operatiuni})



























