from django import template
from ..models import Notification,Citizen,Complain
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

@register.simple_tag
def total():
    c=Complain.objects.all().count()
    return c

@register.simple_tag
def pending():
    c=Complain.objects.filter(complain_status="pending").count()
    return c

@register.simple_tag
def solved():
    c=Complain.objects.filter(complain_status="solved").count()
    return c

@register.simple_tag
def users():
    c=Citizen.objects.all().count()
    return c