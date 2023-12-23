import google.generativeai as genai
import streamlit as st




st.title("Qoutes Generator")
st.write("This is a simple qoutes generator using Gemini")
api_key = st.text_input("Enter gemini pro api_key")
qoutes = st.text_input("Enter the qoutes")


# Configure the API key

genai.configure(api_key=f"{api_key}")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
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

generation_config = GenerationConfig(
    temperature=0.9,
    top_p=1,
    top_k=1,
    max_output_tokens=2048,
)

model = genai.GenerativeModel(model_name="gemini-pro",
                                                            generation_config=generation_config,
                                                            safety_settings=safety_settings)

prompt_parts = [
    f"Write random qoutes about {qoutes}",
]

response = model.generate_content(prompt_parts)
print(response.text)
st.write(response.text)

