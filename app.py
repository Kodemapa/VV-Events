from flask import Flask, render_template, url_for, request, redirect, flash
from datetime import datetime
import os
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure random key in production

# Helper function to get blog posts
def get_blog_posts():
    return [
        {
            'id': 1,
            'slug': 'it-takes-a-real-designer-to-design-for-real-women',
            'title': 'It takes a real designer to design for real women',
            'image': 'https://placehold.co/800x1015',
            'hero_image': 'https://placehold.co/1920x1080',
            'category': 'Jewellery',
            'category_slug': 'jewellery',
            'author': 'Jonse robbert',
            'author_slug': 'jonse-robbert',
            'author_image': 'https://placehold.co/125x125',
            'author_title': 'Co-founder',
            'author_bio': 'Lorem ipsum is simply dummy text of the printing typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the when an unknown printer took a galley.',
            'date': '30 June 2023',
            'excerpt': 'It takes a real designer to design for real women with real bodies and real lives.',
            'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.'
        },
        {
            'id': 2,
            'slug': 'i-get-sent-lots-of-jewellery-by-fans',
            'title': 'I get sent lots of jewellery by fans, that\'s absolutely lovely',
            'image': 'https://placehold.co/800x1015',
            'hero_image': 'https://placehold.co/1920x1080',
            'category': 'Jewellery',
            'category_slug': 'jewellery',
            'author': 'Katie mcgrath',
            'author_slug': 'katie-mcgrath',
            'author_image': 'https://placehold.co/125x125',
            'author_title': 'Designer',
            'author_bio': 'Lorem ipsum is simply dummy text of the printing typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the when an unknown printer took a galley.',
            'date': '22 June 2023',
            'excerpt': 'I get sent lots of jewellery by fans, that\'s absolutely lovely.'
        },
        {
            'id': 3,
            'slug': 'we-dont-have-a-jewellery-background',
            'title': 'We don\'t have a jewellery background, we just come',
            'image': 'https://placehold.co/800x1015',
            'hero_image': 'https://placehold.co/1920x1080',
            'category': 'Jewellery',
            'category_slug': 'jewellery',
            'author': 'Rosald smith',
            'author_slug': 'rosald-smith',
            'author_image': 'https://placehold.co/125x125',
            'author_title': 'Marketing',
            'author_bio': 'Lorem ipsum is simply dummy text of the printing typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the when an unknown printer took a galley.',
            'date': '05 June 2023',
            'excerpt': 'We don\'t have a jewellery background, we just come with fresh ideas.'
        },
        {
            'id': 4,
            'slug': 'i-have-a-lot-of-lion-jewellery-and-lion-art',
            'title': 'I have a lot of lion jewellery and lion art. I also love crystals.',
            'image': 'https://placehold.co/800x1015',
            'hero_image': 'https://placehold.co/1920x1080',
            'category': 'Luxury',
            'category_slug': 'luxury',
            'author': 'Colene landin',
            'author_slug': 'colene-landin',
            'author_image': 'https://placehold.co/125x125',
            'author_title': 'Co-founder',
            'author_bio': 'Lorem ipsum is simply dummy text of the printing typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the when an unknown printer took a galley.',
            'date': '15 June 2023',
            'excerpt': 'I have a lot of lion jewellery and lion art. I also love crystals.'
        },
        {
            'id': 5,
            'slug': 'jewelry-is-the-most-transformative-thing-you-can-wear',
            'title': 'Jewelry is the most transformative thing you can wear',
            'image': 'https://placehold.co/800x1015',
            'category': 'Jewellery',
            'category_slug': 'jewellery',
            'author': 'Jonse robbert',
            'author_slug': 'jonse-robbert',
            'date': '08 May 2023',
            'excerpt': 'Jewelry is the most transformative thing you can wear.'
        },
        {
            'id': 6,
            'slug': 'these-gems-have-life-in-them-their-colors-speak',
            'title': 'These gems have life in them their colors speak',
            'image': 'https://placehold.co/800x1015',
            'category': 'Jewellery',
            'category_slug': 'jewellery',
            'author': 'Den viliamson',
            'author_slug': 'den-viliamson',
            'date': '28 April 2023',
            'excerpt': 'These gems have life in them: their colors speak, saying what words fail of.'
        }
    ]

