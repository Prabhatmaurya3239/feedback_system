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

feedback_system/
├── feedback/ # Core app (models, views, forms, etc.)
│ ├── templates/ # HTML templates
│ ├── static/ # CSS, JS, images (Bootstrap file)
│ ├── models.py # Feedback model
│ ├── views.py # Main logic (feedback, AI, summary)
│ ├── urls.py # Feedback URLs
│ └── utils.py # Sentiment analysis & Gemini summarizer
├── feedback_system/ # Django settings
│ ├── settings.py
│ ├── urls.py
├── manage.py
├── requirements.txt
├── render.yaml # (Render deploy config)
└── README.md