from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
import datetime
from .models import Complain,Citizen
from django.core.files.storage import FileSystemStorage

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
	username='ravi'
	ccatego=request.POST.get('category','')
	cdetail=request.POST.get('details','')
	cadd=request.POST.get('location','')
	ctype=request.POST.get('comps','')
	file1 = request.FILES["image"]
	if file1.size > 2 * 1024 * 1024:
		c["message_of_size"] = "File too large. Size should not exceed 2 MB."
        	
	fs = FileSystemStorage()
	filename = "./demo/static/complains/" + username  + str(datetime.date.today()) + ".png"
	if fs.exists(filename):
	    fs.delete(filename)
	print("hiiiiii")
	print(filename)
	file2 = fs.save(filename, file1)
	c=Complain(complain_type=ctype,complain_image=filename,complain_description=cdetail,complain_address=cadd,complain_category=ccatego)
	c.save()
	return render(request,'complains.html')
def home(request):
	c = {}
	c.update(csrf(request))
	request.session['uname']='ravi'
	return render_to_response('index.html', c)

def wall(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('wall.html', c)

def complain(request):
	uname='ravi'
	complain=Complain.objects.filter(complain_uname=uname)
	list1 =[]
	for c in complain:
		list1.append(c.complain_image[int(c.complain_image.find('/static')):])
	time=datetime.datetime.now()
	return render_to_response('complains.html',{'complains':list1},{'time':time})

def rewards(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('rewards.html', c)

def contact(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('contact.html', c)
# Create your views here.
