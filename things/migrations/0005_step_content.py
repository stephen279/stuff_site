# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-04 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0004_step_number_increment'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
