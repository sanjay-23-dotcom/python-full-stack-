Django Full Stack Web Application
A full stack web application built with Django, featuring user authentication, order management, and a frontend with HTML/CSS. Covers the complete request-response cycle from database to UI.
---
Tech Stack
Python 3.x
Django — web framework (views, models, templates, forms)
HTML / CSS — frontend templates
SQLite — database
Django Auth — built-in user authentication system
---
Features
User registration, login, and logout
Session-based authentication
Order management — create and view orders
Frontend templates with Django templating engine
Static file handling (CSS)
Django Admin panel for data management
---
Project Structure
```
python-full-stack/
├── authentication/       # User registration, login, logout views
├── ordermanagement/      # Order creation and listing
├── firstapp/             # Core app — base views and models
├── frontend/             # Frontend-specific views and templates
├── Newproject/           # Project settings and main urls.py
├── static/
│   └── css/              # Stylesheet files
├── db.sqlite3
└── manage.py
```
---
Getting Started
1. Clone the repo
```bash
git clone https://github.com/sanjay-23-dotcom/python-full-stack-.git
cd python-full-stack-
```
2. Create a virtual environment and install dependencies
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install django
```
3. Apply migrations and run
```bash
python manage.py migrate
python manage.py createsuperuser   # optional
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.
---
Key Pages
URL	Description
`/`	Home page
`/register/`	User registration
`/login/`	User login
`/logout/`	Logout
`/orders/`	Order management
`/admin/`	Django admin panel
---
What I Learned
Django's MVT (Model-View-Template) architecture
User authentication using Django's built-in auth system
Database modelling and Django ORM
Template inheritance and static file management
Form handling and validation in Django
---
Author
Sanjay H  
BCA Data Science — SRM University, Chennai  
LinkedIn · GitHub