#Load Libraries
import os
import openai
from dotenv import load_dotenv
from openai import OpenAI

#Variables
load_dotenv()
API_KEY = os.getenv('CHATGPT_API_KEY')
model = "gpt-5"

#Initialize Client proxy
if API_KEY:
    client = OpenAI(api_key = API_KEY)

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}] # Updated API call for openai>=1.0.0
    response = client.chat.completions.create(
    model=model,
    messages=messages,
      temperature=0, # This is the degree of randomness
      )
    return response.choices[0].message.content

def prompting():
    poem = f"""
      How quietly does the orange branch, observe the sky begin to blanch.
      Without a sigh, without a prayer, with no betrayal of despair'.
      """

    task = f"""
          A poem has been provided de-limited by triple quotes. Your task is add\
          one more stanza to the poem {poem} in a similar meter
          """

    response = get_completion(task)
    from IPython.display import display, HTML
    display(HTML(response))

if __name__ == "__main__":
      prompting()

