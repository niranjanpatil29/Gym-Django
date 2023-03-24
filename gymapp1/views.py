from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import Gym

# Create your views here.
def home(request):
    return render(request,'home.html')

def congrats(request):
    return render(request,'congrats.html')
        
def cancel(request):
    if request.method=="POST":
        s = Gym.objects.get(uname = request.POST['uname'])
        s.delete()
        return redirect('/')
    else:
        return render(request,'cancel.html')
        
def get(request):
    if request.method =="POST":
        s=Gym.objects.create(uname=request.POST['uname'],phone=request.POST['phone'],email=request.POST['email'],
            fdate=request.POST['fdate'],tdate=request.POST['tdate'],gender=request.POST['gender'])
        s.save()
        return redirect('congrats')
    else:
        return render(request,'get.html')
    

def login(request):
    if request.method == "POST":
        user = auth.authenticate(username = request.POST['uname'],password = request.POST['pass1'])
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            print("invalid Credentials")
            return redirect('/')
    else:            
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        if User.objects.filter(email=request.POST['email']).exists():
            print("Email already Exists")
        else:
            u = User.objects.create_user(username = request.POST['uname'],email  = request.POST['email'],
                password = request.POST['pass1'],
                first_name = request.POST['fname'],last_name = request.POST['lname'])
            u.save()
            return redirect("login")
    else:
        return render(request,'register.html')

def update(request):
    if request.method=="POST":
        Gym.objects.filter(uname = request.POST['uname']).update(fdate = request.POST['ufdate'], tdate = request.POST['utdate'])
        return redirect('/')
    else:
        return render(request,'update.html')

def logout(request):
    auth.logout(request)
    return redirect('/')