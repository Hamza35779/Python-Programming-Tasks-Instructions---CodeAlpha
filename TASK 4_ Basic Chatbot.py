def simple_chatbot():
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")  # Take user input
        if user_input.lower() == "hello":
            print("Chatbot: Hi!")
        elif user_input.lower() == "how are you":
            print("Chatbot: I'm fine, thanks!")
        elif user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break  # Exit the loop when the user says "bye"
        else:
            print("Chatbot: I'm sorry, I don't understand that.")

# To run the chatbot, simply call the function
if __name__ == "__main__":
    simple_chatbot()