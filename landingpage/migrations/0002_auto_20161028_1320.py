# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 04:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='fullname',
            new_name='name',
        ),
        migrations.AddField(
            model_name='subscription',
            name='content',
            field=models.CharField(default='defaultMessage', max_length=200),
            preserve_default=False,
        ),
    ]
