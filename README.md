# 🎧 InsightVault – Smart Meeting Summarizer & Sentiment Analyzer

**InsightVault** is a smart AI-powered web application that automatically transcribes meeting audio, summarizes it using NLP, and provides sentiment analysis — all in one elegant interface.

> 🚀 Built by [Payal](https://www.linkedin.com/in/your-profile) with love for innovation and productivity.

---

## ✨ Features

- 🎙️ Upload `.wav` meeting recordings
- 🧠 Auto transcription using **Whisper by OpenAI**
- 📝 Clean, readable summary using **HuggingFace Transformers**
- 😊 Sentiment analysis (Positive, Neutral, Negative)
- 🌗 Dark Mode toggle
- 🌐 Language switch (English / Hindi UI)
- 💻 Responsive UI (Bootstrap 5)
- ⚡ Loader animation during analysis

---

## 🛠️ Tech Stack

- **Backend**: Python Flask  
- **Speech-to-Text**: OpenAI Whisper  
- **NLP Summarization**: HuggingFace Transformers (DistilBART)  
- **Frontend**: HTML, CSS, Bootstrap 5  
- **Sentiment Analysis**: TextBlob  
- **Optional Enhancements**: Language toggle, dark mode, animated loader

---

## 🚀 How to Run Locally

### 1. Clone the repository


git clone https://github.com/your-username/InsightVault.git
cd InsightVault
2..python -m venv venv
venv\Scripts\activate        # On Windows
# source venv/bin/activate   # On Mac/Linux
3...pip install -r requirements.txt
4...python app.py




InsightVault/
│
├── app.py                  # Flask backend
├── summarize.py            # Transcription + NLP logic
├── sentiment.py            # Sentiment analyzer
├── requirements.txt
├── static/
│   └── style.css           # Optional: custom styles
├── templates/
│   └── index.html          # Frontend UI
└── uploads/                # Uploaded audio files
