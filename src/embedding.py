
import sys
from logger import logging as log
from exception import ProjectException

from data_ingestion import load_data
from model_api import load_model

from data_ingestion import load_data
from model_api import load_model

from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import Settings
from llama_index.core import VectorStoreIndex




def download_gemini_embedding(model, documents):
    """
    Downloads and initializes a Gemini Embedding model for vector embeddings.
    Returns: VectorStoreIndex: An index of vector embeddings for efficient similarity queries.
    """

    try:
        log.info("downloading gemini embedding...")
        gemini_embed_model = GeminiEmbedding(model_name="models/text-embedding-004")
        Settings.llm = load_model()
        Settings.embed_model = gemini_embed_model
        Settings.chunk_size = 800
        Settings.num_output = 512
        Settings.chunk_overlap = 20

        log.info("store gemini embedding...")
        index = VectorStoreIndex.from_documents(
            documents,
            embed_model=gemini_embed_model
        )
        index.storage_context.persist()

        log.info("setting up query engine...")
        query_engine = index.as_query_engine()
        log.info("query engine ready...")
        return query_engine

    except Exception as e:
        log.info("exception downloading gemini embedding...")
        raise ProjectException(str(e), sys)