# Sample data - in a real application, this would come from a database
def get_sample_data():
    # Navigation items
    nav_items = [
        {
            'name': 'Home',
            'url': '',  # Changed from 'index' to empty string to point to root URL
            'dropdown': False
        },
        {
            'name': 'Shop',
            'url': 'shop',
            'dropdown': True,
            'mega_menu': True,
            'categories': [
                {
                    'name': 'Rings',
                    'subitems': ['Engagement', 'Gold rings', 'Casual rings', 'Silver rings', 'Platinum rings', 'Diamond rings']
                },
                {
                    'name': 'Earrings',
                    'subitems': ['Jhumkas', 'Barbells', 'Hug hoops', 'Tear drop', 'Suidhaga', 'Gemstone']
                },
                {
                    'name': 'Necklaces',
                    'subitems': ['Bib necklece', 'Collar necklece', 'Rope necklece', 'Locket necklece', 'Chain necklece', 'Opera nacklece']
                },
                {
                    'name': 'Pendants',
                    'subitems': ['Alphabet', 'Mangalsutra', 'Religious', 'Diamond', 'Heart shaped', 'Gemstone']
                },
                {
                    'name': 'Breslet',
                    'subitems': ['Caratlane chain', 'Oval bracelets', 'Pearl bracelets', 'Charm bracelets', 'Silver brcelets', 'Tennis bracelets']
                }
            ],
            'banners': [
                {
                    'url': 'shop',
                    'image': 'https://placehold.co/580x160',
                    'alt': 'Shop Banner 1'
                },
                {
                    'url': 'shop',
                    'image': 'https://placehold.co/580x160',
                    'alt': 'Shop Banner 2'
                }
            ]
        },
        {
            'name': 'Categories',
            'url': 'categories',
            'dropdown': True,
            'categories_grid': True,
            'grid_categories': [
                {'name': 'Rings', 'image': 'https://placehold.co/190x140'},
                {'name': 'Bracelet', 'image': 'https://placehold.co/190x140'},
                {'name': 'Earrings', 'image': 'https://placehold.co/190x140'},
                {'name': 'Necklace', 'image': 'https://placehold.co/190x140'},
                {'name': 'Pendants', 'image': 'https://placehold.co/190x140'},
                {'name': 'Watches', 'image': 'https://placehold.co/190x140'},
                {'name': 'Necklace', 'image': 'https://placehold.co/190x140'},
                {'name': 'Chain', 'image': 'https://placehold.co/190x140'}
            ],
            'featured_image': 'https://placehold.co/290x380'
        },
        {
            'name': 'Pages',
            'url': 'pages',
            'dropdown': True,  # Changed to True to enable dropdown
            'pages': [  # Added pages array for dropdown items
                {'name': 'About', 'url': 'about'},
                {'name': 'Faq', 'url': 'faq'},
                {'name': 'Wishlist', 'url': 'wishlist'},
                {'name': 'Account', 'url': 'account'},
                {'name': 'Cart', 'url': 'cart'},
                {'name': 'Checkout', 'url': 'checkout'}
            ]
        },
        {
            'name': 'Blog',
            'url': 'blog',
            'dropdown': False
        },
        {
            'name': 'Contact',
            'url': 'contact',
            'dropdown': False
        }
    ]

    # Account items
    account_items = [
        {'name': 'Wishlist', 'url': 'wishlist'},
        {'name': 'Order history', 'url': 'order_history'},
        {'name': 'Account details', 'url': 'account_details'},
        {'name': 'Customer support', 'url': 'customer_support'},
        {'name': 'Logout', 'url': 'logout'}
    ]

    # Cart items
    cart_items = [
        {
            'id': 1,
            'name': 'Delica Omtantur',
            'price': 100.00,
            'image': 'https://placehold.co/600x765'
        },
        {
            'id': 2,
            'name': 'Gianvito Rossi',
            'price': 99.99,
            'image': 'https://placehold.co/600x765'
        }
    ]

    # Slider slides
    slider_slides = [
        {
            'title': 'New arrival',
            'subtitle': 'classic jewellery',
            'background_image': 'https://placehold.co/2000x2000',
            'product_image': 'https://placehold.co/2000x2000',
            'button_text': 'Shop this collection'
        },
        {
            'title': 'New arrival',
            'subtitle': 'classic jewellery',
            'background_image': 'https://placehold.co/2000x2000',
            'product_image': 'https://placehold.co/2000x2000',
            'button_text': 'Shop this collection'
        },
        {
            'title': 'New arrival',
            'subtitle': 'classic jewellery',
            'background_image': 'https://placehold.co/2000x2000',
            'product_image': 'https://placehold.co/2000x2000',
            'button_text': 'Shop this collection'
        }
    ]

    # Features
    features = [
        {
            'icon': 'ti-truck',
            'title': 'Free shipping',
            'description': 'On order over $199'
        },
        {
            'icon': 'ti-headphone',
            'title': 'Online support',
            'description': 'Customer service'
        },
        {
            'icon': 'ti-reload',
            'title': '30 Days return',
            'description': 'If goods have problems'
        },
        {
            'icon': 'ti-credit-card',
            'title': 'Secure payment',
            'description': '100% secure payment'
        }
    ]

    # Shop categories
    shop_categories = [
        {
            'name': 'Earrings',
            'image': 'https://placehold.co/600x1003'
        },
        {
            'name': 'Rings',
            'image': 'https://placehold.co/600x477'
        },
        {
            'name': 'Necklace',
            'image': 'https://placehold.co/600x1003'
        },
        {
            'name': 'Bracelet',
            'image': 'https://placehold.co/600x477'
        }
    ]

    # Product tabs
    product_tabs = [
        {
            'id': 'tab_five1',
            'name': 'New arrivals',
            'products': [
                {
                    'id': 1,
                    'name': 'Diamond earrings',
                    'price': 189.00,
                    'old_price': 200.00,
                    'image': 'https://placehold.co/600x765',
                    'label': 'New'
                },
                {
                    'id': 2,
                    'name': 'Geometric gold ring',
                    'price': 159.00,
                    'old_price': 180.00,
                    'image': 'https://placehold.co/600x765'
                },
                {
                    'id': 3,
                    'name': 'Gemstone earrings',
                    'price': 189.00,
                    'old_price': 200.00,
                    'image': 'https://placehold.co/600x765',
                    'label': 'Hot'
                },
                {
                    'id': 4,
                    'name': 'Gold diamond ring',
                    'price': 289.00,
                    'old_price': None,
                    'image': 'https://placehold.co/600x765'
                }
            ]
        },
        {
            'id': 'tab_five2',
            'name': 'Best sellers',
            'products': [
                {
                    'id': 9,
                    'name': 'Geometric gold ring',
                    'price': 239.00,
                    'old_price': 250.00,
                    'image': 'https://placehold.co/600x765',
                    'label': 'Hot'
                },
                {
                    'id': 10,
                    'name': 'Suserrer earring',
                    'price': 189.00,
                    'old_price': 200.00,
                    'image': 'https://placehold.co/600x765',
                    'label': 'Hot'
                },
                {
                    'id': 11,
                    'name': 'The aphrodite band',
                    'price': 150.00,
                    'old_price': 200.00,
                    'image': 'https://placehold.co/600x765'
                },
                {
                    'id': 12,
                    'name': 'Diamond earrings',
                    'price': 89.00,
                    'old_price': 100.00,
                    'image': 'https://placehold.co/600x765'
                }
            ]
        },
        {
            'id': 'tab_five3',
            'name': 'Featured products',
            'products': [
                {
                    'id': 13,
                    'name': 'Gold diamond ring',
                    'price': 289.00,
                    'old_price': None,
                    'image': 'https://placehold.co/600x765'
                },
                {
                    'id': 14,
                    'name': 'Diamond earrings',
                    'price': 189.00,
                    'old_price': 200.00,
                    'image': 'https://placehold.co/600x765'
                },
                {
                    'id': 15,
                    'name': 'Geometric gold ring',
                    'price': 129.00,
                    'old_price': 150.00,
                    'image': 'https://placehold.co/600x765',
                    'label': 'New'
                },
                {
                    'id': 16,
                    'name': 'Diamond earrings',
                    'price': 168.00,
                    'old_price': 220.00,
                    'image': 'https://placehold.co/600x765',
                    'label': 'New'
                }
            ]
        }
    ]

    # Footer columns
    footer_columns = [
        {
            'title': 'Categories',
            'links': [
                {'name': 'Women collection', 'url': 'shop'},
                {'name': 'Men collection', 'url': 'shop'},
                {'name': 'Accessories', 'url': 'shop'},
                {'name': 'Diamond', 'url': 'shop'},
                {'name': 'Gold jewellery', 'url': 'shop'}
            ]
        },
        {
            'title': 'Account',
            'links': [
                {'name': 'My profile', 'url': 'profile'},
                {'name': 'My order history', 'url': 'order_history'},
                {'name': 'My wish list', 'url': 'wishlist'},
                {'name': 'Order tracking', 'url': 'order_tracking'},
                {'name': 'Shopping cart', 'url': 'cart'}
            ]
        },
        {
            'title': 'Information',
            'links': [
                {'name': 'About us', 'url': 'about'},
                {'name': 'Careers', 'url': 'careers'},
                {'name': 'Events', 'url': 'events'},
                {'name': 'Articles', 'url': 'articles'},
                {'name': 'Contact us', 'url': 'contact'}
            ]
        }
    ]

    # Social links
    social_links = [
        {'name': 'Facebook', 'icon': 'fa-brands fa-facebook-f', 'url': 'https://www.facebook.com/'},
        {'name': 'Instagram', 'icon': 'fa-brands fa-instagram', 'url': 'http://www.instagram.com'},
        {'name': 'Twitter', 'icon': 'fa-brands fa-twitter', 'url': 'http://www.twitter.com'},
        {'name': 'Dribbble', 'icon': 'fa-brands fa-dribbble', 'url': 'http://www.dribbble.com'}
    ]

    # Policy links
    policy_links = [
        {'name': 'Terms and conditions', 'url': 'terms'},
        {'name': 'Privacy policy', 'url': 'privacy'}
    ]

    data = {
        'nav_items': nav_items,
        'account_items': account_items,
        'cart_items': cart_items,
        'cart_total': sum(item['price'] for item in cart_items),
        'slider_slides': slider_slides,
        'features': features,
        'shop_categories': shop_categories,
        'product_tabs': product_tabs,
        'footer_columns': footer_columns,
        'social_links': social_links,
        'policy_links': policy_links,
        'current_year': datetime.now().year,
        'show_cookie_message': True,
        'show_subscription_popup': True,
        'subscription_popup_image': 'https://placehold.co/600x660',
        'site_title': 'Crafto - Jewelry Store',
        'site_description': 'Elegant jewelry store with a wide collection of rings, earrings, necklaces, and bracelets.'
    }

    return data

