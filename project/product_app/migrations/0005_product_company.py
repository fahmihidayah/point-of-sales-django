# Generated by Django 4.0.6 on 2022-09-28 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company_app', '0001_initial'),
        ('product_app', '0004_alter_product_price_alter_product_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='company',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='company_app.company'),
        ),
    ]