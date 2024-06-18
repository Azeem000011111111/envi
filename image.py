from pathlib import Path
from google.generativeai import GenerationConfig

import google.generativeai as genai
import streamlit as st

st.title("Image Caption Generator")
st.write("This is a simple image caption generator using Gemini")
image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
st.image(image, caption='Uploaded Image.', use_column_width=True)

genai.configure(api_key="AIzaSyBQscb6hscAKKw7qfGKFTUsmQ2ic0xNpIs")

# Set up the model
generation_config = {
    "temperature": 0.4,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 4096,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

generation_config = GenerationConfig(**generation_config)

model = genai.GenerativeModel(model_name="gemini-pro-vision",
                                                                                                                        generation_config=generation_config,
                                                                                                                        safety_settings=safety_settings)

# Validate that an image is present
if not (img := Path(f"{image}")).exists():
        raise FileNotFoundError(f"Could not find image: {image}")

image_parts = [
    {
        "mime_type": "image/jpeg",
        "data": Path(f"{image}").read_bytes()
    }
]

prompt_parts = [
    "What is in the image explain it with details\n",
    image_parts[0],
    
]

response = model.generate_content(prompt_parts)
st.write(response.text)

