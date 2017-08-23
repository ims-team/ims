# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-22 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ans', '0008_auto_20170821_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ansb',
            name='Image',
            field=models.CharField(choices=[('Redhat', 'Redhat'), ('Centos', 'Centos'), ('Ubuntu', 'Ubuntu')], default='Centos', max_length=10),
        ),
        migrations.AlterField(
            model_name='ansb',
            name='Instance_Type',
            field=models.CharField(choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')], default='Small', max_length=10),
        ),
        migrations.AlterField(
            model_name='ansb',
            name='key_name',
            field=models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], default='Public', max_length=10),
        ),
        migrations.AlterField(
            model_name='ansbe',
            name='Instance',
            field=models.CharField(choices=[(b'0.1.2.3.4.5', b'0.1.2.3.4.5')], default=b'0.1.2.3.4.5', max_length=7),
        ),
        migrations.AlterField(
            model_name='ansbe',
            name='OS',
            field=models.CharField(choices=[('Ubuntu', 'Ubuntu'), ('Centos', 'Centos'), ('Redhat', 'Redhat')], default='Centos', max_length=7),
        ),
    ]
