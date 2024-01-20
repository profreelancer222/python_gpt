from openai import OpenAI

client = OpenAI(api_key="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")


response = client.images.generate(
  model="dall-e-3",
  prompt="A cute baby sea otter",
  n=1,
  size="1024x1024"
)