# Helper function to generate static URLs
def get_static_url(filename):
    return f"/static/{filename}"

# Routes
@app.route('/index')
def index_redirect():
    # Redirect /index to the home page
    return redirect(url_for('index'))

@app.route('/')
def index():
    try:
        data = get_sample_data()

        # Add payment methods with direct static paths to avoid url_for issues
        payment_methods = [
            {'name': 'Visa', 'image': '/static/images/visa.svg', 'url': '#'},
            {'name': 'Mastercard', 'image': '/static/images/mastercard.svg', 'url': '#'},
            {'name': 'American Express', 'image': '/static/images/american-express.svg', 'url': '#'},
            {'name': 'Discover', 'image': '/static/images/discover.svg', 'url': '#'},
            {'name': 'Diners Club', 'image': '/static/images/diners-club.svg', 'url': '#'}
        ]

        data['payment_methods'] = payment_methods

        # Add a static_url helper for templates
        data['static_url'] = get_static_url

        logger.info("Rendering index template")
        return render_template('demo-jewellery-store.html', **data)
    except Exception as e:
        logger.error(f"Error in index route: {str(e)}")
        return f"An error occurred: {str(e)}", 500

@app.route('/shop')
@app.route('/shop/<category>')
@app.route('/shop/<category>/<item>')
def shop(category=None, item=None):
    try:
        data = get_sample_data()

        # Add payment methods with direct static paths
        payment_methods = [
            {'name': 'Visa', 'image': '/static/images/visa.svg', 'url': '#'},
            {'name': 'Mastercard', 'image': '/static/images/mastercard.svg', 'url': '#'},
            {'name': 'American Express', 'image': '/static/images/american-express.svg', 'url': '#'},
            {'name': 'Discover', 'image': '/static/images/discover.svg', 'url': '#'},
            {'name': 'Diners Club', 'image': '/static/images/diners-club.svg', 'url': '#'}
        ]

        data['payment_methods'] = payment_methods
        data['static_url'] = get_static_url

        # Shop page specific data
        shop_data = {
            'page_title': 'Jewellery Store - Shop',
            'meta_description': 'Discover our exquisite collection of handcrafted jewelry.',
            'shipping_offer': 'FREE SHIPPING ON ALL ORDERS $50, DON\'T MISS DISCOUNT.',
            'offer_text': 'GET OFFERS',
            'offer_link': '/offers',
            'home_url': '/',
            'shop_url': '/shop',
            'categories_url': '/categories',
            'wishlist_url': '/wishlist',
            'cart_url': '/cart',
            'checkout_url': '/checkout',
            'cart_count': len(data['cart_items']),
            'subtotal': f"${sum(item['price'] for item in data['cart_items']):.2f}",
            'page_title_image_url': 'https://placehold.co/1920x470',
            'page_heading': 'Shop collection',
            'home_label': 'Home',
            'page_name': 'Shop',
            'total_products': 48,
            'showing_start': 1,
            'showing_end': 12,
            'instagram_images': [
                {'image': 'https://placehold.co/445x445', 'url': 'https://www.instagram.com'},
                {'image': 'https://placehold.co/445x445', 'url': 'https://www.instagram.com'},
                {'image': 'https://placehold.co/445x445', 'url': 'https://www.instagram.com'},
                {'image': 'https://placehold.co/445x445', 'url': 'https://www.instagram.com'},
                {'image': 'https://placehold.co/445x445', 'url': 'https://www.instagram.com'},
                {'image': 'https://placehold.co/445x445', 'url': 'https://www.instagram.com'}
            ],
            'instagram_profile_url': 'https://www.instagram.com'
        }

        # Merge the shop data with the general data
        data.update(shop_data)

        # Create a list of products for the shop page by combining products from all tabs
        products = []
        for tab in data['product_tabs']:
            for product in tab['products']:
                # Add URL and other required fields to each product
                product_with_urls = product.copy()
                product_with_urls['url'] = f"/product/{product['id']}"
                product_with_urls['add_to_cart_url'] = f"/add_to_cart/{product['id']}"
                product_with_urls['image_url'] = product['image']
                products.append(product_with_urls)

        # Add products to the data
        data['products'] = products

        # In a real app, you would filter products based on category and item
        if category:
            data['page_heading'] = f"{category.capitalize()} collection"
            # Filter products by category

        if item:
            data['page_heading'] = f"{item.capitalize()} collection"
            # Further filter products by item

        logger.info(f"Rendering shop template for category: {category}, item: {item}")
        return render_template('demo-jewellery-store-shop.html', **data)
    except Exception as e:
        logger.error(f"Error in shop route: {str(e)}")
        return f"An error occurred: {str(e)}", 500

