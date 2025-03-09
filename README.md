# RoboHome RAG Chatbot

RoboHome RAG Chatbot adalah sistem chatbot berbasis **Retrieval-Augmented Generation (RAG)** yang dapat menjawab pertanyaan berdasarkan **manual pengguna RoboHome**. Chatbot ini menggunakan **FAISS** sebagai vektor pencarian, **Groq API** sebagai model LLM, dan **Gradio** sebagai antarmuka pengguna.

## 🚀 Fitur Utama
- **Retrieval-Augmented Generation (RAG)**: Menggunakan FAISS untuk pencarian dokumen terkait sebelum menghasilkan jawaban.
- **Integrasi LLM (Groq API)**: Menggunakan model open-source seperti **Mixtral-8x7B** untuk menjawab pertanyaan.
- **Antarmuka Gradio**: Chatbot dengan UI interaktif berbasis web.
- **Knowledge Base dari PDF & SQL**: Sistem ini menggunakan dataset sintetik dari manual pengguna RoboHome dan database transaksi RoboHome.

---

## 📂 Struktur Proyek
```
robohome-rag-chatbot/
├── app.py                 # Kode utama chatbot (Gradio + FAISS + Groq API)
├── requirements.txt       # Daftar dependensi
├── faiss_index/           # Folder penyimpanan FAISS index
│   ├── index.faiss
├── data/                  # Dataset untuk chatbot
│   ├── robohome_synthetic.pdf  # Manual pengguna RoboHome (sintetik)
│   ├── robohome_synthetic.sql  # Database RoboHome (sintetik)
├── README.md              # Dokumentasi proyek
```

---

## 🛠 Instalasi & Menjalankan Chatbot

### 1️⃣ **Clone repository ini**
```bash
https://github.com/jaal047/RoboHome-RAG-Chatbot.git
cd RoboHome-RAG-Chatbot
```

### 2️⃣ **Install dependencies**
```bash
pip install -r requirements.txt
```

### 3️⃣ **Jalankan chatbot**
```bash
python app.py
```
Setelah berjalan, chatbot dapat diakses di **http://127.0.0.1:7860/**

---

## 🔑 **Konfigurasi API Key (Groq API)**
Pastikan Anda memiliki API Key dari Groq. Simpan sebagai variabel lingkungan:
```bash
export GROQ_API_KEY='your_groq_api_key_here'
```

Jika Anda menggunakan Windows:
```powershell
$env:GROQ_API_KEY="your_groq_api_key_here"
```

---

## 📊 **Benchmarking RAG vs. LLM Langsung**
Sistem ini dibandingkan dengan LLM biasa tanpa retrieval. Hasilnya:
✅ **RAG memberikan jawaban lebih akurat karena menggunakan knowledge base.**
⚠️ **LLM biasa sering memberikan jawaban umum tanpa konteks spesifik.**

---

## 🚀 Demo RoboHome RAG Chatbot  
Chatbot ini dapat diuji langsung di Hugging Face Spaces:  

👉 **[Demo RoboHome RAG Chatbot](https://huggingface.co/spaces/Jaal047/RoboHome-RAG-Chatbot)**  

Cukup masukkan pertanyaan Anda mengenai RoboHome, dan chatbot akan memberikan jawaban berbasis knowledge base!

---

## 📩 **Kontak & Kontribusi**
Jika ingin berkontribusi atau melaporkan bug, silakan buka **issue** atau ajukan **pull request**.

📧 **Email**: rijal.akhdan.khairullah@gmail.com
