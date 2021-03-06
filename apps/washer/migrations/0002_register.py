# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-23 01:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('washer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('emiil', models.EmailField(blank=True, max_length=70)),
                ('phone', models.CharField(max_length=30)),
                ('birthday', models.DateTimeField()),
                ('image', models.FileField(upload_to='image/%Y/%m/%d')),
                ('status', models.BooleanField()),
                ('working', models.BooleanField()),
                ('sex', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('U', 'Unsure')], max_length=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
