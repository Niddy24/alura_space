from django.shortcuts import render, redirect
from usuarios.forms import loginForms, cadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login(request):
    form = loginForms()

    if request.method == 'POST':
        form = loginForms(request.POST)
        
        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()

        usuario = auth.authenticate(
            username = nome,
            password = senha,
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f'{nome} Logado Com Sucesso')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao Efetuar Login')
            return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = cadastroForms()
    if request.method == 'POST':
        form = cadastroForms(request.POST)

        if form.is_valid():
            if form['senha_1'].value() != form['senha_2'].value():
                return redirect('cadastro')
            
            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha_2'].value()

            if User.objects.filter(username = nome).exists():
                messages.error(request, 'Usuario Existente')
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username = nome,
                email = email,
                password = senha,
            )
            usuario.save()
            messages.success(request, 'Cadastro Efetuado Com Sucesso')
            return redirect('login')
    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout Efetuado Com Sucesso')
    return redirect('login')
