# Generated by Django 3.0.8 on 2020-08-07 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0007_auto_20200805_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='new',
        ),
    ]