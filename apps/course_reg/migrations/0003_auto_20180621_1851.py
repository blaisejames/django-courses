# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-06-21 18:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_reg', '0002_auto_20180621_1829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='bodytext',
        ),
        migrations.RemoveField(
            model_name='course',
            name='permalink',
        ),
        migrations.RemoveField(
            model_name='course',
            name='title',
        ),
    ]