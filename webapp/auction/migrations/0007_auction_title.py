# Generated by Django 4.0.6 on 2022-08-02 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0006_remove_auction_deleted_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='title',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='경매 제목'),
        ),
    ]
