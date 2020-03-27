from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, get_user_model

from .forms import ContactForm, LoginForm, RegisterForm

User = get_user_model()

def home_page(request):
    context = {
        "title": "Hello world",
        "content": "Welcome",
        "premium_content": "Yeahhhh"
    }
    return render(request, 'home_page.html', context)

def about_page(request):
    context = {
        "title": "About page",
        "content": "Welcome !!"
    }
    return render(request, 'home_page.html', {})

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact page",
        "content": "Welcome !",
        "form": contact_form
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    return render(request, 'contact/view.html', context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {"form": form}

    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            pass

    return render(request, 'auth/login.html', context)

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {"form": form}

    if form.is_valid():
        username = form.cleaned_data["username"]
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        new_user = User.objects.create_user(username, email, password)

    return render(request, 'auth/register.html', context)
