from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import os
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

text_input = """Using the provided image of a living room, change only the blue sofa to be a vintage, brown leather chesterfield sofa. Keep the rest of the room, including the pillows on the sofa and the lighting, unchanged."""

image =Image.open("C:/Users/nazmu/Downloads/living_room.png")

response = client.models.generate_content(
    model="gemini-2.5-flash-image-preview",
    contents=[text_input, image],
)
print(response)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"image_{timestamp}.png"
# filename =f"{prompt[:20].replace(' ','_')}_{timestamp}.png"

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = Image.open(BytesIO(part.inline_data.data))
        image.save(f"{filename}")
