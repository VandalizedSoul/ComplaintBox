# Generated by Django 2.0.2 on 2019-03-19 15:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0015_auto_20190317_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='complain',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.date(2019, 3, 19)),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='feed_date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 19, 20, 56, 57, 334595)),
        ),
    ]
