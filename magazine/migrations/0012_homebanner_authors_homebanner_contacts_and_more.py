# Generated by Django 4.1.4 on 2022-12-23 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0011_remove_homebanner_image_homebanner_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='homebanner',
            name='authors',
            field=models.FileField(blank=True, null=True, upload_to='banner'),
        ),
        migrations.AddField(
            model_name='homebanner',
            name='contacts',
            field=models.FileField(blank=True, null=True, upload_to='banner'),
        ),
        migrations.AddField(
            model_name='homebanner',
            name='issues',
            field=models.FileField(blank=True, null=True, upload_to='banner'),
        ),
    ]
