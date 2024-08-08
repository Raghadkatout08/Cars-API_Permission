# Cars API Permission

**Author:** Ragahd Alkatout
**Date:** August 8, 2024

## Overview

The Cars API is a Django-based application designed to manage car listings. It offers functionalities for creating, reading, updating, and deleting car records. This API allows users to interact with car data through both a RESTful interface and a web interface.

## Features

- **CRUD Operations**: Create, Read, Update, and Delete car records.
- **User Authentication**: Manage users and associate car records with individual users.
- **API Endpoints**: Access and manipulate car data via RESTful API endpoints.
- **Web Interface**: View and manage car records through a web interface.


## Installation

### Prerequisites

- Python 3.8 or higher
- Django 5.0.7 or higher
- Django REST framework
- PostgreSQL (or another supported database)

### Setup

1. **Clone the Repository**

   ```bash
   git clone git@github.com:Raghadkatout08/Cars-API_Permission.git


2. **Create and activate a virtual environment**
    ```bash
    python -m venv .venv
    source .venv/bin/activate   # On Windows use `.venv\Scripts\activate`

3. **Install the dependencies**
    ```bash
    pip install -r requirements.txt

4. **Apply migrations**
    ```bash
    python manage.py migrate
    
5. **Create a superuser**
    ```bash
    python manage.py createsuperuser

6. **Run the server**
    ```bash
    python manage.py runserver

### Running Tests
To run the tests, execute:
    ```python manage.py test```

### Running Tests
If you prefer to run the application using Docker, follow these steps:
1. **Build the Docker image**
   ```bash
   docker build -t cars-api .

2. **Run the Docker container**
   ```bash
   docker run -it -p 8000:8000 cars-api

3. **Use Docker Compose**
   ```bash
   docker compose up
