
from urllib.parse import urlparse
from django.http import FileResponse, HttpResponseRedirect
from django.urls.base import resolve
from django.urls.exceptions import Resolver404
from django.utils import translation


from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from taggit.models import Tag
from core.models import AboutUs, Product, Category, Brand, Vendor, CartOrder, CartOrderProducts, ProductImages, ProductReview, wishlist_model, Address, Slider
from userauths.models import ContactUs, Profile
from core.forms import ProductReviewForm
from django.template.loader import render_to_string
from django.contrib import messages

from django.urls import reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm
from django.contrib.auth.decorators import login_required

import calendar
from django.db.models import Count, Avg
from django.db.models.functions import ExtractMonth
from django.core import serializers
from django.core.paginator import Paginator

# from django.core.paginator import Paginator

def index(request):
    # bannanas = Product.objects.all().order_by("-id")
    products = Product.objects.filter(product_status="published", featured=True).order_by("-id")
    products_deal = Product.objects.filter(product_status="published", featured=True, product_sale_status='deal').order_by("-id")[:4]
    new_products = Product.objects.filter(product_status="published", featured=True, product_mainpage_status='new').order_by("-id")[:3]
    top_selling = Product.objects.filter(product_status="published", featured=True, product_mainpage_status='top_selling').order_by("-id")[:3]
    trending_products = Product.objects.filter(product_status="published", featured=True, product_mainpage_status='trending_products').order_by("-id")[:3]
    recent = Product.objects.filter(product_status="published", featured=True, product_mainpage_status='recent').order_by("-id")[:3]
    top_rated = Product.objects.filter(product_status="published", featured=True, product_mainpage_status='top_rated').order_by("-id")[:3]
    vendors = Vendor.objects.all()
    brands = Brand.objects.all()
    categoty = Category.objects.all()
    # sub_cat = Category.objects.exclude(parent=None).annotate(s_count=Count('category'))
    parent_cat = Category.objects.filter(parent=None).annotate(c_count=Count('children__category'))
    sliders = Slider.objects.all()

    context = {
        "products":products,
        'products_deal':products_deal,
        'new_products':new_products,
        'top_selling':top_selling,
        'trending_products':trending_products,
        'recent':recent,
        'top_rated':top_rated,
        "vendors":vendors,
        "brands":brands,
        "categoty":categoty,
        "parent_cat":parent_cat,
        "sliders":sliders,
    }

    return render(request, 'core/index.html', context)


def product_list_view(request):
    products = Product.objects.filter(product_status="published").order_by("-id")
    products_deal = Product.objects.filter(product_status="published", featured=True, product_sale_status='deal').order_by("-id")[:4]
    tags = Tag.objects.all().order_by("-id")[:6]

    context = {
        "products":products,
        "products_deal":products_deal,
        "tags":tags,
    }

    return render(request, 'core/product-list.html', context)

def deal_product_list_view(request):
    products_deal = Product.objects.filter(product_status="published", product_sale_status='deal').order_by("-id")

    context = {
        "products_deal":products_deal,
    }

    return render(request, 'core/deals.html', context)

def category_list_view(request):
    categories = Category.objects.all()
    parent_cat = Category.objects.filter(parent=None).annotate(c_count=Count('children__category'))

    context = {
        "categories":categories,
        "parent_cat":parent_cat,
    }
    return render(request, 'core/category-list.html', context)

def brand_list_view(request):
    brands = Brand.objects.all()

    context = {
        "brands":brands,
    }
    return render(request, 'core/brand-list.html', context)

def brand_product_list__view(request, bid):

    brand = Brand.objects.get(bid=bid)
    products = Product.objects.filter(product_status="published", brand=brand)

    context = {
        "brand":brand,
        "products":products,
    }
    return render(request, "core/brand-product-list.html", context)

