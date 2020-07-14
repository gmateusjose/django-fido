# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-21 11:16
from django.db import migrations


SQL = ("UPDATE django_fido_authenticator "
       "SET attestation_data = 'owFkbm9uZQJYJTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwAAAAACoDoA=='")


class Migration(migrations.Migration):

    dependencies = [
        ('django_fido', '0005_add_attestation_data'),
    ]

    operations = [
        migrations.RunSQL(SQL, reverse_sql=migrations.RunSQL.noop, elidable=True),
    ]
