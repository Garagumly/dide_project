# Generated by Django 3.2.7 on 2023-11-16 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20231116_1137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productattribute',
            old_name='name',
            new_name='title',
        ),
    ]
