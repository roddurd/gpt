"""
This module runs a chat loop, taking in user input and passing it to the OpenAI API, using the davinci-03 model to generate and print a response.
"""
import os
import openai
from dotenv import load_dotenv


def setup():
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    return


def chat(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        temperature=0,
        max_tokens=200,
    )
    return response


# Chat loop: ask user for input, pass input to the OpenAI API, and print the response.
def chat_loop():
    setup()
    print("Welcome to the ChatGPT CLI! Type 'q', 'quit' or 'exit' to exit.")
    print("---")
    prompt = "AI: Hello, how can I help you?\nYou: "
    messages = [
        {
            "role": "system",
            "content": "You are a highly intelligent and enthusiastic assistant. Your goal is to give accurate but concise answers to questions.",
        },
        {"role": "assistant", "content": "Hello, how can I help you?"},
    ]
    while True:
        user_input = input(prompt)
        if user_input.lower().strip() in ["quit", "exit", "q"]:
            print("---")
            print("Goodbye!")
            break
        messages.append({"role": "user", "content": user_input})
        response = chat(messages)
        response_text = response.choices[0].message.content
        messages.append({"role": "assistant", "content": response_text})
        prompt = f"AI: {response_text}\n---\nYou: "


if __name__ == "__main__":
    chat_loop()
