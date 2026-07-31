print("Welcome To Chatbot")

while True:
    user = input("You: ")

    if user == "Hi":
        print("chatbot : hello")

    elif user == "Goodmorning":
        print("chatbot : Goodmorning")

    elif user == "How are you":
        print("chatbot : I am fine")

    elif user == "Bye":
        print("chatbot : Bye Bye")
        break

    else:
        print("I don't understand")