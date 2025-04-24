from flask import Flask, render_template, redirect, url_for, flash, request, session
import os
import json
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def get_static_url(path):
    return '/static/' + path

def get_sample_data():
    # Common data for all pages
    data = {
        'author_name': 'Jewelry Store',
        'favicon_url': '/static/images/favicon.png',
        'apple_icon_url': '/static/images/apple-touch-icon.png',
        'apple_icon_72x72_url': '/static/images/apple-touch-icon-72x72.png',
        'apple_icon_114x114_url': '/static/images/apple-touch-icon-114x114.png',
        'css_vendors_url': '/static/css/vendors.min.css',
        'css_icon_url': '/static/css/icon.min.css',
        'css_style_url': '/static/css/style.css',
        'css_responsive_url': '/static/css/responsive.css',
        'jewellery_store_css_url': '/static/demos/jewellery-store/jewellery-store.css',
        'js_jquery_url': '/static/js/jquery.js',
        'js_modernizr_url': '/static/js/modernizr.js',
        'js_bootstrap_bundle_url': '/static/js/bootstrap.bundle.min.js',
        'js_jquery_appear_url': '/static/js/jquery.appear.js',
        'js_swiper_bundle_url': '/static/js/swiper-bundle.min.js',
        'js_isotope_url': '/static/js/isotope.pkgd.min.js',
        'js_tilt_url': '/static/js/tilt.jquery.min.js',
        'js_jquery_easing_url': '/static/js/jquery.easing.1.3.js',
        'js_jquery_fitvids_url': '/static/js/jquery.fitvids.js',
        'js_jquery_justifiedgallery_url': '/static/js/jquery.justifiedGallery.min.js',
        'js_jquery_magnific_popup_url': '/static/js/jquery.magnific-popup.min.js',
        'js_jquery_easypiechart_url': '/static/js/jquery.easypiechart.min.js',
        'js_jquery_instagramfeed_url': '/static/js/jquery.instagramFeed.min.js',
        'js_jquery_countdown_url': '/static/js/jquery.countdown.min.js',
        'js_jquery_mousewheel_url': '/static/js/jquery.mousewheel.min.js',
        'js_lightgallery_url': '/static/js/lightgallery-all.min.js',
        'js_main_url': '/static/js/main.js',
        'js_vendors_url': '/static/js/vendors.min.js',
        'logo_url': '/static/images/logo.png',
        'logo_2x_url': '/static/images/logo@2x.png',
        'home_url': '/',
        'shop_url': '/shop',
        'blog_url': '/blog',
        'contact_url': '/contact',
        'about_url': '/about',
        'faq_url': '/faq',
        'wishlist_url': '/wishlist',
        'account_url': '/account',
        'cart_url': '/cart',
        'checkout_url': '/checkout',
        'search_result_url': '/search',
        'shipping_offer': 'Free shipping on all orders over $100',
        'offer_text': 'Shop Now',
        'offer_link': '/shop',
        'cart_count': 0,
        'subtotal': '$0.00',
        'cart_items': [],
        'account_items': [
            {'name': 'Wishlist', 'url': '/wishlist'},
            {'name': 'Order history', 'url': '/order-history'},
            {'name': 'Account details', 'url': '/account'},
            {'name': 'Customer support', 'url': '/support'},
            {'name': 'Logout', 'url': '/logout'}
        ],
        'rings': [
            {'name': 'Diamond Rings', 'url': '/shop/rings/diamond'},
            {'name': 'Gold Rings', 'url': '/shop/rings/gold'},
            {'name': 'Silver Rings', 'url': '/shop/rings/silver'},
            {'name': 'Platinum Rings', 'url': '/shop/rings/platinum'}
        ],
        'earrings': [
            {'name': 'Diamond Earrings', 'url': '/shop/earrings/diamond'},
            {'name': 'Gold Earrings', 'url': '/shop/earrings/gold'},
            {'name': 'Silver Earrings', 'url': '/shop/earrings/silver'},
            {'name': 'Platinum Earrings', 'url': '/shop/earrings/platinum'}
        ],
        'necklaces': [
            {'name': 'Diamond Necklaces', 'url': '/shop/necklaces/diamond'},
            {'name': 'Gold Necklaces', 'url': '/shop/necklaces/gold'},
            {'name': 'Silver Necklaces', 'url': '/shop/necklaces/silver'},
            {'name': 'Platinum Necklaces', 'url': '/shop/necklaces/platinum'}
        ],
        'pendants': [
            {'name': 'Diamond Pendants', 'url': '/shop/pendants/diamond'},
            {'name': 'Gold Pendants', 'url': '/shop/pendants/gold'},
            {'name': 'Silver Pendants', 'url': '/shop/pendants/silver'},
            {'name': 'Platinum Pendants', 'url': '/shop/pendants/platinum'}
        ],
        'bracelets': [
            {'name': 'Diamond Bracelets', 'url': '/shop/bracelets/diamond'},
            {'name': 'Gold Bracelets', 'url': '/shop/bracelets/gold'},
            {'name': 'Silver Bracelets', 'url': '/shop/bracelets/silver'},
            {'name': 'Platinum Bracelets', 'url': '/shop/bracelets/platinum'}
        ],
        'footer_bg_image_url': '/static/images/demo-jewellery-store-footer-bg.jpg',
        'support_text': 'We provide the best customer service and support for all your jewelry needs.',
        'phone_number': '+1 (800) 123-4567',
        'email_address': 'info@jewelrystore.com',
        'categories_label': 'Categories',
        'women_collection': 'Women Collection',
        'women_collection_url': '/shop/women',
        'men_collection': 'Men Collection',
        'men_collection_url': '/shop/men',
        'accessories': 'Accessories',
        'accessories_url': '/shop/accessories',
        'diamond': 'Diamond',
        'diamond_url': '/shop/diamond',
        'gold_jewellery': 'Gold Jewellery',
        'gold_jewellery_url': '/shop/gold',
        'account_label': 'My Account',
        'my_profile': 'My Profile',
        'my_profile_url': '/account/profile',
        'order_history': 'Order History',
        'order_history_url': '/account/orders',
        'wish_list': 'Wish List',
        'wish_list_url': '/account/wishlist',
        'order_tracking': 'Order Tracking',
        'order_tracking_url': '/account/track',
        'shopping_cart': 'Shopping Cart',
        'shopping_cart_url': '/cart',
        'information_label': 'Information',
        'about_us': 'About Us',
        'about_us_url': '/about',
        'careers': 'Careers',
        'careers_url': '/careers',
        'events': 'Events',
        'events_url': '/events',
        'articles': 'Articles',
        'articles_url': '/articles',
        'contact_us': 'Contact Us',
        'contact_us_url': '/contact',
        'connect_with_us_label': 'Connect with Us',
        'facebook_url': 'https://www.facebook.com/',
        'instagram_url': 'https://www.instagram.com/',
        'twitter_url': 'https://www.twitter.com/',
        'dribbble_url': 'https://www.dribbble.com/',
        'secure_payment_label': 'Secure Payment',
        'visa_logo_url': '/static/images/visa.svg',
        'mastercard_logo_url': '/static/images/mastercard.svg',
        'american_express_logo_url': '/static/images/american-express.svg',
        'discover_logo_url': '/static/images/discover.svg',
        'diners_club_logo_url': '/static/images/diners-club.svg',
        'cookie_message': 'We use cookies to enhance your experience. By continuing to visit this site you agree to our use of cookies.',
        'accept_cookies_text': 'Accept Cookies',
        'cookie_policy_text': 'Cookie policy',
        'jquery_url': '/static/js/jquery.js',
        'vendors_url': '/static/js/vendors.min.js',
        'main_js_url': '/static/js/main.js'
    }
    return data

@app.route('/')
def home():
    data = get_sample_data()

    # Home page specific data
    home_data = {
        'page_title': 'Home - Jewelry Store',
        'meta_description': 'Discover our exquisite collection of fine jewelry, rings, necklaces, earrings, and more.',
        'hero_subtitle': 'Exquisite Collection',
        'hero_title': 'Luxury Jewelry for Every Occasion',
        'hero_description': 'Discover our handcrafted jewelry pieces made with the finest materials and attention to detail.',
        'hero_button_text': 'Shop Now',
        'featured_categories_subtitle': 'Handcrafted with Love',
        'featured_categories_title': 'Featured Categories',
        'featured_categories': [
            {'name': 'Rings', 'image': 'https://placehold.co/600x600?text=Rings', 'url': '/shop/rings', 'count': '24 Products'},
            {'name': 'Necklaces', 'image': 'https://placehold.co/600x600?text=Necklaces', 'url': '/shop/necklaces', 'count': '18 Products'},
            {'name': 'Earrings', 'image': 'https://placehold.co/600x600?text=Earrings', 'url': '/shop/earrings', 'count': '32 Products'},
            {'name': 'Bracelets', 'image': 'https://placehold.co/600x600?text=Bracelets', 'url': '/shop/bracelets', 'count': '16 Products'}
        ],
        'featured_products_subtitle': 'Bestsellers',
        'featured_products_title': 'Featured Products',
        'featured_products': [
            {'name': 'Diamond Engagement Ring', 'image': 'https://placehold.co/600x800?text=Diamond+Ring', 'url': '/shop/product/1', 'price': '$1,299.00', 'regular_price': '$1,499.00'},
            {'name': 'Gold Chain Necklace', 'image': 'https://placehold.co/600x800?text=Gold+Necklace', 'url': '/shop/product/2', 'price': '$899.00', 'regular_price': '$999.00'},
            {'name': 'Pearl Earrings', 'image': 'https://placehold.co/600x800?text=Pearl+Earrings', 'url': '/shop/product/3', 'price': '$499.00', 'regular_price': '$599.00'},
            {'name': 'Silver Bracelet', 'image': 'https://placehold.co/600x800?text=Silver+Bracelet', 'url': '/shop/product/4', 'price': '$349.00', 'regular_price': '$399.00'}
        ],
        'testimonials_subtitle': 'What Our Customers Say',
        'testimonials_title': 'Testimonials',
        'testimonials': [
            {'name': 'Jennifer Smith', 'position': 'Happy Customer', 'image': 'https://placehold.co/100x100?text=JS', 'content': 'I absolutely love my new diamond ring! The craftsmanship is exceptional and the customer service was outstanding. I will definitely be shopping here again.'},
            {'name': 'Michael Johnson', 'position': 'Loyal Customer', 'image': 'https://placehold.co/100x100?text=MJ', 'content': 'I purchased a necklace for my wife\'s birthday and she was thrilled! The quality is exceptional and the packaging was beautiful. Will definitely recommend to friends and family.'},
            {'name': 'Sarah Williams', 'position': 'First-time Buyer', 'image': 'https://placehold.co/100x100?text=SW', 'content': 'The earrings I ordered arrived promptly and were even more beautiful in person. The attention to detail is remarkable. I\'m already planning my next purchase!'},
            {'name': 'David Brown', 'position': 'Repeat Customer', 'image': 'https://placehold.co/100x100?text=DB', 'content': 'I\'ve been a customer for years and the quality never disappoints. Their jewelry makes the perfect gift for any occasion. The customer service is always top-notch.'}
        ]
    }

    # Merge the home data with the general data
    data.update(home_data)

    # Render the home template with the correct name
    return render_template('demo-jewellery-store.html', **data)

