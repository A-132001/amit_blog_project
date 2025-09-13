from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from .forms import RegisterForm,UpdateUserFrom
def login_view(req):
    if req.method == "POST":
        form = AuthenticationForm(data=req.POST)
        if form.is_valid():
            user = form.get_user()
            login(req,user)
            return redirect("posts")
    else:
        form = AuthenticationForm()
    return render(req,'accounts/login.html',{"form":form})

def logout_view(req):
    logout(req)
    return redirect("posts")
    
def register_view(req):
    if req.method == "POST":
        form = RegisterForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req,user)
            return redirect("posts")
    else:
        form = RegisterForm()
    return render(req,'accounts/register.html',{"form":form})

def update_user_view(req):
    if req.method == "POST":
        form = UpdateUserFrom(req.POST,instance=req.user)
        if form.is_valid():
            form.save()
            return redirect("posts")
    else:
        form = UpdateUserFrom(instance=req.user)
    return render(req,"accounts/update_user.html",{"form":form})