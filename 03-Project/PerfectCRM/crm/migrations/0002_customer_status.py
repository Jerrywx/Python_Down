# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-21 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='status',
            field=models.SmallIntegerField(choices=[(0, '已报名'), (1, '未报名')], default=1),
        ),
    ]
