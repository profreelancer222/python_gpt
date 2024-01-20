import openai
openai.api_key = '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'
messages = [ {"role": "system", "content": 
			"You are a intelligent assistant."} ]
while True:
	message = input("User : ")
	if message:
		messages.append(
			{"role": "user", "content": message},
		)
		chat = openai.chat.completions.create(
			model="gpt-4", messages=messages
		)
	reply = chat.choices[0].message.content
	print(f"ChatGPT: {reply}")
	messages.append({"role": "assistant", "content": reply})