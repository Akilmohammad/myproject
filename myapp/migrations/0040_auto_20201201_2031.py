# Generated by Django 3.1.1 on 2020-12-01 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0039_auto_20201201_2027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='men_accessories',
            name='men_acc_size',
        ),
        migrations.RemoveField(
            model_name='women_accessories',
            name='women_acc_size',
        ),
    ]
