from ast import Add
from core.models import ProductType, MainInfo, Product, Category, Vendor, CartOrder, ProductImages, ProductReview, wishlist_model, Address
from django.db.models import Min, Max
from django.contrib import messages

def default(request):

    maininfo = MainInfo.objects.all()[:1]

    categories = Category.objects.all()
    parent_cat = Category.objects.filter(parent=None)
    sub_cat = Category.objects.exclude(parent=None)

    product_type = ProductType.objects.all()
    vendors = Vendor.objects.all()

    min_max_price = Product.objects.aggregate(Min("price"), Max("price"))

    if request.user.is_authenticated:
        try:
            wishlist = wishlist_model.objects.filter(user=request.user)
        except:
            messages.warning(request, "You need to login before accessing your wishlist.")
            wishlist = 0
    else:
        wishlist = 0

    
    
    try:
        address = Address.objects.get(user=request.user)
    except:
        address = None

    return {
        'maininfo':maininfo,
        'categories':categories,
        'parent_cat':parent_cat,
        'sub_cat':sub_cat,
        'wishlist':wishlist,
        'address':address,
        'product_type':product_type,
        'vendors':vendors,
        'min_max_price':min_max_price,
    }