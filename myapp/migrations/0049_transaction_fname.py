# Generated by Django 3.1.2 on 2020-12-04 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0048_checkout_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='fname',
            field=models.CharField(default='', max_length=20),
        ),
    ]
