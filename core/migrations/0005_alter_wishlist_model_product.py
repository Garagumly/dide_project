# Generated by Django 3.2.7 on 2023-12-04 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20231204_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist_model',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.product'),
        ),
    ]
