from typing import Any
from django import forms

class loginForms(forms.Form):
    nome_login = forms.CharField(
        label = 'nome de login',
        required = True ,
        max_length = 100 ,
        widget = forms.TextInput(
            attrs = {
                    'class': 'form-control',
                    'placeholder': 'EX:João silva'
            }
        )
    )
    senha = forms.CharField(
        label = 'senha',
        required = True ,
        max_length = 70 ,
        widget = forms.PasswordInput(
            attrs = {
                    'class': 'form-control',
                    'placeholder': 'Digite sua senha',
            }
        )
    )

class cadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label = 'Nome de Cadastro',
        required = True ,
        max_length = 100 ,
        widget = forms.TextInput(
            attrs = {
                    'class': 'form-control',
                    'placeholder': 'EX:João silva'
            }
        )
    )
    email = forms.EmailField(
        label = 'email',
        required = True ,
        max_length = 100 ,
        widget = forms.EmailInput(
            attrs = {
                    'class': 'form-control',
                    'placeholder': 'EX:João_silva@gmail.com'
            }
        )
    )
    senha_1 = forms.CharField(
        label = 'Senha',
        required = True ,
        max_length = 70 ,
        widget = forms.PasswordInput(
            attrs = {
                    'class': 'form-control',
                    'placeholder': 'Digite sua senha',
            }
        )
    )
    senha_2 = forms.CharField(
        label = 'Confirme Sua Senha',
        required = True ,
        max_length = 70 ,
        widget = forms.PasswordInput(
            attrs = {
                    'class': 'form-control',
                    'placeholder': 'Digite Sua Senha Novamente',
            }
        )
    )
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')
        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Não é possivel incerir espaços nesse campo')
            else:
                return nome
    
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')
        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('Senhas não são iguais')
            else:
                return senha_2