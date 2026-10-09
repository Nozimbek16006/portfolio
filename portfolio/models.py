from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    technologies = models.CharField(max_length=300, help_text="Vergul bilan ajrating")
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-featured", "-created_at"]

    def tech_list(self):
        return [item.strip() for item in self.technologies.split(",") if item.strip()]

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=180)
    slug = models.SlugField(unique=True)
    excerpt = models.TextField()
    content = models.TextField()
    category = models.CharField(max_length=80, default="Dasturlash")
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.email}"
