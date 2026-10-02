# FoodSpot

A Django-based food and recipe web application where users can browse recipes, explore different food categories, create an account, and interact with recipes through comments.

## Features

* User registration and authentication
* User profiles with profile photos
* Browse recipes
* Browse recipes by category
* View individual recipe details
* Add comments to recipes
* Manage recipe content
* Media and profile photo support
* Responsive web interface
* Django admin for managing application data

## Built With

* **Python**
* **Django**
* **SQLite**
* **HTML**
* **CSS**
* **JavaScript**
* **Django Templates**
* **Django Authentication**
* **Django ORM**

## Project Structure

```text
foodspot-web-app/
├── accounts/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── comments/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── recipes/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── foodspot/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── foodspot_app/
├── media/
├── profile_photos/
├── static/
├── templates/
├── manage.py
├── Procfile
├── requirements.txt
└── .gitignore
```

## Getting Started

### Prerequisites

Make sure you have the following installed:

* Python 3.10+
* pip
* Git

### Installation

1. Clone the repository:

```bash
git clone https://github.com/kalonjic34/foodspot-web-app.git
```

2. Navigate into the project:

```bash
cd foodspot-web-app
```

3. Create a virtual environment:

```bash
python -m venv .venv
```

4. Activate the virtual environment.

**Windows:**

```powershell
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

5. Install the project dependencies:

```bash
pip install -r requirements.txt
```

6. Apply the database migrations:

```bash
python manage.py migrate
```

7. Start the development server:

```bash
python manage.py runserver
```

8. Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## Application Structure

### Accounts

The `accounts` app handles user-related functionality, including authentication and profile information.

### Recipes

The `recipes` app contains the main food and recipe functionality. Recipes can be organised into different categories and displayed through the application's recipe pages.

### Comments

The `comments` app handles user comments associated with recipes, allowing users to interact with the recipe content.

## Django Implementation

FoodSpot uses Django's core features to handle the application's functionality, including:

* Django project and app structure
* URL routing
* Function-based views
* Django templates
* Models and migrations
* Django ORM
* Model relationships
* User authentication
* Form handling
* Static files
* Media files and image uploads
* Template inheritance
* Django admin
* CRUD functionality

## Running the Development Server

After activating the virtual environment and installing the dependencies:

```bash
python manage.py runserver
```

Then visit:

```text
http://127.0.0.1:8000/
```

To stop the server, press `CTRL + C`.

## Future Improvements

Some possible improvements for the application include:

* Recipe search functionality
* Recipe ratings
* Recipe favourites/bookmarks
* Pagination for recipe listings
* Improved user profile functionality
* More advanced filtering
* REST API integration
* Improved form validation and user feedback
* Deployment configuration for production

## Purpose

FoodSpot was built to develop my understanding of building database-driven web applications with Python and Django through a practical application.

The project brings together authentication, models, relationships, templates, forms, comments, and media handling into a single web application.
