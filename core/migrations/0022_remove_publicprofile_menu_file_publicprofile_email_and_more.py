# Generated by Django 5.1.7 on 2025-06-10 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0021_system_custom_link_system_latitude_system_longitude_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="publicprofile",
            name="menu_file",
        ),
        migrations.AddField(
            model_name="publicprofile",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name="publicprofile",
            name="whatsapp_number",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="system",
            name="description",
            field=models.TextField(blank=True),
        ),
    ]
