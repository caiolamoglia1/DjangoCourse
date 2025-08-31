# Create your models here.

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


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
