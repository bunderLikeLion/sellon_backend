# Generated by Django 4.0.6 on 2022-08-01 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0003_alter_auction_dealing_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='end_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='경매 종료 일시'),
        ),
    ]
