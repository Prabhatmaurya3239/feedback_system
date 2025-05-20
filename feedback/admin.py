from django.contrib import admin
from .models import Event, Feedback

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'enrolled_students', 'created_at')
    search_fields = ('name',)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'event', 'sentiment', 'created_at')
    search_fields = ('student_name', 'event__name', 'comments')
    list_filter = ('sentiment', 'event')