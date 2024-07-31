import streamlit as st
from transformers import pipeline

# Load the model once when the app starts
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Streamlit app interface
st.title("Text Summarization App")

user_input = st.text_area("Enter text to summarize", "")

if st.button("Summarize"):
    if user_input:
        summarized_text = summarizer(user_input, max_length=150, min_length=30, do_sample=False)
        summary = summarized_text[0]['summary_text']
        st.subheader("Summary")
        st.write(summary)
    else:
        st.error("Please enter some text to summarize.")

