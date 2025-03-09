import os
import gradio as gr
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from groq import Groq

# ✅ Path FAISS index
faiss_path = "faiss_index"

# ✅ Pastikan FAISS index ada sebelum loading
if not os.path.exists(f"{faiss_path}/index.faiss"):
    raise FileNotFoundError(f"⚠️ FAISS index tidak ditemukan di {faiss_path}. Pastikan Anda telah mengunggahnya!")

# ✅ Load FAISS index
vector_store = FAISS.load_local(
    faiss_path,
    HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"),
    allow_dangerous_deserialization=True  
)

# ✅ Load API Key dari Secrets di Hugging Face Spaces
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("⚠️ API Key Groq tidak ditemukan! Setel variabel lingkungan 'GROQ_API_KEY'.")

# ✅ Inisialisasi API Groq
client = Groq(api_key=GROQ_API_KEY)

def retrieve_and_generate(query, history=[]):
    """🔍 Retrieve dokumen & 🧠 Generate jawaban dari LLM."""
    
    # 🔍 Ambil 3 dokumen yang paling relevan
    docs = vector_store.similarity_search(query, k=3)
    context = "\n\n".join([doc.page_content for doc in docs])

    # 🧠 Generate respons dengan model Groq
    response = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[
            {"role": "system", "content": "Anda adalah asisten AI yang menjawab pertanyaan tentang RoboHome berdasarkan dokumen ini."},
            {"role": "user", "content": f"{context}\n\nPertanyaan: {query}"}
        ],
        temperature=0.7,
        max_tokens=200
    )

    bot_response = response.choices[0].message.content
    history.append((query, bot_response))  # ✅ Simpan chat history
    return history

# ✅ UI dengan Gradio
with gr.Blocks() as demo:
    gr.Markdown("## 🤖 RoboHome RAG Chatbot")
    gr.Markdown("Chatbot ini menjawab pertanyaan berdasarkan dokumentasi RoboHome.")
    
    chatbot = gr.Chatbot(label="💬 Jawaban RoboHome")
    input_text = gr.Textbox(label="✏️ Ajukan pertanyaan tentang RoboHome", placeholder="Ketik pertanyaan di sini...")
    send_button = gr.Button("🚀 Kirim")

    def process_input(user_input, history):
        return retrieve_and_generate(user_input, history)

    send_button.click(process_input, inputs=[input_text, chatbot], outputs=chatbot)

demo.launch(share=True)
