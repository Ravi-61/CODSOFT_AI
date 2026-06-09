from datetime import datetime

def chatbot():
    print("🤖 ChatBot: Hello! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user in ["hello", "hi"]:
            print("🤖 ChatBot: Hello! How can I help you?")

        elif "how are you" in user:
            print("🤖 ChatBot: I'm doing great. Thanks for asking!")

        elif "name" in user:
            print("🤖 ChatBot: My name is CodSoft AI ChatBot.")

        elif "help" in user:
            print("🤖 ChatBot: I can answer questions about time, date, and tell jokes.")

        elif "time" in user:
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"🤖 ChatBot: Current time is {current_time}")

        elif "date" in user:
            current_date = datetime.now().strftime("%d-%m-%Y")
            print(f"🤖 ChatBot: Today's date is {current_date}")

        elif "joke" in user:
            print("🤖 ChatBot: Why do programmers hate nature? It has too many bugs!")

        elif user == "bye":
            print("🤖 ChatBot: Goodbye!")
            break

        else:
            print("🤖 ChatBot: Sorry, I don't understand that.")

chatbot()