# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 12:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_auto_20171016_1330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sponsor',
            old_name='text',
            new_name='name',
        ),
    ]
