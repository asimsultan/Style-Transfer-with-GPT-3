from utils import load_data, generate_shakespearean_text

# Parameters
data_file = 'data/shakespeare.txt'
model_name = 'text-davinci-003'

# Load data
data = load_data(data_file)

# Evaluation function
def evaluate(data, model_name):
    for line in data[:5]:  # Evaluate on first 5 examples
        prompt = f"Translate the following text into Shakespearean English:\n\n{line}\n\nShakespearean English:"
        response = generate_shakespearean_text(prompt, model=model_name)
        print(f"Original: {line}")
        print(f"Shakespearean: {response}\n")

# Evaluate the model
evaluate(data, model_name)