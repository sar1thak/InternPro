🚀 InternPro — Productivity & Internship Tracker (SaaS Web App)

Live Demo: https://internpro-ngsj.onrender.com

InternPro is a full-stack productivity and internship tracking platform built using Django.
It enables users to manage daily tasks, track internship applications, and monitor productivity through a modern analytics dashboard with a clean SaaS-style interface.

This project demonstrates backend development, authentication systems, database design, and deployment of a production-ready Django application.

✨ Features

🔐 Authentication System

1)User signup & login

2)Secure session handling

3)User-specific dashboard

📋 Task Management

1)Add, edit, delete tasks

2)Priority selection (High/Medium/Low)

3)Deadline tracking

4)Mark tasks as completed

5)Urgent task highlighting

🎯 Internship Tracker

1)Track applied internships

2)Application status (Applied, Interview, Selected, Rejected)

3)Organized dashboard table view

📊 Analytics Dashboard

1)Task completion analytics

2)Priority distribution charts

3)Productivity insights

4)Real-time dashboard metrics

🎨 Modern SaaS UI

1)Dark themed responsive interface

2)Clean dashboard layout

3)Bootstrap based UI

4)Glassmorphism styled components

☁️ Deployment

1)Production deployment using Gunicorn

2)Hosted on Render cloud platform

3)Live accessible web application

🛠️ Tech Stack

Backend:

-> Python

-> Django

-> Django ORM

Frontend:

-> HTML5

-> CSS3

-> Bootstrap

-> Chart.js

Database:

-> SQLite (development & deployment)

Deployment & Tools:

-> Gunicorn

-> Render

-> Git & GitHub

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
git clone https://github.com/sar1thak/InternPro.git
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

1)Gunicorn web server

2)Django production settings

3)Static file handling

4)Cloud hosting environment

Live URL:
👉 https://internpro-ngsj.onrender.com

📈 Future Improvements

-> PostgreSQL production database

-> REST API integration

-> Email reminders for deadlines

-> AI productivity insights

-> Mobile responsive optimization

👨‍💻 Author

Sarthak Shukla
B.Tech CSE (AI) — KIET
Full-Stack & Backend Developer

LinkedIn: https://linkedin.com/in/sarthak-shukla

GitHub: https://github.com/sar1thak

⭐ If you found this useful
Give this repo a star and feel free to fork or contribute.
