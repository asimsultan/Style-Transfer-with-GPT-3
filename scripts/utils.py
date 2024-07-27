import openai
import os

def get_openai_api_key():
    return os.getenv('OPENAI_API_KEY')

def load_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return data

def generate_shakespearean_text(prompt, model="text-davinci-003"):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
    )
    return response.choices[0].text.strip()
