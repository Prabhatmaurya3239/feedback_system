from django.db import models
from django.utils import timezone

class Event(models.Model):
    name = models.CharField(max_length=255)
    enrolled_students = models.PositiveIntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    student_name = models.CharField(max_length=255 )
    email = models.EmailField(max_length=255)
    comments = models.TextField()
    sentiment = models.CharField(max_length=20)
    polarity = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now)

  
    def __str__(self):
        return f"Feedback for {self.event.name}" if self.event else "Feedback (No Event)"
