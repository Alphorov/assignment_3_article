from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm


def auth_view(request):
    register_form = CustomUserCreationForm()
    login_form = AuthenticationForm(request)

    if request.method == "POST":
        if "register" in request.POST:
            register_form = CustomUserCreationForm(request.POST)
            if register_form.is_valid():
                user = register_form.save()
                login(request, user)
                return redirect("welcome")

        elif "login" in request.POST:
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect("welcome")

    return render(
        request,
        "authentication/auth_page.html",
        {
            "register_form": register_form,
            "login_form": login_form,
        },
    )


@login_required
def welcome_view(request):
    return render(request, "authentication/welcome_page.html", {"user": request.user})

def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('login') 