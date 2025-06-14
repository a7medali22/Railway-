# Generated by Django 5.1.7 on 2025-05-19 15:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0014_merge_0012_system_uuid_0013_system_uuid"),
    ]

    operations = [
        migrations.AddField(
            model_name="system",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="system",
            name="custom_domain",
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="system",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="system",
            name="ssl_enabled",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="system",
            name="updated_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="system",
            name="category",
            field=models.CharField(
                choices=[("restaurant", "Restaurant"), ("supermarket", "Supermarket")],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="system",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
