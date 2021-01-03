from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Containt
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages


def index(request):
    items = Containt.objects.all()
    return render(request,'index.html',{'Item': items})


def singupuser(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        #error


        if len(username)>10:
            messages.error(request, "Username cannot be more than 10 words.")
            return redirect('index')

        elif pass1 != pass2:
            messages.error(request, "Passwords should be equal.")
            return redirect('index')

        #create user
        myuser = User.objects.create_user(username,email,pass2)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Account Successfully Created")
        return redirect('index')

    else:
        return HttpResponse("404-Error")

def login(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request)
            messages.success(request, "Successfully Logged In")
            return redirect("index")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("index")

    return HttpResponse("404- Not found")

def logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('index')

def search(request):
    query=request.GET['query']
    allPosts= Post.objects.filter(title__icontains=query)
    parameter={'allPosts': allPosts}
    return render(request, 'index/search.html', parameter)