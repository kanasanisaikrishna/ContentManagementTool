from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from . models import *
from . forms import *


def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method== 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password") 
        password2 = request.POST.get("conformpassword")
        
        if password1!=password2 :
            return redirect("signup")
        else :
            my_user=User.objects.create_user(username,email,password1)
            my_user.save()
            return redirect ("signin")

    return render(request,"signup.html")

def signin(request):
    if request.method=="POST":
        username=request.POST.get("username")
        pass1=request.POST.get("password")

        user=authenticate(request,username=username,password=pass1)
        
        if user is not None:
            login(request,user)
            return redirect("home")
        else :
            return redirect("signup")
       
    return render(request,"signin.html")

def home(request):
    AllBlogs=Blogs.objects.all()
    context={
        'blogs':AllBlogs,
    }
    print(AllBlogs)
    return render(request,'home.html',context)

def addBlog(request):
    form=blogForm()
    if request.method=='POST':
        form=blogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={
        'form':form,
    }
    return render(request,'addblog.html',context)


    
def myblog(request):
    context={'blogs':Blogs.objects.filter(auther=request.user)}
    return render (request,'myblog.html',context)

def signout(request):
    
    logout(request)
    return redirect('index')

def likeBlog(request,pk):
    blog=Blogs.objects.get(id=pk)
    blog.likes+=1
    blog.save()
    return redirect('home')

def deleteBlog(request,pk):
    blog=Blogs.objects.get(id=pk)
    blog.delete()
    return redirect('home')
   