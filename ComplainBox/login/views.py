from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib import messages
from django.contrib.auth.models import User,Group
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
import datetime
from demo.models import *

def login(request):
    try:
        if request.user.is_authenticated:
            '''if request.user.is_superuser:
                return render(request,'/demo/index.html')'''
            usertype = request.user.groups.all()[0].name
            if usertype == "citizen":
                #student = Student.objects.get(user = request.user)
                #request.session['student_year'] = student.year
                return HttpResponseRedirect('/demo/home')    
            if usertype == "officer":
                #student = Student.objects.get(user = request.user)
                #request.session['student_year'] = student.year
                return HttpResponseRedirect('/office/complains')    
            if usertype == "admin":
                #student = Student.objects.get(user = request.user)
                #request.session['student_year'] = student.year
                return HttpResponseRedirect('/main/reward')
            
        else:
            c = {}
            c.update(csrf(request))
            return render(request, 'login.html', c)
    except:
        return render(request,'login.html')


def auth_view(request):
    try:
        if request.user.is_authenticated:
            '''if request.user.is_superuser:
                return render(request,' index.html')'''
            return HttpResponseRedirect('/demo/home')

        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        request.session['department']=""
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if user.is_superuser:
                request.session['usertype'] = 'admin'
                #return HttpResponseRedirect('/demo/home')
            usertype = request.user.groups.all()[0].name
            request.session['usertype'] = usertype
            if usertype == "citizen":
                #student = Student.objects.get(user = request.user)
                #request.session['student_year'] = student.year
                return HttpResponseRedirect('/demo/home')    
            if usertype == "officer":
                officer = Officer.objects.get(username = username)
                request.session['department'] = officer.department
                return HttpResponseRedirect('/office/complains')    
            if usertype == "admin":
                #student = Student.objects.get(user = request.user)
                #request.session['student_year'] = student.year
                return HttpResponseRedirect('/main/reward')    
            
        else:
            messages.add_message(request, messages.WARNING, 'Incorect Username or Password')
            return HttpResponseRedirect('/login')
    except:
        return render(request,'login.html')


@login_required()
def logout(request):
    try:
        if request.user.is_authenticated:
            auth.logout(request)
        messages.add_message(request, messages.INFO, 'You are Successfully Logged Out')
        messages.add_message(request, messages.INFO, 'Thanks for visiting.')
        #request.session.clear()
        return HttpResponseRedirect('/login/')
    except:
        messages.add_message(request, messages.WARNING, 'exception Occured..please try again.')
        return render(request,' login.html')

def signup(request):
    c = {}
    c.update(csrf(request))
    return render(request,'signup.html', c)

def addUser(request):
    print(request.POST)
    name = request.POST.get('name', '')
    birthdate = request.POST.get('birthdate', '')
    occupation = request.POST.get('occupation', '')
    address1 = request.POST.get('address1', '')
    address2 = request.POST.get('address2', '')
    contact = request.POST.get('contact', '')
    username = request.POST.get('username', '')
    password= request.POST.get('password', '')
    file1 = request.FILES.get("image")
    print(request.FILES.get("image123"))
    filename=""
    fnm=""
    if file1 != None:
        fs = FileSystemStorage()
        st=str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")).replace(':','-')
        filename = "./login/static/profiles/" + username+st +".png"
        print(filename)
        if fs.exists(filename):
            fs.delete(filename)
        file2=fs.save(filename, file1)
    else:
        filename="/static/profiles/NoImage1.png"
    fnm=filename[int(filename.find('/static')):]
    print(fnm)
    user=Citizen(image=fnm,name=name,username=username,birthdate=birthdate,occupation=occupation,address1=address1,address2=address2,contact=contact)
    user.save()
    u = User.objects.create_user(username = username, password = password)
    u.save()
    group = Group.objects.get(name='citizen')
    group.user_set.add(u)
    group.save()
    return HttpResponseRedirect("/login")