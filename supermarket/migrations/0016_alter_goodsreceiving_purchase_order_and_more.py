# Generated by Django 4.1.2 on 2025-06-11 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket', '0015_alter_purchaseorder_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsreceiving',
            name='purchase_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_receiving', to='supermarket.purchaseorder'),
        ),
        migrations.AlterField(
            model_name='productbatch',
            name='purchase_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='batches', to='supermarket.purchaseorder'),
        ),
    ]
