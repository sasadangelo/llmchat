# ChatBot main - Manage the ChatBOT in text mode.
#
# This file defines the main for the ChatBOT text mode.
#
# Copyright (C) 2023 Salvatore D'Angelo
# Maintainer: Salvatore D'Angelo sasadangelo@gmail.com
#
# SPDX-License-Identifier: MIT
import argparse
from src.chatbot.chat_bot import ChatBOT

# This is the main entry point of the ChatBOT command-line interface.
# It handles command-line arguments, initializes the ChatBOT, and
# facilitates a conversation with the ChatBOT until the user chooses to exit.
def main():
    # Create an ArgumentParser object to handle command-line arguments.
    parser = argparse.ArgumentParser(description="ChatBOT command-line interface")
    
    # Add arguments for model name and temperature
    parser.add_argument("--model-name", type=str, choices=["llama", "chatgpt3.5", "chatgpt4"], default="llama", help="Model name (default: llama)")
    parser.add_argument("--temperature", type=float, default=0.0, help="Temperature (default: 0.0)")
    
    # Parse the command-line arguments.
    args = parser.parse_args()
    
    # Create a ChatBOT object
    chatbot = ChatBOT()
    
    # Check if model-name is different from "llama" and set the model
    if args.model_name != "llama" or args.temperature != 0.0:
        chatbot.set_model(args.model_name, args.temperature)
    
    # Print a welcome message for the ChatBOT command-line interface.
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
    # Call the main function when the script is executed.
    main()
