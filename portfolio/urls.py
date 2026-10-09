from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("projects/", views.projects, name="projects"),
    path("articles/", views.articles, name="articles"),
    path("articles/<slug:slug>/", views.article_detail, name="article_detail"),
    path("contact/", views.contact, name="contact"),
]
