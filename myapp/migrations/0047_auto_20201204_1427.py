# Generated by Django 3.1.2 on 2020-12-04 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0046_auto_20201204_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='lname',
        ),
    ]
