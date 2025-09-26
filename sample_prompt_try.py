PROMPTS = {
    "generate_image": [
        "Create a beautiful artwork of",
        "Generate a stunning image showing", 
        "Make an artistic representation of",
        "Design a creative visual of"
    ],
    "edit_image": [
        "Modify this image to show",
        "Enhance the photo by adding"
    ],
    "virtual_try_on": [
        "Show the person wearing this product"
    ],
    "empty_mode": [],  # Empty list
    "none_mode": None  # This will test our safety mechanism
}




def sample_prompts(mode: str, count:int=None):
    resutl=PROMPTS.get(mode,[])
    print(resutl[:count])


if __name__ == "__main__":
    sample_prompts("laskd")