# Generated by Django 4.2.7 on 2023-11-17 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0007_order_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='type',
            field=models.CharField(choices=[('Syrup', 'Syrup'), ('Tablet', 'Tablet'), ('Vitamin', 'Vitamin')], max_length=50),
        ),
    ]
