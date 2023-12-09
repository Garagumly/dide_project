from .models import AboutUs, ProductType, ProductAttribute, Category, Product, Vendor
from modeltranslation.translator import TranslationOptions, register

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Vendor)
class VendorTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(AboutUs)
class VendorTranslationOptions(TranslationOptions):
    fields = ('title', 'description','we', 'history', 'mission')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ['title']

@register(ProductAttribute)
class ProductAttributeTranslationOptions(TranslationOptions):
    fields = ['title']

@register(ProductType)
class ProductTypeTranslationOptions(TranslationOptions):
    fields = ['title']