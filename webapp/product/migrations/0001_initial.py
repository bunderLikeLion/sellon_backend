# Generated by Django 4.0.6 on 2022-07-26 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='추가된 일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정된 일시')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='삭제된 일시')),
                ('name', models.CharField(max_length=100, verbose_name='물품 명')),
                ('description', models.TextField(blank=True, max_length=300, null=True, verbose_name='물품 설명')),
                ('quality', models.IntegerField(default=1, verbose_name='수량')),
                ('abstract', models.CharField(blank=True, max_length=100, null=True, verbose_name='요약')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'products',
            },
        ),
    ]
