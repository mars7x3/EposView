# Generated by Django 4.1.4 on 2022-12-22 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('instagram', models.CharField(blank=True, max_length=100, null=True)),
                ('whatsapp', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('vk', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.FileField(blank=True, null=True, upload_to='logo')),
                ('banner', models.FileField(blank=True, null=True, upload_to='banner')),
            ],
        ),
        migrations.CreateModel(
            name='ContactsPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priem', models.CharField(blank=True, max_length=50, null=True)),
                ('faqs', models.CharField(blank=True, max_length=50, null=True)),
                ('epos_contacts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='magazine.epos_contacts')),
            ],
        ),
    ]