@app.route('/shop')
def shop():
    data = get_sample_data()
    
    # Shop page specific data
    shop_data = {
        'page_title': 'Shop - Jewelry Store',
        'meta_description': 'Browse our exquisite collection of fine jewelry, rings, necklaces, earrings, and more.',
        'page_heading': 'Shop collection',
        'page_name': 'Shop',
        'home_label': 'Home',
        'page_title_image_url': 'https://placehold.co/1920x470?text=Shop',
        'categories': [
            {'title': 'Rings', 'count': 24, 'url': '/shop/rings'},
            {'title': 'Necklaces', 'count': 18, 'url': '/shop/necklaces'},
            {'title': 'Earrings', 'count': 32, 'url': '/shop/earrings'},
            {'title': 'Bracelets', 'count': 16, 'url': '/shop/bracelets'},
            {'title': 'Pendants', 'count': 12, 'url': '/shop/pendants'},
            {'title': 'Watches', 'count': 8, 'url': '/shop/watches'}
        ],
        'price_ranges': [
            {'range': '$0 - $100', 'url': '/shop?price=0-100', 'count': '08'},
            {'range': '$100 - $500', 'url': '/shop?price=100-500', 'count': '05'},
            {'range': '$500 - $1000', 'url': '/shop?price=500-1000', 'count': '25'},
            {'range': '$1000 - $5000', 'url': '/shop?price=1000-5000', 'count': '18'},
            {'range': '$5000+', 'url': '/shop?price=5000-plus', 'count': '36'}
        ],
        'materials': [
            {'name': 'Gold', 'count': 45, 'url': '/shop?material=gold'},
            {'name': 'Silver', 'count': 38, 'url': '/shop?material=silver'},
            {'name': 'Platinum', 'count': 24, 'url': '/shop?material=platinum'},
            {'name': 'Diamond', 'count': 32, 'url': '/shop?material=diamond'},
            {'name': 'Pearl', 'count': 18, 'url': '/shop?material=pearl'},
            {'name': 'Gemstone', 'count': 27, 'url': '/shop?material=gemstone'}
        ],
        'sort_options': [
            {'name': 'Default sorting', 'value': 'default'},
            {'name': 'Sort by popularity', 'value': 'popularity'},
            {'name': 'Sort by average rating', 'value': 'rating'},
            {'name': 'Sort by latest', 'value': 'latest'},
            {'name': 'Sort by price: low to high', 'value': 'price-low-high'},
            {'name': 'Sort by price: high to low', 'value': 'price-high-low'}
        ],
        'products': [
            {
                'id': 1,
                'name': 'Diamond Engagement Ring',
                'image': 'https://placehold.co/600x765?text=Diamond+Ring',
                'url': '/shop/product/1',
                'price': '$1,299.00',
                'regular_price': '$1,499.00',
                'label': 'Sale',
                'label_class': 'sale'
            },
            {
                'id': 2,
                'name': 'Gold Chain Necklace',
                'image': 'https://placehold.co/600x765?text=Gold+Necklace',
                'url': '/shop/product/2',
                'price': '$899.00',
                'regular_price': '$999.00',
                'label': 'New',
                'label_class': 'new'
            },
            {
                'id': 3,
                'name': 'Pearl Earrings',
                'image': 'https://placehold.co/600x765?text=Pearl+Earrings',
                'url': '/shop/product/3',
                'price': '$499.00',
                'regular_price': '$599.00',
                'label': 'Hot',
                'label_class': 'hot'
            },
            {
                'id': 4,
                'name': 'Silver Bracelet',
                'image': 'https://placehold.co/600x765?text=Silver+Bracelet',
                'url': '/shop/product/4',
                'price': '$349.00',
                'regular_price': '$399.00'
            },
            {
                'id': 5,
                'name': 'Platinum Wedding Band',
                'image': 'https://placehold.co/600x765?text=Platinum+Band',
                'url': '/shop/product/5',
                'price': '$1,199.00',
                'regular_price': '$1,299.00'
            },
            {
                'id': 6,
                'name': 'Ruby Pendant',
                'image': 'https://placehold.co/600x765?text=Ruby+Pendant',
                'url': '/shop/product/6',
                'price': '$799.00',
                'regular_price': '$899.00',
                'label': 'Sale',
                'label_class': 'sale'
            },
            {
                'id': 7,
                'name': 'Sapphire Earrings',
                'image': 'https://placehold.co/600x765?text=Sapphire+Earrings',
                'url': '/shop/product/7',
                'price': '$649.00',
                'regular_price': '$749.00'
            },
            {
                'id': 8,
                'name': 'Gold Bangle',
                'image': 'https://placehold.co/600x765?text=Gold+Bangle',
                'url': '/shop/product/8',
                'price': '$549.00',
                'regular_price': '$599.00'
            },
            {
                'id': 9,
                'name': 'Diamond Tennis Bracelet',
                'image': 'https://placehold.co/600x765?text=Tennis+Bracelet',
                'url': '/shop/product/9',
                'price': '$2,499.00',
                'regular_price': '$2,799.00',
                'label': 'New',
                'label_class': 'new'
            },
            {
                'id': 10,
                'name': 'Pearl Necklace',
                'image': 'https://placehold.co/600x765?text=Pearl+Necklace',
                'url': '/shop/product/10',
                'price': '$899.00',
                'regular_price': '$999.00'
            },
            {
                'id': 11,
                'name': 'Emerald Ring',
                'image': 'https://placehold.co/600x765?text=Emerald+Ring',
                'url': '/shop/product/11',
                'price': '$1,199.00',
                'regular_price': '$1,399.00',
                'label': 'Hot',
                'label_class': 'hot'
            },
            {
                'id': 12,
                'name': 'Silver Hoop Earrings',
                'image': 'https://placehold.co/600x765?text=Hoop+Earrings',
                'url': '/shop/product/12',
                'price': '$249.00',
                'regular_price': '$299.00'
            }
        ],
        'current_page': 1,
        'total_pages': 3,
        'products_per_page': 12,
        'total_products': 36,
        'showing_text': 'Showing 1-12 of 36 results',
        'tags': ['earrings', 'bracelets', 'necklace', 'chains', 'ring', 'kundan', 'casual', 'meenakari'],
        'new_arrivals': [
            {
                'name': 'Diamond ring',
                'image': 'https://placehold.co/600x765',
                'url': '/shop/product/1',
                'price': '$23.00',
                'regular_price': '$30.00'
            },
            {
                'name': 'Geometric ring',
                'image': 'https://placehold.co/600x765',
                'url': '/shop/product/2',
                'price': '$43.00',
                'regular_price': '$50.00'
            },
            {
                'name': 'Suserrer earring',
                'image': 'https://placehold.co/600x765',
                'url': '/shop/product/3',
                'price': '$15.00',
                'regular_price': '$20.00'
            },
            {
                'name': 'Twister bangle',
                'image': 'https://placehold.co/600x765',
                'url': '/shop/product/4',
                'price': '$10.00',
                'regular_price': '$15.00'
            },
            {
                'name': 'Zebra earrings',
                'image': 'https://placehold.co/600x765',
                'url': '/shop/product/5',
                'price': '$30.00',
                'regular_price': '$35.00'
            },
            {
                'name': 'Silver earrings',
                'image': 'https://placehold.co/600x765',
                'url': '/shop/product/6',
                'price': '$15.00',
                'regular_price': '$20.00'
            }
        ],
        'instagram_feed': [
            {'image': 'https://placehold.co/445x445'},
            {'image': 'https://placehold.co/445x445'},
            {'image': 'https://placehold.co/445x445'},
            {'image': 'https://placehold.co/445x445'},
            {'image': 'https://placehold.co/445x445'},
            {'image': 'https://placehold.co/445x445'}
        ]
    }
    
    # Handle filtering and sorting
    category = request.args.get('category')
    price_range = request.args.get('price')
    material = request.args.get('material')
    sort = request.args.get('sort', 'default')
    
    # In a real application, you would filter and sort the products based on these parameters
    # For this example, we'll just update the showing_text if any filters are applied
    
    filters_applied = []
    if category:
        filters_applied.append(f"Category: {category}")
    if price_range:
        filters_applied.append(f"Price: {price_range}")
    if material:
        filters_applied.append(f"Material: {material}")
    
    if filters_applied:
        shop_data['showing_text'] = f"Showing filtered results ({', '.join(filters_applied)})"
    
    # Handle pagination
    page = request.args.get('page', 1, type=int)
    per_page = shop_data['products_per_page']
    start = (page - 1) * per_page
    end = start + per_page
    
    # In a real application, you would paginate the actual filtered products
    # For this example, we'll just update the current_page
    shop_data['current_page'] = page
    
    # Merge the shop data with the general data
    data.update(shop_data)
    
    # Use the new template
    return render_template('demo-jewellery-store-shop.html', **data)

