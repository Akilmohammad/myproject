# Generated by Django 3.1.2 on 2020-12-14 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0054_auto_20201209_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='item_size',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
