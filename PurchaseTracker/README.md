# Django Project: PurchaseTracker

## Overview

This is a simple Django application that allows users to manually enter and track their receipt information. The primary focus is on basic CRUD (Create, Read, Update, Delete) operations and user authentication.

## Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.x
- Django (install it using `pip install django`)

## Getting Started

1. **Clone the repository:**

   git clone https://github.com/rania-kouadri-aichouch/purchase-Tracker.git

2. **Install dependencies:**
   install virtualenv

   - python -m pip install virtualenv
     create virtuel enviroment
   - python -m venv venv

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your settings:**

   Modify `settings.py` as needed, e.g., database configuration, secret key, etc.

4. **Apply database migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate

   ```

5. **Create a superuser (for admin access):**

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create an admin user.

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

   The application will be accessible at http://127.0.0.1:8000/.

7. **Access the admin panel:**

   Visit http://127.0.0.1:8000/admin/ and log in with the superuser credentials created earlier.

## Running Tests

To run the tests, use the following command:

```bash
python manage.py test
```
