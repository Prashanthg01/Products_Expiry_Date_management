# Generated by Django 4.1.7 on 2023-03-27 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0004_product_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
    ]
