from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import AvatarUploadForm, CustomLoginForm, CustomUserRegistrationForm, UserProfileForm
from .models import Article


# Página inicial (home)
def home_page(request):
    return render(request, "core/home.html")


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
                    form.save()

                    messages.success(
                        request,
                        "Conta criada com sucesso! Agora faça login para continuar.",
                    )

                    # Redirecionar para login
                    return redirect("login")

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


# Página de perfil
@login_required
def perfil(request):
    # Obter ou criar perfil do usuário
    from .models import UserProfile

    profile, created = UserProfile.objects.get_or_create(user=request.user)

    # Formulários
    avatar_form = AvatarUploadForm(instance=profile)
    profile_form = UserProfileForm(instance=profile, user=request.user)

    if request.method == "POST":
        print("=" * 50)
        print("POST REQUEST DEBUGGING")
        print("=" * 50)
        print(f"POST keys: {list(request.POST.keys())}")
        print(f"FILES keys: {list(request.FILES.keys())}")
        print(f"avatar_upload in POST: {'avatar_upload' in request.POST}")
        print(f"profile_update in POST: {'profile_update' in request.POST}")
        print("=" * 50)

        if "avatar_upload" in request.POST:
            print("🔄 PROCESSING AVATAR UPLOAD")
            avatar_form = AvatarUploadForm(request.POST, request.FILES, instance=profile)
            print(f"📁 Files in request: {request.FILES}")
            print(f"✅ Form is valid: {avatar_form.is_valid()}")

            if avatar_form.is_valid():
                print("💾 Saving avatar...")
                old_avatar = profile.avatar
                avatar_form.save()
                print(f"🖼️ Old avatar: {old_avatar}")
                print(f"🖼️ New avatar: {profile.avatar}")
                messages.success(request, "Avatar atualizado com sucesso!")
                return redirect("perfil")
            else:
                print(f"❌ Avatar form errors: {avatar_form.errors}")
                for error in avatar_form.non_field_errors():
                    messages.error(request, error)
                if avatar_form.errors.get("avatar"):
                    messages.error(request, avatar_form.errors["avatar"][0])

        elif "profile_update" in request.POST:
            print("Processing profile update...")
            profile_form = UserProfileForm(request.POST, instance=profile, user=request.user)
            print(f"Profile form is valid: {profile_form.is_valid()}")

            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, "Perfil atualizado com sucesso!")
                return redirect("perfil")
            else:
                print(f"Profile form errors: {profile_form.errors}")
                for field, errors in profile_form.errors.items():
                    for error in errors:
                        messages.error(request, f"{profile_form.fields[field].label}: {error}")

        else:
            print("No recognized form action found!")
            print("Available keys in POST:", list(request.POST.keys()))

    context = {
        "user": request.user,
        "profile": profile,
        "avatar_form": avatar_form,
        "profile_form": profile_form,
    }
    return render(request, "core/perfil.html", context)


# Simple avatar test view
@login_required
def avatar_test(request):
    if request.method == "POST":
        print("🧪 AVATAR TEST - POST REQUEST")
        print(f"POST keys: {list(request.POST.keys())}")
        print(f"FILES keys: {list(request.FILES.keys())}")
        return HttpResponse("Test complete - check terminal output")

    return render(request, "core/avatar_test.html")


# Logout
@login_required
def logout_page(request):
    username = request.user.username
    logout(request)
    messages.success(request, f"Até logo, {username}! Você foi desconectado com sucesso!")
    return redirect("login")
