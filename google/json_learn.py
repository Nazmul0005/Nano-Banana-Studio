from dataclasses import dataclass
from typing import List

@dataclass
class Part:
    text: str

@dataclass
class Content:
    parts: List[Part]
    role: str

@dataclass
class Candidate:
    content: Content

# First example with dictionary
response = {
    "candidates": [
        {
            "content": {
                "parts": [
                    {
                        "text": "Okay, how can I help you today? ..."
                    }
                ],
                "role": "model"
            },
            "finish_reason": "STOP",
            "index": 0
        }
    ]
}

#print(response["candidates"][0]["content"]["parts"][0]["text"])

# Second example with classes
candidates = [
    Candidate(
        content=Content(
            parts=[
                Part(
                    text=(
                        "Okay, how can I help you today? "
                        "Do you have an image in mind you'd like me to create, "
                        "or something else I can assist you with?"
                    )
                ),
            ],
            role='model'
        ),
    )
]
print(candidates[0].content.parts[0].text)