# Generated by Django 4.0.6 on 2022-10-07 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company_app', '0001_initial'),
        ('order_item_app', '0003_remove_orderitem_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='company',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='company_app.company'),
        ),
    ]