# Generated by Django 2.0.2 on 2019-03-21 17:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0020_auto_20190321_2246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('contact', models.CharField(max_length=13, null=True)),
                ('detail', models.CharField(max_length=20, null=True)),
                ('department', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='feedback',
            name='feed_date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 21, 23, 26, 36, 554129)),
        ),
    ]
