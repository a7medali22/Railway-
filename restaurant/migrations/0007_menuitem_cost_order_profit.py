# Generated by Django 5.1.7 on 2025-04-30 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0006_alter_menuitem_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="menuitem",
            name="cost",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name="order",
            name="profit",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
