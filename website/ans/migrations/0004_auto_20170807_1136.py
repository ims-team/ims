# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-07 11:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ans', '0003_auto_20170807_0955'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ansb',
            old_name='Instance',
            new_name='Instance_Type',
        ),
    ]
