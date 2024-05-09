import openai
import random

# Setting up the API key
openai.api_key = 'sk-proj-KjEobFLDhovl6hRDoUDuT3BlbkFJ4keSYAvpKKPvIPwKkDx4'

def get_openai_chat_response(message):
    try:
        # Call to OpenAI's chat completions API
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[{"role": "system", "content": "You are chatting with a helpful assistant."},
                      {"role": "user", "content": message}],
            max_tokens=150
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return "I am sorry, I couldn't process your request."

# Define greetings inputs and responses
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey")
GREETING_RESPONSES = ["hi", "hey", "nods", "hi there", "hello", "I am glad you are talking to me"]

def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def main():
    flag = True
    print("ROBO: My name is Robo. I will answer your queries about Chatbots. If you want to exit, type Bye!")
    
    while flag:
        user_response = input().lower()
        if user_response != 'bye':
            if user_response == 'thanks' or user_response == 'thank you':
                flag = False
                print("ROBO: You're welcome!")
            else:
                if greeting(user_response) is not None:
                    print("ROBO: " + greeting(user_response))
                else:
                    print("ROBO: ", end="")
                    print(get_openai_chat_response(user_response))
        else:
            flag = False
            print("ROBO: Bye! take care..")

# Run the main function
if _name_ == "_main_":
    main()