def sub_category_list_view(request, cid):
    parent = Category.objects.get(cid=cid)
    sub_cats = Category.objects.filter(parent__cid=cid).annotate(c_count=Count('category'))
    # parent_cat = Category.objects.filter(parent=None).annotate(c_count=Count('children__category'))
    # products = Product.objects.filter(product_status="published", category=sub_cats)

    context = {
        "sub_cats":sub_cats,
        "parent":parent,
    }
    return render(request, 'core/sub-category-list.html', context)

def category_product_list__view(request, cid):

    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(product_status="published", category=category)
    # products = Product.objects.filter(product_status="published", category__in=category.children.all())

    context = {
        "category":category,
        "products":products,
    }
    return render(request, "core/category-product-list.html", context)


def vendor_list_view(request):
    vendors = Vendor.objects.all()
    context = {
        "vendors": vendors,
    }
    return render(request, "core/vendor-list.html", context)


def vendor_detail_view(request, vid):
    vendor = Vendor.objects.get(vid=vid)
    products = Product.objects.filter(vendor=vendor, product_status="published").order_by("-id")
    parent_cat = Category.objects.filter(parent=None).annotate(c_count=Count('children__category'))
    
    paginator = Paginator(products, 20)
    page_number = request.GET.get("page")
    page_product = paginator.get_page(page_number)
    start_product = paginator.get_page(page_number).start_index()
    end_product = paginator.get_page(page_number).end_index()

    context = {
        "vendor": vendor,
        "products": products,
        "parent_cat": parent_cat,
        "all_products": page_product,
        "paginator": paginator,
        "start_product": start_product,
        "end_product": end_product
    }
    return render(request, "core/vendor-detail.html", context)


def product_detail_view(request, pid):
    product = Product.objects.get(pid=pid)
    # product = get_object_or_404(Product, pid=pid)
    products = Product.objects.filter(category=product.category).exclude(pid=pid)[:8]

    # Getting all reviews related to a product
    reviews = ProductReview.objects.filter(product=product).order_by("-date")

    # Getting average review
    average_rating = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))

    # Product Review form
    review_form = ProductReviewForm()


    make_review = True 

    if request.user.is_authenticated:
        # address = Address.objects.get(status=True, user=request.user)
        # address = Address.objects.get(user=request.user)

        try:
            address = Address.objects.get(status=True, user=request.user)
        except:
            address = None

        user_review_count = ProductReview.objects.filter(user=request.user, product=product).count()

        if user_review_count > 0:
            make_review = False
    
    address = "Login To Continue"


    p_image = product.p_images.all()
    p_attribute = product.productattributevaluess.all()

    context = {
        "p": product,
        "address": address,
        "make_review": make_review,
        "review_form": review_form,
        "p_image": p_image,
        "p_attribute": p_attribute,
        "average_rating": average_rating,
        "reviews": reviews,
        "products": products,
    }

    return render(request, "core/product-detail.html", context)

def tag_list(request, tag_slug=None):

    products = Product.objects.filter(product_status="published").order_by("-id")

    tag = None 
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        products = products.filter(tags__in=[tag])

    context = {
        "products": products,
        "tag": tag
    }

    return render(request, "core/tag.html", context)


def ajax_add_review(request, pid):
    product = Product.objects.get(pk=pid)
    user = request.user 

    review = ProductReview.objects.create(
        user=user,
        product=product,
        review = request.POST['review'],
        rating = request.POST['rating'],
    )

    context = {
        'user': user.username,
        'review': request.POST['review'],
        'rating': request.POST['rating'],
    }

    average_reviews = ProductReview.objects.filter(product=product).aggregate(rating=Avg("rating"))

    return JsonResponse(
       {
         'bool': True,
        'context': context,
        'average_reviews': average_reviews
       }
    )


