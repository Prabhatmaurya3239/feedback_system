# 🎓 Sentiment-Driven Feedback System for College Events

A Django-based web application that allows students to submit feedback for college events and club activities, performs sentiment analysis (using TextBlob or VADER), and provides admins with visual summaries, insights, and AI-based Q&A.

---

## 🚀 Features

- 📝 Students can submit feedback with sentiment analysis
- 📊 Admin dashboard to view feedback and sentiment charts
- 🤖 AI-powered feedback summary & Q&A (Gemini API)
- 📄 Export raw feedback data to CSV
- 📈 Sentiment-based pie charts
- 📬 Admin email alerts (optional)
- 🧠 Gemini summarizer with emoji-rich formatting
- 🎨 Bootstrap responsive design

---

## 📁 Project Structure
---
feedback_system/
├── feedback_system/         # Main project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── feedback/                # Feedback app
│   ├── migrations/
│   ├── templates/
│   │   └── feedback/
│   │       ├── base.html
│   │       └── admin_dashboard.html  #some file
│   ├── static/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── utils.py
├── manage.py
├── requirements.txt
└── README.md
---
---

## ⚙️ Local Setup Instructions

### 🔁 1. Clone the Repository

```bash
git clone https://github.com/prabhatmaurya3239/feedback_system.git
cd feedback_system
### 2. Create Virtual Environment and Install Dependencies
python -m venv venv
source venv/bin/activate           # On Windows: venv\Scripts\activate
pip install -r requirements.txt

###⚙️ 3. Run Migrations and Create Superuser
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

###  ▶️ 4. Run the Server

