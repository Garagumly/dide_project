# Generated by Django 3.2.7 on 2023-10-30 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_mainslider'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainslider',
            name='title',
            field=models.CharField(default='Slider', max_length=100),
        ),
    ]