@app.route('/shop-modern')
def shop_modern():
    """
    Route for the modern shop page layout.
    """
    data = get_sample_data()
    
    # Shop modern page specific data
    shop_modern_data = {
        'page_title': 'Shop Modern - Jewelry Store',
        'meta_description': 'Browse our exquisite collection of fine jewelry with a modern shopping experience.',
        'page_heading': 'Shop Collection',
        'page_name': 'Shop Modern',
        'home_label': 'Home',
        'page_title_image_url': 'https://placehold.co/1920x470?text=Shop+Modern',
        'showing_text': 'Showing 1–12 of 48 results',
        'shop_banner_1': 'https://placehold.co/580x160?text=Shop+Banner+1',
        'shop_banner_2': 'https://placehold.co/580x160?text=Shop+Banner+2',
        'view_two_column_icon': '/static/images/shop-two-column.svg',
        'view_three_column_icon': '/static/images/shop-three-column.svg',
        'view_four_column_icon': '/static/images/shop-four-column.svg',
        'view_list_icon': '/static/images/shop-list.svg',
        'sort_options': [
            {'name': 'Default sorting', 'value': 'default', 'selected': True},
            {'name': 'Sort by popularity', 'value': 'popularity', 'selected': False},
            {'name': 'Sort by average rating', 'value': 'rating', 'selected': False},
            {'name': 'Sort by latest', 'value': 'latest', 'selected': False},
            {'name': 'Sort by price: low to high', 'value': 'price-low-high', 'selected': False},
            {'name': 'Sort by price: high to low', 'value': 'price-high-low', 'selected': False}
        ],
        'products': [
            {
                'id': 1,
                'name': 'Diamond Engagement Ring',
                'image': 'https://placehold.co/600x800?text=Diamond+Ring',
                'url': '/shop/product/1',
                'price': '$1,299.00',
                'regular_price': '$1,499.00',
                'label': 'New',
                'label_class': 'new',
                'wishlist_url': '#',
                'quick_view_url': '#'
            },
            {
                'id': 2,
                'name': 'Gold Chain Necklace',
                'image': 'https://placehold.co/600x800?text=Gold+Necklace',
                'url': '/shop/product/2',
                'price': '$899.00',
                'regular_price': '$999.00',
                'label': 'Hot',
                'label_class': 'hot',
                'wishlist_url': '#',
                'quick_view_url': '#'
            },
            {
                'id': 3,
                'name': 'Pearl Earrings',
                'image': 'https://placehold.co/600x800?text=Pearl+Earrings',
                'url': '/shop/product/3',
                'price': '$499.00',
                'regular_price': '$599.00',
                'wishlist_url': '#',
                'quick_view_url': '#'
            },
            {
                'id': 4,
                'name': 'Silver Bracelet',
                'image': 'https://placehold.co/600x800?text=Silver+Bracelet',
                'url': '/shop/product/4',
                'price': '$349.00',
                'regular_price': '$399.00',
                'label': 'Sale',
                'label_class': 'sale',
                'wishlist_url': '#',
                'quick_view_url': '#'
            },
            {
                'id': 5,
                'name': 'Platinum Wedding Band',
                'image': 'https://placehold.co/600x800?text=Platinum+Band',
                'url': '/shop/product/5',
                'price': '$1,199.00',
                'regular_price': '$1,299.00',
                'wishlist_url': '#',
                'quick_view_url': '#'
            },
            {
                'id': 6,
                'name': 'Ruby Pendant',
                'image': 'https://placehold.co/600x800?text=Ruby+Pendant',
                'url': '/shop/product/6',
                'price': '$799.00',
                'regular_price': '$899.00',
                'label': 'Sale',
                'label_class': 'sale',
                'wishlist_url': '#',
                'quick_view_url': '#'
            },
            {
                'id': 7,
                'name': 'Sapphire Earrings',
                'image': 'https://placehold.co/600x800?text=Sapphire+Earrings',
                'url': '/shop/product/7',
                'price': '$649.00',
                'regular_price': '$749.00',
                'wishlist_url': '#',
                'quick_view_url': '#'
            },
            {
                'id': 8,
                'name': 'Gold Bangle',
                'image': 'https://placehold.co/600x800?text=Gold+Bangle',
                'url': '/shop/product/8',
                'price': '$549.00',
                'regular_price': '$599.00',
                'wishlist_url': '#',
                'quick_view_url': '#'
            },
            {
                'id': 9,
                'name': 'Diamond Tennis Bracelet',
                'image': 'https://placehold.co/600x800?text=Tennis+Bracelet',
                'url': '/shop/product/9',
                'price': '$2,499.00',
                'regular_price': '$2,799.00',
                'label': 'New',
                'label_class': 'new',
                'wishlist_url': '#',
                'quick_view_url': '#'
            },
            {
                'id': 10,
                'name': 'Pearl Necklace',
                'image': 'https://placehold.co/600x800?text=Pearl+Necklace',
                'url': '/shop/product/10',
                'price': '$899.00',
                'regular_price': '$999.00',
                'wishlist_url': '#',
                'quick_view_url': '#'
            },
            {
                'id': 11,
                'name': 'Emerald Ring',
                'image': 'https://placehold.co/600x800?text=Emerald+Ring',
                'url': '/shop/product/11',
                'price': '$1,199.00',
                'regular_price': '$1,399.00',
                'label': 'Hot',
                'label_class': 'hot',
                'wishlist_url': '#',
                'quick_view_url': '#'
            },
            {
                'id': 12,
                'name': 'Silver Hoop Earrings',
                'image': 'https://placehold.co/600x800?text=Hoop+Earrings',
                'url': '/shop/product/12',
                'price': '$249.00',
                'regular_price': '$299.00',
                'wishlist_url': '#',
                'quick_view_url': '#'
            }
        ],
        'pagination': [
            {'icon': 'arrow-left', 'url': '#'},
            {'number': '01', 'url': '#'},
            {'number': '02', 'url': '#', 'active': True},
            {'number': '03', 'url': '#'},
            {'number': '04', 'url': '#'},
            {'icon': 'arrow-right', 'url': '#'}
        ]
    }
    
    # Merge the shop modern data with the general data
    data.update(shop_modern_data)
    
    return render_template('demo-jewellery-store-shop-modern.html', **data)

@app.route('/shop-sidebar')
def shop_sidebar():
    """
    Route for the shop page with sidebar layout.
    """
    data = get_sample_data()
    
    # Shop sidebar page specific data
    shop_sidebar_data = {
        'page_title': 'Shop with Sidebar - Jewelry Store',
        'meta_description': 'Browse our exquisite collection of fine jewelry with convenient sidebar filtering.',
        'page_heading': 'Shop Collection',
        'page_name': 'Shop with Sidebar',
        'home_label': 'Home',
        'page_title_image_url': 'https://placehold.co/1920x470?text=Shop+with+Sidebar',
        'showing_text': 'Showing 1–12 of 48 results',
        'categories_url': '/categories',
        'category_image_1': 'https://placehold.co/190x140?text=Rings',
        'category_image_2': 'https://placehold.co/190x140?text=Bracelet',
        'category_image_3': 'https://placehold.co/190x140?text=Earrings',
        'category_image_4': 'https://placehold.co/190x140?text=Necklace',
        'category_banner': 'https://placehold.co/290x380?text=Categories',
        'view_two_column_icon': '/static/images/shop-two-column.svg',
        'view_three_column_icon': '/static/images/shop-three-column.svg',
        'view_four_column_icon': '/static/images/shop-four-column.svg',
        'view_list_icon': '/static/images/shop-list.svg',
        'sort_options': [
            {'name': 'Default sorting', 'value': 'default', 'selected': True},
            {'name': 'Sort by popularity', 'value': 'popularity', 'selected': False},
            {'name': 'Sort by average rating', 'value': 'rating', 'selected': False},
            {'name': 'Sort by latest', 'value': 'latest', 'selected': False},
            {'name': 'Sort by price: low to high', 'value': 'price-low-high', 'selected': False},
            {'name': 'Sort by price: high to low', 'value': 'price-high-low', 'selected': False}
        ],
        'products': [
            {
                'id': 1,
                'name': 'Diamond Engagement Ring',
                'image': 'https://placehold.co/600x800?text=Diamond+Ring',
                'url': '/shop/product/1',
                'price': '$1,299.00',
                'regular_price': '$1,499.00',
                'label': 'New',
                'label_class': 'new',
                'wishlist_url': '#',
                'quick_view_url': '#'
            },
            {
                'id': 2,
                'name': 'Gold Chain Necklace',
                'image': 'https://placehold.co/600x800?text=Gold+Necklace',
                'url': '/shop/product/2',
                'price': '$899.00',
                'regular_price': '$999.00',
                'label': 'Hot',
                'label_class': 'hot',
                'wishlist_url': '#',
                'quick_view_url': '#'
            },
            {
                'id': 3,
                'name': 'Pearl Earrings',
                'image': 'https://placehold.co/600x800?text=Pearl+Earrings',
                'url': '/shop/product/3',
                'price': '$499.00',
                'regular_price': '$599.00',
                'wishlist_url': '#',
                'quick_view_url': '#'
            },
            {
                'id': 4,
                'name': 'Silver Bracelet',
                'image': 'https://placehold.co/600x800?text=Silver+Bracelet',
                'url': '/shop/product/4',
                'price': '$349.00',
                'regular_price': '$399.00',
                'label': 'Sale',
                'label_class': 'sale',
                'wishlist_url': '#',
                'quick_view_url': '#'
            }
        ],
        'pagination': [
            {'icon': 'arrow-left', 'url': '#'},
            {'number': '01', 'url': '#'},
            {'number': '02', 'url': '#', 'active': True},
            {'number': '03', 'url': '#'},
            {'number': '04', 'url': '#'},
            {'icon': 'arrow-right', 'url': '#'}
        ],
        'sidebar_categories': [
            {'title': 'Rings', 'url': '/shop?category=rings', 'count': '24'},
            {'title': 'Necklaces', 'url': '/shop?category=necklaces', 'count': '18'},
            {'title': 'Earrings', 'url': '/shop?category=earrings', 'count': '32'},
            {'title': 'Bracelets', 'url': '/shop?category=bracelets', 'count': '16'},
            {'title': 'Pendants', 'url': '/shop?category=pendants', 'count': '12'},
            {'title': 'Watches', 'url': '/shop?category=watches', 'count': '8'}
        ],
        'price_ranges': [
            {'range': '$0 - $100', 'url': '/shop?price=0-100', 'count': '08'},
            {'range': '$100 - $500', 'url': '/shop?price=100-500', 'count': '05'},
            {'range': '$500 - $1000', 'url': '/shop?price=500-1000', 'count': '25'},
            {'range': '$1000 - $5000', 'url': '/shop?price=1000-5000', 'count': '18'},
            {'range': '$5000+', 'url': '/shop?price=5000-plus', 'count': '36'}
        ],
        'materials': [
            {'name': 'Gold', 'url': '/shop?material=gold', 'count': '45'},
            {'name': 'Silver', 'url': '/shop?material=silver', 'count': '38'},
            {'name': 'Platinum', 'url': '/shop?material=platinum', 'count': '24'},
            {'name': 'Diamond', 'url': '/shop?material=diamond', 'count': '32'},
            {'name': 'Pearl', 'url': '/shop?material=pearl', 'count': '18'},
            {'name': 'Gemstone', 'url': '/shop?material=gemstone', 'count': '27'}
        ],
        'tags': ['earrings', 'bracelets', 'necklace', 'chains', 'ring', 'kundan', 'casual', 'meenakari'],
        'new_arrivals': [
            {
                'name': 'Diamond ring',
                'image': 'https://placehold.co/600x765?text=Diamond+Ring',
                'url': '/shop/product/1',
                'price': '$23.00',
                'regular_price': '$30.00'
            },
            {
                'name': 'Geometric ring',
                'image': 'https://placehold.co/600x765?text=Geometric+Ring',
                'url': '/shop/product/2',
                'price': '$43.00',
                'regular_price': '$50.00'
            },
            {
                'name': 'Suserrer earring',
                'image': 'https://placehold.co/600x765?text=Earring',
                'url': '/shop/product/3',
                'price': '$15.00',
                'regular_price': '$20.00'
            },
            {
                'name': 'Twister bangle',
                'image': 'https://placehold.co/600x765?text=Bangle',
                'url': '/shop/product/4',
                'price': '$10.00',
                'regular_price': '$15.00'
            },
            {
                'name': 'Zebra earrings',
                'image': 'https://placehold.co/600x765?text=Zebra+Earrings',
                'url': '/shop/product/5',
                'price': '$30.00',
                'regular_price': '$35.00'
            }
        ],
        'instagram_feed': [
            {'image': 'https://placehold.co/445x445?text=Instagram+1', 'url': 'https://www.instagram.com', 'alt': 'Instagram post 1'},
            {'image': 'https://placehold.co/445x445?text=Instagram+2', 'url': 'https://www.instagram.com', 'alt': 'Instagram post 2'},
            {'image': 'https://placehold.co/445x445?text=Instagram+3', 'url': 'https://www.instagram.com', 'alt': 'Instagram post 3'},
            {'image': 'https://placehold.co/445x445?text=Instagram+4', 'url': 'https://www.instagram.com', 'alt': 'Instagram post 4'},
            {'image': 'https://placehold.co/445x445?text=Instagram+5', 'url': 'https://www.instagram.com', 'alt': 'Instagram post 5'},
            {'image': 'https://placehold.co/445x445?text=Instagram+6', 'url': 'https://www.instagram.com', 'alt': 'Instagram post 6'}
        ]
    }
    
    # Merge the shop sidebar data with the general data
    data.update(shop_sidebar_data)
    
    return render_template('demo-jewellery-store-shop-sidebar.html', **data)

