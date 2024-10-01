import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv('gemini_key')

genai.configure(api_key=api_key)

def get_car_ai_bio(model, brand, year):
    generate = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"Me mostre uma descrição de venda para o carro {brand} {model} {year} em apenas 250 caracteres. Fale coisas específicas desse modelo."
    response = generate.generate_content(prompt).text
    return response
