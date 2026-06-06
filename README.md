# TV Time Demo Project

This is a proof-of-concept web application demonstrating a media tracker using Python, Django, and the TVMaze API.

## Requirements
- Python 3.10+
- Django 6.0+
- Pillow (for image processing)
- Requests (for API calls)

## Setup Instructions
1. Install requirements:
   ```bash
   pip install django Pillow requests
   ```
2. Run database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
3. Start the development server:
   ```bash
   python manage.py runserver
   ```
4. Open your browser and go to `http://127.0.0.1:8000`
