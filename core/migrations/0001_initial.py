# Generated by Django 3.2.7 on 2023-11-27 10:02

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, prefix='bran', unique=True)),
                ('title', models.CharField(blank=True, default='Luminarc', max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='CartOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default='1.99', max_digits=99999999999999)),
                ('paid_status', models.BooleanField(blank=True, default=False, null=True)),
                ('order_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('product_status', models.CharField(choices=[('processing', 'Processing'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='processing', max_length=30)),
                ('sku', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', blank=True, length=5, max_length=20, null=True, prefix='SKU')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Cart Order',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, prefix='cat', unique=True)),
                ('cid_ru', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, null=True, prefix='cat', unique=True)),
                ('cid_tk', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, null=True, prefix='cat', unique=True)),
                ('cid_en', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, null=True, prefix='cat', unique=True)),
                ('title', models.CharField(default='Parcel', max_length=100)),
                ('title_ru', models.CharField(default='Parcel', max_length=100, null=True)),
                ('title_tk', models.CharField(default='Parcel', max_length=100, null=True)),
                ('title_en', models.CharField(default='Parcel', max_length=100, null=True)),
                ('image', models.ImageField(default='logo.jpg', upload_to='category_imgs')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='core.category', verbose_name='parent of category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='MainInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Dide', max_length=100)),
                ('from_hours', models.TimeField(blank=True, null=True)),
                ('to_hours', models.TimeField(blank=True, null=True)),
                ('mail', models.CharField(default='dide@gmail.com.', max_length=100)),
                ('address', models.CharField(default='123 Main Street.', max_length=100)),
                ('phone', models.CharField(default='+123 (456) 789', max_length=100)),
                ('image', models.ImageField(default='logo.jpg', upload_to='base-index')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, prefix='', unique=True)),
                ('title', models.CharField(default='Fresh Pear', max_length=100)),
                ('title_ru', models.CharField(default='Fresh Pear', max_length=100, null=True)),
                ('title_tk', models.CharField(default='Fresh Pear', max_length=100, null=True)),
                ('title_en', models.CharField(default='Fresh Pear', max_length=100, null=True)),
                ('image', models.ImageField(default='product.jpg', upload_to='product-images')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='This is the product', null=True)),
                ('description_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='This is the product', null=True)),
                ('description_tk', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='This is the product', null=True)),
                ('description_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='This is the product', null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=99999999999999)),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, max_digits=99999999999999, null=True)),
                ('stock_count', models.CharField(blank=True, default='10', max_length=100, null=True)),
                ('product_status', models.CharField(choices=[('draft', 'Draft'), ('disabled', 'Disabled'), ('rejected', 'Rejected'), ('in_review', 'In Review'), ('published', 'Published')], default='in_review', max_length=10)),
                ('product_sale_status', models.CharField(blank=True, choices=[('hot', 'Hot'), ('sale', 'Sale'), ('new', 'New'), ('deal', 'Deal')], max_length=10, null=True)),
                ('product_mainpage_status', models.CharField(blank=True, choices=[('new', 'New Products'), ('top_selling', 'Top Selling'), ('trending_products', 'Trending Products'), ('recent', 'Recently Added'), ('top_rated', 'Top Rated')], max_length=20, null=True)),
                ('deal_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('in_stock', models.BooleanField(default=True)),
                ('featured', models.BooleanField(default=False)),
                ('sku', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=4, max_length=10, prefix='sku', unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='brand', to='core.brand')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='category', to='core.category')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, prefix='att', unique=True)),
                ('attid_ru', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, null=True, prefix='att', unique=True)),
                ('attid_tk', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, null=True, prefix='att', unique=True)),
                ('attid_en', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, null=True, prefix='att', unique=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('title_ru', models.CharField(blank=True, max_length=255, null=True)),
                ('title_tk', models.CharField(blank=True, max_length=255, null=True)),
                ('title_en', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductAttributeValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_value', models.CharField(blank=True, max_length=255, null=True)),
                ('product_attribute', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_attribute', to='core.productattribute')),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Parcel', max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Slider', max_length=100)),
                ('image', models.ImageField(default='logo.jpg', upload_to='base-index')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='wishlist_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'wishlists',
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, prefix='ven', unique=True)),
                ('title', models.CharField(default='Dide', max_length=100)),
                ('title_ru', models.CharField(default='Dide', max_length=100, null=True)),
                ('title_tk', models.CharField(default='Dide', max_length=100, null=True)),
                ('title_en', models.CharField(default='Dide', max_length=100, null=True)),
                ('image', models.ImageField(default='vendor.jpg', upload_to='product-images')),
                ('cover_image', models.ImageField(default='vendor.jpg', upload_to='product-images')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='I am am Amazing Vendor', null=True)),
                ('description_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='I am am Amazing Vendor', null=True)),
                ('description_tk', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='I am am Amazing Vendor', null=True)),
                ('description_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='I am am Amazing Vendor', null=True)),
                ('address', models.CharField(default='123 Main Street.', max_length=100)),
                ('contact', models.CharField(default='+123 (456) 789', max_length=100)),
                ('chat_resp_time', models.CharField(default='100', max_length=100)),
                ('shipping_on_time', models.CharField(default='100', max_length=100)),
                ('authentic_rating', models.CharField(default='100', max_length=100)),
                ('days_return', models.CharField(default='100', max_length=100)),
                ('warranty_period', models.CharField(default='100', max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Vendors',
            },
        ),
        migrations.CreateModel(
            name='ProductTypeAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_attribute', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='productattribute', to='core.productattribute')),
                ('product_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='producttype', to='core.producttype')),
            ],
            options={
                'unique_together': {('product_attribute', 'product_type')},
            },
        ),
        migrations.AddField(
            model_name='producttype',
            name='product_type_attributes',
            field=models.ManyToManyField(related_name='product_type_attributes', through='core.ProductTypeAttribute', to='core.ProductAttribute'),
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('rating', models.IntegerField(choices=[(1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★')], default=None)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='core.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Product Reviews',
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(default='product.jpg', upload_to='product-images')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p_images', to='core.product')),
            ],
            options={
                'verbose_name_plural': 'Product Images',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_type', to='core.producttype'),
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='product', to='core.vendor'),
        ),
        migrations.CreateModel(
            name='CartOrderProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.CharField(max_length=200)),
                ('product_status', models.CharField(max_length=200)),
                ('item', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('qty', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, default='1.99', max_digits=99999999999999)),
                ('total', models.DecimalField(decimal_places=2, default='1.99', max_digits=99999999999999)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cartorder')),
            ],
            options={
                'verbose_name_plural': 'Cart Order Items',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=300, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Address',
            },
        ),
        migrations.CreateModel(
            name='ProductAttributeValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attributevalues', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attributevaluess', to='core.productattributevalue')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='productattributevaluess', to='core.product')),
            ],
            options={
                'unique_together': {('attributevalues', 'product')},
            },
        ),
    ]
