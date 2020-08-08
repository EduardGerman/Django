# Generated by Django 3.0.8 on 2020-08-01 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, default=None, max_length=60, null=True)),
                ('category_slug', models.SlugField(max_length=200, unique=True)),
                ('category_img', models.ImageField(blank=True, null=True, upload_to='media')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['category_name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, default=None, max_length=60, null=True)),
                ('product_slug', models.SlugField(default=None, max_length=200)),
                ('product_description', models.TextField()),
                ('product_img', models.ImageField(blank=True, null=True, upload_to='media')),
                ('product_price', models.FloatField(default=0.0)),
                ('product_available', models.BooleanField(default=True)),
                ('product_stock', models.PositiveIntegerField(default=0)),
                ('product_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.Category')),
            ],
            options={
                'ordering': ['product_name'],
                'index_together': {('id', 'product_slug')},
            },
        ),
    ]