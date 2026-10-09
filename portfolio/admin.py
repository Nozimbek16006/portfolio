from django.contrib import admin
from .models import Project, Article, ContactMessage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "featured", "created_at")
    list_filter = ("featured",)
    search_fields = ("title", "description", "technologies")


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "published_at")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "content", "category")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "is_read", "created_at")
    list_filter = ("is_read",)
    search_fields = ("name", "email", "message", "response")

    readonly_fields = (
        "name",
        "email",
        "message",
        "created_at",
    )

    fields = (
        "name",
        "email",
        "message",
        "response",
        "is_read",
        "created_at",
    )