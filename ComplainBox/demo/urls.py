from django.urls import path
from demo.views import *
from django.contrib.auth import views as auth_views
from django.conf.urls import url
urlpatterns = [
url(r'^single/(?P<comp_id>\d+)/$', single),
url(r'^addFeedback/(?P<comp_id>\d+)/$', addFeedback),
url(r'^new/$', newcomplain),
url(r'^home/$', home),
url(r'^complain/$', complain),
url(r'^rewards/$', rewards),
url(r'^wall/$', wall),
url(r'^addComplain/$', addComplain),
url(r'^notification/$', notification),
url(r'^increase/$', increase),
url(r'^seen/(?P<noti_id>\d+)/$', seen),

]