from django.db import models
import datetime
# Create your models here.
class Citizen(models.Model):
    user_name=models.CharField(max_length=30)
    full_name=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    level=models.CharField(max_length=20,default='beginner')

class Complain(models.Model):
 complain_description=models.CharField(max_length=200)
 complain_address=models.CharField(max_length=100)
 complain_category=models.CharField(max_length=20)
 complain_type=models.CharField(max_length=20,default='complain')
 complain_status=models.CharField(max_length=20,default='pending')
 complain_priority=models.IntegerField(default=1)
 complain_rating=models.IntegerField(default=0)
 post_to_wall=models.BooleanField(default=False)
 date_time=models.DateTimeField(blank=True)
 complain_count=models.IntegerField(default=1)
