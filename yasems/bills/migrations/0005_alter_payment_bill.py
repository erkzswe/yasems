# Generated by Django 5.0.2 on 2024-06-23 08:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bills", "0004_payment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="bill",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="payments",
                to="bills.bill",
            ),
        ),
    ]