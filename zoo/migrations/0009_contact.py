# Generated by Django 4.1.7 on 2023-06-23 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0008_remove_product_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('message', models.TextField(max_length=1000)),
            ],
        ),
    ]
