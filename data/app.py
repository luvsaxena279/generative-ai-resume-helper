import os
import gradio as gr

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.groq import Groq


# --- Load and index documents --- #

def build_index(data_dir: str = "data"):
    """Load PDFs from data_dir and build a VectorStoreIndex."""
    if not os.path.exists(data_dir):
        raise FileNotFoundError(
            f"Data directory '{data_dir}' not found. "
            "Create it and add one or more resume PDFs."
        )

    documents = SimpleDirectoryReader(data_dir).load_data()
    if not documents:
        raise ValueError(
            f"No documents found in '{data_dir}'. "
            "Add at least one PDF resume file."
        )

    embed_model = HuggingFaceEmbedding(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    index = VectorStoreIndex.from_documents(
        documents,
        embed_model=embed_model,
    )
    return index


# Build index at startup
index = build_index()

# LLM (reads GROQ_API_KEY from environment; set this in HF Spaces / locally)
llm = Groq(model="llama-3.1-8b-instant")
query_engine = index.as_query_engine(llm=llm)


# --- Gradio chat interface --- #

def chat_fn(message, history):
    """Simple chat handler for Gradio ChatInterface."""
    try:
        response = query_engine.query(message)
        return str(response)
    except Exception as e:
        return f"Error: {e}"


demo = gr.ChatInterface(
    fn=chat_fn,
    title="Generative AI Resume Helper",
    description=(
        "Ask questions about the resume PDFs stored in the `data/` folder. "
        "This app uses LlamaIndex + Groq Llama 3 with Retrieval-Augmented Generation."
    ),
)


if __name__ == "__main__":
    # For local testing: `python app.py`
    demo.launch()
