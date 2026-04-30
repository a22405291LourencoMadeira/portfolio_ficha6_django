from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegistoForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect('portfolio_index')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('portfolio_index')
        else:
            return render(request, 'accounts/login.html', {'erro': 'Credenciais inválidas'})
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def registo_view(request):
    form = RegistoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, 'accounts/registo.html', {'form': form})