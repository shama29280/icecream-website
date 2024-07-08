from django.shortcuts import render,redirect
from .models import Table
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"index.html")

def video(request):
    return render(request,"video.html")

def video1(request):
    return render(request,"video1.html")

def video2(request):
    return render(request,"video2.html")

def order(request):
    if request.method=="POST":
        name=request.POST.get('name')
        flavour=request.POST.get('flavour')
        topings=request.POST.get('topings')
        address=request.POST.get('address')
        phno=request.POST.get('phno')
        time=request.POST.get('time')
        quantity=request.POST.get('quantity')
        query=Table(name=name,flavour=flavour,topings=topings,address=address,phno=phno,time=time,quantity=quantity)
        query.save ()
        messages.info(request,"Thanks for Ordering! We will reach out you!!")
        return redirect("/order")
    return render(request,"index.html")

def handlesignup(request):
    if request.method=="POST":
        username=request.POST.get('uname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if password!=cpassword:
            messages.warning(request,"Password is incorrect")
            return redirect("/signup")
        try:
            if User.objects.get(username=username):
                return redirect("/signup")
        except:
            pass
        try:
            if User.objects.get(email=email):
                return redirect("/signup")
        except:
            pass
        query=User.objects.create_user(username=username,email=email,password=password)
        query.save()
        return redirect("/login")
    return render(request,"signup.html")

def handlelogin(request):
    if request.method=="POST":
        username=request.POST.get('uname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        myuser=authenticate(username=username,password=password,email=email)
        if myuser is not None:
            login(request,myuser)
            return redirect("/")
        else:
            return redirect("/login")
    return render(request,"login.html")    
    
def handlelogout(request):    
    logout(request)
    return redirect("/login")
