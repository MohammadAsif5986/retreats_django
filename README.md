# Wellness Service

This project is a Django-based backend service for managing retreat data. It includes API endpoints for fetching, booking, and managing retreats.

## Prerequisites

- Python 3.x
- PostgreSQL
- Git
- SSH key set up for GitHub (for pushing changes)

## Getting Started follow the following steps to run project

### Clone the Repository

1. **Clone the repository using SSH**:

   ```bash
   git clone git@github.com:MohammadAsif5986/retreats_django.git

2. cd retreats_django
3. python -m venv venv
venv\Scripts\activate
4. pip install -r requirements.txt
5. Configure PostgreSQL
     Open wellness_service/settings.py.
    Configure the DATABASES setting to match your PostgreSQL setup. For example:
         DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'retreats',
            'USER': 'your_postgres_user',
            'PASSWORD': 'your_postgres_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
      }

6.python manage.py migrate
7. python manage.py createsuperuser
8. python manage.py runserver
9. http://127.0.0.1:8000/
10. API Endpoints
Fetch all retreats: GET /retreats
Create a new booking: POST /book


