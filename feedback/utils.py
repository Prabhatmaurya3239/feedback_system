import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def summarize_comments(comments_list,prompt):
    
    try:
        model = genai.GenerativeModel( model_name='gemini-2.0-flash')
        response = model.generate_content(prompt)
        print ("new")
        return response.text
    except Exception as e:
        return f"Error in summarizing comments: {e}"
