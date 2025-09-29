from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import os
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash-image-preview",
    contents="A photorealistic close-up shot of a golden retriever puppy, tilting its head curiously, set in a sunlit grassy park. The scene is illuminated by soft golden-hour sunlight with gentle shadows, creating a warm and serene atmosphere. Captured with a Canon EOS R5 and a 50mm f/1.2 lens, emphasizing the fine fur textures and sparkling eyes. The image should be in a 16:9 format.",
)
image_parts = [
    part.inline_data.data
    for part in response.candidates[0].content.parts
    if part.inline_data
]

if image_parts:
    image=Image.open(BytesIO(image_parts[0]))
    image.save("photorealistic_exampl.png")
    image.show()