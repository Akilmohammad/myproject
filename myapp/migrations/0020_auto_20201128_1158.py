# Generated by Django 3.1.2 on 2020-11-28 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_auto_20201128_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='men_accessories',
            name='men_acc_image1',
        ),
        migrations.RemoveField(
            model_name='men_accessories',
            name='men_acc_image2',
        ),
        migrations.RemoveField(
            model_name='men_accessories',
            name='men_acc_image3',
        ),
    ]
