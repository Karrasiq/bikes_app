# Generated by Django 2.1.4 on 2019-05-12 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikes_site', '0005_auto_20190512_1135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manager',
            old_name='company',
            new_name='company_name',
        ),
        migrations.RenameField(
            model_name='manager',
            old_name='user',
            new_name='user_name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='category_name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='company',
            new_name='company_name',
        ),
    ]
