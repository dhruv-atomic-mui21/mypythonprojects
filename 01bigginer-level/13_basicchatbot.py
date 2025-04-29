def chatbot():
    print("Hello! I am a basic chatbot. Type 'exit' to quit.")
    responses = {
        "hi": "Hello!",
        "hello": "Hi there!",
        "how are you": "I'm a bot, so always good!",
        "what is your name": "I am a basic chatbot.",
        "bye": "Goodbye! Have a nice day!"
    }

    while True:
        user_input = input("You: ").lower().strip()
        if user_input == "exit":
            print("Chatbot: Goodbye!")
            break
        response = responses.get(user_input, "Sorry, I don't understand that.")
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
