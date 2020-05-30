from django.shortcuts import render,redirect
from django.http import HttpResponse
from astromania.forms import UserForm
from astromania.models import User
from django.contrib import messages



# Create your views here.


def homepage(request):
    return render (request,"home.html",)

def login(request):
    return render(request,"login.html")


def log_check(request):
    if request.method == "POST":
        email= request.POST['email']
        password1= request.POST['password1']
        try:
            u = User.objects.get(email=email, password1=password1)

            if u is not None:
                return render(request, 'home.html',{'u': u})

            else:
                messages.info(request, 'Please give correct email and passworrd')
                return redirect('../astromania/login')
        except:
            messages.info(request, 'Please give correct email and password')
            return redirect('../astromania/login')
    else:
        return render(request,'login.html')
    
def reg(request):
    return render(request,'register.html')

def register(request):
    if request.method=="POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        username=request.POST["username"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        email=request.POST["email"]

        if password1==password2:
            if User.objects.filter(username=username).exists():
               messages.info(request,'Username Taken')
            elif User.objects.filter(email=email).exists():
                 messages.info(request,'Email Taken')
                 return redirect('../astromania/register')
            else:
                form = UserForm(request.POST)
                form.save()
                return redirect('../astromania/login')
        else:
            messages.info(request,'password not matching..')
            return redirect('../astromania/register')
    else:
        return render(request,'register.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def recipes(request):
    return render(request,'recipes.html')
def Tandoori(request):
     return render(request,'Tandoori.html')
