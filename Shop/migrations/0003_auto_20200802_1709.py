# Generated by Django 3.0.8 on 2020-08-02 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0002_auto_20200802_1548'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_available',
            new_name='available',
        ),
    ]
