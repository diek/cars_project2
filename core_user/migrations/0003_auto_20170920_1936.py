# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 19:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_user', '0002_secondaryemailsms'),
    ]

    operations = [
        migrations.RenameField(
            model_name='secondaryemailsms',
            old_name='user',
            new_name='users',
        ),
    ]
