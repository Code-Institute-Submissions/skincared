# Generated by Django 3.2 on 2022-09-24 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'ordering': ['friendly_name']},
        ),
        migrations.AlterModelOptions(
            name='producttype',
            options={'verbose_name_plural': 'Product Type'},
        ),
        migrations.AlterModelOptions(
            name='skincare',
            options={'verbose_name_plural': 'Skincare'},
        ),
    ]
