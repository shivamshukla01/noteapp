# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-08 09:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0002_auto_20170508_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='subj',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='noteapp.Subject'),
        ),
    ]