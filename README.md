# HRMS – Human Resource Management System

## 🚀 Overview  
A comprehensive HRMS built with **Django**, **Python**, **HTML/CSS/Bootstrap**, and **SQLite/MySQL**.  
Automates key HR functions such as employee management, attendance, leave tracking, payroll, and performance reviews.

## 📋 Table of Contents  
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [Challenges & Solutions](#challenges--solutions)  
- [Future Scope](#future-scope)  
- [Contributing](#contributing)  
- [License](#license)  
- [Contact](#contact)

## ✨ Features  
- Role-based authentication for **Admin** and **Employees**  
- Employee profile & department management  
- Attendance and leave processing  
- Automated payroll calculation  
- Performance evaluation and reporting dashboard  
- Employee Self‑Service Portal: payslips, leave requests, profile updates

## 🛠️ Tech Stack  
- **Backend:** Django (Python)  
- **Frontend:** HTML, CSS, Bootstrap, JavaScript  
- **Database:** SQLite (development) / MySQL (production)  
- **Tools:** Git, VS Code, Django ORM  

## ⚙️ Installation  

```bash
git clone <repo-url>
cd hrms
python3 -m venv venv
source venv/bin/activate      # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

✅ Access the app at: `http://127.0.0.1:8000`

## 🧭 Usage  
- **Admin Dashboard:** Manage employees, leaves, attendance, payroll & generate reports  
- **Employee Portal:** Update profile, apply for leave, view payslips & attendance logs

## 📂 Project Structure  
```
hrms/
├── hrms_app/           # Core Django application
├── templates/
├── static/
├── manage.py
├── requirements.txt
└── README.md
```

## 🧩 Challenges & Solutions  
- **Resistance to change** – Communicated benefits clearly and involved staff early  
- **Data migration risks** – Cleaned and verified data before import  
- **Integration issues** – Used APIs and rigorous testing for system compatibility  
- **User training gaps** – Conducted sessions and provided user documentation  
- **Security concerns** – Implemented encryption, audits, and compliance measures  
- **Customization limitations** – Used flexible modules tailored to organization needs  
- **Budget constraints** – Prioritized features and managed costs effectively  
- **Scalability planning** – Adopted modular architecture for future growth

## 🚀 Future Scope  
- **AI‑based analytics**: Predict turnover and recommend training using AI  
- **Mobile app support**: Access HRMS via smartphones and tablets  
- **Blockchain integration**: Ensures secure, transparent employee records  
- **Wellness & training modules**: Add health & learning programs to HRMS  
- **Hybrid workforce support**: Manage and engage remote/hybrid employees

