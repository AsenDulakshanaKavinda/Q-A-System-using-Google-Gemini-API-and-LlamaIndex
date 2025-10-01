import sys
from llama_index.core import SimpleDirectoryReader
from logger import logging as log
from exception import ProjectException

def load_data(data: str) -> list:
    """
    load PDF documents from a specified directory.
    :param data: the directory to load data from.
    :return: the loaded data in PDF file as a list.
    """
    try:
        log.info("data loading started...")
        loader = SimpleDirectoryReader("Data")
        documents = loader.load_data()
        log.info("data loading completed...")
        return documents
    except Exception as e:
        log.info("exception loading data")
        raise ProjectException(str(e), sys)










