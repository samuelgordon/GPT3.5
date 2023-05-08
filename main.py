import os
import openai

openai.api_key = os.getenv("OpenAI API Key")

while True:
  question = input("\033[34mWhat can I answer incorrectly for you?\n\033[0m")

  if question.lower() == "exit":
    print("\033[31mGoodbye!\n\033[0m")
    break
    
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are an assistant. Answer the given question with a clearly incorrect answer."},
      {"role": "user", "content": question}
  ]
  )

  print("\033[32m"+ completion.choices[0].message.content + "\n")