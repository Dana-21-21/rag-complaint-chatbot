# CrediTrust Complaint Intelligence Chatbot (RAG System)

## Project Overview

This project develops a Retrieval-Augmented Generation (RAG) chatbot for analyzing customer complaints submitted to the Consumer Financial Protection Bureau (CFPB). The system enables users to ask natural language questions about customer complaints and receive evidence-based answers generated from actual complaint records.

The solution combines semantic search, vector databases, and Large Language Models (LLMs) to transform large volumes of unstructured complaint data into actionable business insights.

---

## Business Problem

Financial institutions receive thousands of customer complaints across multiple products and services. Analyzing these complaints manually is time-consuming and makes it difficult for business stakeholders to identify emerging issues quickly.

This creates challenges for:

* Customer Support Teams attempting to resolve recurring issues.
* Product Managers seeking to improve customer experience.
* Compliance and Risk Teams monitoring regulatory concerns.
* Business Leaders making data-driven strategic decisions.

For example, a stakeholder such as Asha, a Customer Experience Manager, may want to quickly answer questions like:

* What are the most common complaints about checking accounts?
* Are fraud-related complaints increasing?
* What issues are customers reporting about payment processing?
* Which product categories generate the highest number of complaints?

Traditionally, answering these questions would require manually reviewing thousands of complaint records.

The proposed RAG chatbot addresses this challenge by allowing users to retrieve complaint insights instantly through natural language queries.

---

## Project Objectives

The primary objectives of this project are:

* Analyze CFPB complaint data.
* Build a semantic search system using vector embeddings.
* Develop a Retrieval-Augmented Generation (RAG) pipeline.
* Enable users to interact with complaint data using natural language.
* Improve complaint trend identification and investigation speed.
* Support proactive issue identification and business decision-making.

---

## Success Metrics

The project aims to:

* Reduce the time required to identify complaint trends.
* Improve accessibility of complaint information.
* Enable evidence-based responses grounded in actual complaints.
* Increase efficiency for support, compliance, and product teams.
* Support proactive detection of recurring customer issues.

---

## Dataset

Dataset Source:

Consumer Financial Protection Bureau (CFPB) Consumer Complaint Database

The dataset contains customer complaints related to financial products and services, including:

* Checking and savings accounts
* Credit cards
* Personal loans
* Credit reporting
* Money transfers
* Debt collection

---

## Project Workflow

### Task 1: Data Preprocessing and Exploratory Data Analysis

Activities performed:

* Data loading and inspection
* Missing value analysis
* Data cleaning
* Text preprocessing
* Product-level complaint analysis
* Complaint trend analysis
* Exploratory visualizations

### Task 2: Chunking, Embedding, and Vector Store Creation

Activities performed:

* Text chunking
* Metadata creation
* Embedding generation using Sentence Transformers
* Vector database creation using ChromaDB

Embedding Model:

sentence-transformers/all-MiniLM-L6-v2

### Task 3: RAG Pipeline Development

Activities performed:

* Vector store retrieval
* Similarity search
* Prompt engineering
* Response generation using an LLM
* Qualitative evaluation

### Task 4: Interactive Chat Interface

Activities performed:

* Gradio web application development
* User query interface
* Source display
* Response generation
* Conversation reset functionality

---

## Technologies Used

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy
* Matplotlib
* Seaborn

### Embedding Model

* sentence-transformers
* all-MiniLM-L6-v2

### Vector Database

* ChromaDB

### RAG Framework

* LangChain

### Large Language Models

* Transformers
* Hugging Face

### User Interface

* Gradio

---

## Project Structure

```text
rag-complaint-chatbot/
│
├── data/
│   └── complaints.csv
│
├── notebooks/
│   ├── 01_EDA_Preprocessing.ipynb
│   ├── 02_chunking_embedding.ipynb
│   └── task3_rag_pipeline.ipynb
│
├── vector_store/
│
├── app.py
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

## Installation

### 1. Clone Repository

```bash
git clone <repository-url>
cd rag-complaint-chatbot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Environment

Mac/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Required Libraries

Ensure the following key libraries are included in requirements.txt:

```text
pandas
numpy
matplotlib
seaborn
jupyter
sentence-transformers
transformers
torch
langchain
langchain-community
chromadb
gradio
huggingface-hub
```

---

## Running the Project

### Run Notebooks

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open notebooks in the following order:

1. 01_EDA_Preprocessing.ipynb
2. 02_chunking_embedding.ipynb
3. task3_rag_pipeline.ipynb

---

### Run the Chat Application

```bash
python app.py
```

After launching, open the provided local URL in your browser.

Example:

```text
http://127.0.0.1:7860
```

---

## Example Questions

Users can ask questions such as:

* What are the most common complaints about checking accounts?
* What fraud-related issues are customers reporting?
* Which products receive the highest complaint volume?
* What recurring problems exist in payment processing?
* What concerns do customers report about credit reporting?

---

## System Evaluation

The RAG system was evaluated using representative business questions.

Evaluation focused on:

* Retrieval relevance
* Response accuracy
* Context utilization
* Business usefulness

Results showed that the system successfully retrieves relevant complaint records and generates grounded responses with reduced hallucination.

---

## Key Business Benefits

The chatbot provides value by:

* Accelerating complaint investigation.
* Improving customer support efficiency.
* Supporting compliance monitoring.
* Identifying recurring customer issues.
* Enabling data-driven decision-making.
* Reducing manual review effort.

---

## Future Improvements

Potential enhancements include:

* Hybrid search (semantic + keyword retrieval).
* Larger language models.
* Response streaming.
* Multi-turn conversation memory.
* Automated evaluation metrics.
* Cloud deployment for enterprise usage.

---

## Author

CrediTrust Complaint Intelligence Chatbot

Built as part of the Retrieval-Augmented Generation (RAG) Financial Complaint Analysis Project.

