from django.shortcuts import render,redirect
from django.http import HttpResponse
from account.forms import RegistrationForms
from django.contrib.auth.models import User  
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
# Create your views here.


def Register(request):
    if request.user.is_authenticated:
        return HttpResponse("You are already Authenticated.....")
    else:
        form = RegistrationForms()

        if request.method == 'post' or request.method == 'POST':
            form = RegistrationForms(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')

    context = {
        'form': form,
    }

    return render(request, 'account/register.html',context)


def Login(request):
    if request.user.is_authenticated:
        return HttpResponse("You are already LoggedIn.....")
    else:
        if request.method == "POST" or request.method == "post":
            username = request.POST.get('username')
            password = request.POST.get('password')
            login_user = authenticate(request, username=username, password=password)
            if login_user is not None:
                login(request,login_user)
                return redirect('home')
            else:
                return HttpResponse("404 NOT FOUND")

    return render(request, 'account/login.html')

def Logout(request):
    logout(request)
    return redirect('login')

