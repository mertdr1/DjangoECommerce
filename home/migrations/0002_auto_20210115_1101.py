# Generated by Django 3.1.5 on 2021-01-15 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Settings',
            new_name='Setting',
        ),
    ]