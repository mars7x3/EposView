# Generated by Django 4.1.4 on 2022-12-22 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactsphone',
            name='epos_contacts',
        ),
    ]
