# Generated by Django 3.1.2 on 2020-11-11 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_delete_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='women_cloth',
            name='women_cloth_image',
            field=models.ImageField(default='', upload_to='women_cloths/'),
        ),
    ]