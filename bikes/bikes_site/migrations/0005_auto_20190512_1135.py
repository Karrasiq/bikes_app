# Generated by Django 2.1.4 on 2019-05-12 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikes_site', '0004_manager'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Motobike',
            new_name='Product',
        ),
    ]