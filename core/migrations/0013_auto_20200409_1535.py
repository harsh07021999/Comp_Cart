# Generated by Django 2.2 on 2020-04-09 10:05

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_order_billing_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billingaddress',
            name='countries',
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='country',
            field=django_countries.fields.CountryField(default='India', max_length=2),
            preserve_default=False,
        ),
    ]
