# Generated by Django 4.1.7 on 2023-06-21 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0003_product_hottest'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(default=1, upload_to='%Y/%m/%d/', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]