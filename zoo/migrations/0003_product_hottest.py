# Generated by Django 4.1.7 on 2023-06-21 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0002_alter_product_name_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='hottest',
            field=models.BooleanField(default=False, verbose_name='Является горячим предложением'),
        ),
    ]
