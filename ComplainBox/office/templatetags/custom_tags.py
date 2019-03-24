from django import template
from demo.models import *
register = template.Library()

@register.simple_tag
def unread(name):
    count=Notification.objects.filter(seen=0,user_name=name).count()
    return count

@register.simple_tag
def url(name):
    c=Citizen.objects.filter(username=name)
    print(name)
    url=""
    for i in c:
        url=i.image
        print(i.image)
    print(url + "hiiiiiiii")
    return url