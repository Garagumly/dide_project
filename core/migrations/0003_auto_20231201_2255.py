# Generated by Django 3.2.7 on 2023-12-01 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20231127_1558'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Адреса пользователей'},
        ),
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name_plural': 'Бренды'},
        ),
        migrations.AlterModelOptions(
            name='cartorder',
            options={'verbose_name_plural': 'Корзина (Заказы)'},
        ),
        migrations.AlterModelOptions(
            name='cartorderproducts',
            options={'verbose_name_plural': 'Корзина (Товары)'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='maininfo',
            options={'verbose_name_plural': 'Основная информация'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='productattribute',
            options={'verbose_name_plural': 'Атрибуты'},
        ),
        migrations.AlterModelOptions(
            name='productattributevalue',
            options={'verbose_name_plural': 'Значение атрибута'},
        ),
        migrations.AlterModelOptions(
            name='productattributevalues',
            options={'verbose_name_plural': 'Атрибуты товаров'},
        ),
        migrations.AlterModelOptions(
            name='productimages',
            options={'verbose_name_plural': 'Изображения товаров'},
        ),
        migrations.AlterModelOptions(
            name='productreview',
            options={'verbose_name_plural': 'Обзоры продуктов'},
        ),
        migrations.AlterModelOptions(
            name='producttype',
            options={'verbose_name_plural': 'Виды товаров'},
        ),
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name_plural': 'Слайдеры'},
        ),
        migrations.AlterModelOptions(
            name='vendor',
            options={'verbose_name_plural': 'Магазины'},
        ),
        migrations.AlterModelOptions(
            name='wishlist_model',
            options={'verbose_name_plural': 'Избранные'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='cid_en',
        ),
        migrations.RemoveField(
            model_name='category',
            name='cid_ru',
        ),
        migrations.RemoveField(
            model_name='category',
            name='cid_tk',
        ),
        migrations.RemoveField(
            model_name='productattribute',
            name='attid_en',
        ),
        migrations.RemoveField(
            model_name='productattribute',
            name='attid_ru',
        ),
        migrations.RemoveField(
            model_name='productattribute',
            name='attid_tk',
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='didecat.jpeg', upload_to='category_imgs'),
        ),
        migrations.AlterField(
            model_name='maininfo',
            name='image',
            field=models.ImageField(default='logo.png', upload_to='base-index'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='didecat.jpeg', upload_to='product-images'),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='images',
            field=models.ImageField(default='didecat.jpeg', upload_to='product-images'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(default='logo.png', upload_to='base-index'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='cover_image',
            field=models.ImageField(default='logo.png', upload_to='product-images'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='image',
            field=models.ImageField(default='logo.png', upload_to='product-images'),
        ),
        migrations.AlterUniqueTogether(
            name='productattributevalues',
            unique_together=set(),
        ),
    ]
