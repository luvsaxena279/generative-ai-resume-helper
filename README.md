[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<luvsaxena279>/generative-ai-resume-helper/blob/main/notebook.ipynb)

# Resume RAG Chatbot (Gradio + Groq)

## 🚀 Demo

- **Interactive notebook (recommended):** click the “Open in Colab” badge above to run the resume chatbot in your browser with no local setup.
- **What you can try:** upload your own public resume PDF to the `data/` folder in Colab and ask questions like:
  - “What are the main skills in this resume?”
  - “Which roles does this profile fit best?”

An interactive **Generative AI chatbot** that can read resume PDF files and answer questions about them using **Retrieval-Augmented Generation (RAG)**.  
It is designed as a portfolio project for an AI generalist, showing skills in embeddings, vector search, LLMs, and web app deployment.

## 🧠 What this app does

- Loads one or more **resume PDFs** from the `data/` folder.
- Splits them into chunks and creates **vector embeddings**.
- Uses **Groq's Llama 3** model to answer questions grounded in the resumes.
- Provides an easy **chat interface (Gradio)** for recruiters or candidates.

Example questions:
- “What technical skills are mentioned across these resumes?”
- “What kinds of roles do these candidates target?”
- “Summarize the strongest candidate profile in this dataset.”

## 🏗️ Tech stack

- **Python** (Google Colab / local)
- **LlamaIndex** – document loading, indexing, and RAG pipeline
- **Hugging Face sentence-transformers** – `all-MiniLM-L6-v2` embeddings
- **GroqCloud LLM** – `llama-3.1-8b-instant` model
- **Gradio** – web chat UI
- (Optional) **Hugging Face Spaces** – public deployment

## 📂 Project structure

```text
.
├── app.py                # Gradio app entrypoint (for Spaces)
├── notebook.ipynb        # Colab notebook used for development
├── requirements.txt      # Python dependencies
├── data/
│   └── resume-sample.pdf # Example resume PDF (not committed if private)
└── README.md
