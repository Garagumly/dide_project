from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import User
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import  RichTextUploadingField


STATUS_CHOICE = (
    ("processing", "Processing"),
    ("shipped", "Shipped"),
    ("delivered", "Delivered"),
)


STATUS = (
    ("draft", "Draft"),
    ("disabled", "Disabled"),
    ("rejected", "Rejected"),
    ("in_review", "In Review"),
    ("published", "Published"),
)



RATING = (
    ( 1,  "★☆☆☆☆"),
    ( 2,  "★★☆☆☆"),
    ( 3,  "★★★☆☆"),
    ( 4,  "★★★★☆"),
    ( 5,  "★★★★★"),
)

SALE_STATUS = (
    ("hot", "Hot"),
    ("sale", "Sale"),
    ("new", "New"),
    ("deal", "Deal"),
)

MAINPAGE_STATUS = (
    ("new", "New Products"),
    ("top_selling", "Top Selling"),
    ("trending_products", "Trending Products"),
    ("recent", "Recently Added"),
    ("top_rated", "Top Rated"),
)



def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Slider(models.Model):
    title = models.CharField(max_length=100, default="Slider")
    image = models.ImageField(upload_to="base-index", default="logo.jpg")

class Banner(models.Model):
    banner_1 = models.ImageField(upload_to="base-index", default="logo.jpg")
    banner_2 = models.ImageField(upload_to="base-index", default="logo.jpg")
    banner_3 = models.ImageField(upload_to="base-index", default="logo.jpg")
    banner_4 = models.ImageField(upload_to="base-index", default="logo.jpg")

class MainInfo(models.Model):
    name = models.CharField(max_length=100, default="Dide")
    from_hours = models.TimeField( null=True, blank=True)
    to_hours = models.TimeField( null=True, blank=True)
    mail = models.CharField(max_length=100, default="dide@gmail.com.")
    address = models.CharField(max_length=100, default="123 Main Street.")
    phone = models.CharField(max_length=100, default="+123 (456) 789")
    image = models.ImageField(upload_to="base-index", default="logo.jpg")

# class Category(models.Model):
#     cid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="cat", alphabet="abcdefgh12345")

#     title = models.CharField(max_length=100, default="Food")
#     image = models.ImageField(upload_to="category", default="category.jpg")

#     class Meta:
#         verbose_name_plural = "Categories"

#     def category_image(self):
#         return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

#     def __str__(self):
#         return self.title

class Category(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="cat", alphabet="abcdefgh12345")

    title = models.CharField(max_length=100, default="Food")
    image = models.ImageField(upload_to="category", default="logo.jpg")

    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title



class Tags(models.Model):
    pass


class Vendor(models.Model):
    vid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="ven", alphabet="abcdefgh12345")

    title = models.CharField(max_length=100, default="Nestify")
    image = models.ImageField(upload_to="product-images", default="vendor.jpg")
    cover_image = models.ImageField(upload_to="product-images", default="vendor.jpg")
    # description = models.TextField(null=True, blank=True, default="I am am Amazing Vendor")
    description = RichTextUploadingField(null=True, blank=True, default="I am am Amazing Vendor")

    address = models.CharField(max_length=100, default="123 Main Street.")
    contact = models.CharField(max_length=100, default="+123 (456) 789")
    chat_resp_time = models.CharField(max_length=100, default="100")
    shipping_on_time = models.CharField(max_length=100, default="100")
    authentic_rating = models.CharField(max_length=100, default="100")
    days_return = models.CharField(max_length=100, default="100")
    warranty_period = models.CharField(max_length=100, default="100")

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Vendors"

    def vendor_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title


