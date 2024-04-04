from django.db import models

# Create your models here.

class News(models.Model):
    palace = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True, unique=True)
    game_count = models.IntegerField(null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан в")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено в")

    def __str__(self):
        return self.name


class OlxHome(models.Model):
    name = models.CharField(max_length=1024, null=True, blank=True, unique=True, verbose_name="E'lon")
    summHome = models.CharField(max_length=1024, null=True, blank=True, verbose_name="Uyning narxi")
    accept = models.CharField(max_length=1024, null=True, blank=True, verbose_name="Kelishish")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqti")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "E'lon"
        verbose_name_plural = "E'lonlar"