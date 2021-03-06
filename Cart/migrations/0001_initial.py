# Generated by Django 4.0 on 2022-01-08 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='CartMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priceTotla', models.PositiveIntegerField(blank=True, null=True, verbose_name='priceTotla')),
                ('discount', models.CharField(max_length=10, verbose_name='discount')),
                ('date', models.DateTimeField(auto_now=True)),
                ('ispaid', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Cart',
                'verbose_name_plural': 'Carts',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('factor', models.JSONField(blank=True, help_text='فاکتور خرید', null=True, verbose_name='factor')),
                ('cartme', models.ManyToManyField(help_text='کالاها', to='Cart.CartMe')),
            ],
            options={
                'verbose_name': 'History',
                'verbose_name_plural': 'Historys',
            },
        ),
    ]
