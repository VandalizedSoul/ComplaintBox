from django.db import models
from ComplainBox.settings import *
import datetime
from django.contrib.auth.models import User
# Create your models here.
class Citizen(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    username=models.CharField(max_length=30,null=True)
    name=models.CharField(max_length=100,null=True)
    birthdate=models.DateTimeField(null=True)
    address1=models.CharField(max_length=100,null=True)
    address2=models.CharField(max_length=100,null=True)
    contact=models.CharField(max_length=13,null=True)
    occupation=models.CharField(max_length=20,null=True)
    level=models.CharField(max_length=20,default='soldier')
    image = models.CharField(max_length=200,default="/static/profiles/NoImage.png")
    
class Officer(models.Model):
    username=models.CharField(max_length=30,null=True)
    name=models.CharField(max_length=100,null=True)
    contact=models.CharField(max_length=13,null=True)
    detail=models.CharField(max_length=20,null=True)
    department=models.CharField(max_length=20)

class Complain(models.Model):
 complain_id=models.IntegerField(default=1)    
 complain_description=models.CharField(max_length=200)
 complain_address=models.CharField(max_length=100)
 complain_category=models.CharField(max_length=20)
 complain_type=models.CharField(max_length=20,default='complain')
 complain_status=models.CharField(max_length=20,default='pending')
 complain_priority=models.IntegerField(default=1)
 complain_rating=models.IntegerField(default=1)
 post_to_wall=models.BooleanField(default=False)
 date_time=models.DateTimeField(default=datetime.date.today(), blank=True)
 complain_count=models.IntegerField(default=1)
 complain_uname=models.CharField(max_length=30,null=True,default='ravi')
 complain_image = models.CharField(max_length=200,null=True)
 to_admin=models.BooleanField(default=False)

class Feedback(models.Model):
    feed_complain_id=models.IntegerField(default=1)
    feed_username=models.CharField(max_length=30,null=True,default='ravi')
    feed_feedback=models.CharField(max_length=200)
    feed_date_time=models.DateTimeField(default=datetime.datetime.now(), blank=True)

class Support(models.Model):
    comp_id = models.IntegerField(default=1)
    u_id = models.IntegerField(default=1)

class Notification(models.Model):
    notification_id=models.IntegerField(default=1)
    user_name=models.CharField(max_length=30,null=True,default='ravi')
    complain_id=models.IntegerField(default=1)
    description=models.CharField(max_length=100)
    seen=models.BooleanField(default=False)

class Reward(models.Model):
    reward_id=models.IntegerField(default=1)
    description=models.CharField(max_length=100)
    name=models.CharField(max_length=50,null=True)
    level=models.CharField(max_length=50,default='soldier')

class Category(models.Model):
    category=models.CharField(max_length=100)

