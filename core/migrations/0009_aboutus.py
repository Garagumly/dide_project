# Generated by Django 3.2.7 on 2023-12-09 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_category_ordering'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='logo.png', upload_to='base-index')),
                ('title', models.CharField(max_length=100)),
                ('title_ru', models.CharField(max_length=100, null=True)),
                ('title_tk', models.CharField(max_length=100, null=True)),
                ('title_en', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_ru', models.TextField(blank=True, null=True)),
                ('description_tk', models.TextField(blank=True, null=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('we', models.TextField(blank=True, help_text='кто мы', null=True)),
                ('we_ru', models.TextField(blank=True, help_text='кто мы', null=True)),
                ('we_tk', models.TextField(blank=True, help_text='кто мы', null=True)),
                ('we_en', models.TextField(blank=True, help_text='кто мы', null=True)),
                ('history', models.TextField(blank=True, help_text='наша история', null=True)),
                ('history_ru', models.TextField(blank=True, help_text='наша история', null=True)),
                ('history_tk', models.TextField(blank=True, help_text='наша история', null=True)),
                ('history_en', models.TextField(blank=True, help_text='наша история', null=True)),
                ('mission', models.TextField(blank=True, help_text='наша миссия', null=True)),
                ('mission_ru', models.TextField(blank=True, help_text='наша миссия', null=True)),
                ('mission_tk', models.TextField(blank=True, help_text='наша миссия', null=True)),
                ('mission_en', models.TextField(blank=True, help_text='наша миссия', null=True)),
            ],
            options={
                'verbose_name': 'Информация О нас',
                'verbose_name_plural': 'Информация О нас',
            },
        ),
    ]
