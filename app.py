import streamlit as st
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="Smart PDF Chatbot")
st.header("📄 Smart PDF Chatbot")

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file is not None:
    pdf_reader = PdfReader(uploaded_file)

    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    st.subheader("Extracted Text")
    st.write(text[:5000])  # Display first 5000 characters
    