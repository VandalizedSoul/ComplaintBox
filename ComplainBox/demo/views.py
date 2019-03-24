from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.decorators import user_passes_test,login_required
import datetime 
import string
import re,requests
from wit import Wit
from django.db.models import Avg
from .models import *
from django.core.files.storage import FileSystemStorage

access_token="GVULD55QMRASSPSJD6D2FELJY4AHFXWG"
client = Wit(access_token)
entity="intent"
message=""

def is_citizen(user):
   u=user.groups.filter(name="citizen").count()
   if u==0:
       return False
   return True

@login_required
@user_passes_test(is_citizen)
def newcomplain(request):
	#
	#
	category=Category.objects.all()
	return render(request,'newcomplain.html',{'categories':category})

@login_required
@user_passes_test(is_citizen)
def addComplain(request):
 username=request.user.username
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
 related=Complain.objects.filter(complain_address=cadd,complain_category=ccatego,complain_status="pending").order_by('-complain_count','complain_priority')
 if related :
  c=Category.objects.all()
  return render(request,'newcomplain.html',{'suggestions':related,'categories':c})
 c=Complain(complain_uname=username,complain_type=ctype,complain_image=fnm,post_to_wall=1,complain_description=cdetail,complain_address=cadd,complain_category=ccatego)
 c.save()	
 return HttpResponseRedirect('/demo/complain')

@login_required
@user_passes_test(is_citizen)
def addFeedback(request,comp_id='1'):
	username=request.user.username
	feedback=request.POST.get('feedback','')
	f=Feedback(feed_complain_id=comp_id,feed_username=username,feed_feedback=feedback)
	f.save()
	url="/demo/single/"+comp_id
	return HttpResponseRedirect(url)

@login_required
@user_passes_test(is_citizen)
def increase(request):
	#
	#
	compid=request.POST.get('id','')
	#print("this is   " +compid)
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
	#
	#
	uname=request.user.username
	count=Complain.objects.filter(complain_uname=uname).count()
	average=Complain.objects.filter(complain_uname=uname).aggregate(Avg('complain_rating'))
	#print(count)
	#print(average)
	level=""
	if count>10 and average['complain_rating__avg'] > 3:
		level="commander"
	elif count>15 and average>3:
		level="brigadier"
	elif count>20 and average>4:
		level="leiutenant"
	else:
		level="soldier"
	count=Notification.objects.filter(seen=0).count()
	return render(request,'index.html',{'level':level,'count':count})


def wall(request):
	#
	#
	complain=Complain.objects.filter(post_to_wall=1).order_by('-date_time')
	return render(request,'wall.html', {'complain':complain})


def complain(request):
	uname=request.user.username
	print(uname)
	complain=Complain.objects.filter(complain_uname=uname).order_by('-date_time')
	time1=datetime.datetime.now()
	print(time1)
	return render(request,'complains.html',{'complain':complain,'time':time1})

@login_required
@user_passes_test(is_citizen)
def rewards(request):
	#
	#
	users=Citizen.objects.filter(username=request.user.username)
	rewards=Reward.objects.all()
	rank=''
	reward1=[]
	reward2=[]
	for user in users:
		rank=user.level 
	if rank=='soldier':
		for reward in rewards:
			if reward.level == 'soldier':
				reward1.append(reward)
			else:
				reward2.append(reward)
	elif rank=='commander':
		for reward in rewards:
			if reward.level == 'soldier' or reward.level == 'commander' :
				reward1.append(reward)
			else:
				reward2.append(reward)
	elif rank=='brigadier':
		for reward in rewards:
			if reward.level == 'lieutenant' :
				reward2.append(reward)
			else:
				reward1.append(reward)
	elif rank=='lieutenant':
		for reward in rewards:
			reward1.append(reward)
	return render(request,'rewards.html',{'reward1':reward1,'reward2':reward2})


def single(request,comp_id='1'):
	#
	#
	uname=request.user.username
	complain=Complain.objects.filter(id=comp_id)
	comments=Feedback.objects.filter(feed_complain_id=comp_id,feed_username=uname)
	return render(request,'single.html',{'complain':complain,'comments':comments})

@login_required
@user_passes_test(is_citizen)
def notification(request):
	#
	#
	uname=request.user.username
	noti=Notification.objects.filter(user_name=uname).order_by('-id')
	return render(request,'notification.html',{'notifications':noti})

@login_required
@user_passes_test(is_citizen)
def seen(request,noti_id='1'):
	#
	#
	noti=Notification.objects.filter(id=noti_id)
	url=""
	for notif in noti:
		notif.seen=1
		url="/demo/single/"+str(notif.complain_id)+"/"
		notif.save()
	return HttpResponseRedirect(url)