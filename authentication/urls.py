from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("", views.auth_view, name="auth"),
    path("welcome/", views.welcome_view, name="welcome"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
