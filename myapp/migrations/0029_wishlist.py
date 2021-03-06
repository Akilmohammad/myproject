# Generated by Django 3.1.2 on 2020-11-30 06:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_auto_20201128_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='WISHLIST',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_date', models.DateField(default=django.utils.timezone.now)),
                ('men_acc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.men_accessories')),
                ('men_cloth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.men_cloth')),
                ('men_footwear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.men_footwear')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
                ('women_acc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.women_accessories')),
                ('women_cloth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.women_cloth')),
                ('women_footwear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.women_footwear')),
            ],
        ),
    ]
