from email import message
from http.client import HTTPResponse
from urllib.request import HTTPPasswordMgr
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def handlelogin(request):
    if request.method == 'POST':
        uname =  request.POST['username']
        password = request.POST['pass1'] 
        user = authenticate(username=uname,pass1=password)

        if user is not None:
            login(request,user)
            return render(request,"/")

        else:
            messages.error("Invalid Credentials")
            return redirect("/login")

    return render(request,"login.html")
   



def handlesignup(request):
    if request.method =="POST":
        
        uname = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("pass1")
        confirmpassword = request.POST.get("pass2")
       

        myuser = User.objects.create(uname,email,password)
    

        myuser.save()
            
        messages.succes(request,"Your Account has been Successfully created")

        return redirect("/signup")
        

        
    
    return render(request,'signup.html')

def verification(request):
    return render(request,'verification.html')