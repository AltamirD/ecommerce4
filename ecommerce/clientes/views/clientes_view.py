from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import get_user_model, authenticate, logout, login

def criar_cliente(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_created = get_user_model().objects.create(
            email=email,
            # password=password
        )
        user_created.set_password(password)
        user_created.save()
        
        return redirect(reverse('clientes:login'))
    return render(request, 'criar_cliente.html')

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(
            username=email,
            password=password
        )
        if user:
            login(request, user)
            return redirect('produtos:listar_produtos')
        else:
            print("Usuário ou senha inválida.")

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect(reverse('produtos:listar_produtos'))