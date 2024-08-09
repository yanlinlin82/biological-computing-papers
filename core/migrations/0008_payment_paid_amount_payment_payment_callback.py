# Generated by Django 5.1 on 2024-08-10 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_payment_order_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='paid_amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_callback',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
