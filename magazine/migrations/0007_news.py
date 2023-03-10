# Generated by Django 4.1.4 on 2022-12-23 18:07

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0006_homestatistic'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='news')),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('Text', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
