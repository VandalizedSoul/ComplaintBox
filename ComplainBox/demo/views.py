from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from datetime import datetime
from .models import Complain,Citizen

def printf(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('printf.html', c)
	
def about(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('about.html', c)

def newcomplain(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('newcomplain.html', c)

def addComplain(request):
	ccatego=request.POST.get('category','')
	cdetail=request.POST.get('details','')
	cadd=request.POST.get('location','')
	ctype=request.POST.get('comps','')
	print(ctype)
	c=Complain(complain_type=ctype,complain_description=cdetail,complain_address=cadd,complain_category=ccatego)
	c.save()
	return render(request,'complains.html')
def home(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('index.html', c)

def wall(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('wall.html', c)

def complain(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('complains.html', c)

def rewards(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('rewards.html', c)

def contact(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('contact.html', c)
# Create your views here.
