# Generated by Django 3.2.7 on 2023-10-26 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20231027_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_sale_status',
            field=models.CharField(blank=True, choices=[('hot', 'Hot'), ('sale', 'Sale'), ('new', 'New'), ('deal', 'Deal')], max_length=10, null=True),
        ),
    ]