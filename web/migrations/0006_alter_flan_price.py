# Generated by Django 5.0.6 on 2024-07-20 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_flan_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flan',
            name='price',
            field=models.DecimalField(decimal_places=0, default='0', max_digits=10),
        ),
    ]