@app.route('/categories')
@app.route('/categories/<category>')
def categories(category=None):
    try:
        data = get_sample_data()
        
        # Add payment methods with direct static paths
        payment_methods = [
            {'name': 'Visa', 'image': '/static/images/visa.svg', 'url': '#'},
            {'name': 'Mastercard', 'image': '/static/images/mastercard.svg', 'url': '#'},
            {'name': 'American Express', 'image': '/static/images/american-express.svg', 'url': '#'},
            {'name': 'Discover', 'image': '/static/images/discover.svg', 'url': '#'},
            {'name': 'Diners Club', 'image': '/static/images/diners-club.svg', 'url': '#'}
        ]
        
        data['payment_methods'] = payment_methods
        data['static_url'] = get_static_url
        
        # Categories page specific data
        categories_data = {
            'page_title': 'Jewellery Store - Categories',
            'meta_description': 'Browse our jewelry categories and find the perfect piece for any occasion.',
            'page_title_image_url': 'https://placehold.co/1920x470',
            'page_heading': 'Categories',
            'home_label': 'Home',
            'page_name': 'Categories',
            'shop_url': '/shop',
            'instagram_images': [
                {'image': 'https://placehold.co/445x445', 'url': 'https://www.instagram.com'},
                {'image': 'https://placehold.co/445x445', 'url': 'https://www.instagram.com'},
                {'image': 'https://placehold.co/445x445', 'url': 'https://www.instagram.com'},
                {'image': 'https://placehold.co/445x445', 'url': 'https://www.instagram.com'},
                {'image': 'https://placehold.co/445x445', 'url': 'https://www.instagram.com'},
                {'image': 'https://placehold.co/445x445', 'url': 'https://www.instagram.com'}
            ],
            'instagram_profile_url': 'https://www.instagram.com'
        }
        
        # Merge the categories data with the general data
        data.update(categories_data)
        
        # Define jewelry categories for the categories page
        jewelry_categories = [
            {'name': 'Bangles', 'image': 'https://placehold.co/600x477', 'letter': 'B'},
            {'name': 'Pendants', 'image': 'https://placehold.co/600x477', 'letter': 'P'},
            {'name': 'Chain', 'image': 'https://placehold.co/600x477', 'letter': 'C'},
            {'name': 'Earrings', 'image': 'https://placehold.co/600x1003', 'letter': 'E'},
            {'name': 'Rings', 'image': 'https://placehold.co/600x477', 'letter': 'R'},
            {'name': 'Necklace', 'image': 'https://placehold.co/600x1003', 'letter': 'N'},
            {'name': 'Bracelet', 'image': 'https://placehold.co/600x477', 'letter': 'B'}
        ]
        
        # Add categories to the data
        data['categories'] = jewelry_categories
        
        # If a specific category is requested, filter the data
        if category:
            data['page_heading'] = f"{category.capitalize()} Collection"
            # In a real app, you would filter products by the selected category
        
        logger.info(f"Rendering categories template for category: {category}")
        return render_template('demo-jewellery-store-categories.html', **data)
    except Exception as e:
        logger.error(f"Error in categories route: {str(e)}")
        return f"An error occurred: {str(e)}", 500

