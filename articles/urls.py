from django.urls import path
from . import views

urlpatterns = [
    path("articles", views.articles_view, name="articles"),
    path("articles/new", views.create_article, name="add_article"),
    path("articles/article/<int:id>/", views.detailed_article, name="detailed_article"),
    path("article/<int:id>/delete/", views.delete_article, name="article_delete"),
    path("article/<int:id>/edit/", views.article_edit, name="article_edit"),
]
