# RAG Teaching Assistant

An AI-powered teaching assistant that transforms lecture videos into a searchable knowledge base using Retrieval-Augmented Generation (RAG). The system transcribes lecture videos with OpenAI Whisper, generates semantic embeddings using BGE-M3, stores them in a FAISS vector database, and retrieves the most relevant lecture content to generate accurate, context-aware answers using DeepSeek-R1.

Instead of manually searching through hours of lecture videos, users can ask questions in natural language and receive precise answers grounded in the lecture content, along with the corresponding lecture number and timestamp.

---

## Features

- 🎥 Convert lecture videos into text using OpenAI Whisper
- ✂️ Split transcripts into semantic chunks
- 🧠 Generate embeddings using BGE-M3
- 🗄️ Store embeddings in a FAISS vector database
- 🔍 Retrieve relevant lecture chunks using semantic similarity search
- 🤖 Generate context-aware responses using DeepSeek-R1
- 📚 Answer questions across multiple lecture videos
- ⏱️ Return lecture number and timestamp with every answer

---

## Project Workflow

```text
🎥 Lecture Videos
        │
        ▼
🎙️ OpenAI Whisper
(Video → Text)
        │
        ▼
📄 Text Chunking
+ Metadata
(Number, Title, Time)
        │
        ▼
🧠 BGE-M3 Embeddings
        │
        ▼
🗄️ FAISS Vector Database
        ▲
        │
❓ User Question
        │
        ▼
🧠 Query Embedding
        │
        ▼
🔍 Semantic Search
        │
        ▼
📚 Retrieved Chunks
        │
        ▼
🤖 DeepSeek-R1
        │
        ▼
💬 Final Answer
```

---

## Chunk Format

Each transcript is divided into semantic chunks before embedding generation.

Example:

```json
{
    "number": 7,
    "title": "Binary Trees",
    "start": 487,
    "end": 489,
    "text": "A binary tree is a data structure where each node has at most two children."
}
```

---

## Example

### User Question

```
What is a Binary Tree?
```

### Retrieved Context

```json
{
    "number": 7,
    "title": "Binary Trees",
    "start": 487,
    "end": 489,
    "text": "A binary tree is a data structure where each node has at most two children."
}
```

### Generated Response

```
A Binary Tree is a hierarchical data structure in which each node has at most two children (i.e., a left child and a right child).

According to Lecture 7, binary trees are introduced with an explanation of their properties and binary search trees. The lecture also discusses complete binary trees, where every level is completely filled except possibly the last, and all nodes are positioned as far left as possible.

Source:
Lecture Number : 7
Timestamp      : 487s - 489s
```

---

## Tech Stack

### Programming Language

- Python

### AI Models

- OpenAI Whisper
- BGE-M3 Embedding Model
- DeepSeek-R1

### Vector Database

- FAISS

### Libraries

- NumPy
- Pandas
- Requests
- FFmpeg

---

## Project Structure

```
rag-teaching-assistant/
│
├── data/
│   ├── videos/
│   ├── transcripts/
│   ├── chunks/
│   └── embeddings/
│
├── src/
│   ├── video_to_text.py
│   ├── chunking.py
│   ├── embedding.py
│   ├── vector_store.py
│   ├── retrieval.py
│   ├── rag_pipeline.py
│   └── inference.py
│
├── requirements.txt
├── README.md
└── main.py
```

---

## How It Works

### Step 1 — Video Transcription

Lecture videos are converted into text using OpenAI Whisper.

### Step 2 — Text Chunking

The transcript is divided into semantic chunks while preserving context.

Each chunk contains:

- Lecture Number
- Lecture Title
- Start Timestamp
- End Timestamp
- Transcript Text

### Step 3 — Embedding Generation

Each chunk is converted into a dense vector representation using the BGE-M3 embedding model.

### Step 4 — Vector Storage

The generated embeddings are stored in a FAISS vector database for efficient semantic similarity search.

### Step 5 — Retrieval

When a user asks a question, the query is converted into an embedding. The system retrieves the most relevant lecture chunks based on vector similarity.

### Step 6 — Response Generation

The retrieved chunks are provided as context to DeepSeek-R1, which generates an accurate answer grounded in the lecture content.

---

## Installation

Clone the repository

```bash
git clone https://github.com/adas63931-debug/rag-teaching-assistant.git
```

Navigate to the project directory

```bash
cd rag-teaching-assistant
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python main.py
```

---

## Future Improvements

- 🌐 Streamlit or Gradio web interface
- 📄 PDF and PowerPoint support
- 🔎 Hybrid Search (BM25 + Semantic Search)
- 🌍 Multi-language lecture support
- 📌 Clickable timestamp citations
- ☁️ Cloud deployment
- 📊 RAG evaluation metrics
- 🎯 Multi-course indexing

---

## Applications

- AI Teaching Assistant
- University Lecture Search
- Online Learning Platforms
- Corporate Training
- Personal Knowledge Assistant

---

## Author

**Akash Das**

Final Year Project

Artificial Intelligence & Data Science

---
