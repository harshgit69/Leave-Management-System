# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-23 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SIS', '0003_auto_20160723_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='attendance',
            field=models.IntegerField(default=0),
        ),
    ]