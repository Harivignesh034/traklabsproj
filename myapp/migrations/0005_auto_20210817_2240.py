# Generated by Django 3.1.4 on 2021-08-17 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20210817_2231'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='myapp_Departments',
            new_name='Departments',
        ),
        migrations.RenameModel(
            old_name='myapp_employees',
            new_name='employees',
        ),
    ]
