from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import CreateMotiveForm
from django.contrib import messages
# Create your views here.

class CreateMotive(View):
    def get(self,request):
        context ={
            "form":CreateMotiveForm()
        }
        return render(request,'community/create_motive.html',context)
    def post(self,request):
        form = CreateMotiveForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Motive created succesfully")

        else:
            context ={
                "form":form
            }
            messages.error(request,"Fill the required Fields")
            return render(request,'community/create_motive.html',context)   
        return redirect("index")