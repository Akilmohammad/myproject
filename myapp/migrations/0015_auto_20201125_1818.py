# Generated by Django 3.1.2 on 2020-11-25 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_women_cloth_women_cloth_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='men_accessories',
            name='men_acc_stock',
            field=models.CharField(default='Available', max_length=100),
        ),
        migrations.AddField(
            model_name='men_cloth',
            name='men_cloth_stock',
            field=models.CharField(default='Available', max_length=100),
        ),
        migrations.AddField(
            model_name='men_footwear',
            name='men_footwear_stock',
            field=models.CharField(default='Available', max_length=100),
        ),
        migrations.AddField(
            model_name='women_accessories',
            name='women_acc_stock',
            field=models.CharField(default='Available', max_length=100),
        ),
        migrations.AddField(
            model_name='women_footwear',
            name='women_footwear_stock',
            field=models.CharField(default='Available', max_length=100),
        ),
    ]
