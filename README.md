# Authenticate System — Django Auth Demo

A small **Django** web app with user registration, login, a private
"my account" page and logout. Built on Django's own authentication system,
so passwords are never stored as plain text: they are salted and hashed
with PBKDF2.

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0-092E20?logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?logo=bootstrap&logoColor=white)

## Features

- **Registration** with username, name, unique email and birth date
- **Login / logout** using Django's `LoginView` and `LogoutView`
- **Secure passwords**: hashing, strength validation and confirmation check
- **Protected page**: the account page is only available after login
- **Custom user model** extending `AbstractUser` (adds `birth_date`, unique `email`)
- **Admin panel** for managing users
- **Tests** covering registration, login, logout and access control
- Clean, responsive UI with Bootstrap 5 (interface in Russian)

## Getting started

```bash
# 1. Clone the repository
git clone https://github.com/marcsovnurislom/Authenticate-Sistem.git
cd Authenticate-Sistem

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
copy .env.example .env       # Windows
# cp .env.example .env       # macOS / Linux
# then put a real SECRET_KEY into .env

# 5. Create the database
python manage.py migrate
python manage.py createsuperuser   # optional, for /admin/

# 6. Run the development server
python manage.py runserver
```

Open http://127.0.0.1:8000/ to log in, or http://127.0.0.1:8000/register/ to create an account.

## Running tests

```bash
python manage.py test
```

## Pages

| URL           | Page                                  |
|---------------|---------------------------------------|
| `/`           | Login                                 |
| `/register/`  | Registration                          |
| `/user_home/` | Account page (login required)         |
| `/logout/`    | Logout (POST)                         |
| `/admin/`     | Django admin                          |

## Project structure

```
Authenticate-Sistem/
├── auth_sistem/        # Project settings and root URL config
├── users/              # Custom user model, forms, views, tests
├── templates/          # Base layout, login, register and account pages
├── static/css/         # Styles
├── manage.py
├── requirements.txt
└── .env.example        # Template for environment variables
```
