from django.shortcuts import render,redirect
from django.views.generic import View
from main.models import Motors
from main.forms import MotorCreateForm,RegistrationForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout



# Create your views here.

class MotorCreateView(View):
    def get(self,request,*args,**kwargs):
        form=MotorCreateForm()
        return render(request,"motor_add.html",{"form":form})
    def post(self,request,*args,**kwrags):
        form=MotorCreateForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            print("saved")
            return render(request,"motor_add.html",{"form":form})
        else:
            return render(request,"motor_add.html",{"form":form})
class MotorListView(View):
    def get(self,request,*args,**kwargs):
        qs=Motors.objects.all()
        return render(request,"motor_list.html",{"motors":qs})


class MotorDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Motors.objects.get(id=id)
        return render(request,"motor_detail.html",{"motor":qs})
    
class MotorDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Motors.objects.filter(id=id).delete()
        return redirect("mot-list")
    
class MotorUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Motors.objects.get(id=id)
        form=MotorCreateForm(instance=obj)
        return render(request,"motor_change.html",{"form":form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Motors.objects.get(id=id)
        form=MotorCreateForm(request.POST,instance=obj,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("mot-list")
        else:
            return render(request,"motor_change.html",{"form":form})
        
      
class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"registration.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            # form.save()
            User.objects.create_user(**form.cleaned_data)
            return redirect("signin")
        else:
            return render(request,"registration.html",{"form":form})
        
class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwarsg):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("mot-list")
            else:
                # print("invalid")
                return render(request,"login.html",{"form":form})
            
def sign_outview(request,*args,**kwargs):
    logout(request)
    return redirect("signin")

