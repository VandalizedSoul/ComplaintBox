# Generated by Django 2.0.2 on 2019-03-21 17:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0019_auto_20190320_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citizen',
            name='address',
        ),
        migrations.RemoveField(
            model_name='citizen',
            name='age',
        ),
        migrations.RemoveField(
            model_name='citizen',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='citizen',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='citizen',
            name='user_name',
        ),
        migrations.AddField(
            model_name='citizen',
            name='address1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='citizen',
            name='address2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='citizen',
            name='birthdate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='citizen',
            name='contact',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='citizen',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='citizen',
            name='occupation',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='citizen',
            name='username',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='level',
            field=models.CharField(default='soldier', max_length=20),
        ),
        migrations.AlterField(
            model_name='complain',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.date(2019, 3, 21)),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='feed_date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 21, 22, 46, 10, 101364)),
        ),
    ]