@app.route('/categories')
def categories():
    data = get_sample_data()
    
    # Categories page specific data
    categories_data = {
        'page_title': 'Categories - Jewelry Store',
        'meta_description': 'Browse our exquisite collection of jewelry categories including rings, necklaces, earrings, bracelets, pendants, and more.',
        'page_heading': 'Categories',
        'page_name': 'Categories',
        'home_label': 'Home',
        'page_title_image_url': 'https://placehold.co/1920x470?text=Categories',
        'footer_bg_image_url': url_for('static', filename='images/demo-jewellery-store-footer-bg.jpg'),
        'category_items': [
            {
                'title': 'Bangles',
                'image': 'https://placehold.co/600x477?text=Bangles',
                'url': '/shop?category=bangles',
                'view_text': 'View collection'
            },
            {
                'title': 'Pendants',
                'image': 'https://placehold.co/600x477?text=Pendants',
                'url': '/shop?category=pendants',
                'view_text': 'View collection'
            },
            {
                'title': 'Chain',
                'image': 'https://placehold.co/600x477?text=Chain',
                'url': '/shop?category=chain',
                'view_text': 'View collection'
            },
            {
                'title': 'Earrings',
                'image': 'https://placehold.co/600x1003?text=Earrings',
                'url': '/shop?category=earrings',
                'view_text': 'View collection'
            },
            {
                'title': 'Rings',
                'image': 'https://placehold.co/600x477?text=Rings',
                'url': '/shop?category=rings',
                'view_text': 'View collection'
            },
            {
                'title': 'Necklace',
                'image': 'https://placehold.co/600x1003?text=Necklace',
                'url': '/shop?category=necklace',
                'view_text': 'View collection'
            },
            {
                'title': 'Bracelet',
                'image': 'https://placehold.co/600x477?text=Bracelet',
                'url': '/shop?category=bracelet',
                'view_text': 'View collection'
            }
        ],
        'instagram_feed': [
            {'image': 'https://placehold.co/445x445?text=Instagram+1'},
            {'image': 'https://placehold.co/445x445?text=Instagram+2'},
            {'image': 'https://placehold.co/445x445?text=Instagram+3'},
            {'image': 'https://placehold.co/445x445?text=Instagram+4'},
            {'image': 'https://placehold.co/445x445?text=Instagram+5'},
            {'image': 'https://placehold.co/445x445?text=Instagram+6'}
        ],
        'account_items': [
            {'name': 'Wishlist', 'url': '/wishlist'},
            {'name': 'Order history', 'url': '/order-history'},
            {'name': 'Account details', 'url': '/account'},
            {'name': 'Customer support', 'url': '/support'},
            {'name': 'Logout', 'url': '/logout'}
        ],
        'cart_items': [
            {
                'name': 'Delica Omtantur',
                'image': 'https://placehold.co/600x765?text=Delica+Omtantur',
                'price': '$100.00',
                'url': '/shop/product/1'
            },
            {
                'name': 'Gianvito Rossi',
                'image': 'https://placehold.co/600x765?text=Gianvito+Rossi',
                'price': '$99.99',
                'url': '/shop/product/2'
            }
        ],
        'rings': [
            {'name': 'Engagement', 'url': '/shop?category=rings&type=engagement'},
            {'name': 'Gold rings', 'url': '/shop?category=rings&type=gold'},
            {'name': 'Casual rings', 'url': '/shop?category=rings&type=casual'},
            {'name': 'Silver rings', 'url': '/shop?category=rings&type=silver'},
            {'name': 'Platinum rings', 'url': '/shop?category=rings&type=platinum'},
            {'name': 'Diamond rings', 'url': '/shop?category=rings&type=diamond'}
        ],
        'earrings': [
            {'name': 'Jhumkas', 'url': '/shop?category=earrings&type=jhumkas'},
            {'name': 'Barbells', 'url': '/shop?category=earrings&type=barbells'},
            {'name': 'Hug hoops', 'url': '/shop?category=earrings&type=hug-hoops'},
            {'name': 'Tear drop', 'url': '/shop?category=earrings&type=tear-drop'},
            {'name': 'Suidhaga', 'url': '/shop?category=earrings&type=suidhaga'},
            {'name': 'Gemstone', 'url': '/shop?category=earrings&type=gemstone'}
        ],
        'necklaces': [
            {'name': 'Bib necklece', 'url': '/shop?category=necklaces&type=bib'},
            {'name': 'Collar necklece', 'url': '/shop?category=necklaces&type=collar'},
            {'name': 'Rope necklece', 'url': '/shop?category=necklaces&type=rope'},
            {'name': 'Locket necklece', 'url': '/shop?category=necklaces&type=locket'},
            {'name': 'Chain necklece', 'url': '/shop?category=necklaces&type=chain'},
            {'name': 'Opera nacklece', 'url': '/shop?category=necklaces&type=opera'}
        ],
        'pendants': [
            {'name': 'Alphabet', 'url': '/shop?category=pendants&type=alphabet'},
            {'name': 'Mangalsutra', 'url': '/shop?category=pendants&type=mangalsutra'},
            {'name': 'Religious', 'url': '/shop?category=pendants&type=religious'},
            {'name': 'Diamond', 'url': '/shop?category=pendants&type=diamond'},
            {'name': 'Heart shaped', 'url': '/shop?category=pendants&type=heart'},
            {'name': 'Gemstone', 'url': '/shop?category=pendants&type=gemstone'}
        ],
        'bracelets': [
            {'name': 'Caratlane chain', 'url': '/shop?category=bracelets&type=caratlane'},
            {'name': 'Oval bracelets', 'url': '/shop?category=bracelets&type=oval'},
            {'name': 'Pearl bracelets', 'url': '/shop?category=bracelets&type=pearl'},
            {'name': 'Charm bracelets', 'url': '/shop?category=bracelets&type=charm'},
            {'name': 'Silver brcelets', 'url': '/shop?category=bracelets&type=silver'},
            {'name': 'Tennis bracelets', 'url': '/shop?category=bracelets&type=tennis'}
        ],
        'categories': [
            {'title': 'Rings', 'url': '/shop?category=rings', 'image': 'https://placehold.co/190x140?text=Rings'},
            {'title': 'Bracelet', 'url': '/shop?category=bracelet', 'image': 'https://placehold.co/190x140?text=Bracelet'},
            {'title': 'Earrings', 'url': '/shop?category=earrings', 'image': 'https://placehold.co/190x140?text=Earrings'},
            {'title': 'Necklace', 'url': '/shop?category=necklace', 'image': 'https://placehold.co/190x140?text=Necklace'},
            {'title': 'Pendants', 'url': '/shop?category=pendants', 'image': 'https://placehold.co/190x140?text=Pendants'},
            {'title': 'Watches', 'url': '/shop?category=watches', 'image': 'https://placehold.co/190x140?text=Watches'},
            {'title': 'Chain', 'url': '/shop?category=chain', 'image': 'https://placehold.co/190x140?text=Chain'}
        ],
        'legal_links': [
            {'title': 'Terms and conditions', 'url': '/terms'},
            {'title': 'Privacy policy', 'url': '/privacy'}
        ]
    }
    
    # Merge the about data with the general data
    data.update(categories_data)
    
    return render_template('demo-jewellery-store-categories.html', **data)

@app.route('/wishlist')
def wishlist():
    data = get_sample_data()
    
    # Wishlist page specific data
    wishlist_data = {
        'page_title': 'Jewelry Store - My Wishlist',
        'site_author': 'Jewelry Store',
        'site_title': 'Jewelry Store',
        'meta_description': 'View and manage your favorite jewelry items in your wishlist.',
        'page_heading': 'Wishlist',
        'page_name': 'Wishlist',
        'home_label': 'Home',
        'page_title_image_url': 'https://placehold.co/1920x470?text=Wishlist',
        
        # Wishlist products
        'wishlist_products': [
            {
                'name': 'Diamond earrings',
                'price': '$189.00',
                'original_price': '$200.00',
                'image': 'https://placehold.co/600x765',
                'url': '/shop/product/1',
                'label': 'New',
                'label_class': 'new'
            },
            {
                'name': 'Geometric gold ring',
                'price': '$159.00',
                'original_price': '$180.00',
                'image': 'https://placehold.co/600x765',
                'url': '/shop/product/2'
            },
            {
                'name': 'Gemstone earrings',
                'price': '$189.00',
                'original_price': '$200.00',
                'image': 'https://placehold.co/600x765',
                'url': '/shop/product/3',
                'label': 'Hot',
                'label_class': 'hot'
            },
            {
                'name': 'Gold diamond ring',
                'price': '$289.00',
                'image': 'https://placehold.co/600x765',
                'url': '/shop/product/4'
            },
            {
                'name': 'Diamond pendant',
                'price': '$189.00',
                'original_price': '$200.00',
                'image': 'https://placehold.co/600x765',
                'url': '/shop/product/5'
            },
            {
                'name': 'Platinum band',
                'price': '$129.00',
                'original_price': '$150.00',
                'image': 'https://placehold.co/600x765',
                'url': '/shop/product/6',
                'label': 'New',
                'label_class': 'new'
            },
            {
                'name': 'The aphrodite band',
                'price': '$200.00',
                'image': 'https://placehold.co/600x765',
                'url': '/shop/product/7'
            },
            {
                'name': 'Suserrer earring',
                'price': '$179.00',
                'original_price': '$200.00',
                'image': 'https://placehold.co/600x765',
                'url': '/shop/product/8'
            }
        ],
        
        # Instagram feed
        'instagram_feed': [
            {'image': 'https://placehold.co/445x445'},
            {'image': 'https://placehold.co/445x445'},
            {'image': 'https://placehold.co/445x445'},
            {'image': 'https://placehold.co/445x445'},
            {'image': 'https://placehold.co/445x445'},
            {'image': 'https://placehold.co/445x445'}
        ],
        
        # Cart items
        'cart_items': [
            {
                'name': 'Delica Omtantur',
                'price': '$100.00',
                'image': 'https://placehold.co/600x765',
                'url': '/shop/product/9'
            },
            {
                'name': 'Gianvito Rossi',
                'price': '$99.99',
                'image': 'https://placehold.co/600x765',
                'url': '/shop/product/10'
            }
        ]
    }
    
    # Merge the wishlist data with the general data
    data.update(wishlist_data)
    
    return render_template('demo-jewellery-store-wishlist.html', **data)

