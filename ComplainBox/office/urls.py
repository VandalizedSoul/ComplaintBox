from django.urls import path
from office.views import generate,report,ratings,priority,status,redirect,newcomplain,single,post,remove,addPost,newPost
from django.contrib.auth import views as auth_views
from django.conf.urls import url
urlpatterns = [
url(r'^complains/$', newcomplain),
url(r'^single/(?P<comp_id>\d+)/$', single),
url(r'^post/(?P<comp_id>\d+)/$', post),
url(r'^remove/(?P<comp_id>\d+)/$', remove),
url(r'^addPost/$', addPost),
url(r'^newPost/$', newPost),
url(r'^redirect/$', redirect),
url(r'^status/$', status),
url(r'^priority/$', priority),
url(r'^ratings/$', ratings),
url(r'^report/$', report),
url(r'^generate/$', generate),

]