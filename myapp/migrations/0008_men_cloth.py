# Generated by Django 3.1.2 on 2020-11-17 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20201111_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='MEN_CLOTH',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('men_cloth_category', models.CharField(choices=[('shirt', 'shirt'), ('t-shirt', 't-shirt'), ('jeans', 'jeans'), ('jackets', 'jackets'), ('casual', 'casual')], default='', max_length=100)),
                ('men_cloth_name', models.CharField(max_length=100)),
                ('men_cloth_price', models.CharField(max_length=100)),
                ('men_cloth_brand', models.CharField(max_length=100)),
                ('men_cloth_desc', models.TextField()),
                ('men_cloth_image', models.ImageField(default='', upload_to='men_cloths/')),
                ('user', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
