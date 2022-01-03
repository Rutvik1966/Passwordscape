from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterUserForm
from .models import Contactus
from django.http import HttpResponse


# Create your views here.
def helloworld(request):
    return render(request, "index.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Your account Username or Password is incorrect.😢')
            return redirect('login')
    else:
        return render(request, "login.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, ("Logout Successfully 😊"))
    return redirect('home')


def user_register(request):
    if request.method == "POST":
        forms = RegisterUserForm(request.POST)
        if forms.is_valid():
            forms.save()
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ("User Registered Succefully 😊"))
            return redirect('home')
    else:
        forms = RegisterUserForm()
    return render(request, "register.html", {'form': forms})


def contact_us(request):
    if request.method == "POST":
        mess = request.POST.get('message')
        names = request.POST.get('name')
        emailid = request.POST.get('emails')
        forms = Contactus(message=mess, name=names, email=emailid)
        forms.save()
        messages.success(request,("Thank You for sharing your views with us. We will get back to you as soon as possible. 😊"))
    return render(request,"index.html")
