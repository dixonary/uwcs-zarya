# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-19 21:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160719_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='description',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='facebook_url',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='twitter_url',
        ),
    ]
