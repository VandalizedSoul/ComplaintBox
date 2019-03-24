from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.conf.urls import url
urlpatterns = [
url(r'^category/$', category),
url(r'^reward/$', reward),
url(r'^addCategory/$', addCategory),
url(r'^deleteCategory/$', deleteCategory),
url(r'^addReward/$', addReward),
url(r'^deleteReward/$', deleteReward),
url(r'^evaluate/$', evaluate),
url(r'^requests/$', requests),
url(r'^users/$', users),
url(r'^addOfficer/$', addOfficer),
]
