import gradio as gr
import chromadb
from sentence_transformers import SentenceTransformer
from transformers import pipeline

# -----------------------------
# LOAD MODELS
# -----------------------------
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-small"
)

# -----------------------------
# LOAD VECTOR DB
# -----------------------------
client = chromadb.PersistentClient(path="./vector_store")
collection = client.get_or_create_collection("complaints")


# -----------------------------
# RETRIEVER
# -----------------------------
def retrieve_chunks(question, k=5):
    query_embedding = embedding_model.encode([question])[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    return results


# -----------------------------
# PROMPT TEMPLATE
# -----------------------------
PROMPT_TEMPLATE = """
You are a helpful financial analyst assistant for CrediTrust.

Use ONLY the context below to answer the question.
If the answer is not in the context, say "I don't have enough information."

Context:
{context}

Question:
{question}

Answer:
"""


# -----------------------------
# RAG PIPELINE
# -----------------------------
def rag_pipeline(question):

    retrieved = retrieve_chunks(question, k=5)

    docs = retrieved["documents"][0]
    metadatas = retrieved["metadatas"][0]

    context = "\n\n".join(docs[:3])  # prevent token overflow

    prompt = PROMPT_TEMPLATE.format(
        context=context,
        question=question
    )

    response = generator(prompt, max_new_tokens=200)

    answer = response[0]["generated_text"]

    # format sources nicely
    sources = []
    for i in range(len(docs)):
        sources.append(
            f"📌 Source {i+1} (Complaint ID: {metadatas[i]['complaint_id']}):\n{docs[i]}"
        )

    return answer, "\n\n".join(sources)


# -----------------------------
# GRADIO FUNCTION WRAPPER
# -----------------------------
def chat_interface(user_input):
    answer, sources = rag_pipeline(user_input)
    return answer, sources


# -----------------------------
# GRADIO UI
# -----------------------------
with gr.Blocks(title="CrediTrust RAG Chatbot") as app:

    gr.Markdown("# 💬 CrediTrust Complaint RAG Chatbot")

    with gr.Row():
        input_box = gr.Textbox(
            label="Ask a question",
            placeholder="e.g. What are common complaints about checking accounts?"
        )

    with gr.Row():
        submit_btn = gr.Button("Ask")
        clear_btn = gr.Button("Clear")

    output_answer = gr.Textbox(label="Answer")
    output_sources = gr.Textbox(label="Sources (For Transparency)")

    # button actions
    submit_btn.click(
        chat_interface,
        inputs=input_box,
        outputs=[output_answer, output_sources]
    )

    clear_btn.click(
        lambda: ("", ""),
        inputs=[],
        outputs=[output_answer, output_sources]
    )


# -----------------------------
# RUN APP
# -----------------------------
app.launch()