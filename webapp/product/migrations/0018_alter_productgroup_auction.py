# Generated by Django 4.0.6 on 2022-08-06 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0010_interestedauction_unique_interested_auction_by_user'),
        ('product', '0017_alter_productgroup_auction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productgroup',
            name='auction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_groups', to='auction.auction', verbose_name='경매'),
        ),
    ]
