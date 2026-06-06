# 📺 TV Time Demo Project

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Django](https://img.shields.io/badge/Django-6.0%2B-green)
![Status](https://img.shields.io/badge/Status-Demo-orange)

A proof-of-concept media tracking web application built with **Python**, **Django**, and the **TVMaze API**.

This project was created to demonstrate how a modern TV and movie tracking experience could be implemented on the web, inspired by the TV Time platform.

---

## ✨ Features

* 🔍 Search TV shows using the TVMaze API
* 📺 Browse detailed show information
* 🖼️ Display show posters and metadata
* 💾 Store data using Django's ORM
* 🎨 Clean and responsive web interface
* 🚀 Simple local deployment

---

## 🛠️ Tech Stack

| Technology | Purpose            |
| ---------- | ------------------ |
| Python     | Backend Language   |
| Django     | Web Framework      |
| TVMaze API | Show Data Provider |
| Pillow     | Image Processing   |
| Requests   | API Communication  |

---

## 📋 Requirements

* Python 3.10 or newer
* Django 6.0+
* Pillow
* Requests

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/tv-time-demo.git
cd tv-time-demo
```

### 2. Install Dependencies

```bash
pip install django Pillow requests
```

### 3. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Start the Development Server

```bash
python manage.py runserver
```

### 5. Open the Application

Visit:

```text
http://127.0.0.1:8000
```

---

## 🎯 Purpose

This repository is a demonstration project designed to showcase ideas and potential improvements for a TV tracking web experience.

It is **not intended as a production-ready application**, but rather as a proof-of-concept for experimentation and discussion.

---

## 📄 License

This project is provided for demonstration purposes.
