from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
import datetime 
import string
import re
from wit import Wit
from .models import Complain,Citizen,Feedback
from django.core.files.storage import FileSystemStorage

access_token="GVULD55QMRASSPSJD6D2FELJY4AHFXWG"
client = Wit(access_token)
entity="intent"
message=""
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
	return render_to_response('newcomplain.html',c)

@csrf_exempt
def addComplain(request):
 username='ravi'
 ccatego=request.POST.get('category','')
 cdetail=request.POST.get('details','')
 cadd=request.POST.get('location','')
 ctype=request.POST.get('comps','')
 file1 = request.FILES.get("image")
 filename=""
 if file1 != None:
  fs = FileSystemStorage()
  st=str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")).replace(':','-')
  filename = "./demo/static/complains/" + username+st +".png"
  if fs.exists(filename):
   fs.delete(filename)
  print(filename)
  file2 = fs.save(filename, file1)
 c=Complain(complain_type=ctype,complain_image=filename,post_to_wall=1,complain_description=cdetail,complain_address=cadd,complain_category=ccatego)
 c.save()
 return HttpResponseRedirect('/demo/complain')

@csrf_exempt
def addFeedback(request,comp_id='1'):
	username='ravi'
	feedback=request.POST.get('feedback','')
	f=Feedback(feed_complain_id=comp_id,feed_username=username,feed_feedback=feedback)
	f.save()
	url="/demo/single/"+comp_id
	return HttpResponseRedirect(url)

def home(request):
	c = {}
	c.update(csrf(request))
	request.session['uname']='ravi'
	return render_to_response('index.html', c)

def wall(request):
	c = {}
	c.update(csrf(request))
	uname='ravi'
	complain=Complain.objects.filter(post_to_wall=1)
	list1 =[]
	for c in complain:
		list1.append(c.complain_image[int(c.complain_image.find('/static')):])
		print(c.complain_image[int(c.complain_image.find('/static')):])
	combined=zip(complain,list1)
	return render_to_response('wall.html', {'combined':combined},c)

def complain(request):
	uname='ravi'
	complain=Complain.objects.filter(complain_uname=uname)
	list1 =[]
	for c in complain:
		list1.append(c.complain_image[int(c.complain_image.find('/static')):])
		print(c.complain_image[int(c.complain_image.find('/static')):])
	time1=datetime.datetime.now()
	combined=zip(complain,list1)
	print(time1)
	return render_to_response('complains.html',{'combined':combined,'time':time1})

def rewards(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('rewards.html', c)

def single(request,comp_id='1'):
	c = {}
	c.update(csrf(request))
	uname='ravi'
	complain=Complain.objects.filter(id=comp_id)
	for ci in complain:
		img=ci.complain_image[int(ci.complain_image.find('/static')):]
	comments=Feedback.objects.filter(feed_complain_id=comp_id,feed_username=uname)
	return render_to_response('single.html',{'complain':complain,'img':img,'comments':comments}, c)


def contact(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('contact.html', c)
# Create your views here.
