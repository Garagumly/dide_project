# Generated by Django 3.2.7 on 2023-11-03 14:00

import ckeditor_uploader.fields
import core.models
from django.db import migrations, models
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_category_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, prefix='kat', unique=True)),
                ('title', models.CharField(default='Parcel', max_length=100)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='I am am Amazing Kategory', null=True)),
                ('image', models.ImageField(default='logo.jpg', upload_to=core.models.user_directory_path)),
            ],
            options={
                'verbose_name_plural': 'Kategories',
            },
        ),
    ]
