# Generated by Django 3.2.7 on 2023-11-16 06:30

from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='bid',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, prefix='bran', unique=True),
        ),
        migrations.AddField(
            model_name='productattribute',
            name='attid',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, prefix='att', unique=True),
        ),
        migrations.RemoveField(
            model_name='product',
            name='attribute_values',
        ),
        migrations.AddField(
            model_name='product',
            name='attribute_values',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_attribute_values', to='core.productattributevalue'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='brand', to='core.brand'),
        ),
    ]