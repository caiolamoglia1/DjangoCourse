from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import transaction
from django.shortcuts import redirect, render

from .forms import CustomLoginForm, CustomUserRegistrationForm
from .models import Article


# Página inicial (home)
def home_page(request):
    return render(request, "core/home_page.html")


# Página de artigos
def artigos(request):
    articles = Article.objects.all().order_by("-published_at")
    return render(request, "core/artigos.html", {"articles": articles})


# Página sobre
def sobre(request):
    return render(request, "core/sobre.html")


# Página contato
def contato(request):
    return render(request, "core/contato.html")


# Página recursos
def recursos(request):
    return render(request, "core/recursos.html")


# Página cadastro melhorada
def cadastro(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = CustomUserRegistrationForm()

    if request.method == "POST":
        form = CustomUserRegistrationForm(request.POST)

        if form.is_valid():
            try:
                with transaction.atomic():
                    # Validar senha
                    password = form.cleaned_data["password"]
                    validate_password(password)

                    # Criar usuário
                    user = form.save()

                    messages.success(
                        request,
                        f"Conta criada com sucesso! Bem-vindo, "
                        f"{user.first_name or user.username}! 🎉",
                    )

                    # Fazer login automático
                    login(request, user)
                    return redirect("home")

            except ValidationError as e:
                messages.error(request, f'Erro na senha: {", ".join(e.messages)}')
            except Exception:
                messages.error(request, "Erro ao criar conta. Tente novamente.")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{form.fields[field].label}: {error}")

    context = {
        "form": form,
        "show_login_link": True,
    }
    return render(request, "core/cadastro.html", context)


# Página de login melhorada
def login_page(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = CustomLoginForm()

    if request.method == "POST":
        form = CustomLoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Verificar se deve lembrar do usuário
            remember_me = form.cleaned_data.get("remember_me")
            if remember_me:
                request.session.set_expiry(1209600)  # 2 semanas
            else:
                request.session.set_expiry(0)  # Expira quando o navegador fechar

            messages.success(request, f"Bem-vindo de volta, {user.first_name or user.username}! 🎉")

            # Redirecionar para a página solicitada ou home
            next_page = request.GET.get("next", "home")
            return redirect(next_page)
        else:
            messages.error(request, "Credenciais inválidas. Verifique seu usuário/email e senha.")

    context = {
        "form": form,
        "show_register_link": True,
    }
    return render(request, "core/login.html", context)


# Logout
@login_required
def logout_page(request):
    username = request.user.username
    logout(request)
    messages.success(request, f"Até logo, {username}! Você foi desconectado com sucesso!")
    return redirect("home")
