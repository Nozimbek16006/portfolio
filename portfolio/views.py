from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ContactForm
from .models import Article, Project, ContactMessage
from django.db import models
import uuid


response = models.TextField(
    blank=True,
    default="",
    verbose_name="Javob"
)

def base_context():
    return {
        "developer": {
            "name": "Nozimbek Azamov",
            "role": "Full-Stack Developer",
            "location": "Uzbekistan",
            "education": "Acharya University, India",
            "status": "active",
        },
        "skills": [
            "Python", "Django", "JavaScript", "HTML", "CSS",
            "C", "C++", "Bootstrap", "Git & GitHub",
            "Telegram Bots", "Firebase", "Linux"
        ],
    }


def home(request):
    context = base_context()
    context["projects"] = Project.objects.all()[:6]
    context["articles"] = Article.objects.all()[:5]
    context["project_count"] = Project.objects.count()
    context["article_count"] = Article.objects.count()
    return render(request, "portfolio/home.html", context)


def about(request):
    context = base_context()
    return render(request, "portfolio/about.html", context)


def projects(request):
    context = base_context()
    context["projects"] = Project.objects.all()
    return render(request, "portfolio/projects.html", context)


def articles(request):
    context = base_context()
    context["articles"] = Article.objects.all()
    return render(request, "portfolio/articles.html", context)


def article_detail(request, slug):
    context = base_context()
    context["article"] = get_object_or_404(Article, slug=slug)
    return render(request, "portfolio/article_detail.html", context)


def contact(request):
    context = base_context()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Xabaringiz muvaffaqiyatli yuborildi.")
            return redirect("portfolio:contact")
    else:
        form = ContactForm()
    context["form"] = form
    return render(request, "portfolio/contact.html", context)

def contact(request):
    context = base_context()

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            contact_message = form.save()
            messages.success(
                request,
                "Savolingiz yuborildi. Javobni kuzatish uchun sahifani oching."
            )
            return redirect(
                "portfolio:message_status",
                # token=contact_message.token
            )
    else:
        form = ContactForm()

    context["form"] = form
    return render(request, "portfolio/contact.html", context)


def message_status(request):
    contact_message = ContactMessage.objects.all()

    return render(
        request,
        "portfolio/message_status.html",{"responses": contact_message})