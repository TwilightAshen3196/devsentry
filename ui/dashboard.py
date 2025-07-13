import streamlit as st
import requests
import time
from streamlit_lottie import st_lottie
import requests as rqs

# === SETUP ===
st.set_page_config(page_title="DevSentry", layout="wide", page_icon="🛠️")

def load_lottieurl(url: str):
    res = rqs.get(url)
    if res.status_code != 200:
        return None
    return res.json()

lottie_bot = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_pprxh53t.json")

# === CUSTOM CSS ===
st.markdown("""
    <style>
    .title {
        font-size: 3em;
        font-weight: 800;
        text-align: center;
        color: #FF4B4B;
        margin-bottom: 0.1em;
    }
    .subtitle {
        font-size: 1.2em;
        text-align: center;
        color: #666;
        margin-bottom: 1.5em;
    }
    .card {
        padding: 1.2em;
        border-radius: 12px;
        margin-bottom: 1em;
        background-color: #fafafa;
        border: 1px solid #eee;
        box-shadow: 0 2px 6px rgba(0,0,0,0.04);
    }
    .badge {
        padding: 0.4em 0.9em;
        border-radius: 6px;
        font-weight: 600;
        font-size: 0.9em;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# === HEADER ===
st.markdown('<div class="title">🛠️ DevSentry</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your private AI for error triage & code repair</div>', unsafe_allow_html=True)
st_lottie(lottie_bot, height=180, key="bot")

# === INPUT FORM ===
st.markdown("---")
st.markdown("### 📝 Submit Your Error")

error_message = st.text_area("🔴 Error Message", height=100, placeholder="e.g. TypeError: NoneType is not iterable")
stack_trace = st.text_area("📄 Stack Trace", height=150, placeholder="Paste full traceback here...")
language = st.selectbox("💻 Language", ["python", "javascript", "java", "c++"])

# === PROCESS ===
if st.button("🚀 Analyze Error", use_container_width=True):
    with st.spinner("Analyzing with Gemini 1.5 Flash..."):
        time.sleep(0.8)
        payload = {
            "error_message": error_message.strip(),
            "stack_trace": stack_trace.strip(),
            "language": language.lower()
        }

        try:
            response = requests.post("http://localhost:8000/analyze", json=payload)
            data = response.json()

            classification = data.get("classification")
            fix = data.get("fix_suggestion")

            col1, col2 = st.columns(2)

            # === CLASSIFICATION ===
            with col1:
                st.markdown("#### 📌 Classification")
                if isinstance(classification, dict):
                    cause = classification.get("cause", "N/A")
                    component = classification.get("component", "N/A")
                    severity = classification.get("severity", "unknown").lower()

                    sev_map = {
                        "low":   ("🟢 Low", "#28a745"),
                        "medium":("🟠 Medium", "#ffc107"),
                        "high":  ("🔴 High", "#dc3545"),
                        "critical": ("🔥 Critical", "#b30000")
                    }
                    sev_text, sev_color = sev_map.get(severity, ("❓ Unknown", "#6c757d"))

                    st.markdown(f"""<div class="card">
                        <div><b>Cause:</b> {cause}</div><br>
                        <div><b>Component:</b> {component}</div><br>
                        <div><b>Severity:</b> <span class="badge" style="background-color:{sev_color};">{sev_text}</span></div>
                    </div>""", unsafe_allow_html=True)

                else:
                    st.error("⚠️ Classification result was malformed.")

            # === FIX SUGGESTION ===
            with col2:
                st.markdown("#### 🛠️ Suggested Fix")
                if isinstance(fix, dict):
                    explanation = fix.get("explanation", "N/A")
                    fix_strategy = fix.get("fix", "N/A")
                    code = fix.get("code", "")

                    st.markdown(f"""<div class="card">
                        <div><b>🧠 Explanation:</b></div>
                        <div>{explanation}</div><br>
                        <div><b>🔧 Fix Strategy:</b></div>
                        <div>{fix_strategy}</div>
                    </div>""", unsafe_allow_html=True)

                    st.markdown("**📜 Patch Code:**")
                    st.code(code, language)
                else:
                    st.error("⚠️ Fix suggestion was malformed.")

            # === FEEDBACK ===
            st.markdown("---")
            st.markdown("##### 🙋 Was this suggestion helpful?")
            fb1, fb2 = st.columns(2)
            with fb1:
                st.button("👍 Yes", use_container_width=True)
            with fb2:
                st.button("👎 No", use_container_width=True)

        except Exception as e:
            st.error(f"❌ API request failed: {e}")