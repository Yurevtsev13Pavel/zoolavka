# Generated by Django 4.1.7 on 2023-06-22 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0004_product_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='hottest',
        ),
    ]