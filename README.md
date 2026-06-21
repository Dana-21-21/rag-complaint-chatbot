# # RAG Complaint Chatbot

## Project Overview

This project develops a Retrieval-Augmented Generation (RAG) chatbot using the Consumer Financial Protection Bureau (CFPB) complaint dataset. The system enables users to ask questions related to consumer complaints and receive responses generated from relevant complaint narratives retrieved through semantic search.

The project combines data preprocessing, text chunking, vector embeddings, and a vector database to support efficient retrieval of complaint information. Retrieved complaint chunks are then used as context for a Large Language Model (LLM) to generate informative responses.

## Project Structure

```text
rag-complaint-chatbot/
├── .vscode/
├── .github/
│   └── workflows/
├── data/
│   ├── raw/
│   └── processed/
├── vector_store/
├── notebooks/
├── src/
├── tests/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Tasks Completed

### Task 1: Exploratory Data Analysis and Preprocessing

* Loaded and explored the CFPB complaint dataset.
* Analyzed complaint distribution across financial products.
* Examined narrative length distributions.
* Identified records with and without complaint narratives.
* Filtered the dataset to selected product categories.
* Cleaned and normalized complaint narratives.
* Saved the cleaned dataset for downstream processing.

### Task 2: Text Chunking, Embedding, and Indexing

* Created a representative sample from the filtered dataset.
* Implemented text chunking using RecursiveCharacterTextSplitter.
* Generated embeddings using the sentence-transformers/all-MiniLM-L6-v2 model.
* Stored embeddings and metadata in ChromaDB.
* Persisted the vector store for future retrieval operations.

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* LangChain
* Sentence Transformers
* ChromaDB
* Jupyter Notebook
* Git and GitHub

## Vector Store Metadata

Each stored chunk contains metadata including:

* Complaint ID
* Product Category
* Chunk ID

This metadata allows retrieved chunks to be traced back to their original complaint records.

## Future Work

The next stages of the project include:

* Implementing semantic retrieval using ChromaDB.
* Integrating a Large Language Model (LLM).
* Building a chatbot interface using Streamlit or Gradio.
* Evaluating retrieval accuracy and response quality.
* Deploying the complete RAG application.

## Author

Prepared as part of the RAG Complaint Chatbot project.

