# Generated by Django 4.0 on 2022-01-10 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_product_img1_product_img2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cat_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='producttocat', to='Product.category'),
        ),
    ]