@app.route('/account')
def account():
    data = get_sample_data()
    
    # Account page specific data
    account_data = {
        'page_title': 'Jewelry Store - My Account',
        'site_author': 'Jewelry Store',
        'site_title': 'Jewelry Store',
        'meta_description': 'Manage your account settings and view your order history.',
        'page_heading': 'My Account',
        'page_name': 'Account',
        'home_label': 'Home',
        'page_title_image_url': 'https://placehold.co/1920x470?text=My+Account',
        
        # User information
        'user': {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'phone': '+1 123-456-7890',
            'address': '123 Main St, Anytown, USA',
            'orders': [
                {
                    'order_id': 'ORD-12345',
                    'date': '2023-05-15',
                    'status': 'Delivered',
                    'total': '$289.00'
                },
                {
                    'order_id': 'ORD-12346',
                    'date': '2023-06-20',
                    'status': 'Processing',
                    'total': '$159.00'
                }
            ]
        },
        
        # Instagram feed
        'instagram_feed': [
            {'image': 'https://placehold.co/445x445'},
            {'image': 'https://placehold.co/445x445'},
            {'image': 'https://placehold.co/445x445'},
            {'image': 'https://placehold.co/445x445'},
            {'image': 'https://placehold.co/445x445'},
            {'image': 'https://placehold.co/445x445'}
        ],
        
        # Cart items
        'cart_items': [
            {
                'name': 'Delica Omtantur',
                'price': '$100.00',
                'image': 'https://placehold.co/600x765',
                'url': '/shop/product/9'
            },
            {
                'name': 'Gianvito Rossi',
                'price': '$99.99',
                'image': 'https://placehold.co/600x765',
                'url': '/shop/product/10'
            }
        ]
    }
    
    # Merge the account data with the general data
    data.update(account_data)
    
    return render_template('demo-jewellery-store-account.html', **data)

@app.route('/about')
def about():
    data = get_sample_data()
    
    # About page specific data
    about_data = {
        'page_title': 'About Us - Jewelry Store',
        'meta_description': 'Learn about our jewelry store, our history, our team, and why customers trust us for fine jewelry since 1998.',
        'page_heading': 'About us',
        'page_name': 'About us',
        'home_label': 'Home',
        'page_title_image_url': 'https://placehold.co/1920x470?text=About+Us',
        'footer_bg_image_url': url_for('static', filename='images/demo-jewellery-store-footer-bg.jpg'),
        'about_heading': 'The great thing about costume jewellery there\'s something.',
        'about_text': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the when an unknown printer took standard.',
        'about_image': 'https://placehold.co/540x565?text=About+Image',
        'video_image': 'https://placehold.co/885x570?text=Video+Image',
        'video_url': 'https://www.youtube.com/watch?v=cfXHhfNy7tU',
        'started_since_text': 'Started store since',
        'started_year': '1998',
        'why_choose_heading': 'Why choose us?',
        'why_choose_text': 'Lorem ipsum dolor amet consectetur adipiscing dictum placerat diam in vestibulum vivamus in eros.',
        'features': [
            {
                'icon': 'ti-truck',
                'title': 'Free shipping',
                'description': 'Lorem ipsum is simply dummy text printing.'
            },
            {
                'icon': 'ti-headphone',
                'title': 'Online support',
                'description': 'Lorem ipsum is simply dummy text printing.'
            },
            {
                'icon': 'ti-reload',
                'title': '30 Days return',
                'description': 'Lorem ipsum is simply dummy text printing.'
            },
            {
                'icon': 'ti-credit-card',
                'title': 'Secure payment',
                'description': 'Lorem ipsum is simply dummy text printing.'
            }
        ],
        'trust_badge_text': 'trust',
        'trust_text': 'Genuine <span class="text-decoration-line-bottom">10000+ customer</span> trusting our products.',
        'slider_image': 'https://placehold.co/580x420?text=Slider+Image',
        'slider_slides': [
            {
                'subtitle': 'World class designers',
                'title': 'Exclusive design',
                'description': 'Lorem ipsum dolor sit amet consectetur adipiscing elit do eiusmod tempor incididunt ut labore et dolore magna ut enim veniam. Lorem ipsum dolor sit amet consectetur adipiscing elit.'
            },
            {
                'subtitle': '100% secure method',
                'title': 'Secure payment',
                'description': 'Lorem ipsum dolor sit amet consectetur adipiscing elit do eiusmod tempor incididunt ut labore et dolore magna ut enim veniam. Lorem ipsum dolor sit amet consectetur adipiscing elit.'
            },
            {
                'subtitle': '24/7 support center',
                'title': 'Online support',
                'description': 'Lorem ipsum dolor sit amet consectetur adipiscing elit do eiusmod tempor incididunt ut labore et dolore magna ut enim veniam. Lorem ipsum dolor sit amet consectetur adipiscing elit.'
            }
        ],
        'team_heading': 'Our amazing team',
        'team_text': 'Lorem ipsum dolor amet consectetur adipiscing dictum placerat diam in vestibulum vivamus in eros.',
        'team_members': [
            {
                'name': 'Jeremy dupont',
                'position': 'Director',
                'image': 'https://placehold.co/600x756?text=Jeremy',
                'social_links': [
                    {'icon': 'fa-brands fa-facebook-f', 'url': 'https://www.facebook.com/'},
                    {'icon': 'fa-brands fa-dribbble', 'url': 'http://www.dribbble.com/'},
                    {'icon': 'fa-brands fa-twitter', 'url': 'https://www.twitter.com/'},
                    {'icon': 'fa-brands fa-instagram', 'url': 'http://www.instagram.com'}
                ]
            },
            {
                'name': 'Jessica dover',
                'position': 'Founder',
                'image': 'https://placehold.co/600x756?text=Jessica',
                'social_links': [
                    {'icon': 'fa-brands fa-facebook-f', 'url': 'https://www.facebook.com/'},
                    {'icon': 'fa-brands fa-dribbble', 'url': 'http://www.dribbble.com/'},
                    {'icon': 'fa-brands fa-twitter', 'url': 'https://www.twitter.com/'},
                    {'icon': 'fa-brands fa-instagram', 'url': 'http://www.instagram.com'}
                ]
            },
            {
                'name': 'Matthew taylor',
                'position': 'Operator',
                'image': 'https://placehold.co/600x756?text=Matthew',
                'social_links': [
                    {'icon': 'fa-brands fa-facebook-f', 'url': 'https://www.facebook.com/'},
                    {'icon': 'fa-brands fa-dribbble', 'url': 'http://www.dribbble.com/'},
                    {'icon': 'fa-brands fa-twitter', 'url': 'https://www.twitter.com/'},
                    {'icon': 'fa-brands fa-instagram', 'url': 'http://www.instagram.com'}
                ]
            },
            {
                'name': 'Johncy parker',
                'position': 'Accounter',
                'image': 'https://placehold.co/600x756?text=Johncy',
                'social_links': [
                    {'icon': 'fa-brands fa-facebook-f', 'url': 'https://www.facebook.com/'},
                    {'icon': 'fa-brands fa-dribbble', 'url': 'http://www.dribbble.com/'},
                    {'icon': 'fa-brands fa-twitter', 'url': 'https://www.twitter.com/'},
                    {'icon': 'fa-brands fa-instagram', 'url': 'http://www.instagram.com'}
                ]
            }
        ],
        'clients': [
            {'name': 'Pingdom', 'logo': 'images/logo-pingdom-dark-gray.svg', 'url': '#'},
            {'name': 'PayPal', 'logo': 'images/logo-paypal-dark-gray.svg', 'url': '#'},
            {'name': 'Walmart', 'logo': 'images/logo-walmart-dark-gray.svg', 'url': '#'},
            {'name': 'Amazon', 'logo': 'images/logo-amazon-dark-gray.svg', 'url': '#'},
            {'name': 'Logitech', 'logo': 'images/logo-logitech-dark-gray.svg', 'url': '#'},
            {'name': 'Pingdom', 'logo': 'images/logo-pingdom-dark-gray.svg', 'url': '#'},
            {'name': 'PayPal', 'logo': 'images/logo-paypal-dark-gray.svg', 'url': '#'},
            {'name': 'Walmart', 'logo': 'images/logo-walmart-dark-gray.svg', 'url': '#'}
        ],
        'categories': [
            {'title': 'Rings', 'url': '/shop?category=rings', 'image': 'https://placehold.co/190x140?text=Rings'},
            {'title': 'Bracelet', 'url': '/shop?category=bracelet', 'image': 'https://placehold.co/190x140?text=Bracelet'},
            {'title': 'Earrings', 'url': '/shop?category=earrings', 'image': 'https://placehold.co/190x140?text=Earrings'},
            {'title': 'Necklace', 'url': '/shop?category=necklace', 'image': 'https://placehold.co/190x140?text=Necklace'},
            {'title': 'Pendants', 'url': '/shop?category=pendants', 'image': 'https://placehold.co/190x140?text=Pendants'},
            {'title': 'Watches', 'url': '/shop?category=watches', 'image': 'https://placehold.co/190x140?text=Watches'},
            {'title': 'Chain', 'url': '/shop?category=chain', 'image': 'https://placehold.co/190x140?text=Chain'}
        ],
        'account_items': [
            {'name': 'Wishlist', 'url': '/wishlist'},
            {'name': 'Order history', 'url': '/order-history'},
            {'name': 'Account details', 'url': '/account'},
            {'name': 'Customer support', 'url': '/support'},
            {'name': 'Logout', 'url': '/logout'}
        ],
        'cart_items': [
            {
                'name': 'Delica Omtantur',
                'image': 'https://placehold.co/600x765?text=Delica+Omtantur',
                'price': '$100.00',
                'url': '/shop/product/1'
            },
            {
                'name': 'Gianvito Rossi',
                'image': 'https://placehold.co/600x765?text=Gianvito+Rossi',
                'price': '$99.99',
                'url': '/shop/product/2'
            }
        ]
    }
    
    # Merge the about data with the general data
    data.update(about_data)
    
    return render_template('demo-jewellery-store-about.html', **data)

