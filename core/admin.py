from django.contrib import admin
from core.models import *
from modeltranslation.admin import TranslationAdmin


class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages


class ProductAttributeValueInline(admin.TabularInline):
        model = ProductAttributeValue
    
@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
        inlines = [ProductAttributeValueInline]

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    inlines = [ProductImagesAdmin]
    list_editable = ['title', 'price', 'featured', 'product_status']
    list_display = ['user', 'title', 'product_image', 'price', 'category', 'vendor', 'featured', 'product_status', 'pid']

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



# class ProductAdmin(admin.ModelAdmin):
#     inlines = [ProductImagesAdmin]
#     list_editable = ['title', 'price', 'featured', 'product_status']
#     list_display = ['user', 'title', 'product_image', 'price', 'category', 'vendor', 'featured', 'product_status', 'pid']



# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['title', 'category_image']


# class VendorAdmin(admin.ModelAdmin):
#     list_display = ['title', 'vendor_image']


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
    # list_editable = ['hours', 'mail', 'address', 'phone']
    list_display = ['name', 'main_image', 'from_hours', 'to_hours', 'mail', 'address', 'phone']

class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'slider_image']

class BrandAdmin(admin.ModelAdmin):
    list_display = ['title',]


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ['title',]


# class ProductAttributeValueAdmin(admin.ModelAdmin):
#     list_display = ['product_attribute', 'attribute_value',]


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = [ 'title',]

# admin.site.register(Product, ProductAdmin) 
# admin.site.register(Product, ProductAdmin)    
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Vendor, VendorAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderProducts, CartOrderProductsAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(wishlist_model, wishlistAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(MainInfo, MainInfoAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Brand, BrandAdmin)
# admin.site.register(ProductAttribute, ProductAttributeAdmin)
# admin.site.register(ProductAttributeValue, ProductAttributeValueInline)
# admin.site.register(ProductAttributeValue, ProductAttributeValueAdmin)
admin.site.register(ProductType, ProductTypeAdmin)



