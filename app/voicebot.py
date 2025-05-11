import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel('gemini-pro')

def generate_response(user_input):
    prompt = f"You are a helpful appointment assistant.\nUser: {user_input}\nAssistant:"
    response = model.generate_content(prompt)
    return response.text.strip()
