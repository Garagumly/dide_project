from django.contrib import admin
from core.models import *
from modeltranslation.admin import TranslationAdmin


class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages

class ProductAttributeValuesAdmin(admin.TabularInline):
    model = ProductAttributeValues

class ProductAttributeValueInline(admin.TabularInline):
        model = ProductAttributeValue
    
@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    inlines = [ProductAttributeValueInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    inlines = [ProductImagesAdmin, ProductAttributeValuesAdmin]
    list_editable = [ 'price', 'featured', 'product_status']
    list_display = [ 'title', 'product_image', 'price', 'category', 'vendor', 'featured', 'product_status', 'pid']

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Vendor)
class VendorAdmin(TranslationAdmin):
    list_display = ['title', 'vendor_image']

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(AboutUs)
class AboutUsAdmin(TranslationAdmin):
    list_display = ['title', 'main_image', 'description', 'we', 'history', 'mission',]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ['title', 'category_image']

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



class CartOrderAdmin(admin.ModelAdmin):
    list_editable = ['paid_status', 'product_status', 'sku']
    list_display = ['user',  'price', 'paid_status', 'order_date','product_status', 'sku']


class CartOrderProductsAdmin(admin.ModelAdmin):
    list_display = ['order', 'invoice_no', 'item', 'order_img','qty', 'price', 'total']


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'review', 'rating']


class wishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'date']


class AddressAdmin(admin.ModelAdmin):
    list_editable = ['address', 'status']
    list_display = ['user', 'address', 'status']

class MainInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'main_image', 'from_hours', 'to_hours', 'mail', 'address', 'phone']
    

class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'slider_image']

class BrandAdmin(admin.ModelAdmin):
    list_display = ['title',]


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ['title',]


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = [ 'title',]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderProducts, CartOrderProductsAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(wishlist_model, wishlistAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(MainInfo, MainInfoAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(ProductType, ProductTypeAdmin)



