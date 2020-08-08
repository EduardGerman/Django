# Generated by Django 3.0.8 on 2020-07-30 21:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0008_auto_20200730_2241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='slider_discount_date',
        ),
        migrations.AddField(
            model_name='slider',
            name='slider_discount_date_main',
            field=models.DurationField(default=datetime.timedelta(seconds=2400)),
        ),
    ]