# Generated by Django 4.1.4 on 2023-02-01 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='product-img'),
        ),
    ]
