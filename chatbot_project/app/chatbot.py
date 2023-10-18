from transformers import GPT2LMHeadModel, GPT2Tokenizer
import random

# Initialize the GPT-3 model and tokenizer
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Load and preprocess the dataset
with open('data/dialogs.txt', 'r') as file:
    dialogs = file.readlines()

# Define a function for chatbot responses
def chat_with_bot(user_input):
    # Preprocess user input
    input_ids = tokenizer.encode(user_input, return_tensors="pt")

    # Generate a response from the chatbot
    bot_response = model.generate(input_ids, max_length=50, num_return_sequences=1, no_repeat_ngram_size=2)

    # Decode the chatbot's response
    chatbot_response = tokenizer.decode(bot_response[0], skip_special_tokens=True)

    if chatbot_response:
        return chatbot_response
    else:
        # If chatbot response is empty, provide a random response from the dataset
        return random.choice(dialogs)
