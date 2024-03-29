# Generated by Django 4.0.6 on 2022-08-06 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0010_interestedauction_unique_interested_auction_by_user'),
        ('dealing', '0002_remove_dealing_deleted_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dealing',
            name='status',
        ),
        migrations.AddField(
            model_name='dealing',
            name='auction',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dealing', to='auction.auction', verbose_name='경매장'),
        ),
    ]
