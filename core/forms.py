from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import UserProfile


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite seu usuário ou email",
                "id": "username",
                "autocomplete": "username",
            }
        ),
        label="Usuário ou Email",
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha",
                "id": "password",
                "autocomplete": "current-password",
            }
        ),
        label="Senha",
    )
    remember_me = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-check-input",
                "id": "remember",
            }
        ),
        label="Lembrar de mim",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"autofocus": True})

    def clean_username(self):
        username = self.cleaned_data.get("username")
        # Permitir login com email
        if "@" in username:
            try:
                user = User.objects.get(email=username)
                return user.username
            except User.DoesNotExist:
                pass
        return username


class CustomUserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": " ",  # Espaço em branco para floating labels
                "autocomplete": "new-password",
                "required": True,
            }
        ),
        label="Senha",
        required=True,
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": " ",  # Espaço em branco para floating labels
                "autocomplete": "new-password",
                "required": True,
            }
        ),
        label="Confirmar Senha",
        required=True,
    )
    terms = forms.BooleanField(
        required=False,  # Removendo obrigatoriedade até criarmos as páginas
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-check-input",
                "id": "terms",
            }
        ),
        label="Aceito os Termos de Uso e Política de Privacidade",
        initial=True,  # Marcar por padrão
    )
    newsletter = forms.BooleanField(
        required=False,
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-check-input",
                "id": "newsletter",
            }
        ),
        label="Quero receber dicas exclusivas e novidades por email",
    )

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": " ",  # Espaço em branco para floating labels
                    "autocomplete": "username",
                    "required": True,
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": " ",  # Espaço em branco para floating labels
                    "autocomplete": "email",
                    "required": True,
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": " ",  # Espaço em branco para floating labels
                    "autocomplete": "given-name",
                    "required": True,
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": " ",  # Espaço em branco para floating labels
                    "autocomplete": "family-name",
                    "required": True,
                }
            ),
        }
        labels = {
            "username": "Nome de Usuário",
            "email": "Email",
            "first_name": "Primeiro Nome",
            "last_name": "Sobrenome",
        }

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("As senhas não coincidem.")

        return password_confirm

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está em uso.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class AvatarUploadForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["avatar"]
        widgets = {
            "avatar": forms.FileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/*",
                    "id": "avatar-upload",
                    "name": "avatar",
                }
            )
        }

    def clean_avatar(self):
        avatar = self.cleaned_data.get("avatar")
        if avatar:
            if avatar.size > 5 * 1024 * 1024:  # 5MB
                raise forms.ValidationError("A imagem deve ter no máximo 5MB.")

            # Verificar se é uma imagem válida
            try:
                from PIL import Image

                img = Image.open(avatar)
                img.verify()
                # Reset file pointer after verify
                avatar.seek(0)
            except Exception as e:
                print(f"❌ Image validation error: {e}")
                raise forms.ValidationError("Arquivo deve ser uma imagem válida.") from e

        return avatar


class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": " "}),
        label="Nome",
    )

    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": " "}),
        label="Sobrenome",
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": " "}), 
        label="Email"
    )

    phone = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": " "}),
        label="Telefone",
    )

    birth_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date", "placeholder": " "}),
        label="Data de Nascimento",
    )

    class Meta:
        model = UserProfile
        fields = ["bio", "location", "birth_date"]
        widgets = {
            "bio": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": " "}),
            "location": forms.TextInput(attrs={"class": "form-control", "placeholder": " "}),
            "birth_date": forms.DateInput(attrs={"class": "form-control", "type": "date", "placeholder": " "}),
        }
        labels = {
            "bio": "Biografia", 
            "location": "Localização",
            "birth_date": "Data de Nascimento",
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields["first_name"].initial = user.first_name
            self.fields["last_name"].initial = user.last_name
            self.fields["email"].initial = user.email
            
            # Se há uma instância (profile), preencher os campos
            if self.instance and self.instance.pk:
                self.fields["birth_date"].initial = self.instance.birth_date

    def save(self, commit=True):
        profile = super().save(commit=False)

        if commit:
            # Atualizar dados do usuário também
            user = profile.user
            user.first_name = self.cleaned_data["first_name"]
            user.last_name = self.cleaned_data["last_name"]
            user.email = self.cleaned_data["email"]
            user.save()
            
            # Salvar os dados do perfil
            profile.birth_date = self.cleaned_data["birth_date"]
            profile.save()

        return profile
