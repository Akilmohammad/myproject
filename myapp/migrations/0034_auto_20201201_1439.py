# Generated by Django 3.1.1 on 2020-12-01 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0033_women_cloth_women_cloth_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='men_acc',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='men_cloth',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='men_footwear',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='women_acc',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='women_footwear',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='men_acc',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='men_cloth',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='men_footwear',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='women_acc',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='women_footwear',
        ),
    ]
