from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        usern = request.POST['username']
        pas = request.POST['password']
        user = auth.authenticate(username=usern,password=pas)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method == 'POST':
        user = request.POST['username']
        email = request.POST['email']
        pas = request.POST['password']
        cpas = request.POST['password1']
        if pas == cpas:
            if User.objects.filter(username=user).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email exists')
                return redirect('register')
            else:
                userobj = User.objects.create_user(username=user,email=email,password=pas)

                userobj.save();
                return redirect('login')

        else:
            messages.info(request,'password not matching')
            return redirect('register')
        print("usesr register")
        return redirect('/')

    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')