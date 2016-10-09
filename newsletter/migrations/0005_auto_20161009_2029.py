# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-09 20:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0004_auto_20161009_2022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mail',
            name='sender',
        ),
        migrations.AddField(
            model_name='mail',
            name='sender_email',
            field=models.EmailField(default='noreply@uwcs.co.uk', max_length=254),
        ),
        migrations.AddField(
            model_name='mail',
            name='sender_name',
            field=models.CharField(default='UWCS Newsletter', max_length=50),
        ),
    ]
