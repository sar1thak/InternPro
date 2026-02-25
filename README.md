🚀 InternPro — Productivity & Internship Tracker (SaaS Web App)

Live Demo: https://internpro-ngsj.onrender.com

InternPro is a full-stack productivity and internship tracking platform built using Django.
It enables users to manage daily tasks, track internship applications, and monitor productivity through a modern analytics dashboard with a clean SaaS-style interface.

This project demonstrates backend development, authentication systems, database design, and deployment of a production-ready Django application.

✨ Features
🔐 Authentication System

User signup & login

Secure session handling

User-specific dashboard

📋 Task Management

Add, edit, delete tasks

Priority selection (High/Medium/Low)

Deadline tracking

Mark tasks as completed

Urgent task highlighting

🎯 Internship Tracker

Track applied internships

Application status (Applied, Interview, Selected, Rejected)

Organized dashboard table view

📊 Analytics Dashboard

Task completion analytics

Priority distribution charts

Productivity insights

Real-time dashboard metrics

🎨 Modern SaaS UI

Dark themed responsive interface

Clean dashboard layout

Bootstrap based UI

Glassmorphism styled components

☁️ Deployment

Production deployment using Gunicorn

Hosted on Render cloud platform

Live accessible web application

🛠️ Tech Stack

Backend:

Python

Django

Django ORM

Frontend:

HTML5

CSS3

Bootstrap

Chart.js

Database:

SQLite (development & deployment)

Deployment & Tools:

Gunicorn

Render

Git & GitHub

🏗️ Project Structure
InternPro/
│
├── dashboard/          # Main app (tasks, internships, analytics)
├── InternPro/          # Project settings & configuration
├── templates/          # HTML templates
├── static/             # CSS & JS
├── manage.py
└── requirements.txt

⚙️ Installation (Run Locally)
1. Clone repository
git clone https://github.com/yourusername/InternPro.git
cd InternPro
2. Create virtual environment
python -m venv venv
venv\Scripts\activate   (Windows)
3. Install dependencies
pip install -r requirements.txt
4. Run migrations
python manage.py migrate
5. Start server
python manage.py runserver

Open:
http://127.0.0.1:8000

🌐 Deployment

This project is deployed on Render using:

Gunicorn web server

Django production settings

Static file handling

Cloud hosting environment

Live URL:
👉 https://internpro-ngsj.onrender.com

📈 Future Improvements

PostgreSQL production database

REST API integration

Email reminders for deadlines

AI productivity insights

Mobile responsive optimization

👨‍💻 Author

Sarthak Shukla
B.Tech CSE (AI) — KIET
Full-Stack & Backend Developer

LinkedIn: https://linkedin.com/in/sarthak-shukla

GitHub: https://github.com/sar1thak

⭐ If you found this useful
Give this repo a star and feel free to fork or contribute.
