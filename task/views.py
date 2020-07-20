from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.
@login_required(login_url='login')   
def index(request):
    task = Task.objects.all()
    form = TaskForm()

    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'task': task,'form':form}
    return render(request,'task/list.html',context)

    
@login_required(login_url='login')   
def deleteTask(request , pk):
    item = Task.objects.get(id=pk)

    if request.method =='POST':
        item.delete()
        return redirect('/')


    context = {'item':item}
    return render(request,'task/delete.html',context)





    




