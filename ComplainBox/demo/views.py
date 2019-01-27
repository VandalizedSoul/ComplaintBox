from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf

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
