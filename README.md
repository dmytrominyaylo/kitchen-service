# 🍽️ Kitchen Service

## 📋 Project Description

This Django-based project is a simple kitchen management system that allows users to manage and interact with three core entities: **Cooks**, **Dishes**, and **Dish Types**. It provides full **CRUD** (Create, Read, Update, Delete) functionality for each entity and demonstrates the relationships between them in a structured, user-friendly interface.

---

## 👥 Target Users

This project is designed for both:
- 👨‍🍳 **Admins** – can create, update, and manage all entities.
- 👤 **Users** – can view and interact with available data.

---

## 🔧 Features

- 🔑 **User Registration**: Allows new users to sign up and access the system.
- 🍽️ **CRUD Functionality**: Full management of **Cooks**, **Dishes**, and **Dish Types**.

---

## ⚙️ Technology Stack

- 🐍 **Backend**: Django  
- 💅 **Frontend**: Bootstrap, custom **HTML templates** and **CSS styles**

---

## 📦 Dependencies

All project dependencies are listed in the `requirements.txt` file.

---

## 🚀 How to Run Locally

### 🖥️ 1. Create and link your GitHub repository
Create a GitHub repository and link it to your local project via PyCharm or Git CLI.

### 🌿 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows
```

### 📲 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 🔐 4. Set the SECRET_KEY

1. Create a `.env` file in your root directory.
2. Add the following line (with your own key):

```env
SECRET_KEY='your-secret-key-here'
```

### 🗂️ 5. Make and apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 👑 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 🚀 7. Run the development server

```bash
python manage.py runserver
```

---

## 📁 Database

Uses **SQLite** for local development.
