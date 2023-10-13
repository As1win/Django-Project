from django.shortcuts import render
from Shop.models import Category,Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def Allcategory(request):
    c=Category.objects.all()
    return render(request,'Category.html',{'c':c})
@login_required
def Allproduct(request,c):
    p=Product.objects.filter(category__cname=c)
    catagory=Category.objects.get(cname=c)
    return render(request,'Product.html',{'p':p,'category':catagory})
@login_required
def Details(request,p):
    d=Product.objects.get(pname=p)
    return render(request,'details.html',{'d':d})
def Login(request):
    if (request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return Allcategory(request)
        else:
             messages.error(request,"Invalid Credentials")
    return render(request,'Login.html')
@login_required
def Logout(request):
    logout(request)
    return Login(request)

def Register(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        p1 = request.POST['p1']
        e = request.POST['e']
        f = request.POST['f']
        l = request.POST['l']
        if (p == p1):
            u = User.objects.create_user(username=u, password=p, email=e, first_name=f, last_name=l)
            u.save()
            return Login(request)
    return render(request,'Register.html')