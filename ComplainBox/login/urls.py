from django.conf.urls import url
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'auth',auth_view),
    url(r'login',login),
    url(r'signup',signup),
    url(r'addUser',addUser),
    url(r'logout',logout),
    url(r'',login)
]