@app.route('/about')
def about():
    try:
        data = get_sample_data()

        # Add payment methods with direct static paths
        payment_methods = [
            {'name': 'Visa', 'image': '/static/images/visa.svg', 'url': '#'},
            {'name': 'Mastercard', 'image': '/static/images/mastercard.svg', 'url': '#'},
            {'name': 'American Express', 'image': '/static/images/american-express.svg', 'url': '#'},
            {'name': 'Discover', 'image': '/static/images/discover.svg', 'url': '#'},
            {'name': 'Diners Club', 'image': '/static/images/diners-club.svg', 'url': '#'}
        ]

        data['payment_methods'] = payment_methods
        data['static_url'] = get_static_url

        # About page specific data
        about_data = {
            'page_title': 'Jewellery Store - About Us',
            'meta_description': 'Learn about our jewelry store and our commitment to quality and craftsmanship.',
            'about_page_title': 'About us',
            'about_heading': 'The great thing about costume jewellery there\'s something.',
            'about_description': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry\'s standard dummy text ever since the when an unknown printer took standard.',
            'about_image_1': 'https://placehold.co/540x565',
            'about_image_2': 'https://placehold.co/885x570',
            'about_image_3': 'https://placehold.co/580x420',
            'about_video_url': 'https://www.youtube.com/watch?v=cfXHhfNy7tU',
            'store_since_year': '1998',
            'why_choose_us_title': 'Why choose us?',
            'why_choose_us_description': 'Lorem ipsum dolor amet consectetur adipiscing dictum placerat diam in vestibulum vivamus in eros.',
            'trust_badge': 'trust',
            'trust_text': 'Genuine <span class="text-decoration-line-bottom">10000+ customer</span> trusting our products.',
            'team_title': 'Our amazing team',
            'team_description': 'Lorem ipsum dolor amet consectetur adipiscing dictum placerat diam in vestibulum vivamus in eros.',
            'instagram_images': [
                {'image': 'https://placehold.co/445x445', 'url': 'https://www.instagram.com'},
                {'image': 'https://placehold.co/445x445', 'url': 'https://www.instagram.com'},
                {'image': 'https://placehold.co/445x445', 'url': 'https://www.instagram.com'},
                {'image': 'https://placehold.co/445x445', 'url': 'https://www.instagram.com'},
                {'image': 'https://placehold.co/445x445', 'url': 'https://www.instagram.com'},
                {'image': 'https://placehold.co/445x445', 'url': 'https://www.instagram.com'}
            ],
            'instagram_profile_url': 'https://www.instagram.com'
        }

        # Merge the about data with the general data
        data.update(about_data)

        logger.info("Rendering about template")
        return render_template('demo-jewellery-store-about.html', **data)
    except Exception as e:
        logger.error(f"Error in about route: {str(e)}")
        return f"An error occurred: {str(e)}", 500

