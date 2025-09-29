from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import os
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

text_input = """Create a professional e-commerce fashion photo. Take the blue floral dress from the first image and let the woman from the second image wear it. Generate a realistic, full-body shot of the woman wearing the dress, with the lighting and shadows adjusted to match the outdoor environment."""

# Generate an image from a text prompt

dress_image =Image.open("C:/Users/nazmu/Downloads/dress.png")
model_image=Image.open("C:/Users/nazmu/Downloads/model.png")

response = client.models.generate_content(
    model="gemini-2.5-flash-image-preview",
    contents=[dress_image, model_image, text_input],
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
