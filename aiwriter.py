import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

for model in genai.list_models():
   print(model.name)

def rewrite_text(text):
    model = genai.GenerativeModel("models/gemini-1.5-flash")


    prompt = f"""You are a skilled and creative book writer. Rewrite the following chapter to improve its narrative flow, sentence structure, and overall readability. Keep the original story and meaning intact, but rephrase it using modern, vivid, and engaging language. Your rewrite should sound natural and fluid, like it was written by a human author.

    Chapter:
    {text}
    """
    response = model.generate_content(prompt)
    return response.text
    
    