# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 09:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0005_auto_20161028_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='message',
        ),
    ]
