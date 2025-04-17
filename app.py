from flask import Flask, render_template, url_for, request, redirect, flash
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure random key in production

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
            'url': 'javascript:void(0);',
            'dropdown': True,
            'subitems': [
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
    
    return render_template('demo-jewellery-store.html', **data)

@app.route('/about')
def about():
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
        'about_slides': [
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
        'team_members': [
            {
                'name': 'Jeremy dupont',
                'position': 'Director',
                'image': 'https://placehold.co/600x756',
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
                'image': 'https://placehold.co/600x756',
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
                'image': 'https://placehold.co/600x756',
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
                'image': 'https://placehold.co/600x756',
                'social_links': [
                    {'icon': 'fa-brands fa-facebook-f', 'url': 'https://www.facebook.com/'},
                    {'icon': 'fa-brands fa-dribbble', 'url': 'http://www.dribbble.com/'},
                    {'icon': 'fa-brands fa-twitter', 'url': 'https://www.twitter.com/'},
                    {'icon': 'fa-brands fa-instagram', 'url': 'http://www.instagram.com'}
                ]
            }
        ],
        'clients': [
            {'name': 'Pingdom', 'logo': '/static/images/logo-pingdom-dark-gray.svg', 'url': '#'},
            {'name': 'PayPal', 'logo': '/static/images/logo-paypal-dark-gray.svg', 'url': '#'},
            {'name': 'Walmart', 'logo': '/static/images/logo-walmart-dark-gray.svg', 'url': '#'},
            {'name': 'Amazon', 'logo': '/static/images/logo-amazon-dark-gray.svg', 'url': '#'},
            {'name': 'Logitech', 'logo': '/static/images/logo-logitech-dark-gray.svg', 'url': '#'},
            {'name': 'Pingdom', 'logo': '/static/images/logo-pingdom-dark-gray.svg', 'url': '#'},
            {'name': 'PayPal', 'logo': '/static/images/logo-paypal-dark-gray.svg', 'url': '#'},
            {'name': 'Walmart', 'logo': '/static/images/logo-walmart-dark-gray.svg', 'url': '#'}
        ],
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
    
    return render_template('demo-jewellery-store-about.html', **data)

@app.route('/shop')
@app.route('/shop/<category>')
@app.route('/shop/<category>/<item>')
def shop(category=None, item=None):
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
    
    # In a real app, you would filter products based on category and item
    return render_template('shop.html', category=category, item=item, **data)

@app.route('/categories')
@app.route('/categories/<category>')
def categories(category=None):
    data = get_sample_data()
    data['payment_methods'] = [
        {'name': 'Visa', 'image': '/static/images/visa.svg', 'url': '#'},
        {'name': 'Mastercard', 'image': '/static/images/mastercard.svg', 'url': '#'},
        {'name': 'American Express', 'image': '/static/images/american-express.svg', 'url': '#'},
        {'name': 'Discover', 'image': '/static/images/discover.svg', 'url': '#'},
        {'name': 'Diners Club', 'image': '/static/images/diners-club.svg', 'url': '#'}
    ]
    data['static_url'] = get_static_url
    return render_template('categories.html', category=category, **data)

@app.route('/product/<int:product_id>')
def product(product_id):
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
    
    return render_template('product.html', **data)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    # In a real app, you would add the product to the cart in the session or database
    flash('Product added to cart', 'success')
    return redirect(url_for('product', product_id=product_id))

@app.route('/add_to_wishlist/<int:product_id>')
def add_to_wishlist(product_id):
    # In a real app, you would add the product to the wishlist in the session or database
    flash('Product added to wishlist', 'success')
    return redirect(url_for('product', product_id=product_id))

@app.route('/quick_view/<int:product_id>')
def quick_view(product_id):
    # In a real app, you would return a modal with product details
    return redirect(url_for('product', product_id=product_id))

@app.route('/cart')
def cart():
    data = get_sample_data()
    data['payment_methods'] = [
        {'name': 'Visa', 'image': '/static/images/visa.svg', 'url': '#'},
        {'name': 'Mastercard', 'image': '/static/images/mastercard.svg', 'url': '#'},
        {'name': 'American Express', 'image': '/static/images/american-express.svg', 'url': '#'},
        {'name': 'Discover', 'image': '/static/images/discover.svg', 'url': '#'},
        {'name': 'Diners Club', 'image': '/static/images/diners-club.svg', 'url': '#'}
    ]
    data['static_url'] = get_static_url
    return render_template('cart.html', **data)

@app.route('/checkout')
def checkout():
    data = get_sample_data()
    data['payment_methods'] = [
        {'name': 'Visa', 'image': '/static/images/visa.svg', 'url': '#'},
        {'name': 'Mastercard', 'image': '/static/images/mastercard.svg', 'url': '#'},
        {'name': 'American Express', 'image': '/static/images/american-express.svg', 'url': '#'},
        {'name': 'Discover', 'image': '/static/images/discover.svg', 'url': '#'},
        {'name': 'Diners Club', 'image': '/static/images/diners-club.svg', 'url': '#'}
    ]
    data['static_url'] = get_static_url
    return render_template('checkout.html', **data)

@app.route('/wishlist')
def wishlist():
    data = get_sample_data()
    data['payment_methods'] = [
        {'name': 'Visa', 'image': '/static/images/visa.svg', 'url': '#'},
        {'name': 'Mastercard', 'image': '/static/images/mastercard.svg', 'url': '#'},
        {'name': 'American Express', 'image': '/static/images/american-express.svg', 'url': '#'},
        {'name': 'Discover', 'image': '/static/images/discover.svg', 'url': '#'},
        {'name': 'Diners Club', 'image': '/static/images/diners-club.svg', 'url': '#'}
    ]
    data['static_url'] = get_static_url
    return render_template('wishlist.html', **data)

@app.route('/search')
def search():
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
    # In a real app, you would search for products matching the query
    return render_template('search.html', **data)

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email', '')
    # In a real app, you would add the email to your newsletter database
    flash('Thank you for subscribing!', 'success')
    return redirect(url_for('index'))

@app.route('/offers')
def offers():
    data = get_sample_data()
    data['payment_methods'] = [
        {'name': 'Visa', 'image': '/static/images/visa.svg', 'url': '#'},
        {'name': 'Mastercard', 'image': '/static/images/mastercard.svg', 'url': '#'},
        {'name': 'American Express', 'image': '/static/images/american-express.svg', 'url': '#'},
        {'name': 'Discover', 'image': '/static/images/discover.svg', 'url': '#'},
        {'name': 'Diners Club', 'image': '/static/images/diners-club.svg', 'url': '#'}
    ]
    data['static_url'] = get_static_url
    return render_template('offers.html', **data)

@app.route('/blog')
def blog():
    data = get_sample_data()
    data['payment_methods'] = [
        {'name': 'Visa', 'image': '/static/images/visa.svg', 'url': '#'},
        {'name': 'Mastercard', 'image': '/static/images/mastercard.svg', 'url': '#'},
        {'name': 'American Express', 'image': '/static/images/american-express.svg', 'url': '#'},
        {'name': 'Discover', 'image': '/static/images/discover.svg', 'url': '#'},
        {'name': 'Diners Club', 'image': '/static/images/diners-club.svg', 'url': '#'}
    ]
    data['static_url'] = get_static_url
    return render_template('blog.html', **data)

@app.route('/contact')
def contact():
    data = get_sample_data()
    data['payment_methods'] = [
        {'name': 'Visa', 'image': '/static/images/visa.svg', 'url': '#'},
        {'name': 'Mastercard', 'image': '/static/images/mastercard.svg', 'url': '#'},
        {'name': 'American Express', 'image': '/static/images/american-express.svg', 'url': '#'},
        {'name': 'Discover', 'image': '/static/images/discover.svg', 'url': '#'},
        {'name': 'Diners Club', 'image': '/static/images/diners-club.svg', 'url': '#'}
    ]
    data['static_url'] = get_static_url
    return render_template('contact.html', **data)

@app.route('/faq')
def faq():
    data = get_sample_data()
    data['payment_methods'] = [
        {'name': 'Visa', 'image': '/static/images/visa.svg', 'url': '#'},
        {'name': 'Mastercard', 'image': '/static/images/mastercard.svg', 'url': '#'},
        {'name': 'American Express', 'image': '/static/images/american-express.svg', 'url': '#'},
        {'name': 'Discover', 'image': '/static/images/discover.svg', 'url': '#'},
        {'name': 'Diners Club', 'image': '/static/images/diners-club.svg', 'url': '#'}
    ]
    data['static_url'] = get_static_url
    return render_template('faq.html', **data)

@app.route('/account')
def account():
    data = get_sample_data()
    data['payment_methods'] = [
        {'name': 'Visa', 'image': '/static/images/visa.svg', 'url': '#'},
        {'name': 'Mastercard', 'image': '/static/images/mastercard.svg', 'url': '#'},
        {'name': 'American Express', 'image': '/static/images/american-express.svg', 'url': '#'},
        {'name': 'Discover', 'image': '/static/images/discover.svg', 'url': '#'},
        {'name': 'Diners Club', 'image': '/static/images/diners-club.svg', 'url': '#'}
    ]
    data['static_url'] = get_static_url
    return render_template('account.html', **data)

@app.route('/cookie_policy')
def cookie_policy():
    data = get_sample_data()
    data['payment_methods'] = [
        {'name': 'Visa', 'image': '/static/images/visa.svg', 'url': '#'},
        {'name': 'Mastercard', 'image': '/static/images/mastercard.svg', 'url': '#'},
        {'name': 'American Express', 'image': '/static/images/american-express.svg', 'url': '#'},
        {'name': 'Discover', 'image': '/static/images/discover.svg', 'url': '#'},
        {'name': 'Diners Club', 'image': '/static/images/diners-club.svg', 'url': '#'}
    ]
    data['static_url'] = get_static_url
    return render_template('cookie_policy.html', **data)

@app.route('/terms')
def terms():
    data = get_sample_data()
    data['payment_methods'] = [
        {'name': 'Visa', 'image': '/static/images/visa.svg', 'url': '#'},
        {'name': 'Mastercard', 'image': '/static/images/mastercard.svg', 'url': '#'},
        {'name': 'American Express', 'image': '/static/images/american-express.svg', 'url': '#'},
        {'name': 'Discover', 'image': '/static/images/discover.svg', 'url': '#'},
        {'name': 'Diners Club', 'image': '/static/images/diners-club.svg', 'url': '#'}
    ]
    data['static_url'] = get_static_url
    return render_template('terms.html', **data)

@app.route('/privacy')
def privacy():
    data = get_sample_data()
    data['payment_methods'] = [
        {'name': 'Visa', 'image': '/static/images/visa.svg', 'url': '#'},
        {'name': 'Mastercard', 'image': '/static/images/mastercard.svg', 'url': '#'},
        {'name': 'American Express', 'image': '/static/images/american-express.svg', 'url': '#'},
        {'name': 'Discover', 'image': '/static/images/discover.svg', 'url': '#'},
        {'name': 'Diners Club', 'image': '/static/images/diners-club.svg', 'url': '#'}
    ]
    data['static_url'] = get_static_url
    return render_template('privacy.html', **data)

@app.route('/order_history')
def order_history():
    data = get_sample_data()
    data['payment_methods'] = [
        {'name': 'Visa', 'image': '/static/images/visa.svg', 'url': '#'},
        {'name': 'Mastercard', 'image': '/static/images/mastercard.svg', 'url': '#'},
        {'name': 'American Express', 'image': '/static/images/american-express.svg', 'url': '#'},
        {'name': 'Discover', 'image': '/static/images/discover.svg', 'url': '#'},
        {'name': 'Diners Club', 'image': '/static/images/diners-club.svg', 'url': '#'}
    ]
    data['static_url'] = get_static_url
    return render_template('order_history.html', **data)

@app.route('/account_details')
def account_details():
    data = get_sample_data()
    data['payment_methods'] = [
        {'name': 'Visa', 'image': '/static/images/visa.svg', 'url': '#'},
        {'name': 'Mastercard', 'image': '/static/images/mastercard.svg', 'url': '#'},
        {'name': 'American Express', 'image': '/static/images/american-express.svg', 'url': '#'},
        {'name': 'Discover', 'image': '/static/images/discover.svg', 'url': '#'},
        {'name': 'Diners Club', 'image': '/static/images/diners-club.svg', 'url': '#'}
    ]
    data['static_url'] = get_static_url
    return render_template('account_details.html', **data)

@app.route('/customer_support')
def customer_support():
    data = get_sample_data()
    data['payment_methods'] = [
        {'name': 'Visa', 'image': '/static/images/visa.svg', 'url': '#'},
        {'name': 'Mastercard', 'image': '/static/images/mastercard.svg', 'url': '#'},
        {'name': 'American Express', 'image': '/static/images/american-express.svg', 'url': '#'},
        {'name': 'Discover', 'image': '/static/images/discover.svg', 'url': '#'},
        {'name': 'Diners Club', 'image': '/static/images/diners-club.svg', 'url': '#'}
    ]
    data['static_url'] = get_static_url
    return render_template('customer_support.html', **data)

@app.route('/logout')
def logout():
    # In a real app, you would log the user out
    flash('You have been logged out', 'success')
    return redirect(url_for('index'))

@app.route('/profile')
def profile():
    data = get_sample_data()
    data['payment_methods'] = [
        {'name': 'Visa', 'image': '/static/images/visa.svg', 'url': '#'},
        {'name': 'Mastercard', 'image': '/static/images/mastercard.svg', 'url': '#'},
        {'name': 'American Express', 'image': '/static/images/american-express.svg', 'url': '#'},
        {'name': 'Discover', 'image': '/static/images/discover.svg', 'url': '#'},
        {'name': 'Diners Club', 'image': '/static/images/diners-club.svg', 'url': '#'}
    ]
    data['static_url'] = get_static_url
    return render_template('profile.html', **data)

@app.route('/order_tracking')
def order_tracking():
    data = get_sample_data()
    data['payment_methods'] = [
        {'name': 'Visa', 'image': '/static/images/visa.svg', 'url': '#'},
        {'name': 'Mastercard', 'image': '/static/images/mastercard.svg', 'url': '#'},
        {'name': 'American Express', 'image': '/static/images/american-express.svg', 'url': '#'},
        {'name': 'Discover', 'image': '/static/images/discover.svg', 'url': '#'},
        {'name': 'Diners Club', 'image': '/static/images/diners-club.svg', 'url': '#'}
    ]
    data['static_url'] = get_static_url
    return render_template('order_tracking.html', **data)

@app.route('/careers')
def careers():
    data = get_sample_data()
    data['payment_methods'] = [
        {'name': 'Visa', 'image': '/static/images/visa.svg', 'url': '#'},
        {'name': 'Mastercard', 'image': '/static/images/mastercard.svg', 'url': '#'},
        {'name': 'American Express', 'image': '/static/images/american-express.svg', 'url': '#'},
        {'name': 'Discover', 'image': '/static/images/discover.svg', 'url': '#'},
        {'name': 'Diners Club', 'image': '/static/images/diners-club.svg', 'url': '#'}
    ]
    data['static_url'] = get_static_url
    return render_template('careers.html', **data)

@app.route('/events')
def events():
    data = get_sample_data()
    data['payment_methods'] = [
        {'name': 'Visa', 'image': '/static/images/visa.svg', 'url': '#'},
        {'name': 'Mastercard', 'image': '/static/images/mastercard.svg', 'url': '#'},
        {'name': 'American Express', 'image': '/static/images/american-express.svg', 'url': '#'},
        {'name': 'Discover', 'image': '/static/images/discover.svg', 'url': '#'},
        {'name': 'Diners Club', 'image': '/static/images/diners-club.svg', 'url': '#'}
    ]
    data['static_url'] = get_static_url
    return render_template('events.html', **data)

@app.route('/articles')
def articles():
    data = get_sample_data()
    data['payment_methods'] = [
        {'name': 'Visa', 'image': '/static/images/visa.svg', 'url': '#'},
        {'name': 'Mastercard', 'image': '/static/images/mastercard.svg', 'url': '#'},
        {'name': 'American Express', 'image': '/static/images/american-express.svg', 'url': '#'},
        {'name': 'Discover', 'image': '/static/images/discover.svg', 'url': '#'},
        {'name': 'Diners Club', 'image': '/static/images/diners-club.svg', 'url': '#'}
    ]
    data['static_url'] = get_static_url
    return render_template('articles.html', **data)

if __name__ == '__main__':
    app.run(debug=True)