from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Project(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Loyiha nomi"
    )
    description = models.TextField(
        verbose_name="Loyiha haqida"
    )
    technologies = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="Texnologiyalar"
    )
    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True,
        verbose_name="Loyiha rasmi"
    )
    project_url = models.URLField(
        blank=True,
        verbose_name="Loyiha havolasi"
    )
    github_url = models.URLField(
        blank=True,
        verbose_name="GitHub havolasi"
    )
    featured = models.BooleanField(
        default=False,
        verbose_name="Asosiy sahifada ko‘rsatish"
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="Yaratilgan vaqt"
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Loyiha"
        verbose_name_plural = "Loyihalar"

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(
        max_length=250,
        verbose_name="Maqola sarlavhasi"
    )
    slug = models.SlugField(
        max_length=270,
        unique=True,
        blank=True,
        verbose_name="URL nomi"
    )
    category = models.CharField(
        max_length=100,
        default="Dasturlash",
        verbose_name="Kategoriya"
    )
    content = models.TextField(
        verbose_name="Maqola matni"
    )
    image = models.ImageField(
        upload_to="articles/",
        blank=True,
        null=True,
        verbose_name="Maqola rasmi"
    )
    published_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="E'lon qilingan vaqt"
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name="Saytda ko‘rsatish"
    )

    class Meta:
        ordering = ["-published_at"]
        verbose_name = "Maqola"
        verbose_name_plural = "Maqolalar"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Ism"
    )
    email = models.EmailField(
        verbose_name="Email"
    )
    message = models.TextField(
        verbose_name="Savol yoki xabar"
    )
    response = models.TextField(
        blank=True,
        default="",
        verbose_name="Javob"
    )

    is_read = models.BooleanField(
        default=False,
        verbose_name="O‘qilgan"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Yuborilgan vaqt"
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Foydalanuvchi xabari"
        verbose_name_plural = "Foydalanuvchi xabarlari"

    def __str__(self):
        return f"{self.name} — {self.email}"