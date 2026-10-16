print("===== BASIC CHATBOT =====")

while True:
    message=input("You: ").lower()
    if message=="hello":
        print("Hi!")
    elif message=="how are you":
        print("I'm fine,thanks!")
    elif message=="bye":
        print("Goodbye!")
        break
    else:
        print("Sorry, I don't understand.")
    