def search_view(request):

    products = Product.objects.all()

    title = request.GET.get("q")
    cat = request.GET.get("r")

    if title and cat:
        category = Category.objects.get(cid=cat)
        products = Product.objects.filter(title__icontains=title, category__parent=category).order_by("-date") | Product.objects.filter(description__icontains=title).order_by("-date")

    elif cat:
        category = Category.objects.get(cid=cat)
        products = Product.objects.filter(category__parent=category).order_by("-date")

    else:
        products = Product.objects.filter(title__icontains=title).order_by("-date") | Product.objects.filter(description__icontains=title).order_by("-date")

    # if request.GET.get("r"):
    #     category = Category.objects.get(cid=request.GET.get("r"))
    #     products = Product.objects.filter(title__icontains=title, category__in=category.children.all()).order_by("-date") | Product.objects.filter(description__icontains=title).order_by("-date")
    
    # elif title == None:
    #     products =  Product.objects.all()

    # else:
    #     products = Product.objects.filter(title__icontains=title).order_by("-date") | Product.objects.filter(description__icontains=title).order_by("-date")
        # products = Product.objects.filter(title__icontains=title, description__icontains=title).order_by("-date")

    paginator = Paginator(products, 20)
    page_number = request.GET.get("page")
    page_product = paginator.get_page(page_number)
    start_product = paginator.get_page(page_number).start_index()
    end_product = paginator.get_page(page_number).end_index()

    context = {
        "products": products,
        "title": title,
        "all_products": page_product,
        "paginator": paginator,
        "start_product": start_product,
        "end_product": end_product,
        'title':title,
        'cat':cat,
    }
    return render(request, "core/search.html", context)


def filter_product(request):
    categories = request.GET.getlist("category[]")
    vendors = request.GET.getlist("vendor[]")
    types = request.GET.getlist("product_type[]")


    min_price = request.GET['min_price']
    max_price = request.GET['max_price']

    products = Product.objects.filter(product_status="published").order_by("-id").distinct()

    products = products.filter(price__gte=min_price)
    products = products.filter(price__lte=max_price)


    if len(categories) > 0:
        products = products.filter(category__id__in=categories).distinct() 

    if len(vendors) > 0:
        products = products.filter(vendor__id__in=vendors).distinct() 
    
    if len(types) > 0:
        products = products.filter(type__id__in=types).distinct()


    data = render_to_string("core/async/product-list.html", {"products": products})
    return JsonResponse({"data": data})


