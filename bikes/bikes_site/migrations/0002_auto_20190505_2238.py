# Generated by Django 2.1.4 on 2019-05-05 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motobike',
            name='description',
            field=models.TextField(default='', null=True),
        ),
    ]
