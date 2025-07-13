# 🛠️ DevSentry

[🌐 Live Demo](http://94.16.31.129:8501/)

**DevSentry** is a production-grade AI-powered debugging assistant that analyzes runtime errors, suggests structured fixes, and surfaces relevant GitHub issues — acting like a senior engineer for your codebase. Built with LangChain, Streamlit, FastAPI, and Gemini 1.5 Flash.

---

## 🚀 Features

- ✅ Analyze runtime errors in Python, JavaScript, Java, C++
- ✅ Classify error cause, component, and severity
- ✅ Suggest fix explanation + patch-ready code
- ✅ Related GitHub issue search (via REST API)
- ✅ Fast, minimal UI with animation and dark-mode styling
- ✅ Visualize structural patterns + PDF report export
- ✅ Modular FastAPI backend + Docker-ready setup

---

## 🧠 Powered By

- LangChain
- Gemini 1.5 Flash
- FastAPI
- Streamlit
- GitHub REST API
- Lottie Animations

---

## ⚙️ Tech Stack

Frontend : Streamlit  
Backend  : FastAPI  
LLM Agent: LangChain + Gemini Flash  
Tools    : GitHub Search API  
Logging  : Python logging module  
Deploy   : Docker + systemctl (optional)

---

## 📁 Folder Structure

devsentry/
├── app/
│   ├── agent.py             # LangChain logic
│   ├── github_search.py     # GitHub REST API calls
│   ├── main.py              # FastAPI routing
│   └── utils.py             # PDF/chart helpers
├── ui/
│   └── dashboard.py         # Streamlit frontend
├── .env.example             # API key config template
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── start.sh
└── README.md

---

## ⚙️ Installation

git clone https://github.com/yourusername/devsentry.git  
cd devsentry

python -m venv v-struct  
source v-struct/bin/activate  

pip install -r requirements.txt  

cp .env.example .env  
Edit `.env`:

GEMINI_API_KEY=your_gemini_api_key  
GITHUB_TOKEN=your_optional_github_token

---

## 🚀 Run

bash start.sh

- UI → http://localhost:8501  
- API → http://localhost:8000/docs

---

## 🔍 Example Input

{
  "error_message": "TypeError: 'NoneType' object is not iterable",
  "stack_trace": "File 'main.py', line 42, in get_items\n    for item in data:",
  "language": "python"
}

---

## 📤 Output Example

Cause: data is None  
Severity: Critical  
Fix:
if data:
    for item in data:
        process(item)

GitHub Issues:
- [NoneType iteration fix — pandas] (link)
- [Crash when parsing empty list] (link)

---

## 📝 License

MIT License © 2025

---

## 🙋 Contributions Welcome

Open an issue or submit a pull request.