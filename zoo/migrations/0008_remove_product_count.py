# Generated by Django 4.1.7 on 2023-06-23 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0007_product_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='count',
        ),
    ]