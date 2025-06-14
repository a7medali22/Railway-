# Generated by Django 5.1.7 on 2025-05-01 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_alter_employee_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="role",
            field=models.CharField(
                choices=[
                    ("waiter", "Waiter"),
                    ("chef", "Chef"),
                    ("delivery", "Delivery"),
                    ("manager", "Manager"),
                ],
                max_length=50,
            ),
        ),
    ]
