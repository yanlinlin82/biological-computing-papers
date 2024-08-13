# Generated by Django 5.1 on 2024-08-12 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_payment_paid_amount_payment_payment_callback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, unique=True)),
                ('abbreviation', models.CharField(max_length=32, unique=True)),
                ('impact_factor', models.DecimalField(blank=True, decimal_places=3, default=None, max_digits=6, null=True)),
                ('impact_factor_year', models.IntegerField(blank=True, default=None, null=True)),
                ('impact_factor_quartile', models.CharField(blank=True, default=None, max_length=1, null=True)),
            ],
        ),
    ]