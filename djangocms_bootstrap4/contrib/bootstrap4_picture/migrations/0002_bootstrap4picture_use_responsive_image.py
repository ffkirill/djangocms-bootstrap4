# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-28 17:18
from __future__ import unicode_literals

from django.db import migrations, models

from djangocms_picture.models import RESPONSIVE_IMAGE_CHOICES


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap4_picture', '0001_initial'),
        ('djangocms_picture', '0008_picture_use_responsive_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='Bootstrap4Picture',
            name='use_responsive_image',
            field=models.CharField(choices=RESPONSIVE_IMAGE_CHOICES, default='inherit', help_text='Uses responsive image technique to choose better image to display based upon screen viewport. This configuration only applies to uploaded images (external pictures will not be affected). ', max_length=7, verbose_name='Use responsive image'),
        ),
    ]
