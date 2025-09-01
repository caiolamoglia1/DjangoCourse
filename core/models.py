# Create your models here.

import os

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from PIL import Image


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(
        upload_to="avatars/", blank=True, null=True, verbose_name="Foto de Perfil"
    )
    bio = models.TextField(max_length=500, blank=True, verbose_name="Biografia")
    location = models.CharField(max_length=100, blank=True, verbose_name="Localização")
    birth_date = models.DateField(blank=True, null=True, verbose_name="Data de Nascimento")
    website = models.URLField(blank=True, verbose_name="Website")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        verbose_name = "Perfil do Usuário"
        verbose_name_plural = "Perfis dos Usuários"

    def __str__(self):
        return f"Perfil de {self.user.username}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Redimensionar a imagem se for muito grande
        if self.avatar:
            img_path = self.avatar.path
            if os.path.exists(img_path):
                with Image.open(img_path) as img:
                    if img.height > 300 or img.width > 300:
                        output_size = (300, 300)
                        img.thumbnail(output_size)
                        img.save(img_path)

    def get_avatar_url(self):
        """Retorna a URL do avatar ou um placeholder se não houver"""
        if self.avatar and hasattr(self.avatar, "url"):
            return self.avatar.url
        return "/static/core/images/default-avatar.png"


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Conteúdo")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Autor", null=True, blank=True
    )
    published_at = models.DateTimeField(auto_now_add=True, verbose_name="Publicado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")
    is_active = models.BooleanField(default=True, verbose_name="Ativo")

    class Meta:
        verbose_name = "Artigo"
        verbose_name_plural = "Artigos"
        ordering = ["-published_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, "profile"):
        instance.profile.save()
    else:
        UserProfile.objects.create(user=instance)
