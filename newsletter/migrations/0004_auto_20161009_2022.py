# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-09 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_auto_20161008_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='sender',
            field=models.EmailField(default='UWCS Newsletter <newsletter@uwcs.co.uk>', max_length=254),
        ),
    ]
