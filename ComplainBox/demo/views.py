from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
import datetime 
import string
import re,requests
from wit import Wit
from .models import Complain,Citizen,Feedback,Support
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
 request.session['cat']=ccatego
 cdetail=request.POST.get('details','')
 request.session['detail']=cdetail
 cadd=request.POST.get('location','')
 request.session['add']=cadd
 ctype=request.POST.get('comps','')
 request.session['type']=ctype
 file1 = request.FILES.get("image")
 filename=""
 fnm=""
 if file1 != None:
  fs = FileSystemStorage()
  st=str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")).replace(':','-')
  filename = "./demo/static/complains/" + username+st +".png"
  if fs.exists(filename):
   fs.delete(filename)
  print(filename)
  file2 = fs.save(filename, file1)
  fnm=filename[int(filename.find('/static')):]
 else:
  fnm="/static/complains/NoImage.png"
 related=Complain.objects.filter(complain_address=cadd,complain_category=ccatego,complain_status="pending").order_by('-complain_count')
 if related != None :
  return render_to_response('newcomplain.html',{'suggestions':related})
 c=Complain(complain_type=ctype,complain_image=fnm,post_to_wall=1,complain_description=cdetail,complain_address=cadd,complain_category=ccatego)
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

@csrf_exempt
def increase(request):
	c = {}
	c.update(csrf(request))
	compid=request.POST.get('id','')
	print("this is   " +compid)
	uid=1
	s=Support(comp_id=int(compid),u_id=uid)
	complain=Complain.objects.filter(id=compid)
	count=1
	for c in complain:
		count=c.complain_count
		count+=1
	c=Complain.objects.filter(id=compid).update(complain_count=count)
	s.save()
	return HttpResponseRedirect("/demo/new/")


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
	return render_to_response('wall.html', {'complain':complain},c)

def complain(request):
	uname='ravi'
	complain=Complain.objects.filter(complain_uname=uname)
	time1=datetime.datetime.now()
	print(time1)
	return render_to_response('complains.html',{'complain':complain,'time':time1})

def rewards(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('rewards.html', c)

def single(request,comp_id='1'):
	c = {}
	c.update(csrf(request))
	uname='ravi'
	complain=Complain.objects.filter(id=comp_id)
	comments=Feedback.objects.filter(feed_complain_id=comp_id,feed_username=uname)
	return render_to_response('single.html',{'complain':complain,'comments':comments}, c)


def contact(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('contact.html', c)
# Create your views here.

def notification(request):
	c={}
	c.update(csrf(request))
	return render_to_response('notification.html',c)

def suggestion(request):
	c={}
	c.update(csrf(request))

	return render_to_response('suggestion.html',c)