# Generated by Django 4.0.6 on 2022-07-31 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0003_alter_auction_dealing_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='product_groups_count',
            field=models.IntegerField(default=0, null=True, verbose_name='참여자 수'),
        ),
    ]
