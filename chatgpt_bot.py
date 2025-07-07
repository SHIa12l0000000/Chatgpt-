import openai

openai.api_key = "your-api-key-here"

def chat_with_gpt():
    print("🤖 ChatGPT Assistant (type 'exit' to quit)")
    chat_history = []

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("🤖 Goodbye!")
            break

        chat_history.append({"role": "user", "content": user_input})

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=chat_history
            )
            bot_reply = response['choices'][0]['message']['content'].strip()
            print(f"ChatGPT: {bot_reply}")
            chat_history.append({"role": "assistant", "content": bot_reply})
        except Exception as e:
            print(f"❌ Error: {str(e)}")

chat_with_gpt()
