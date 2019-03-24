from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User,Group
from django.contrib.auth.decorators import user_passes_test,login_required
from django.template.context_processors import csrf
import datetime 
from datetime import timedelta
from demo.models import *


def newpost(request):
	return render(request,'new.html')


def addPost(request):
 username = request.user.username
 ccatego = request.POST.get('category', '')
 cdetail = request.POST.get('details', '')
 cadd = request.POST.get('location', '')
 ctype = "suggestion"
 file1 = request.FILES.get("image")
 filename=""
 if file1 != None:
  fs = FileSystemStorage()
  st=str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")).replace(':','-')
  filename = "./main/static/complains/" + username+st +".png"
  if fs.exists(filename):
   fs.delete(filename)
  print(filename)
  file2 = fs.save(filename, file1)
 fnm=filename[int(filename.find('/static')):]
 c=Complain(complain_type=ctype,complain_image=fnm,post_to_wall=1,complain_description=cdetail,complain_address=cadd,complain_category=ccatego)
 c.save()
 return HttpResponseRedirect('/main/post')

def is_admin(user):
   u=user.groups.filter(name="admin").count()
   if u==0:
       return False
   return True

@login_required
@user_passes_test(is_admin)
def evaluate(request):
    date=datetime.datetime.now() - timedelta(days=90)
    complains=Complain.objects.filter(date_time__lte=date)
    return render(request,'evaluate.html',{'complains':complains})

@login_required
@user_passes_test(is_admin)
def requests(request):
    comps=Complain.objects.filter(to_admin=1)
    return render(request,'requested.html',{'complains':comps})

@login_required
@user_passes_test(is_admin)
def category(request):
    category=Category.objects.all()
    return render(request,'category.html',{'category':category})

@login_required
@user_passes_test(is_admin)
def reward(request):
    reward=Reward.objects.all()
    return render(request,'reward.html',{'rewards':reward})

@login_required
@user_passes_test(is_admin)
def addCategory(request):
    ccategory=request.POST.get('category','')
    c1=Category(category=ccategory)
    c1.save()
    url="/main/category"
    return HttpResponseRedirect(url)

@login_required
@user_passes_test(is_admin)
def deleteCategory(request):
    ccategory=request.POST.get('category','')
    Category.objects.filter(category=ccategory).delete()
    url="/main/category"
    return HttpResponseRedirect(url)

@login_required
@user_passes_test(is_admin)
def addReward(request):
    name=request.POST.get('rewardname','')
    desc=request.POST.get('rewarddesc','')
    level=request.POST.get('level','')
    c1=Reward(name=name,description=desc,level=level)
    c1.save()
    url="/main/reward"
    return HttpResponseRedirect(url)

@login_required
@user_passes_test(is_admin)
def deleteReward(request):
    id=request.POST.get('reward','')
    Reward.objects.filter(id=id).delete()
    url="/main/reward"
    return HttpResponseRedirect(url)

@login_required
@user_passes_test(is_admin)
def users(request):
    category=Category.objects.all()
    return render(request,'users.html',{'categories':category})


@login_required
@user_passes_test(is_admin)
def addOfficer(request):
    name = request.POST.get('name', '')
    department = request.POST.get('department', '')
    detail = request.POST.get('detail', '')
    contact = request.POST.get('contact', '')
    username = request.POST.get('username', '')
    password= request.POST.get('password', '')
    user=Officer(name=name,username=username,detail=detail,department=department,contact=contact)
    user.save()
    u = User.objects.create_user(username = username, password = password)
    u.save()
    group = Group.objects.get(name='officer')
    group.user_set.add(u)
    group.save()
    return HttpResponseRedirect('/main/users')