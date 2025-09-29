# for photorealistic

response = {
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Sure! Here is a cute comic-style image of a corgi dog wearing sunglasses and a hat: "
          },
          {
            "inline_data": {
              "data": "iVBORw0KGgoAAAANSUhEUgAABAAAAAQAAgMAAAB8f7zUAAAgAElEQVR4nO... (base64 continues)",
              "mime_type": "image/png"
            }
          }
        ],
        "role": "model"
      },
      "finish_reason": "STOP",
      "index": 0
    }
  ]
}

image_parts = [
    part["inline_data"]["data"]
    for part in response["candidates"][0]["content"]["parts"]
      if part.get("inline_data")
]

print(image_parts)

#equivalent to image parts

image_parts = []

for part in response["candidates"][0]["content"]["parts"]:
    if part.get("inline_data"):
        image_parts.append(part["inline_data"]["data"])
print(image_parts)