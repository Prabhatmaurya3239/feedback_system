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
## ⚙️ Tech Stack Used

### 🧠 Backend
- **Python 3.11+**
- **Django**: High-level Python web framework
- **Django Admin**: Built-in admin dashboard for managing feedback
- **Gunicorn**: WSGI HTTP server for deployment

### 💬 Sentiment Analysis
- **TextBlob**: For Natural Language Processing and classifying feedback into Positive, Neutral, or Negative

### 🤖 AI Integration (Optional)
- **Gemini API (Google Generative AI)**: Summarizes feedback into concise AI-generated summaries

### 🌐 Frontend
- **HTML5**, **CSS3**
- **Bootstrap 5**: Responsive design and UI components
- **Chart.js**: Data visualization for sentiment graphs

### 🛠️ Tools & Deployment
- **Render**: Cloud platform to deploy Django apps easily
- **Gunicorn**: WSGI server for Render deployment
- **Procfile**: Render-specific entry point
- **Environment Variables**: Secure management of secret keys and configs
- **CSRF Trusted Origins**: Secured setup for production

---

## 🔐 Security & Configurations

| Feature | Tool/Library | Notes |
|--------|--------------|-------|
| CSRF Protection | Django Middleware | `CSRF_TRUSTED_ORIGINS` configured for Render |
| Environment Secrets | `os.environ` | Secure storage of `SECRET_KEY`, `DEBUG`, API keys |
| Admin Panel | Django Admin | Password-protected superuser access |

---

## 💻 Developer Tools

| Tool | Purpose |
|------|---------|
| `manage.py` | CLI for migrations, superuser creation, etc. |
| `requirements.txt` | Python dependency management |
| `Procfile` | Render-compatible start command |
| `venv` | Python virtual environment |
| `.env` (optional) | Local development environment secrets |


## 📁 Project Structure
---
```bash
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
--- '''
---

## ⚙️ Local Setup Instructions

### 🔁 1. Clone the Repository

```bash
git clone https://github.com/prabhatmaurya3239/feedback_system.git
cd feedback_system
'''

### 2. Create Virtual Environment and Install Dependencies
```bash
python -m venv venv
source venv/bin/activate           # On Windows: venv\Scripts\activate
pip install -r requirements.txt '''


###⚙️ 3. Run Migrations and Create Superuser
'''bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser '''


###  ▶️ 4. Run the Server
'''bash
python manage.py runserver


