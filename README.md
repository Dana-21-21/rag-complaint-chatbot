# RAG Complaint Chatbot

## Project Overview

This project develops a Retrieval-Augmented Generation (RAG) chatbot using Consumer Financial Protection Bureau (CFPB) complaint data. The objective is to enable users to ask questions about consumer complaints and receive responses generated from relevant complaint narratives retrieved through semantic search.

The project follows a complete RAG pipeline, including data preprocessing, exploratory data analysis, text chunking, embedding generation, vector database indexing, retrieval, and response generation.

---

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

---

## Features

* Exploratory Data Analysis (EDA)
* Complaint narrative preprocessing
* Stratified sampling
* Text chunking using LangChain
* Sentence-transformer embeddings
* ChromaDB vector storage
* Semantic retrieval
* Retrieval-Augmented Generation (RAG)

---

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/rag-complaint-chatbot.git
cd rag-complaint-chatbot
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the environment

Mac/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Launch Jupyter Notebook

```bash
jupyter notebook
```

Open the notebook inside the `notebooks/` directory and run all cells.

### Run the application

```bash
python app.py
```

---

## Task 1: EDA and Preprocessing

This stage includes:

* Loading CFPB complaint data
* Product distribution analysis
* Narrative length analysis
* Missing value assessment
* Complaint filtering
* Text cleaning and normalization

Output:

```text
data/filtered_complaints.csv
```

---

## Task 2: Chunking, Embedding, and Indexing

This stage includes:

* Stratified sampling
* Text chunking
* Embedding generation
* ChromaDB indexing
* Metadata creation

Stored metadata:

* Complaint ID
* Product category
* Chunk ID

Output:

```text
vector_store/
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* LangChain
* Sentence Transformers
* ChromaDB
* Jupyter Notebook
* Git
* GitHub

---

## Future Work

* Implement semantic retrieval
* Integrate Large Language Models
* Build chatbot interface
* Evaluate retrieval quality
* Deploy complete RAG system

```
```

