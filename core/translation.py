from .models import Product, Category, Vendor
from modeltranslation.translator import TranslationOptions, register

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Vendor)
class VendorTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


# @register(Category)
# class CategoryTranslationOptions(TranslationOptions):
#     fields = ('cid')