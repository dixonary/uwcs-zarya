# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 17:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_auto_20160921_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='facebook_link',
            field=models.URLField(blank=True, default='', help_text='A link to the associated Facebook event if one exists', verbose_name='Facebook event'),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='finish',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 21, 18, 59, 25, 500321, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='signup_close',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 21, 18, 59, 25, 500398, tzinfo=utc)),
        ),
    ]
