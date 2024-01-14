from django.shortcuts import render
from django.views.generic import View
from bazaarapp.forms import LoginForm,CategoryForm
from api.models import Category
from django.contrib.auth import authenticate,login
from django.contrib import messages


class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_object=authenticate(request,username=uname,password=pwd)
            if user_object:
                login(request,user_object)
                return render(request,"login.html",{"form":form})
        print("invalid login")    
        return render(request,"login.html",{"form":form})
    

class CategoryCreateView(View):
    def get (self,request,*args,**kwargs):
        form=CategoryForm()
        return render(request,"category_create.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=CategoryForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"created")
            return render(request,"category_create.html",{"form":form})
        else:
            messages.error(request,"failed to create the message")    
            return render(request,"category_create.html",{"form":form})
        

class CategoryListView(View):
    def get(self,request,*args,**kwargs):
        qs=Category.objects.all()    
        return render (request,"category_list.html",{"data":qs})    


class CategoryDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Category.objects.get(id=id)
        print(qs)
        return render(request,"category_detail.html",{"data":qs})

class CategoryDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Category.objects.delete(id=id)
        return render(request,"category_list.html")

