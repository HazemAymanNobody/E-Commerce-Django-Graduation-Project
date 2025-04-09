# E-Commerce Django Project

A full-featured e-commerce platform built with Django.

## Features

- User Authentication
- Product Management
- Shopping Cart
- Payment Integration (Stripe & PayPal)
- Order Management
- Vendor Dashboard
- Admin Dashboard
- Product Reviews
- Wishlist
- Search & Filter
- Responsive Design

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

## Installation

1. Clone the repository:
```bash
git clone https://github.com/HazemAymanNobody/E-Commerce-Django-Graduation-Project.git
cd E-Commerce-Django-Graduation-Project
```

2. Create and activate virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create .env file:
Create a new file named `.env` in the root directory with the following content:
```
# Payment Gateway Keys
STRIPE_SECRET_KEY=your_stripe_secret_key
STRIPE_PUBLISHABLE_KEY=your_stripe_publishable_key
PAYPAL_RECEIVER_EMAIL=your-paypal-email@example.com
PAYPAL_CLIENT_ID=your-paypal-client-id
PAYPAL_SECRET_KEY=your-paypal-secret-key

# Django Settings
DEBUG=True
SECRET_KEY=your-django-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1

# Email Settings (Optional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-specific-password
```

5. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create superuser:
```bash
python manage.py createsuperuser
```

7. Collect static files:
```bash
python manage.py collectstatic
```

8. Run the development server:
```bash
python manage.py runserver
```

9. Access the application:
- Main site: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

## Important Notes

1. Make sure to replace the placeholder values in the `.env` file with your actual credentials:
   - Generate a new Django secret key
   - Add your Stripe API keys
   - Add your PayPal API credentials
   - Configure email settings if needed

2. The media files are included in the repository. Make sure the `media` directory is properly set up.

3. For payment processing to work:
   - Set up a Stripe account and add your API keys
   - Set up a PayPal account and add your API credentials

4. For email functionality:
   - Configure your email settings in the `.env` file
   - If using Gmail, you'll need to create an App Password

## Troubleshooting

If you encounter the "no such table" error:
1. Make sure you've run all migrations
2. Check if your virtual environment is activated
3. Verify that all requirements are installed correctly
4. Try deleting the db.sqlite3 file and running migrations again

## Contributing

Feel free to submit issues and enhancement requests.

## License

This project is licensed under the MIT License.