def add_to_cart(request):
    cart_product = {}

    cart_product[str(request.GET['id'])] = {
        'title': request.GET['title'],
        'qty': request.GET['qty'],
        'price': request.GET['price'],
        'image': request.GET['image'],
        'pid': request.GET['pid'],
    }

    if 'cart_data_obj' in request.session:
        if str(request.GET['id']) in request.session['cart_data_obj']:

            cart_data = request.session['cart_data_obj']
            cart_data[str(request.GET['id'])]['qty'] = int(cart_product[str(request.GET['id'])]['qty'])
            cart_data.update(cart_data)
            request.session['cart_data_obj'] = cart_data
        else:
            cart_data = request.session['cart_data_obj']
            cart_data.update(cart_product)
            request.session['cart_data_obj'] = cart_data

    else:
        request.session['cart_data_obj'] = cart_product
    return JsonResponse({"data":request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj'])})



def cart_view(request):
    cart_total_amount = 0
    sub_total = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            
            print(item['price'],'#####################################')
            print(type(item['price']))
            if int(item['qty']) > 0:
                sub_total = int(item['qty']) * float(item['price'].replace(',', '.'))
            else:
                sub_total = 0
            cart_total_amount += int(item['qty']) * float(item['price'].replace(',', '.'))
            # cart_total_amount += int(item['qty']) * item['price']
        return render(request, "core/cart.html", {"cart_data":request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount':cart_total_amount, 'sub_total':sub_total})
    else:
        messages.warning(request, "Your cart is empty")
        return redirect("index")


def delete_item_from_cart(request):
    product_id = str(request.GET['id'])
    if 'cart_data_obj' in request.session:
        if product_id in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']
            del request.session['cart_data_obj'][product_id]
            request.session['cart_data_obj'] = cart_data
    
    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'].replace(',', '.'))
            # cart_total_amount += int(item['qty']) * item['price']

    context = render_to_string("core/async/cart-list.html", {"cart_data":request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount':cart_total_amount})
    return JsonResponse({"data": context, 'totalcartitems': len(request.session['cart_data_obj'])})


def update_cart(request):
    product_id = str(request.GET['id'])
    product_qty = request.GET['qty']

    if 'cart_data_obj' in request.session:
        if product_id in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']
            cart_data[str(request.GET['id'])]['qty'] = product_qty
            request.session['cart_data_obj'] = cart_data
    
    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'].replace(',', '.'))
            # cart_total_amount += int(item['qty']) * item['price']

    context = render_to_string("core/async/cart-list.html", {"cart_data":request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount':cart_total_amount})
    return JsonResponse({"data": context, 'totalcartitems': len(request.session['cart_data_obj'])})


@login_required
def checkout_view(request):
    cart_total_amount = 0
    total_amount = 0

    # Checking if cart_data_obj session exists
    if 'cart_data_obj' in request.session:

        # Getting total amount for Paypal Amount
        # for p_id, item in request.session['cart_data_obj'].items():
        #     total_amount += int(item['qty']) * float(item['price'])

        # Create ORder Object
        order = CartOrder.objects.create(
            user=request.user,
            price=total_amount
        )

        # Getting total amount for The Cart
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'].replace(',', '.'))
            # cart_total_amount += int(item['qty']) * item['price']

            cart_order_products = CartOrderProducts.objects.create(
                order=order,
                invoice_no="INVOICE_NO-" + str(order.id), # INVOICE_NO-5,
                item=item['title'],
                image=item['image'],
                qty=item['qty'],
                price=item['price'].replace(',', '.'),
                # price=item['price'],
                total=int(item['qty']) * float(item['price'].replace(',', '.'))
                # total=item['qty'] * item['price']
            )

        host = request.get_host()
        paypal_dict = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': cart_total_amount,
            'item_name': "Order-Item-No-" + str(order.id),
            'invoice': "INVOICE_NO-" + str(order.id),
            'currency_code': "USD",
            'notify_url': 'http://{}{}'.format(host, reverse("paypal-ipn")),
            'return_url': 'http://{}{}'.format(host, reverse("payment-completed")),
            'cancel_url': 'http://{}{}'.format(host, reverse("payment-failed")),
        }

        paypal_payment_button = PayPalPaymentsForm(initial=paypal_dict)

        # cart_total_amount = 0
        # if 'cart_data_obj' in request.session:
        #     for p_id, item in request.session['cart_data_obj'].items():
        #         cart_total_amount += int(item['qty']) * float(item['price'])

        try:
            active_address = Address.objects.get(user=request.user, status=True)
        except:
            messages.warning(request, "There are multiple addresses, only one should be activated.")
            active_address = None

        return render(request, "core/checkout.html", {"cart_data":request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount':cart_total_amount, 'paypal_payment_button':paypal_payment_button, "active_address":active_address})


@login_required
def payment_completed_view(request):
    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            sub_total = int(item['qty']) * float(item['price'].replace(',', '.'))
            cart_total_amount += int(item['qty']) * float(item['price'].replace(',', '.'))
            # cart_total_amount += int(item['qty']) * item['price']
    return render(request, 'core/payment-completed.html',  {'cart_data':request.session['cart_data_obj'],'totalcartitems':len(request.session['cart_data_obj']),'cart_total_amount':cart_total_amount, 'sub_total':sub_total})

@login_required
def payment_failed_view(request):
    return render(request, 'core/payment-failed.html')


@login_required
def customer_dashboard(request):
    orders_list = CartOrder.objects.filter(user=request.user).order_by("-id")
    address = Address.objects.filter(user=request.user)


    orders = CartOrder.objects.annotate(month=ExtractMonth("order_date")).values("month").annotate(count=Count("id")).values("month", "count")
    month = []
    total_orders = []

    for i in orders:
        month.append(calendar.month_name[i["month"]])
        total_orders.append(i["count"])

    if request.method == "POST":
        address = request.POST.get("address")
        mobile = request.POST.get("mobile")

        new_address = Address.objects.create(
            user=request.user,
            address=address,
            mobile=mobile,
        )
        messages.success(request, "Address Added Successfully.")
        return redirect("core-dashboard")
    else:
        print("Error")
    
    user_profile = Profile.objects.get(user=request.user)
    print("user profile is: #########################",  user_profile)

    context = {
        "user_profile": user_profile,
        "orders": orders,
        "orders_list": orders_list,
        "address": address,
        "month": month,
        "total_orders": total_orders,
    }
    return render(request, 'core/dashboard.html', context)

def order_detail(request, id):
    order = CartOrder.objects.get(user=request.user, id=id)
    order_items = CartOrderProducts.objects.filter(order=order)

    
    context = {
        "order_items": order_items,
    }
    return render(request, 'core/order-detail.html', context)


def make_address_default(request):
    id = request.GET['id']
    Address.objects.update(status=False)
    Address.objects.filter(id=id).update(status=True)
    return JsonResponse({"boolean": True})

@login_required
def wishlist_view(request):
    wishlist = wishlist_model.objects.all()
    context = {
        "w":wishlist
    }
    return render(request, "core/wishlist.html", context)


    # w

def add_to_wishlist(request):
    product_id = request.GET['id']
    product = Product.objects.get(id=product_id)
    print("product id isssssssssssss:" + product_id)

    context = {}

    wishlist_count = wishlist_model.objects.filter(product=product, user=request.user).count()
    print(wishlist_count)

    if wishlist_count > 0:
        context = {
            "bool": True
        }
    else:
        new_wishlist = wishlist_model.objects.create(
            user=request.user,
            product=product,
        )
        context = {
            "bool": True
        }

    return JsonResponse(context)


# def remove_wishlist(request):
#     pid = request.GET['id']
#     wishlist = wishlist_model.objects.filter(user=request.user).values()

#     product = wishlist_model.objects.get(id=pid)
#     h = product.delete()

#     context = {
#         "bool": True,
#         "wishlist":wishlist
#     }
#     t = render_to_string("core/async/wishlist-list.html", context)
#     return JsonResponse({"data": t, "w":wishlist})

def remove_wishlist(request):
    pid = request.GET['id']
    wishlist = wishlist_model.objects.filter(user=request.user)
    wishlist_d = wishlist_model.objects.get(id=pid)
    delete_product = wishlist_d.delete()
    
    context = {
        "bool":True,
        "w":wishlist
    }
    wishlist_json = serializers.serialize('json', wishlist)
    t = render_to_string('core/async/wishlist-list.html', context)
    return JsonResponse({'data':t,'w':wishlist_json})





# Other Pages 
def contact(request):
    return render(request, "core/contact.html")


def ajax_contact_form(request):
    full_name = request.GET['full_name']
    email = request.GET['email']
    phone = request.GET['phone']
    subject = request.GET['subject']
    message = request.GET['message']

    contact = ContactUs.objects.create(
        full_name=full_name,
        email=email,
        phone=phone,
        subject=subject,
        message=message,
    )

    data = {
        "bool": True,
        "message": "Message Sent Successfully"
    }

    return JsonResponse({"data":data})


def about_us(request):
    info = AboutUs.objects.all()[0]
    brands = Brand.objects.all()
    context = {
        'brands':brands,
        'info':info,
    }
    return render(request, "core/about_us.html", context)


def purchase_guide(request):
    return render(request, "core/purchase_guide.html")

def privacy_policy(request):
    return render(request, "core/privacy_policy.html")

def terms_of_service(request):
    return render(request, "core/terms_of_service.html")


def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response
