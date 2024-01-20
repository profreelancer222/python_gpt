import openai

openai.api_key = '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'

response = openai.chat.completions.create(
  model="gpt-4",  # Replace with appropriate GPT model name
  messages=[
        {"role": "user", "content": "You are a helpful assistant. Extract the keywords from the following text."}
    ]
)

print(response.choices[0].message.content)