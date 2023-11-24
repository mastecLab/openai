from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What’s in this image?"},
                {
                    "type": "image_url",
                    "image_url": "https://cdn.sanity.io/images/7p2whiua/production/e4aa6a729372745047db1e06ca48fa300e292409-2048x1536.jpg",
                },
            ],
        }
    ],
    max_tokens=300,
)

print(response.choices[0])
