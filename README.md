# 🛠️ DevSentry

[🌐 Live Demo](https://your-live-demo-url.com)

**DevSentry** is a production-grade, AI-powered error triage assistant that detects, analyzes, and suggests fixes for runtime errors across multiple languages. It combines FastAPI, Streamlit, and Gemini 1.5 Flash (via LangChain) to act like a senior developer sitting next to you.

---

## 🚀 Features

- ✅ Analyze errors in Python, JavaScript, Java, C++
- ✅ Suggest structured, patch-ready code fixes
- ✅ Severity classification (Low → Critical)
- ✅ Gemini 1.5 Flash integration via LangChain
- ✅ Beautiful, animated Streamlit UI
- ✅ One-click API + UI startup

---

## 🧠 Powered By

- [LangChain](https://github.com/langchain-ai/langchain)
- [Gemini 1.5 Flash](https://ai.google.dev/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Streamlit](https://streamlit.io/)
- [Lottie](https://lottiefiles.com/) animations

---

## 📦 Tech Stack

| Layer     | Tech                     |
|-----------|--------------------------|
| Frontend  | `Streamlit`              |
| Backend   | `FastAPI` + `LangChain`  |
| LLM       | `Gemini 1.5 Flash`       |
| API Agent | `RunnableMap` + Prompt Templates |
| Styling   | CSS + HTML + Lottie      |

---

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourname/devsentry.git
cd devsentry
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Create a `.env` file**
```env
GEMINI_API_KEY=your_gemini_key_here
```

4. **Run DevSentry**
```bash
bash start.sh
```

- Backend: [http://localhost:8000](http://localhost:8000)
- UI: [http://localhost:8501](http://localhost:8501)

---

## 🔍 Example Input

```json
{
  "error_message": "TypeError: 'NoneType' object is not iterable",
  "stack_trace": "File 'main.py', line 42, in get_items\n    for item in data:\nTypeError: 'NoneType' object is not iterable",
  "language": "python"
}
```

---

## 📤 Output Preview

- Cause: `data` is `None` — cannot iterate a null object
- Severity: 🔴 High
- Fix:
```python
if data:
    for item in data:
        process(item)
```

---

## 📁 Folder Structure

```
devsentry/
├── app/                # FastAPI backend
│   ├── agent.py
│   ├── main.py
│   ├── triage.py
│   ├── fixgen.py
│   └── schemas.py
├── ui/                 # Streamlit frontend
│   └── dashboard.py
├── start.sh
├── .env
├── README.md
└── requirements.txt
```

---

## 📄 License

MIT License © 2025

---

## 🙋 Questions or Contributions?

Open an issue or submit a pull request — contributions are welcome.