# Import necessary modules and create a Flask application
from flask import Flask, request, jsonify, render_template
import openai
import pandas as pd

app = Flask(__name__)

# Set your OpenAI API key
api_key = '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'
openai.api_key = api_key

# Load conversation data from a CSV file into a pandas DataFrame
df = pd.read_csv('dialogs.txt')

# Rename DataFrame columns to match the conversation format (role and content)
df.rename(columns={'User': 'role', 'Message': 'content'}, inplace=True)

# Convert the DataFrame to a list of conversation dictionaries
conversations = df.to_dict('records')

# Function to read the content of a text file
def read_text_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"

# Define the root route, which renders an HTML template
@app.route('/')
def index():
    return render_template('index.html')

# Define the '/chat' route, which handles user messages via POST requests
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']

    # Check if the user's message is "read file"
    if user_message.lower() == "read file":
        # Read the content of 'response.txt' and return it as a JSON response
        file_content = read_text_file('response.txt')
        return jsonify({'message': file_content})
    else:
        # Prepare a conversation by copying the existing conversation history and appending the user's message
        conversation = conversations.copy()
        conversation.append({'role': 'user', 'content': user_message})

        # Use OpenAI's Chat API to generate a response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation,
        )

        # Extract and return the chatbot's response as a JSON object
        chatbot_message = response['choices'][0]['message']['content']
        return jsonify({'message': chatbot_message})

# Run the Flask app if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
