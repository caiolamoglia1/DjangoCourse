#!/usr/bin/env python
"""
Script para testar o cadastro de usuário
"""
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from core.forms import CustomUserRegistrationForm

def test_signup():
    print("=== Teste de Cadastro ===")
    
    # Dados de teste
    form_data = {
        'username': 'usuario_teste',
        'email': 'teste@exemplo.com',
        'first_name': 'João',
        'last_name': 'Silva',
        'password': 'minhasenha123',
        'password_confirm': 'minhasenha123',
        'terms': True,
        'newsletter': True,
    }
    
    print(f"Dados do formulário: {form_data}")
    
    # Verificar se usuário já existe
    if User.objects.filter(username=form_data['username']).exists():
        print("Usuário já existe, removendo...")
        User.objects.filter(username=form_data['username']).delete()
    
    # Testar formulário
    form = CustomUserRegistrationForm(data=form_data)
    
    print(f"Formulário válido: {form.is_valid()}")
    
    if form.is_valid():
        try:
            user = form.save()
            print(f"✅ Usuário criado com sucesso: {user.username} ({user.email})")
            print(f"✅ Total de usuários no banco: {User.objects.count()}")
            
            # Testar autenticação
            from django.contrib.auth import authenticate
            auth_user = authenticate(username=user.username, password='minhasenha123')
            if auth_user:
                print(f"✅ Autenticação funcionando: {auth_user.username}")
            else:
                print("❌ Falha na autenticação")
                
        except Exception as e:
            print(f"❌ Erro ao salvar usuário: {e}")
    else:
        print(f"❌ Erros do formulário: {form.errors}")

if __name__ == '__main__':
    test_signup()
