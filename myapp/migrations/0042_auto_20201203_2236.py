# Generated by Django 3.1.2 on 2020-12-03 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0041_auto_20201203_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='add1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='add2',
            field=models.CharField(max_length=50),
        ),
    ]
