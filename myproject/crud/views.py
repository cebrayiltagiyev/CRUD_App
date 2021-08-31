from django.shortcuts import render,redirect
from .forms import StudentForm
from django.http import HttpResponseRedirect
from .models import Student

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def add(request):
	form=StudentForm(request.POST or None)
	
	if form.is_valid():
		form.save()
	return render(request,'add.html',{'form':form})


def show(request):
	student=Student.objects.all()
	return render(request,'show.html',{'student':student})
@login_required

def update(request,id):
	
	student=Student.objects.get(id=id)
	form=StudentForm(request.POST,instance=student)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/show')
	return render(request,'update.html',{'student':student})


def delete(request,id):
	form=Student.objects.get(id=id)
	form.delete()
	return HttpResponseRedirect('/show') 


def indexView(request):
	return render(request,'index.html')
@login_required

def registerView(request):
	if request.method== "POST":
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login_url')
	else:
		form=UserCreationForm()
		

	return render(request,'registration/register.html',{'form':form}) 