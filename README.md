# E-Commerce Django Project

A full-featured e-commerce platform built with Django, featuring both customer-facing and admin interfaces.

## Features

- User Authentication and Authorization
- Product Management
- Shopping Cart
- Order Processing
- Admin Dashboard
- User Profile Management
- Product Reviews and Ratings
- Tag Management
- Category Management

## Tech Stack

- Python 3.x
- Django 4.2.7
- SQLite (Database)
- HTML/CSS
- JavaScript
- Bootstrap

## Installation

1. Clone the repository
```bash
git clone <your-repository-url>
cd graduation-project-main
```

2. Create a virtual environment
```bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py migrate
```

5. Create a superuser
```bash
python manage.py createsuperuser
```

6. Run the development server
```bash
python manage.py runserver
```

## Project Structure

- `core/` - Main application with product and order management
- `useradmin/` - Admin dashboard and user management
- `userauths/` - Authentication and user models
- `templates/` - HTML templates
- `static/` - Static files (CSS, JS, images)
- `media/` - User-uploaded files

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
