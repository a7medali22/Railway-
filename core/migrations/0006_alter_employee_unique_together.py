# Generated by Django 5.1.7 on 2025-04-28 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_alter_employee_user"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="employee",
            unique_together=set(),
        ),
    ]
