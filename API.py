

import requests
import openai
import time


def asteroid_data():
  url = "https://api.nasa.gov/neo/rest/v1/feed"
  params = {
      "api_key": "DEMO_KEY"
  }
  response = requests.get(url, params=params)
  data = response.json()
  near_earth_objects = data.get("near_earth_objects")
  for date in near_earth_objects:
  
      for obj in near_earth_objects[date]:

          print("")
          print('The asteroid was first sighted and named ' + obj.get("name"))
          print('The asteroid will pass Earth on ' + obj.get("close_approach_data")[0].get("close_approach_date_full") + " UTC")
          time.sleep(.1)





def chatgpt():
  api_key = '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'
  
  # Start the OpenAI API client
  openai.api_key = api_key
  


  
  # Define a function to send a message to ChatGPT and get a response
  def chat_with_gpt(prompt):
      response = openai.Completion.create(
          engine="text-davinci-002",
          prompt=prompt,
          max_tokens=50  # Adjust the max_tokens for longer or shorter responses
      )
      return response.choices[0].text
  
  # Input from user
  conversation = [
    input("Write your prompt here: ")
  ]

  for message in conversation:
    response = chat_with_gpt(message)
    print(f"User: {message}")
    print(f"ChatGPT: {response}")
  

  setup()



  
def setup():
  print("")
  choice=input("Do you want to get Near Earth Asteroid Data [NEAD], do you want to ask ChatGpt something [CG], or to exit, type ctrl+c: ").lower()
  if choice=="nead" or choice=="near earth asteroid data":
    asteroid_data()
  elif choice=="cg" or choice=="chatgpt":
    chatgpt()
  elif choice=="exit":
    print("Bye")
  else:
    time.sleep(.5)
    print("")
    print("Please enter a valid choice")
    time.sleep(.5)
    setup()
setup()