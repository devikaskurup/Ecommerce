from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserAddForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from.decorators import admin_only,unauthenticate_user,allowed_user
from Product.models import ProductDetails


@admin_only
def index(request):
    Product = ProductDetails.objects.all()
    
    context ={
        "product":Product
    }
    return render(request,'index.html',context)

@allowed_user
def AdminIndex(request):
    return render(request,"adminhome.html")

@unauthenticate_user
def SignIn(request):
    if request.method == "POST":
        username = request.POST["uname"]
        password = request.POST["pswd"]
        user = authenticate(request,username = username,password =password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,"username or password incorrect")
            return redirect('SignIn')

    return render(request,'login.html')

@unauthenticate_user
def SignUp(request):
    form = UserAddForm()

    if request.method == "POST":
        form=UserAddForm(request.POST)

        if form.is_valid():
            username=form.cleaned_data.get("username")
            email=form.cleaned_data.get("email")

            if User.objects.filter(username=username).exists():
                 messages.info(request,"username already Exists")
                 return redirect('SignUp')

            if User.objects.filter(email=email).exists():
                messages.info(request,"email already Exists")
                return redirect('SignUp')
            else:
                form.save()
                messages.success(request,"user created")
                return redirect('SignIn')
    context = {
        "form":form
    }
    return render(request,'register.html',context)

def SignOut(request):
    logout(request)
    return redirect('index')