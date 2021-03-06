# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
