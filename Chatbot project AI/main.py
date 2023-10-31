from flask import Flask, render_template, request
app = Flask(__name__)
from datas import chat_datas

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "You're welcome.",
    "How old are you?",
    "I don't have an age.",
    "What can you do?",
    "I can answer questions, provide information, and have conversations with you.",
    "What's the weather like today?",
    "I'm sorry, I don't have access to real-time weather information.",
    "What's the meaning of life?",
    "That's a difficult question. There are many different answers depending on who you ask.",
    "Do you like pizza?",
    "I don't have a physical body, so I can't eat pizza. But I know many people enjoy it!",
    "Can you tell me a joke?",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "What's the capital of France?",
    "The capital of France is Paris.",
    "What's the largest animal on Earth?",
    "The largest animal on Earth is the blue whale.",
    "What's the most populous country in the world?",
    "The most populous country in the world is China.",
    "What's the tallest mountain in the world?",
    "The tallest mountain in the world is Mount Everest.",
]
conversation.extend(chat_datas)
def Give_Replay(qus):
    dic_set = {}
    for i in range(0,len(conversation),2):
        try:
            dic_set[conversation[i]] = conversation[i+1]
            print(conversation[i+1])
        except:
            print("Last Data..")
    message = dic_set.get(qus)
    if message:
        return message
    else:
        return "Try with different Question :)"
    
    

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get("msg")
    return str(Give_Replay(userText))


app.run(debug=True)
