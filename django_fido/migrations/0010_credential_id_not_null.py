# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-20 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_fido', '0009_fill_credential_ids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authenticator',
            name='credential_id_data',
            field=models.TextField(unique=True),
        ),
    ]
