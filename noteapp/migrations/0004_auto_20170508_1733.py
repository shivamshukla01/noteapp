# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-08 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0003_auto_20170508_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='srcfile',
            field=models.FileField(null=True, upload_to='uploads/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='subject',
            name='title2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]