import openai
from utils import get_openai_api_key, load_data

# Set API key
openai.api_key = get_openai_api_key()

# Parameters
data_file = 'data/shakespeare.txt'
model_name = 'text-davinci-003'

# Load data
data = load_data(data_file)

# Fine-tuning (in this case, generating examples)
def fine_tune(data, model_name):
    for line in data:
        prompt = f"Translate the following text into Shakespearean English:\n\n{line}\n\nShakespearean English:"
        response = generate_shakespearean_text(prompt, model=model_name)
        print(f"Original: {line}")
        print(f"Shakespearean: {response}\n")

# Fine-tune the model
fine_tune(data, model_name)