@app.route('/faq')
def faq():
    try:
        data = get_sample_data()
        data['payment_methods'] = [
            {'name': 'Visa', 'image': '/static/images/visa.svg', 'url': '#'},
            {'name': 'Mastercard', 'image': '/static/images/mastercard.svg', 'url': '#'},
            {'name': 'American Express', 'image': '/static/images/american-express.svg', 'url': '#'},
            {'name': 'Discover', 'image': '/static/images/discover.svg', 'url': '#'},
            {'name': 'Diners Club', 'image': '/static/images/diners-club.svg', 'url': '#'}
        ]
        data['static_url'] = get_static_url
        
        # FAQ page specific data
        faq_data = {
            'page_title': 'Jewellery Store - FAQ',
            'meta_description': 'Frequently asked questions about our jewelry products and services.',
            'page_heading': 'Frequently Asked Questions',
            'home_label': 'Home',
            'page_name': 'FAQ'
        }
        
        data.update(faq_data)
        
        logger.info("Rendering FAQ template")
        return render_template('demo-jewellery-store-faq.html', **data)
    except Exception as e:
        logger.error(f"Error in faq route: {str(e)}")
        return f"An error occurred: {str(e)}", 500

@app.route('/wishlist')
def wishlist():
    try:
        data = get_sample_data()
        data['payment_methods'] = [
            {'name': 'Visa', 'image': '/static/images/visa.svg', 'url': '#'},
            {'name': 'Mastercard', 'image': '/static/images/mastercard.svg', 'url': '#'},
            {'name': 'American Express', 'image': '/static/images/american-express.svg', 'url': '#'},
            {'name': 'Discover', 'image': '/static/images/discover.svg', 'url': '#'},
            {'name': 'Diners Club', 'image': '/static/images/diners-club.svg', 'url': '#'}
        ]
        data['static_url'] = get_static_url
        
        # Wishlist page specific data
        wishlist_data = {
            'page_title': 'Jewellery Store - Wishlist',
            'meta_description': 'View and manage your wishlist of favorite jewelry items.',
            'page_title_image_url': 'https://placehold.co/1920x470',
            'page_heading': 'Wishlist',
            'home_label': 'Home',
            'page_name': 'Wishlist',
            'instagram_images': [
                {'image': 'https://placehold.co/445x445', 'url': 'https://www.instagram.com'},
                {'image': 'https://placehold.co/445x445', 'url': 'https://www.instagram.com'},
                {'image': 'https://placehold.co/445x445', 'url': 'https://www.instagram.com'},
                {'image': 'https://placehold.co/445x445', 'url': 'https://www.instagram.com'},
                {'image': 'https://placehold.co/445x445', 'url': 'https://www.instagram.com'},
                {'image': 'https://placehold.co/445x445', 'url': 'https://www.instagram.com'}
            ],
            'instagram_profile_url': 'https://www.instagram.com'
        }
        
        data.update(wishlist_data)
        
        # Create wishlist products - in a real app, these would come from the user's saved wishlist
        # For now, we'll use products from the product tabs
        wishlist_products = []
        for tab in data['product_tabs']:
            for product in tab['products']:
                product_with_urls = product.copy()
                product_with_urls['url'] = f"/product/{product['id']}"
                product_with_urls['add_to_cart_url'] = f"/add_to_cart/{product['id']}"
                product_with_urls['image_url'] = product['image']
                wishlist_products.append(product_with_urls)
                # Limit to 8 products for the wishlist page
                if len(wishlist_products) >= 8:
                    break
            if len(wishlist_products) >= 8:
                break
        
        data['wishlist_products'] = wishlist_products
        
        logger.info("Rendering wishlist template")
        return render_template('demo-jewellery-store-wishlist.html', **data)
    except Exception as e:
        logger.error(f"Error in wishlist route: {str(e)}")
        return f"An error occurred: {str(e)}", 500