class Product(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=20, alphabet="abcdefgh12345")

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="category")
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, related_name="product")

    title = models.CharField(max_length=100, default="Fresh Pear")
    image = models.ImageField(upload_to="product-images", default="product.jpg")
    # description = models.TextField(null=True, blank=True, default="This is the product")
    description = RichTextUploadingField(null=True, blank=True, default="This is the product")

    price = models.DecimalField(max_digits=99999999999999, decimal_places=2,)
    old_price = models.DecimalField(max_digits=99999999999999, decimal_places=2, null=True, blank=True)

    # specifications = RichTextUploadingField(null=True, blank=True)
    # specifications = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    stock_count = models.CharField(max_length=100, default="10", null=True, blank=True)
    # life = models.CharField(max_length=100, default="100 Days", null=True, blank=True)
    # mfd = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    tags = TaggableManager(blank=True)

    # tags = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True)

    product_status = models.CharField(choices=STATUS, max_length=10, default="in_review")
    product_sale_status = models.CharField(choices=SALE_STATUS, max_length=10, null=True, blank=True)
    product_mainpage_status = models.CharField(choices=MAINPAGE_STATUS, max_length=20, null=True, blank=True)
    
    deal_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    # digital = models.BooleanField(default=False)

    sku = ShortUUIDField(unique=True, length=4, max_length=10, prefix="sku", alphabet="1234567890")

    date = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(null=True, blank=True)



    class Meta:
        verbose_name_plural = "Products"

    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title

    def get_precentage(self):
        new_price = (1-(self.price / self.old_price)) * 100
        return new_price

    def num_of_reviews(self):
        return ProductReview.objects.filter(product=self).count()

    def average_rating(self):
        from django.db.models import Avg
        # return ProductReview.objects.filter(product=self).aggregate(Avg('rating'))['rating__avg']
        rating_list = []
        if  ProductReview.objects.filter(product=self).aggregate(Avg('rating'))['rating__avg']:
            num = ProductReview.objects.filter(product=self).aggregate(Avg('rating'))['rating__avg']
        else:
            num = 1
        for i in range(int(num)):
            rating_list.append(i)
        return rating_list

    def average_rating_int(self):
        from django.db.models import Avg
        if  ProductReview.objects.filter(product=self).aggregate(Avg('rating'))['rating__avg']:
            return ProductReview.objects.filter(product=self).aggregate(Avg('rating'))['rating__avg']
        else:
            return float(1)


class ProductImages(models.Model):
    images = models.ImageField(upload_to="product-images", default="product.jpg")
    product = models.ForeignKey(Product, related_name="p_images", on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "Product Images"





############################################## Cart, Order, OrderITems and Address ##################################
############################################## Cart, Order, OrderITems and Address ##################################
############################################## Cart, Order, OrderITems and Address ##################################
############################################## Cart, Order, OrderITems and Address ##################################




class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=99999999999999, decimal_places=2, default="1.99")
    paid_status = models.BooleanField(default=False, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    product_status = models.CharField(choices=STATUS_CHOICE, max_length=30, default="processing")
    sku = ShortUUIDField(null=True, blank=True, length=5, prefix="SKU", max_length=20, alphabet="abcdefgh12345")

    class Meta:
        verbose_name_plural = "Cart Order"


class CartOrderProducts(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=200)
    product_status = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    qty = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=99999999999999, decimal_places=2, default="1.99")
    total = models.DecimalField(max_digits=99999999999999, decimal_places=2, default="1.99")


    class Meta:
        verbose_name_plural = "Cart Order Items"


    def order_img(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image))




############################################## Product Revew, wishlists, Address ##################################
############################################## Product Revew, wishlists, Address ##################################
############################################## Product Revew, wishlists, Address ##################################
############################################## Product Revew, wishlists, Address ##################################




class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="reviews")
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Reviews"

    def __str__(self):
        try:
            return self.product.title
        except:
            return str(self.date)

    def get_rating(self):
        return self.rating



class wishlist_model(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "wishlists"

    def __str__(self):
        try:
            return self.product.title
        except:
            return str(self.date)
        


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    mobile = models.CharField(max_length=300, null=True)
    address = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Address"
