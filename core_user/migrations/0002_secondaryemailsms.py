# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 18:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecondaryEmailSMS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alternate_email', models.EmailField(max_length=255, unique=True, verbose_name='email')),
                ('alternate_sms_telephone', models.CharField(blank=True, max_length=20, null=True, verbose_name='telephone')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]