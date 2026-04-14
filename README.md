# RAG chatbot

Simple chatbot designed to answer user's questions based on the provided data.

## How it works

1. Data is loaded and split into chunks using openai/gpt-4.1-nano model (wip - will be model agnostic in the future)
2. Chunks are passed to encoder model and saved in Chroma vector database.

## Setup

1. run `uv sync`

2. Create a folder called `knowledge-base` and place your data documents in `.md` format there in separate folders, preferably naming them semantically.
   Required structure (subfolder and documents naming is up to the user):
   knowledge-base/
   ├── projects/
   │ ├── doc1.md
   │ └── doc2.md
   ├── employees/
   │ ├── doc3.md
   │ └── doc4.md
   ....

3. run `uv run encode.py` to encode the data and save it in a vector database.
4. run `uv run answer.py`
