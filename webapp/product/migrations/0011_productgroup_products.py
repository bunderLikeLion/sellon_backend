# Generated by Django 4.0.6 on 2022-08-01 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_alter_product_quality'),
    ]

    operations = [
        migrations.AddField(
            model_name='productgroup',
            name='products',
            field=models.ManyToManyField(through='product.ProductGroupItem', to='product.product'),
        ),
    ]
