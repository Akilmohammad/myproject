# Generated by Django 3.1.2 on 2020-12-08 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0049_transaction_fname'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='lname',
            field=models.CharField(default='', max_length=20),
        ),
    ]
