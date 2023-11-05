# Generated by Django 3.2.7 on 2023-10-26 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20231026_1039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='digital',
        ),
        migrations.RemoveField(
            model_name='product',
            name='life',
        ),
        migrations.RemoveField(
            model_name='product',
            name='mfd',
        ),
        migrations.RemoveField(
            model_name='product',
            name='updated',
        ),
        migrations.AddField(
            model_name='product',
            name='deal_product',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_sale_status',
            field=models.CharField(blank=True, choices=[('hot', 'Hot'), ('sale', 'Sale'), ('new', 'New')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=99999999999999, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=99999999999999),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
