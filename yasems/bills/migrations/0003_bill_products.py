# Generated by Django 5.0.2 on 2024-06-15 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bills", "0002_alter_bill_contributors"),
    ]

    operations = [
        migrations.AddField(
            model_name="bill",
            name="products",
            field=models.ManyToManyField(
                blank=True, related_name="bills", to="bills.product"
            ),
        ),
    ]
