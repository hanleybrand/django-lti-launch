# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ltilaunch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LTIToolProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(unique=True)),
                ('display_name', models.CharField(max_length=50)),
                ('visibility', models.CharField(choices=[('', 'All'), ('admins', 'Admins'), ('members', 'Members')], max_length=10)),
                ('description', models.TextField()),
                ('icon_url', models.URLField(blank=True)),
                ('launch_path', models.TextField()),
            ],
            options={
                'verbose_name': 'LTI tool provider',
            },
        ),
    ]