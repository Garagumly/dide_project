# Generated by Django 3.2.7 on 2023-12-07 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_category_ordering'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='ordering',
        ),
    ]
