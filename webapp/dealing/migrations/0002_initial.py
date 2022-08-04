# Generated by Django 4.0.6 on 2022-08-04 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dealing', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealing',
            name='product',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='물품'),
        ),
        migrations.AddField(
            model_name='dealing',
            name='product_group',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='product.productgroup', verbose_name='물품 그룹'),
        ),
    ]
