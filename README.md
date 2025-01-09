# Zibondiwe (A recipe management API)
This project implements a Recipe_box API using Django and Django REST Framework. It allows users to manage recipes by creating, updating, deleting, and viewing them by category or ingredient. The API also provides authentication, search functionality, and the ability to filter recipes by various attributes such as preparation time and servings.

# recipe_box

This project implements a Recipe Box API using Django and Django REST Framework. It allows users to manage recipes by creating, updating, deleting, and viewing them by category or ingredient. The API also provides authentication, search functionality, and the ability to filter recipes by various attributes such as preparation time and servings.

# Features
Recipe Manager (CRUD):
1. Create, read, update, and delete recipes.
2. Each recipe includes attributes like title, description, ingredients, instructions, category, preparation time, cooking time, servings, and created date.

# User Management:
1. Users can register and authenticate with a username and password.
2. Users can only create, update, or delete their own recipes.

# Search and Filtering:
1. Search recipes by title, category, ingredients, or preparation time.
2. Filter recipes by cooking time, preparation time, or servings.

# Recipe Viewing:
1. View recipes by category (e.g., Dessert, Breakfast).
2. View recipes by ingredient (e.g., all recipes containing “chicken”).

# Static Files and Templates:
1. Templates render the recipe list. (Option)
2. Static files (CSS, JavaScript) are served for frontend styling and interaction.(Option)

# Pagination and Sorting:
1. Pagination is implemented for recipe listings.
2. Recipes can be sorted by preparation time, cooking time, or servings.

# Installation
Prerequisites (requirements.txt)

1. Python (preferably version 3.10)
2. pip (Python package manager)
3. Django (web framework)
4. Django REST Framework (for API creation)
5. Django auth-token and simple-jwt
6. Virtual environment (.venv)

# Setup
1. Clone the repository from my github account:
git clone https://github.com/ITgeekbeginner/recipe-manager.git
2. cd recipe-manager
3. Create a virtual environment (highly recommended otherwise the django commands won't run):python3 -m venv venv
4. Activate the virtual environment: python manage.py venv\Scripts\activate. Please note if your are using a different os system check relevant documentation.

# Install required dependencies:
1. pip install -r requirements.txt
2. Apply the database migrations: python manage.py migrate
3.Create a superuser for admin access and token generation: python manage.py createsuperuser
4. Run the development server:python manage.py runserver, the project will be accessible at http://127.0.0.1:8000/recipes. 

# For this project API below are some of the Endpoints
1. admin/ ## redirects users to the admin web page where users can login via the superuser credentials 
2. api/ auth/token/ ## obtains token inorder to authenticate users
3. api/ auth/token/refresh/ ## refreshes token
4. api/ recipes/ ## this endpoint creates a new recipe and lists it after successful creation
5. api/ recipes/<int:pk>/ ## this endpoint retrieves a recipe as per id request, updates the recipe, and deletes.
6. api/ recipes/category/ ## lists recipes as per their categories
7. api/ recipes/ingredient/ ## lists recipes as per their ingredients
8. api/ favorites/ ## lists users favorites
9. api/ favorites/add/ ## allows users to add their favorite recpices
10. api/ favorites/remove/ ## allows users to delete their favorite recipes from the favorite's list of recipes
11. ^media/(?P<path>.*)$ ## handles recipe images

# Authentication
This project uses Django's built-in authentication system. Users must authenticate to create, update, or delete their own recipes.

# Register:
Use the /api/auth/token endpoint to authenticate a new user account.

# Postman and tests
Postman tests available in the directory named Postman_tests.

# Prepare for Production:
1. Set DEBUG = False in settings.py.
2. Configure the allowed hosts (ALLOWED_HOSTS) in settings.py.
3. Set up a production database (PostgreSQL).

# Deploy to PythonAnywhere:
1. Login or signup to PythonAnywhere.
2. Prepare project (requirement.txt, venv and framework).
3. upload application to PythonAnywhere.
4. Configure web application in the console.
5. Add static files and templates, and reset application.
6. test application.

# Steps to Contribute:
1.Fork the repository.
2.Create a new branch.
3. Make your changes.
4. Submit a pull request.

# License
This project is open source.
