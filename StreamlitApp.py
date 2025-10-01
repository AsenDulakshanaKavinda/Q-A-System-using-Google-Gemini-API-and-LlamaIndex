import streamlit as st
from src.data_ingestion import load_data
from src.embedding import download_gemini_embedding
from src.model_api import load_model

from logger import logging as log


def main():
    st.set_page_config("QA with Documents")
    doc = st.file_uploader("upload your document")
    st.header("QA with documents (Information Retrieval)")
    user_question = st.text_input("Ask your question")
    if st.button("submitted & process"):
        with st.spinner("Processing..."):
            document = load_data(doc)
            model = load_model()
            query_engine = download_gemini_embedding(model, document)
            response = query_engine.query(user_question)
            log.info("Processing the response...")
            st.write(response.response)
            log.info("Displaying the response...")

main()



