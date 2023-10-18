from flask import Flask, request, render_template
from app.chatbot import chat_with_bot

app = Flask(__name)

@app.route('/')
def chatbot_page():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat_with_bot_endpoint():
    user_input = request.form['user_input']
    bot_response = chat_with_bot(user_input)
    return render_template('chat.html', user_input=user_input, bot_response=bot_response)

if __name__ == '__main__':
    app.run()
    
@app.route('/chat', methods=['POST'])
