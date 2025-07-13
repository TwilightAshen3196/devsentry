import streamlit as st
import requests
import time
from streamlit_lottie import st_lottie
import requests as rqs

# === PAGE SETUP ===
st.set_page_config(page_title="DevSentry", layout="wide", page_icon="🛠️")

# === LOTTIE ANIMATION ===
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
    </style>
""", unsafe_allow_html=True)

# === HEADER ===
st.markdown('<div class="title">DevSentry</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-Powered Error Triage & Auto-Fix Assistant</div>', unsafe_allow_html=True)
st_lottie(lottie_bot, height=180, key="bot")

# === DEMO BUTTON ===
if "demo_loaded" not in st.session_state:
    st.session_state.demo_loaded = False

if st.button("🔁 Load Demo Error"):
    st.session_state.code = "def divide(x, y):\n    return x / y\n\nresult = divide(1, 0)"
    st.session_state.stack = "ZeroDivisionError: division by zero\nFile \"main.py\", line 2, in divide"
    st.session_state.lang = "Python"
    st.session_state.demo_loaded = True

# === FORM ===
st.subheader("🔍 Paste Error Details")

code_input = st.text_area("Paste the Code Causing Error", value=st.session_state.get("code", ""))
stack_input = st.text_area("Paste the Stack Trace", value=st.session_state.get("stack", ""))
lang_input = st.selectbox("Select Language", ["Python", "JavaScript", "Java", "C++"], 
                          index=["Python", "JavaScript", "Java", "C++"].index(st.session_state.get("lang", "Python")))

if st.button("Analyze"):
    with st.spinner("Analyzing error..."):
        try:
            res = requests.post("http://localhost:8000/analyze", json={
                "error_message": code_input,
                "stack_trace": stack_input,
                "language": lang_input
            })
            res.raise_for_status()
            result = res.json()
            st.success("Analysis completed.")
            st.json(result)
        except Exception as e:
            st.error(f"Analysis failed: {e}")