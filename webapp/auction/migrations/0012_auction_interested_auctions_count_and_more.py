# Generated by Django 4.0.6 on 2022-08-09 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0011_alter_interestedauction_auction'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='interested_auctions_count',
            field=models.PositiveIntegerField(default=0, verbose_name='관심 수'),
        ),
        migrations.AlterField(
            model_name='auction',
            name='product_groups_count',
            field=models.PositiveIntegerField(default=0, verbose_name='참여자 수'),
        ),
    ]
