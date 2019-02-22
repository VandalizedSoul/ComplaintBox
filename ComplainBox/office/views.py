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
from demo.models import Complain, Citizen, Feedback
from django.core.files.storage import FileSystemStorage

access_token = "GVULD55QMRASSPSJD6D2FELJY4AHFXWG"
client = Wit(access_token)
entity = "intent"
message = ""


def newcomplain(request):
 complain = Complain.objects.all()
 list1 = []
 for c in complain:
    list1.append(c.complain_image[int(c.complain_image.find('/static')):])
 combined = zip(complain, list1)
 time1 = datetime.datetime.now()
 return render_to_response('complainArrived.html', {'combined': combined, 'time': time1})


def single(request, comp_id='1'):
 c = {}
 c.update(csrf(request))
 uname = 'ravi'
 complain = Complain.objects.filter(id=comp_id)
 for ci in complain:
    img = ci.complain_image[int(ci.complain_image.find('/static')):]
    comments = Feedback.objects.filter(
        feed_complain_id=comp_id, feed_username=uname)
 print("ha moju ha")
 return render_to_response('singleO.html', {'complain': complain, 'img': img, 'comments': comments}, c)


@csrf_exempt
def post(request, comp_id='1'):
    complain = Complain.objects.filter(id=comp_id).update(post_to_wall=1)
    url = "/office/single/"+comp_id
    return HttpResponseRedirect(url)


@csrf_exempt
def remove(request, comp_id='1'):
    complain = Complain.objects.filter(id=comp_id).update(post_to_wall=0)
    url = "/office/single/"+comp_id
    return HttpResponseRedirect(url)


def newPost(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('newPost.html', c)


@csrf_exempt
def addPost(request):
 username = 'ravi'
 ccatego = request.POST.get('category', '')
 cdetail = request.POST.get('details', '')
 cadd = request.POST.get('location', '')
 ctype = "suggestion"
 file1 = request.FILES.get("image")
 filename=""
 if file1 != None:
  fs = FileSystemStorage()
  st=str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")).replace(':','-')
  filename = "./office/static/complains/" + username+st +".png"
  if fs.exists(filename):
   fs.delete(filename)
  print(filename)
  file2 = fs.save(filename, file1)
 c=Complain(complain_type=ctype,complain_image=filename,post_to_wall=1,complain_description=cdetail,complain_address=cadd,complain_category=ccatego)
 c.save()
 return HttpResponseRedirect('/office/complains')
