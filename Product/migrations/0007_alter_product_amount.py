# Generated by Django 4.0 on 2022-01-27 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0006_alter_category_sub_cat_alter_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.PositiveIntegerField(null=True),
        ),
    ]