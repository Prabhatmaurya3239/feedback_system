from django.urls import path
from . import views
urlpatterns = [
    path('', views.submit_feedback, name='feedback'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('ask-feedback-question/', views.ask_feedback_question, name='ask_feedback_question'),
    path('feedback-summary/', views.feedback_summary, name='feedback_summary'),
    path('get-all-comments/', views.get_all_comments, name='get_all_comments'),

]