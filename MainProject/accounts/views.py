from django.shortcuts import render,redirect
from django.views import View
from .forms import *
from django.contrib.auth import login,authenticate

class Login(View):
    def get(self,request):
        form = LoginForm() 
        return render(request,'accounts/login.html',{'form': form})
    def post(self,request):
            form  = LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(request=request,username = form.cleaned_data['username'], 
                                password= form.cleaned_data['password'])
                if user :
                    login(request,user)
                    return redirect("register")
            return render(request,'accounts/login.html',{'form': form})

class Register(View):
    def get(self,request):
        form = RegisterForm()
        return render(request,'accounts/register.html',{'form': form})
    def post(self,request):
        form  = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect("login")
        else:
            return render(request,'accounts/register.html',{'form': form})
