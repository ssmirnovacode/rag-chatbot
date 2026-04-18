# RAG chatbot

Simple chatbot designed to answer user's questions based on the provided data, showing the retrieved relevant context.

## How it works

1. Knowledge data is loaded and split into chunks using openai/gpt-4.1-nano model (wip - will be model agnostic in the future)
2. Chunks are passed to encoder model and saved in Chroma vector database.
3. Once the user submits a request, this request gets encoded and the vector data base is queried for relevant chunks.
4. Once retrieved, the relevent chunks are processed by the LLM and reordered by relevance if needed.
5. Final chunks get submitted to the actual chatbot query along with user's question.
6. The chatbot answers the question and the retrieved context is also shown on the right side of the screen for reference.

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

3. save your api tokens for openai and huggingface in `.env` as OPENAI_API_KEY and HF_TOKEN.
4. run `uv run app.py` - the chat app will be launched in the browser
