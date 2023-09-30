import argparse
from src.chatbot.chat_bot import ChatBOT

def main():
    parser = argparse.ArgumentParser(description="ChatBOT command-line interface")
    
    # Add arguments for model name and temperature
    parser.add_argument("--model-name", type=str, choices=["llama", "chatgpt3.5", "chatgpt4"], default="llama", help="Model name (default: llama)")
    parser.add_argument("--temperature", type=float, default=0.0, help="Temperature (default: 0.0)")
    
    args = parser.parse_args()
    
    # Create a ChatBOT object
    chatbot = ChatBOT()
    
    # Check if model-name is different from "llama" and set the model
    if args.model_name != "llama" or args.temperature != 0.0:
        chatbot.set_model(args.model_name, args.temperature)
    
    print("Welcome to the ChatBOT command-line interface!")
    print("Start the conversation (Type 'quit' to exit)")

    while True:
        user_input = input("you> ")
        if user_input.lower() == "quit":
            break

        # Generate the chatbot's response
        response, _ = chatbot.get_answer(user_input)

        # Print the chatbot's response
        print("mychatbot>", response)

if __name__ == "__main__":
    main()
