![Ranarose](https://github.com/user-attachments/assets/a9ba4e45-bd6e-416c-8529-302baefabdc3)

# RanaRose E-commerce Platform

RanaRose is an e-commerce platform built using Django, specializing in roses and related products. The platform allows users to browse products, manage their shopping cart, process orders, and manage their accounts. It provides a user-friendly online storefront with features such as product catalogs, user authentication, and a streamlined checkout process.

## Features

*   **Product Catalog**: Browse and view available products, including details like name, description, price, and images.
*   **User Authentication**: Secure user registration, login, and logout functionality.
*   **Shopping Cart**: Add, remove, and manage products in a shopping cart.
*   **Order Processing**: Streamlined checkout process for placing orders.
*   **Responsive Design**: Utilizes Bootstrap for a responsive and visually appealing user interface.
*   **Product Offers**: Display product discounts with start and end dates.

## Technologies Used

*   **Python**: Primary programming language.
*   **Django**: High-level Python web framework.
*   **SQLite**: Database engine (for development).
*   **HTML, CSS, JavaScript**: Front-end design and interactive elements.
*   **Ajax**: .
*   **Bootstrap**: CSS framework for responsive design.
*   **Font Awesome**: UI icon toolkit.
*   **Popper.js**: Library to position tooltip and popover elements in the application

## Directory Structure
*akfaqih3-rana-rose/
*├── Cart/             # Contains cart-related functionality (models, views, urls)
*├── Order/            # Contains order processing functionality
*├── Product/          # Manages product catalog (categories, products, offers)
*├── RanaRose/         # Main Django project settings and media files
*├── Registration/     # Handles user registration, login, and logout
*├── Site/             # Contains core site views (e.g., home page)
*├── db.sqlite3        # SQLite database (development)
*├── manage.py         # Django management script
*└── requirments.txt   # Application dependencies


## Setup
*  Install the project dependencies:
```
pip install -r requirements.txt
```

## Apply database migrations:
python manage.py migrate

