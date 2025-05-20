from django.shortcuts import render, redirect
from .models import Event, Feedback
from textblob import TextBlob
from django.contrib import messages
from .utils import summarize_comments
from markdown2 import markdown
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# Feedback submission view
def submit_feedback(request):
    events = Event.objects.all()
    try:
       if request.method == 'POST':
            event_id = request.POST.get('event')
            event = Event.objects.get(id=event_id)
            student_name = request.POST.get('student_name')
            email = request.POST.get('email')
            comments = request.POST.get('comments')
            if not event_id or not student_name or not email or not comments:
                raise ValueError("❌ All fields are required.")
                return redirect('submit_feedback')

            
            blob = TextBlob(comments)
            polarity = blob.sentiment.polarity

  # This block of code is determining the sentiment of the feedback comments based on the polarity score calculated using TextBlob. Here's how it works:
            if polarity > 0.2:
               sentiment = 'Positive'
            elif polarity < 0:
               sentiment = 'Negative'
            else:
               sentiment = 'Neutral'

            Feedback.objects.create(
                event = event,
                student_name=student_name,
                email=email,
                comments=comments,
                sentiment=sentiment,
                polarity=polarity
            )
            messages.success(request, "✅  Feedback submitted successfully!")
            return redirect('feedback')
    except Exception as e:
        print(f"Error submitting feedback: {e}")
        messages.error(request, "❌ An error occurred while submitting feedback."+str(e))

    return render(request, 'submit_feedback.html', {'events': events})

# Admin dashboard view
def admin_dashboard(request):
    try:
        if request.method == 'POST':
          name = request.POST.get('event_name')
          enrolled = request.POST.get('enrolled')
          Event.objects.create(name=name, enrolled_students=enrolled)
          messages.success(request, "✅ Event created successfully!")
          print(f"Event created: {name} with {enrolled} enrolled students")
          return redirect('admin_dashboard')
    except Exception as e:
        messages.error(request, "❌ An error occurred while creating the event."+str(e))
        print(f"Error creating event: {e}")
    events = Event.objects.all()
    context = {'events': []}

    for event in events:
        feedbacks = event.feedback_set.all()
        total = feedbacks.count()
        pos = feedbacks.filter(sentiment='Positive').count()
        neg = feedbacks.filter(sentiment='Negative').count()
        neu = feedbacks.filter(sentiment='Neutral').count()
        context['events'].append({
            'id': event.id,
            'name': event.name,
            'enrolled': event.enrolled_students,
            'total_feedback': total,
            'positive': pos,
            'negative': neg,
            'neutral': neu,
        })

    return render(request, 'admin_dashboard.html', context)



@csrf_exempt
def ask_feedback_question(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            question = data.get('question', '')
            if not question:
                return JsonResponse({'error': 'Question is required.'}, status=400)

            event_id = data.get('id')
            prevdata = data.get('prevdata')
            feedbacks = Feedback.objects.filter(event_id=event_id)
            comments = [f.comments for f in feedbacks]
            all_comments_text = "\n".join(comments)

            
            if prevdata:
                prompt = (
                    f"You are an AI assistant. Based on the following student feedback:\n\n{all_comments_text}\n\n"
                    f"Answer this question: {question}"
                    f"\n\nPrevious Question Answer data: {prevdata}"
                )
            else:
                prompt = (
                    f"You are an AI assistant. Based on the following student feedback:\n\n{all_comments_text}\n\n"
                    f"Answer this question: {question}"
                )

            summary = summarize_comments(all_comments_text, prompt) if comments else "No feedback yet."
            answer = markdown(summary)
            return JsonResponse({'answer': answer})

        return JsonResponse({'error': 'Invalid request method'}, status=405)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
@csrf_exempt
def feedback_summary(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            event_id = data.get('id')
            feedbacks = Feedback.objects.filter(event_id=event_id)
            comments = [f.comments for f in feedbacks]
            all_comments_text = "\n".join(comments)        
            prompt = (
            "Summarize the following student feedback with the following format:\n\n"
            "1. Overall Sentiment (as a paragraph)\n"
            "2. Positive Feedback (as a bullet list)\n"
            "3. Negative Feedback (as a bullet list)\n"
            "4. Neutral/Mixed Feedback (as a bullet list)\n"
            "5. Key Takeaways (as a bullet list)\n\n"
            "Add emoji headers and bold section titles, and structure it clearly. Do NOT add code blocks or raw markdown syntax (like triple backticks)."
            "\n\nFeedback:\n"+ all_comments_text
            )
            summary = summarize_comments(comments, prompt) if comments else "No feedback yet."
            summary = markdown(summary)
            summary = summary.replace("✅", "<h6 class='mt-4 text-success'>✅ Positive Feedback:</h6>")
            summary = summary.replace("❌", "<h6 class='mt-4 text-danger'>❌ Negative Feedback:</h6>")
            summary = summary.replace("😐", "<h6 class='mt-4 text-warning'>😐 Neutral/Mixed Feedback:</h6>")
            summary = summary.replace("📌", "<h6 class='mt-4 text-info'>📌 Key Takeaways:</h6>")
            summary = summary.replace("📊", "<p class='fw-bold text-primary'>📊 Overall Sentiment:</p>")
            summary = markdown(summary)
            return JsonResponse({'summary': summary})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
@csrf_exempt
def get_all_comments(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            event_id = data.get('id')
            feedbacks = Feedback.objects.filter(event =event_id)
            feedback_data = []
            for fb in feedbacks:
                feedback_data.append({
                    'name': fb.student_name,
                    'email': fb.email,
                    'sentiment': fb.sentiment,
                    'comment': fb.comments
                })
            return JsonResponse({'comments': feedback_data})
        return JsonResponse({'error': 'Invalid request'}, status=400)  
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

