import streamlit as st
from transformers import pipeline

# Initialize the translation pipeline
@st.cache_resource
def load_pipeline():
    translator = pipeline("translation", model="Helsinki-NLP/opus-mt-mul-en")
    return translator

translator = load_pipeline()

# Streamlit App
def main():
    st.title("Multilingual Translator to English")
    st.write("This app translates text from any language to English using a pre-trained NLP model.")

    # Input for text to translate
    user_input = st.text_area("Enter text in any language", "")
    
    if st.button("Translate"):
        if user_input:
            # Translate and display output
            translated_text = translator(user_input)[0]["translation_text"]
            st.write("Translated text:")
            st.write(translated_text)
        else:
            st.warning("Please enter text to translate.")

if __name__ == "__main__":
    main()
