# Personal Blog Web Application – Flask

A full-featured **Personal Blog Web Application** built with **Flask**. This project demonstrates core web development concepts including authentication, database integration, CRUD operations, templating, and responsive design.

## Project Overview

This application allows users to:

* Register and log in securely
* Create, edit, and delete blog posts
* Comment on blog posts
* View posts from other users
* Experience a responsive, styled UI using Bootstrap

It follows a **modular Flask application structure** using Blueprints and the Application Factory pattern.

## Features

### User Authentication

* User registration and login
* Password hashing for security
* Logout functionality
* Protected routes for logged-in users

### Blog Post System (CRUD)

* Create new blog posts
* View all posts on the homepage
* View single post details
* Edit your own posts
* Delete your own posts
* Post timestamps and author display

### Comment System

* Users can comment on posts
* Comments linked to users and posts
* Display comments under each post

### Frontend & UI

* Responsive design using **Bootstrap 5**
* Base layout with navigation bar
* Clean blog-style layout
* Mobile-friendly interface

### Database

* SQLite database
* SQLAlchemy ORM
* Flask-Migrate for database migrations

---

## Project Structure

```
week8-flask-blog/
│── app/
│   ├── __init__.py        # Application factory
│   ├── models.py          # Database models
│   ├── auth/              # Authentication blueprint
│   ├── main/              # Main routes (home, profile)
│   ├── posts/             # Blog post routes
│   ├── comments/          # Comment system routes
│   └── static/            # CSS, JS, images
│
│── templates/             # Jinja2 HTML templates
│── migrations/            # Database migration files
│── tests/                 # Unit tests
│── config.py              # Configuration settings
│── requirements.txt       # Python dependencies
│── run.py                 # Application entry point
└── .gitignore

## Installation & Setup

### Clone the Repository

```bash
git clone https://github.com/yourusername/week8-flask-blog.git
cd week8-flask-blog
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Environment Variables

**Windows (PowerShell)**

```bash
set FLASK_APP=run.py
set FLASK_ENV=development
```

**Mac/Linux**

```bash
export FLASK_APP=run.py
export FLASK_ENV=development
```

### Initialize Database

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### Run the Application

```bash
flask run
```

Open in browser:

```
http://127.0.0.1:5000
```

## Technologies Used

| Technology    | Purpose                 |
| ------------- | ----------------------- |
| Flask         | Web framework           |
| Jinja2        | HTML templating         |
| SQLAlchemy    | Database ORM            |
| Flask-Login   | User session management |
| Flask-Migrate | Database migrations     |
| Bootstrap 5   | Responsive UI styling   |
| SQLite        | Database                |

## Database Models

### User

* id
* username
* email
* password_hash
* about_me
* member_since
* last_seen

### Post

* id
* title
* content
* timestamp
* updated_at
* user_id (Foreign Key)

### Comment

* id
* content
* timestamp
* user_id (Foreign Key)
* post_id (Foreign Key)

## Security Features

* Password hashing using Werkzeug security
* Login required for creating/editing content
* CSRF protection via Flask-WTF forms
* Session-based authentication

## Testing

Run tests using:

```bash
pytest
```

Tests include:
* Model creation tests
* Authentication tests
* Post CRUD tests
* Comment system tests