@app.route('/faq')
def faq():
    data = get_sample_data()
    
    # FAQ page specific data
    faq_data = {
        'page_title': 'FAQs - Jewelry Store',
        'meta_description': 'Find answers to frequently asked questions about our jewelry, ordering process, shipping, returns, and more.',
        'page_heading': 'FAQs',
        'page_name': 'Faqs',
        'home_label': 'Home',
        'page_title_image_url': 'https://placehold.co/1920x470?text=FAQs',
        'footer_bg_image_url': url_for('static', filename='images/demo-jewellery-store-footer-bg.jpg'),
        'faq_tabs': [
            {
                'title': 'General',
                'faqs': [
                    {
                        'question': 'Can i order over the phone?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    },
                    {
                        'question': 'I am having difficulty placing an order?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    },
                    {
                        'question': 'What payment methods does accept?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    },
                    {
                        'question': 'Can i amend my order once placed?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    },
                    {
                        'question': 'How do i know if my order was successful?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    },
                    {
                        'question': 'What if my order is incorrect?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    }
                ]
            },
            {
                'title': 'Shopping information',
                'faqs': [
                    {
                        'question': 'Can i order over the phone?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    },
                    {
                        'question': 'I am having difficulty placing an order?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    },
                    {
                        'question': 'What payment methods does accept?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    },
                    {
                        'question': 'Can i amend my order once placed?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    },
                    {
                        'question': 'How do i know if my order was successful?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    },
                    {
                        'question': 'What if my order is incorrect?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    }
                ]
            },
            {
                'title': 'Payment information',
                'faqs': [
                    {
                        'question': 'Can I return my order?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    },
                    {
                        'question': 'What if my item is damaged or faulty?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    },
                    {
                        'question': 'How long will it take to process a return?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    },
                    {
                        'question': 'Why does the refund amount exclude delivery?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    },
                    {
                        'question': 'Need more help?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    },
                    {
                        'question': 'What if my item is damaged or faulty?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    }
                ]
            },
            {
                'title': 'Orders and returns',
                'faqs': [
                    {
                        'question': 'Can i order over the phone?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    },
                    {
                        'question': 'I am having difficulty placing an order?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    },
                    {
                        'question': 'What payment methods does accept?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    },
                    {
                        'question': 'Can i amend my order once placed?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    },
                    {
                        'question': 'How do i know if my order was successful?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    },
                    {
                        'question': 'What if my order is incorrect?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    }
                ]
            },
            {
                'title': 'Ordering from crafto',
                'faqs': [
                    {
                        'question': 'Can i order over the phone?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    },
                    {
                        'question': 'I am having difficulty placing an order?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    },
                    {
                        'question': 'What payment methods does accept?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    },
                    {
                        'question': 'Can i amend my order once placed?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    },
                    {
                        'question': 'How do i know if my order was successful?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    },
                    {
                        'question': 'What if my order is incorrect?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    }
                ]
            },
            {
                'title': 'Help and support',
                'faqs': [
                    {
                        'question': 'Can i order over the phone?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    },
                    {
                        'question': 'I am having difficulty placing an order?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    },
                    {
                        'question': 'What payment methods does accept?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    },
                    {
                        'question': 'Can i amend my order once placed?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    },
                    {
                        'question': 'How do i know if my order was successful?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    },
                    {
                        'question': 'What if my order is incorrect?',
                        'answer': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took galley of type and scrambled to make type.'
                    }
                ]
            }
        ],
        'instagram_feed': [
            {'image': 'https://placehold.co/445x445?text=Instagram+1'},
            {'image': 'https://placehold.co/445x445?text=Instagram+2'},
            {'image': 'https://placehold.co/445x445?text=Instagram+3'},
            {'image': 'https://placehold.co/445x445?text=Instagram+4'},
            {'image': 'https://placehold.co/445x445?text=Instagram+5'},
            {'image': 'https://placehold.co/445x445?text=Instagram+6'}
        ],
        'account_items': [
            {'name': 'Wishlist', 'url': '/wishlist'},
            {'name': 'Order history', 'url': '/order-history'},
            {'name': 'Account details', 'url': '/account'},
            {'name': 'Customer support', 'url': '/support'},
            {'name': 'Logout', 'url': '/logout'}
        ],
        'cart_items': [
            {
                'name': 'Delica Omtantur',
                'image': 'https://placehold.co/600x765?text=Delica+Omtantur',
                'price': '$100.00',
                'url': '/shop/product/1'
            },
            {
                'name': 'Gianvito Rossi',
                'image': 'https://placehold.co/600x765?text=Gianvito+Rossi',
                'price': '$99.99',
                'url': '/shop/product/2'
            }
        ],
        'legal_links': [
            {'title': 'Terms and conditions', 'url': '/terms'},
            {'title': 'Privacy policy', 'url': '/privacy'}
        ]
    }
    
    # Merge the FAQ data with the general data
    data.update(faq_data)
    
    return render_template('demo-jewellery-store-faq.html', **data)

@app.route('/blog')
def blog():
    data = get_sample_data()

    # Blog page specific data
    blog_data = {
        'page_title': 'Blog - Jewelry Store',
        'meta_description': 'Read the latest news and articles from our jewelry store.',
        'page_heading': 'Latest Blog',
        'page_name': 'Blog',
        'home_label': 'Home',
        'page_title_image_url': 'https://placehold.co/1920x470?text=Blog',
        'blog_posts': [
            {
                'id': 1,
                'title': 'It takes a real designer to design for real women',
                'image': 'https://placehold.co/800x1015?text=Jewelry+Design',
                'date': '30 June 2023',
                'author': 'Jonse robbert',
                'category': 'Jewellery',
                'comments_count': 5,
                'excerpt': 'Designing jewelry for real women requires understanding their needs, preferences, and lifestyles. It goes beyond creating beautiful pieces to crafting wearable art that enhances a woman\'s natural beauty.'
            },
            {
                'id': 2,
                'title': 'I get sent lots of jewellery by fans, that\'s absolutely lovely',
                'image': 'https://placehold.co/800x1015?text=Fine+Jewelry',
                'date': '22 June 2023',
                'author': 'Katie mcgrath',
                'category': 'Jewellery',
                'comments_count': 8,
                'excerpt': 'Fine jewelry carries stories, memories, and emotions. Each piece becomes a companion, a silent witness to life\'s moments, offering comfort and confidence to its wearer.'
            },
            {
                'id': 3,
                'title': 'We don\'t have a jewellery background, we just come',
                'image': 'https://placehold.co/800x1015?text=Jewelry+Craftsmanship',
                'date': '05 June 2023',
                'author': 'Rosald smith',
                'category': 'Jewellery',
                'comments_count': 3,
                'excerpt': 'In the world of jewelry, it\'s the bold statement pieces that capture attention and imagination. While details matter, it\'s the overall impact and presence of jewelry that truly bewitches and captivates.'
            },
            {
                'id': 4,
                'title': 'Jewelry has the power to be the one little thing',
                'image': 'https://placehold.co/800x1015?text=Jewelry+Power',
                'date': '22 May 2023',
                'author': 'Elizabeth taylor',
                'category': 'Jewellery',
                'comments_count': 6,
                'excerpt': 'Jewelry has the power to be the one little thing that makes you feel unique. It\'s not about the size or cost of the piece, but the meaning behind it and how it makes you feel when you wear it.'
            },
            {
                'id': 5,
                'title': 'Jewelry is the most transformative thing you can wear',
                'image': 'https://placehold.co/800x1015?text=Transformative+Jewelry',
                'date': '08 May 2023',
                'author': 'Jonse robbert',
                'category': 'Jewellery',
                'comments_count': 4,
                'excerpt': 'Jewelry is the most transformative thing you can wear. A simple outfit can be completely changed with the right piece of jewelry, elevating your look from ordinary to extraordinary.'
            },
            {
                'id': 6,
                'title': 'These gems have life in them their colors speak',
                'image': 'https://placehold.co/800x1015?text=Gemstones',
                'date': '28 April 2023',
                'author': 'Den viliamson',
                'category': 'Jewellery',
                'comments_count': 7,
                'excerpt': 'These gems have life in them: their colors speak, say what words fail of. Each gemstone has its own unique energy and character, telling a story that transcends language.'
            },
            {
                'id': 7,
                'title': 'Jewelry takes people\'s minds off your wrinkles',
                'image': 'https://placehold.co/800x1015?text=Jewelry+Magic',
                'date': '19 April 2023',
                'author': 'Sarah phillips',
                'category': 'Jewellery',
                'comments_count': 5,
                'excerpt': 'Jewelry takes people\'s minds off your wrinkles. It\'s a distraction from the signs of aging, drawing attention to your personal style and taste rather than physical imperfections.'
            },
            {
                'id': 8,
                'title': 'If you don\'t know jewelry, know the jeweler',
                'image': 'https://placehold.co/800x1015?text=Know+Your+Jeweler',
                'date': '08 April 2023',
                'author': 'Andy glamere',
                'category': 'Jewellery',
                'comments_count': 3,
                'excerpt': 'If you don\'t know jewelry, know the jeweler. Building a relationship with a trusted jeweler ensures that you\'re getting quality pieces that are worth their price and will stand the test of time.'
            },
            {
                'id': 9,
                'title': 'A woman needs ropes and ropes of pearls',
                'image': 'https://placehold.co/800x1015?text=Pearl+Jewelry',
                'date': '08 March 2023',
                'author': 'Jonse robbert',
                'category': 'Jewellery',
                'comments_count': 9,
                'excerpt': 'A woman needs ropes and ropes of pearls. Pearls are timeless and versatile, adding elegance and sophistication to any outfit, whether it\'s a casual day look or formal evening attire.'
            }
        ],
        'current_page': 1,
        'total_pages': 3
    }

    # Merge the blog data with the general data
    data.update(blog_data)

    # Handle pagination
    page = request.args.get('page', 1, type=int)
    per_page = 6
    start = (page - 1) * per_page
    end = start + per_page

    data['blog_posts'] = data['blog_posts'][start:end]
    data['current_page'] = page

    return render_template('demo-jewellery-store-blog.html', **data)

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    data = get_sample_data()

    # Blog posts data (in a real app, this would come from a database)
    blog_posts = [
        {
            'id': 1,
            'title': 'It takes a real designer to design for real women',
            'image': 'https://placehold.co/800x500?text=Jewelry+Design',
            'hero_image': 'https://placehold.co/1920x1080?text=Jewelry+Design',
            'date': '30 June 2023',
            'author': 'Emma Johnson',
            'author_title': 'Co-founder',
            'author_image': 'https://placehold.co/125x125',
            'author_bio': 'Lorem ipsum is simply dummy text of the printing typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the when an unknown printer took a galley.',
            'category': 'Jewelry Design',
            'comments_count': 5,
            'content': '<p><span class="alt-font first-letter first-letter-block border first-letter-round border-2 border-color-light-medium-gray text-dark-gray">D</span>esigning jewelry for real women requires understanding their needs, preferences, and lifestyles. It goes beyond creating beautiful pieces to crafting wearable art that enhances a woman\'s natural beauty.</p><p>A real designer considers factors like comfort, versatility, and durability, ensuring that each piece not only looks stunning but also integrates seamlessly into a woman\'s daily life. They recognize that jewelry is not just an accessory but an expression of identity and personal style.</p><p>The best designers draw inspiration from the diverse beauty of women around the world, creating inclusive collections that celebrate individuality rather than conforming to narrow beauty standards.</p>',
            'quote': 'Architecture tends to consume everything else it has become one\'s entire life.',
            'quote_author': '- Shoko mugikura -',
            'featured_image': 'https://placehold.co/1920x1080?text=Featured+Image',
            'section_title': 'Tomorrow is the most important thing in life comes into us at midnight very clean.',
            'section_content': '<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent ullamcorper ex nunc, in fringilla fringilla sed. Nam semper odio eu urna viverra, eu luctus mauris sollicitudin. Morbi ultricies est et odio vehicula, vel lacinia ipsum ullamcorper. Mauris mattis placerat quam, aliquam vestibulum dui bibendum eu. Curabitur eu euismod ex, et hendrerit purus. Donec condimentum neque id iaculis. Etiam dui id dolor lobortis cursus ac maximus nisl in sodales lacus nec cursus varius.</p>',
            'gallery_images': ['https://placehold.co/1200x700?text=Gallery+Image+1', 'https://placehold.co/1200x700?text=Gallery+Image+2'],
            'additional_sections': [
                {'title': 'Architecture is inhabited sculpture.', 'content': '<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent ullamcorper ex nunc, in fringilla fringilla sed. Nam semper odio eu urna viverra, eu luctus mauris sollicitudin. Morbi ultricies est et odio vehicula, vel lacinia ipsum ullamcorper. Mauris mattis placerat quam, aliquam vestibulum dui bibendum eu. Curabitur eu euismod ex, et hendrerit purus. Donec condimentum neque id iaculis. Etiam dui id dolor lobortis cursus ac maximus nisl in sodales lacus nec cursus varius.</p>'},
                {'title': 'A room is not a room without natural light.', 'content': '<p>Morbi ultricies est et odio vehicula, vel lacinia ipsum ullamcorper. Mauris mattis placerat quam, aliquam vestibulum dui bibendum eu. Curabitur eu euismod ex, and many hendrerit purus. Donec condimentum vel neque id iaculis. Etiam dolor lobortis cursus ac maximus nisl. In sodales lacus ullamcorper ultricies est et odio vehicula mattis placerat quam cursus varius.</p>'}
            ],
            'tags': ['design', 'women', 'jewelry'],
            'likes': '05',
            'comments': [
                {'author': 'Herman Miller', 'date': '17 July 2020, 6:05 PM', 'content': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the make book.', 'image': 'https://placehold.co/130x130', 'replies': [
                    {'author': 'Wilbur Haddock', 'date': '18 July 2020, 10:19 PM', 'content': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since.', 'image': 'https://placehold.co/130x130'},
                    {'author': 'Colene Landin', 'date': '18 July 2020, 12:39 PM', 'content': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Ipsum has been the industry\'s standard dummy text ever since.', 'image': 'https://placehold.co/130x130', 'highlight': True}
                ]},
                {'author': 'Jennifer Freeman', 'date': '19 July 2020, 8:25 PM', 'content': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the make a type specimen book.', 'image': 'https://placehold.co/130x130'}
            ]
        },
        {
            'id': 2,
            'title': 'A girl with fine jewelry is never truly alone',
            'image': 'https://placehold.co/800x500?text=Fine+Jewelry',
            'hero_image': 'https://placehold.co/1920x1080?text=Fine+Jewelry',
            'date': '15 June 2023',
            'author': 'Michael Smith',
            'author_title': 'Jewelry Designer',
            'author_image': 'https://placehold.co/125x125',
            'author_bio': 'Lorem ipsum is simply dummy text of the printing typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the when an unknown printer took a galley.',
            'category': 'Fine Jewelry',
            'comments_count': 8,
            'content': '<p><span class="alt-font first-letter first-letter-block border first-letter-round border-2 border-color-light-medium-gray text-dark-gray">F</span>ine jewelry carries stories, memories, and emotions. Each piece becomes a companion, a silent witness to life\'s moments, offering comfort and confidence to its wearer.</p><p>When a woman adorns herself with fine jewelry, she carries with her not just precious metals and gemstones, but also heritage, craftsmanship, and artistry. These pieces often become talismans of strength and reminders of significant life events.</p><p>Unlike fashion trends that come and go, fine jewelry remains a constant companion, often passed down through generations, carrying with it the stories and spirits of those who wore it before.</p>',
            'tags': ['fine jewelry', 'women', 'luxury']
        },
        {
            'id': 3,
            'title': 'The devil lives in jewelry, not in details',
            'image': 'https://placehold.co/800x500?text=Jewelry+Craftsmanship',
            'hero_image': 'https://placehold.co/1920x1080?text=Jewelry+Craftsmanship',
            'date': '10 June 2023',
            'author': 'Sophia Williams',
            'author_title': 'Jewelry Artisan',
            'author_image': 'https://placehold.co/125x125',
            'author_bio': 'Lorem ipsum is simply dummy text of the printing typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the when an unknown printer took a galley.',
            'category': 'Jewelry Craftsmanship',
            'comments_count': 3,
            'content': '<p><span class="alt-font first-letter first-letter-block border first-letter-round border-2 border-color-light-medium-gray text-dark-gray">I</span>n the world of jewelry, it\'s the bold statement pieces that capture attention and imagination. While details matter, it\'s the overall impact and presence of jewelry that truly bewitches and captivates.</p><p>The most memorable jewelry pieces are those that make a statement, that transform an outfit and elevate the wearer\'s presence. They possess a certain magic that goes beyond technical perfection, embodying emotion, character, and soul.</p><p>Master jewelers understand that while precision is important, it\'s the passion, creativity, and artistic vision infused into each piece that gives jewelry its power to enchant and seduce.</p>',
            'tags': ['craftsmanship', 'design', 'statement pieces']
        }
    ]

    # Find the blog post by ID
    post = None
    for p in blog_posts:
        if p['id'] == post_id:
            post = p
            break

    if not post:
        flash('Blog post not found', 'error')
        return redirect(url_for('blog'))

    # Get related posts (excluding current post)
    related_posts = []
    for p in blog_posts:
        if p['id'] != post_id:
            related_posts.append(p)

    # Blog post specific data
    blog_post_data = {
        'page_title': f'{post["title"]} - Jewelry Store Blog',
        'meta_description': f'Read about {post["title"]} in our jewelry store blog.',
        'post': post,
        'related_posts': related_posts[:3],  # Limit to 3 related posts
        'comments_heading': f'{len(post.get("comments", []))} Comments',
        'leave_comment_heading': 'Write a Comment',
        'name_label': 'Enter your name*',
        'email_label': 'Enter your email address*',
        'comment_label': 'Your message',
        'submit_button_text': 'Post Comment'
    }

    # Merge the blog post data with the general data
    data.update(blog_post_data)

    return render_template('demo-jewellery-store-blog-single-clean.html', **data)

@app.route('/contact')
def contact():
    data = get_sample_data()

    # Contact page specific data
    contact_data = {
        'page_title': 'Contact Us - Jewelry Store',
        'meta_description': 'Contact our jewelry store for inquiries, support, or to schedule an appointment. We\'re here to help with all your jewelry needs.',
        'page_heading': 'Contact us',
        'page_name': 'Contact',
        'home_label': 'Home',
        'page_title_image_url': 'https://placehold.co/1920x470?text=Contact+Us',
        'contact_image_url': 'https://placehold.co/510x620?text=Contact+Us',
        'happy_customers': '540',
        'happy_customers_text': 'Happy customer',
        'positive_feedback': '98%',
        'positive_feedback_text': 'Positive feedback',
        'award_winning': '150',
        'award_winning_text': 'Award winning',
        'contact_heading': 'We\'d love to hear from you.',
        'phone_label': 'Get in touch with us?',
        'phone_number': '1234567890',
        'phone_number_display': '123 456 7890',
        'email_label': 'How can help you?',
        'email_address': 'help@domain.com',
        'address_label': 'Are you ready for visit?',
        'address': '12 Orchard, London',
        'chat_label': 'Need live chat?',
        'chat_email': 'chat@domain.com',
        'contact_form_action': '/submit-contact',
        'name_placeholder': 'Your name*',
        'email_placeholder': 'Your email address*',
        'phone_placeholder': 'Your phone',
        'message_placeholder': 'Your message',
        'submit_button_text': 'Send message',
        'map_lat': '-37.805688',
        'map_lng': '144.962312',
        'store_name': 'Jewelry Store',
        'store_address': '16122 Collins street, Melbourne, Australia',
        'google_maps_api_key': 'AIzaSyCA56KqSJ11nQUw_tXgXyNMiPmQeM7EaSA'
    }

    # Merge the contact data with the general data
    data.update(contact_data)

    return render_template('demo-jewellery-store-contact.html', **data)

@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    # In a real application, you would process the form data here
    # For now, we'll just redirect back to the contact page with a success message
    flash('Your message has been sent successfully!', 'success')
    return redirect(url_for('contact'))

@app.route('/layout')
def layout_template():
    """
    Route to demonstrate the base layout template.
    This doesn't affect other routes and can be used as a starting point for new pages.
    """
    data = get_sample_data()
    
    # Add any specific data for this template
    layout_data = {
        'page_title': 'Layout Template - Jewelry Store',
        'meta_description': 'Base layout template for the jewelry store website.',
        'page_heading': 'Layout Template',
        'page_name': 'Layout',
        'page_title_image_url': 'https://placehold.co/1920x470?text=Layout+Template',
        'cart_title': 'Template Overview',
        'cart_content': 'This is a demonstration of the base layout template that can be used for creating new pages.'
    }
    
    # Merge the layout data with the general data
    data.update(layout_data)
    
    # Change this line to use an existing template instead of the missing one
    return render_template('demo-jewellery-store.html', **data)

@app.route('/cart')
def cart():
    """
    Route for the shopping cart page using the new layout template.
    """
    data = get_sample_data()
    
    # Cart page specific data
    cart_data = {
        'page_title': 'Shopping Cart - Jewelry Store',
        'meta_description': 'View and manage items in your shopping cart.',
        'page_heading': 'Shopping Cart',
        'page_name': 'Cart',
        'home_label': 'Home',
        'page_title_image_url': 'https://placehold.co/1920x470?text=Shopping+Cart',
        'cart_title': 'Your Shopping Cart',
        'cart_content': 'Review the items in your cart before proceeding to checkout.',
        'cart_items': [
            {
                'id': 1,
                'name': 'Diamond Engagement Ring',
                'image': 'https://placehold.co/100x100?text=Diamond+Ring',
                'price': '$1,299.00',
                'quantity': 1,
                'total': '$1,299.00'
            },
            {
                'id': 2,
                'name': 'Gold Chain Necklace',
                'image': 'https://placehold.co/100x100?text=Gold+Necklace',
                'price': '$899.00',
                'quantity': 1,
                'total': '$899.00'
            }
        ],
        'subtotal': '$2,198.00',
        'shipping': '$0.00',
        'tax': '$175.84',
        'total': '$2,373.84',
        'continue_shopping_url': '/shop',
        'checkout_url': '/checkout'
    }
    
    # Merge the cart data with the general data
    data.update(cart_data)
    
    # Change this line to use an existing template
    return render_template('demo-jewellery-store-cart.html', **data)


@app.route('/shop/product/<int:product_id>')
def product_detail(product_id):
    """
    Route for the product detail page.
    """
    data = get_sample_data()
    
    # Sample product data - in a real application, you would fetch this from a database
    products = [
        {
            'id': 1,
            'name': 'Diamond Engagement Ring',
            'image': 'https://placehold.co/800x800?text=Diamond+Ring',
            'price': '$1,299.00',
            'regular_price': '$1,499.00',
            'description': 'This exquisite diamond engagement ring features a brilliant-cut center stone set in a classic prong setting. Crafted with the finest materials, this ring symbolizes eternal love and commitment.',
            'sku': 'JWL-DR-1001',
            'categories': [
                {'name': 'Rings', 'url': '/shop/rings'},
                {'name': 'Engagement', 'url': '/shop/engagement'}
            ],
            'tags': [
                {'name': 'Diamond', 'url': '/shop/tags/diamond'},
                {'name': 'Engagement', 'url': '/shop/tags/engagement'},
                {'name': 'Luxury', 'url': '/shop/tags/luxury'}
            ],
            'attributes': [
                {
                    'name': 'Metal',
                    'type': 'button',
                    'options': [
                        {'label': 'White Gold', 'value': 'white-gold', 'selected': True},
                        {'label': 'Yellow Gold', 'value': 'yellow-gold', 'selected': False},
                        {'label': 'Rose Gold', 'value': 'rose-gold', 'selected': False},
                        {'label': 'Platinum', 'value': 'platinum', 'selected': False}
                    ]
                },
                {
                    'name': 'Size',
                    'type': 'size',
                    'options': [
                        {'label': '4', 'value': '4', 'selected': False},
                        {'label': '4.5', 'value': '4.5', 'selected': False},
                        {'label': '5', 'value': '5', 'selected': True},
                        {'label': '5.5', 'value': '5.5', 'selected': False},
                        {'label': '6', 'value': '6', 'selected': False},
                        {'label': '6.5', 'value': '6.5', 'selected': False},
                        {'label': '7', 'value': '7', 'selected': False}
                    ]
                }
            ],
            'specifications': [
                {'name': 'Metal', 'value': '14K White Gold, Yellow Gold, Rose Gold, Platinum'},
                {'name': 'Center Stone', 'value': 'Diamond'},
                {'name': 'Diamond Carat', 'value': '1.0 ct'},
                {'name': 'Diamond Cut', 'value': 'Brilliant Round'},
                {'name': 'Diamond Color', 'value': 'G-H'},
                {'name': 'Diamond Clarity', 'value': 'VS1-VS2'},
                {'name': 'Setting', 'value': 'Prong'},
                {'name': 'Ring Size', 'value': '4-9 (Resizable)'},
                {'name': 'Width', 'value': '2.0 mm'}
            ],
            'gallery': [
                {'url': 'https://placehold.co/800x800?text=Diamond+Ring+1', 'alt': 'Diamond Ring Front View'},
                {'url': 'https://placehold.co/800x800?text=Diamond+Ring+2', 'alt': 'Diamond Ring Side View'},
                {'url': 'https://placehold.co/800x800?text=Diamond+Ring+3', 'alt': 'Diamond Ring Top View'},
                {'url': 'https://placehold.co/800x800?text=Diamond+Ring+4', 'alt': 'Diamond Ring on Hand'}
            ],
            'rating': 5,
            'review_count': 12,
            'average_rating': 4.8,
            'rating_distribution': {
                5: 85,
                4: 10,
                3: 3,
                2: 1,
                1: 1
            },
            'reviews': [
                {
                    'author': 'Jennifer Smith',
                    'date': 'June 15, 2023',
                    'rating': 5,
                    'content': 'This ring exceeded all my expectations! The diamond is absolutely stunning and catches light from every angle. The craftsmanship is impeccable, and it fits perfectly. My fiancée was speechless when I proposed with this ring. Worth every penny!'
                },
                {
                    'author': 'Michael Johnson',
                    'date': 'May 28, 2023',
                    'rating': 4,
                    'content': 'Beautiful ring with excellent quality. The diamond is brilliant and the setting is secure. I took off one star because the sizing ran a bit small, but the customer service was very helpful with the exchange process. My wife loves it!'
                },
                {
                    'author': 'Sarah Williams',
                    'date': 'April 12, 2023',
                    'rating': 5,
                    'content': 'I\'ve been wearing this ring for three months now and I\'m still in awe every time I look at it. The diamond is so clear and sparkly! The white gold setting complements it perfectly. I\'ve received countless compliments. The packaging was also beautiful and made the unboxing experience special.'
                }
            ],
            'stock': 10,
            'label': 'New',
            'label_class': 'new'
        },
        {
            'id': 2,
            'name': 'Gold Chain Necklace',
            'image': 'https://placehold.co/800x800?text=Gold+Necklace',
            'price': '$899.00',
            'regular_price': '$999.00',
            'description': 'Elegant gold chain necklace crafted from 18K gold. Perfect for everyday wear or special occasions.',
            'label': 'Hot',
            'label_class': 'hot'
        },
        {
            'id': 3,
            'name': 'Pearl Earrings',
            'image': 'https://placehold.co/800x800?text=Pearl+Earrings',
            'price': '$499.00',
            'regular_price': '$599.00',
            'description': 'Beautiful pearl earrings with 14K gold settings. These freshwater pearls have excellent luster and shine.'
        },
        {
            'id': 4,
            'name': 'Silver Bracelet',
            'image': 'https://placehold.co/800x800?text=Silver+Bracelet',
            'price': '$349.00',
            'regular_price': '$399.00',
            'description': 'Sterling silver bracelet with intricate design. Adjustable size fits most wrists.',
            'label': 'Sale',
            'label_class': 'sale'
        },
        {
            'id': 5,
            'name': 'Platinum Wedding Band',
            'image': 'https://placehold.co/800x800?text=Platinum+Band',
            'price': '$1,199.00',
            'regular_price': '$1,299.00',
            'description': 'Classic platinum wedding band with a polished finish. Durable and timeless.'
        }
    ]
    
    # Find the product by ID
    product = None
    for p in products:
        if p['id'] == product_id:
            product = p
            break
    
    if not product:
        # If product not found, redirect to shop page
        flash('Product not found', 'error')
        return redirect(url_for('shop'))
    
    # Get related products (excluding current product)
    related_products = []
    for p in products:
        if p['id'] != product_id:
            related_products.append(p)
    
    # Product detail page specific data
    product_detail_data = {
        'page_title': f"{product['name']} - Jewelry Store",
        'meta_description': f"View details and purchase {product['name']} from our exquisite jewelry collection.",
        'page_heading': 'Product Details',
        'page_name': product['name'],
        'home_label': 'Home',
        'shop_label': 'Shop',
        'page_title_image_url': 'https://placehold.co/1920x470?text=Product+Details',
        'shop_banner_1': 'https://placehold.co/580x160?text=Shop+Banner+1',
        'shop_banner_2': 'https://placehold.co/580x160?text=Shop+Banner+2',
        'product': product,
        'product_name': product['name'],
        'product_image_url': product['image'],
        'product_price': product['price'],
        'product_regular_price': product.get('regular_price'),
        'product_description': product['description'],
        'product_full_description': product.get('full_description'),
        'product_sku': product.get('sku'),
        'product_categories': product.get('categories'),
        'product_tags': product.get('tags'),
        'product_attributes': product.get('attributes'),
        'product_specifications': product.get('specifications'),
        'product_gallery': product.get('gallery'),
        'product_rating': product.get('rating'),
        'product_review_count': product.get('review_count'),
        'product_average_rating': product.get('average_rating'),
        'product_rating_distribution': product.get('rating_distribution', {}),
        'product_reviews': product.get('reviews'),
        'product_stock': product.get('stock', 10),
        'product_label': product.get('label'),
        'product_label_class': product.get('label_class'),
        'related_products': related_products[:4],  # Limit to 4 related products
        'review_form_action': '/submit-review'
    }
    
    # Merge the product detail data with the general data
    data.update(product_detail_data)
    
    return render_template('demo-jewellery-store-product-detail.html', **data)

@app.route('/submit-review', methods=['POST'])
def submit_review():
    """
    Process the review form submission.
    """
    # In a real application, you would process the form data here
    # For now, we'll just redirect back to the product page with a success message
    product_id = request.form.get('product_id', 1)
    flash('Your review has been submitted successfully!', 'success')
    return redirect(url_for('product_detail', product_id=product_id))

@app.route('/checkout')
def checkout():
    """
    Route for the checkout page.
    """
    data = get_sample_data()
    
    # Checkout page specific data
    checkout_data = {
        'page_title': 'Checkout - Jewelry Store',
        'meta_description': 'Complete your purchase at our jewelry store.',
        'page_heading': 'Checkout',
        'page_name': 'Checkout',
        'home_label': 'Home',
        'page_title_image_url': 'https://placehold.co/1920x470?text=Checkout',
        'cart_title': 'Your Checkout',
        'cart_content': 'Complete your purchase by providing your billing details and payment information.',
        'item_price': '30.00',
        'subtotal': '30.00',
        'shipping': 'Free',
        'tax': '2.40',
        'total': '32.40',
        'checkout_items': [
            {
                'id': 1,
                'name': 'Zebra earrings',
                'image': 'https://placehold.co/100x100?text=Zebra+Earrings',
                'price': '$30.00',
                'quantity': 1,
                'color': 'Pink',
                'total': '$30.00',
                'url': '/shop/product/1'
            }
        ],
        'shipping_options': [
            {
                'id': 'free_shipping',
                'name': 'Free shipping',
                'price': '$0.00',
                'checked': True
            },
            {
                'id': 'standard_shipping',
                'name': 'Standard shipping',
                'price': '$5.00',
                'checked': False
            },
            {
                'id': 'express_shipping',
                'name': 'Express shipping',
                'price': '$15.00',
                'checked': False
            }
        ],
        'instagram_feed': [
            {'image': 'https://placehold.co/445x445?text=Instagram+1', 'url': 'https://www.instagram.com', 'alt': 'Instagram post 1'},
            {'image': 'https://placehold.co/445x445?text=Instagram+2', 'url': 'https://www.instagram.com', 'alt': 'Instagram post 2'},
            {'image': 'https://placehold.co/445x445?text=Instagram+3', 'url': 'https://www.instagram.com', 'alt': 'Instagram post 3'},
            {'image': 'https://placehold.co/445x445?text=Instagram+4', 'url': 'https://www.instagram.com', 'alt': 'Instagram post 4'},
            {'image': 'https://placehold.co/445x445?text=Instagram+5', 'url': 'https://www.instagram.com', 'alt': 'Instagram post 5'},
            {'image': 'https://placehold.co/445x445?text=Instagram+6', 'url': 'https://www.instagram.com', 'alt': 'Instagram post 6'}
        ],
        'account_items': [
            {'name': 'Wishlist', 'url': '/wishlist'},
            {'name': 'Order history', 'url': '/order-history'},
            {'name': 'Account details', 'url': '/account'},
            {'name': 'Customer support', 'url': '/support'},
            {'name': 'Logout', 'url': '/logout'}
        ],
        'cart_items': [
            {
                'name': 'Zebra earrings',
                'image': 'https://placehold.co/100x100?text=Zebra+Earrings',
                'price': '$30.00',
                'url': '/shop/product/1'
            }
        ],
        'checkout_form_action': '/process-checkout',
        'place_order_url': '/place-order',
        'login_url': '/login',
        'coupon_url': '/apply-coupon',
        'terms_url': '/terms'
    }
    
    # Merge the checkout data with the general data
    data.update(checkout_data)
    
    return render_template('demo-jewellery-store-checkout.html', **data)

@app.route('/process-checkout', methods=['POST'])
def process_checkout():
    """
    Process the checkout form submission.
    """
    # In a real application, you would process the form data here
    # For now, we'll just redirect to a thank you page
    flash('Your order has been placed successfully!', 'success')
    return redirect(url_for('thank_you'))

@app.route('/thank-you')
def thank_you():
    """
    Thank you page after successful checkout.
    """
    data = get_sample_data()
    
    thank_you_data = {
        'page_title': 'Thank You - Jewelry Store',
        'meta_description': 'Thank you for your order at our jewelry store.',
        'page_heading': 'Thank You',
        'page_name': 'Thank You',
        'home_label': 'Home',
        'page_title_image_url': 'https://placehold.co/1920x470?text=Thank+You',
        'thank_you_message': 'Your order has been placed successfully!',
        'order_number': 'ORD-' + str(random.randint(10000, 99999)),
        'order_date': datetime.now().strftime('%B %d, %Y'),
        'continue_shopping_url': '/shop'
    }
    
    # Merge the thank you data with the general data
    data.update(thank_you_data)
    
    return render_template('demo-jewellery-store-thank-you.html', **data)

if __name__ == '__main__':
    app.run(debug=True)