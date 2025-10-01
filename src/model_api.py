import os
from dotenv import load_dotenv
import sys

from exception import ProjectException
from logger import logging as log

from llama_index.llms.gemini import Gemini

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def load_model():
    """
    loads a Gemini-Pro model for natural language processing.
    :return: Gemini: An instance of the Gemini class initialized with the 'gemini-pro' model.
    """


    try:
        log.info("Loading model...")
        llm = Gemini(
            model = "models/gemini-2.5-pro",
            api_key=GOOGLE_API_KEY,
        )
        log.info("Model loaded...")
        return llm
    except Exception as e:
        log.info("exception loading model...")
        raise ProjectException(str(e), sys)