@app.route('/account')
def account():
    try:
        data = get_sample_data()
        data['payment_methods'] = [
            {'name': 'Visa', 'image': '/static/images/visa.svg', 'url': '#'},
            {'name': 'Mastercard', 'image': '/static/images/mastercard.svg', 'url': '#'},
            {'name': 'American Express', 'image': '/static/images/american-express.svg', 'url': '#'},
            {'name': 'Discover', 'image': '/static/images/discover.svg', 'url': '#'},
            {'name': 'Diners Club', 'image': '/static/images/diners-club.svg', 'url': '#'}
        ]
        data['static_url'] = get_static_url
        
        # Account page specific data
        account_data = {
            'page_title': 'Jewellery Store - My Account',
            'meta_description': 'Manage your account details, orders, and preferences.',
            'page_heading': 'My Account',
            'home_label': 'Home',
            'page_name': 'Account'
        }
        
        data.update(account_data)
        
        logger.info("Rendering account template")
        return render_template('demo-jewellery-store-account.html', **data)
    except Exception as e:
        logger.error(f"Error in account route: {str(e)}")
        return f"An error occurred: {str(e)}", 500

@app.route('/cart')
def cart():
    try:
        data = get_sample_data()
        data['payment_methods'] = [
            {'name': 'Visa', 'image': '/static/images/visa.svg', 'url': '#'},
            {'name': 'Mastercard', 'image': '/static/images/mastercard.svg', 'url': '#'},
            {'name': 'American Express', 'image': '/static/images/american-express.svg', 'url': '#'},
            {'name': 'Discover', 'image': '/static/images/discover.svg', 'url': '#'},
            {'name': 'Diners Club', 'image': '/static/images/diners-club.svg', 'url': '#'}
        ]
        data['static_url'] = get_static_url
        
        # Cart page specific data
        cart_data = {
            'page_title': 'Jewellery Store - Shopping Cart',
            'meta_description': 'View and manage items in your shopping cart.',
            'page_heading': 'Shopping Cart',
            'home_label': 'Home',
            'page_name': 'Cart'
        }
        
        data.update(cart_data)
        
        logger.info("Rendering cart template")
        return render_template('demo-jewellery-store-cart.html', **data)
    except Exception as e:
        logger.error(f"Error in cart route: {str(e)}")
        return f"An error occurred: {str(e)}", 500

