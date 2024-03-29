# Generated by Django 4.1 on 2022-08-16 21:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_user_avatar'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auction', '0014_auction_participants_alter_auction_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='participants',
            field=models.ManyToManyField(related_name='participating_auctions', through='product.ProductGroup', to=settings.AUTH_USER_MODEL),
        ),
    ]
