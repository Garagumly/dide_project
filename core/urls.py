from django import views
from django.urls import path, include
from core.views import *


urlpatterns = [

    # Homepage
    path("", index, name="index"),
    
    path("set_language/<str:language>/",
         set_language, name="set-language"),

    path("products/", product_list_view, name="product-list"),
    path("delas/", deal_product_list_view, name="deal-product-list"),
    path("product/<pid>/", product_detail_view, name="product-detail"),

    #Brands
    path("brand/", brand_list_view, name="brand-list"),
    path("brand/<bid>/", brand_product_list__view, name="brand-product-list"),



    # Category
    path("category/", category_list_view, name="category-list"),
    path("sub_category/<cid>/", sub_category_list_view, name="sub-category-list"),
    path("category/<cid>/", category_product_list__view, name="category-product-list"),

    # Vendor
    path("vendors/", vendor_list_view, name="vendor-list"),
    path("vendor/<vid>/", vendor_detail_view, name="vendor-detail"),

    # Tags
    path("products/tag/<slug:tag_slug>/", tag_list, name="tags"),

    # Add Review
    path("ajax-add-review/<int:pid>/", ajax_add_review, name="ajax-add-review"),

    # Search
    path("search/", search_view, name="search"),

    # Filter product URL
    path("filter-products/", filter_product, name="filter-product"),

    # Add to cart URL
    path("add-to-cart/", add_to_cart, name="add-to-cart"),

    # Cart Page URL
    path("cart/", cart_view, name="cart"),

    # Delete ITem from Cart
    path("delete-from-cart/", delete_item_from_cart, name="delete-from-cart"),

    # Update  Cart
    path("update-cart/", update_cart, name="update-cart"),

      # Checkout  URL
    path("checkout/", checkout_view, name="checkout"),

    # Paypal URL
    path('paypal/', include('paypal.standard.ipn.urls')),

    # Payment Successful
    path("payment-completed/", payment_completed_view, name="payment-completed"),

    # Payment Failed
    path("payment-failed/", payment_failed_view, name="payment-failed"),

    # Dahboard URL
    path("dashboard/", customer_dashboard, name="core-dashboard"),

    # Order Detail URL
    path("dashboard/order/<int:id>", order_detail, name="core-order-detail"),

    # Making address defauly
    path("make-default-address/", make_address_default, name="core-make-default-address"),

    # wishlist page
    path("wishlist/", wishlist_view, name="wishlist"),

    # adding to wishlist
    path("add-to-wishlist/", add_to_wishlist, name="add-to-wishlist"),


    # Remvoing from wishlist
    path("remove-from-wishlist/", remove_wishlist, name="remove-from-wishlist"),


    path("contact/", contact, name="contact"),
    path("ajax-contact-form/", ajax_contact_form, name="ajax-contact-form"),

    path("about_us/", about_us, name="about_us"),
    path("purchase_guide/", purchase_guide, name="purchase_guide"),
    path("privacy_policy/", privacy_policy, name="privacy_policy"),
    path("terms_of_service/", terms_of_service, name="terms_of_service"),
]