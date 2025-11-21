def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! 👋"
    elif "how are you" in user_input:
        return "I'm fine, thanks for asking! 😊"
    elif "bye" in user_input:
        return "Goodbye! 👋 Have a great day!"
    elif "your name" in user_input:
        return "I'm a simple chatbot created in Python!"
    else:
        return "Sorry, I didn't understand that. 🤔"


print("🤖 Chatbot: Hello! Type something (type 'bye' to exit)\n")

while True:
    user_message = input("You: ")

    reply = chatbot_response(user_message)
    print("Bot:", reply)

    if "bye" in user_message.lower():
        break