@app.route('/checkout')
def checkout():
    try:
        data = get_sample_data()
        data['payment_methods'] = [
            {'name': 'Visa', 'image': '/static/images/visa.svg', 'url': '#'},
            {'name': 'Mastercard', 'image': '/static/images/mastercard.svg', 'url': '#'},
            {'name': 'American Express', 'image': '/static/images/american-express.svg', 'url': '#'},
            {'name': 'Discover', 'image': '/static/images/discover.svg', 'url': '#'},
            {'name': 'Diners Club', 'image': '/static/images/diners-club.svg', 'url': '#'}
        ]
        data['static_url'] = get_static_url
        
        # Checkout page specific data
        checkout_data = {
            'page_title': 'Jewellery Store - Checkout',
            'meta_description': 'Complete your purchase securely.',
            'page_heading': 'Checkout',
            'home_label': 'Home',
            'page_name': 'Checkout'
        }
        
        data.update(checkout_data)
        
        logger.info("Rendering checkout template")
        return render_template('demo-jewellery-store-checkout.html', **data)
    except Exception as e:
        logger.error(f"Error in checkout route: {str(e)}")
        return f"An error occurred: {str(e)}", 500

@app.route('/product/<int:product_id>')
def product(product_id):
    try:
        data = get_sample_data()

        # Find the product in any of the tabs
        product = None
        for tab in data['product_tabs']:
            for p in tab['products']:
                if p['id'] == product_id:
                    product = p
                    break
            if product:
                break

        if not product:
            flash('Product not found', 'error')
            return redirect(url_for('index'))

        data['payment_methods'] = [
            {'name': 'Visa', 'image': '/static/images/visa.svg', 'url': '#'},
            {'name': 'Mastercard', 'image': '/static/images/mastercard.svg', 'url': '#'},
            {'name': 'American Express', 'image': '/static/images/american-express.svg', 'url': '#'},
            {'name': 'Discover', 'image': '/static/images/discover.svg', 'url': '#'},
            {'name': 'Diners Club', 'image': '/static/images/diners-club.svg', 'url': '#'}
        ]
        data['static_url'] = get_static_url
        data['product'] = product

        logger.info(f"Rendering product template for product ID: {product_id}")
        return render_template('demo-jewellery-store-product.html', **data)
    except Exception as e:
        logger.error(f"Error in product route: {str(e)}")
        return f"An error occurred: {str(e)}", 500

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    try:
        # In a real app, you would add the product to the cart in the session or database
        flash('Product added to cart', 'success')
        logger.info(f"Product {product_id} added to cart")
        return redirect(url_for('product', product_id=product_id))
    except Exception as e:
        logger.error(f"Error in add_to_cart route: {str(e)}")
        return f"An error occurred: {str(e)}", 500

@app.route('/add_to_wishlist/<int:product_id>')
def add_to_wishlist(product_id):
    try:
        # In a real app, you would add the product to the wishlist in the session or database
        flash('Product added to wishlist', 'success')
        logger.info(f"Product {product_id} added to wishlist")
        return redirect(url_for('product', product_id=product_id))
    except Exception as e:
        logger.error(f"Error in add_to_wishlist route: {str(e)}")
        return f"An error occurred: {str(e)}", 500

@app.route('/search')
def search():
    try:
        query = request.args.get('s', '')
        data = get_sample_data()
        data['payment_methods'] = [
            {'name': 'Visa', 'image': '/static/images/visa.svg', 'url': '#'},
            {'name': 'Mastercard', 'image': '/static/images/mastercard.svg', 'url': '#'},
            {'name': 'American Express', 'image': '/static/images/american-express.svg', 'url': '#'},
            {'name': 'Discover', 'image': '/static/images/discover.svg', 'url': '#'},
            {'name': 'Diners Club', 'image': '/static/images/diners-club.svg', 'url': '#'}
        ]
        data['static_url'] = get_static_url
        data['query'] = query
        
        logger.info(f"Searching for: {query}")
        # In a real app, you would search for products matching the query
        return render_template('demo-jewellery-store-shop.html', **data)
    except Exception as e:
        logger.error(f"Error in search route: {str(e)}")
        return f"An error occurred: {str(e)}", 500


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
                    {'author': 'Colene Landin', 'date': '18 July 2020, 12:39 PM', 'content': 'Lorem ipsum is simply dummy text of the printing and typesetting industry. Ipsum has been the industry\'s standard dummy text.', 'image': 'https://placehold.co/130x130', 'highlight': True}
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

@app.route('/pages')
def pages():
    # This route will redirect to the about page as a default for the Pages menu
    return redirect(url_for('about'))

if __name__ == '__main__':
    # Print the template folder path on startup
    logger.info(f"Template folder: {app.template_folder}")
    app.run(debug=True)
    
    