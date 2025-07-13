import streamlit as st
import requests
import json
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

# === CSS ===
st.markdown("""
    <style>
    .title { font-size: 3em; font-weight: 800; text-align: center; color: #FF4B4B; }
    .subtitle { font-size: 1.2em; text-align: center; color: #666; margin-bottom: 2em; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">DevSentry</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-Powered Error Triage & Auto-Fix Assistant</div>', unsafe_allow_html=True)
st_lottie(lottie_bot, height=180, key="bot")

# === DEMO PAYLOAD ===
demo_code = "def divide(x, y):\n    return x / y\n\nresult = divide(1, 0)"
demo_stack = "ZeroDivisionError: division by zero\nFile \"main.py\", line 2, in divide"
demo_lang = "Python"

if "code" not in st.session_state:
    st.session_state.code = ""
if "stack" not in st.session_state:
    st.session_state.stack = ""
if "lang" not in st.session_state:
    st.session_state.lang = "Python"

# === DEMO BUTTON ===
if st.button("🔁 Load Demo Error"):
    st.session_state.code = demo_code
    st.session_state.stack = demo_stack
    st.session_state.lang = demo_lang

# === FORM INPUT ===
st.subheader("🔍 Paste Error Details")

with st.form("error_form"):
    code_input = st.text_area("Paste the Code Causing Error", value=st.session_state.code)
    stack_input = st.text_area("Paste the Stack Trace", value=st.session_state.stack)
    lang_input = st.selectbox("Select Language", ["Python", "JavaScript", "Java", "C++"],
                              index=["Python", "JavaScript", "Java", "C++"].index(st.session_state.lang))

    submitted = st.form_submit_button("Analyze")

if submitted:
    with st.spinner("Analyzing error..."):
        try:
            res = requests.post("http://localhost:8000/analyze", json={
                "error_message": code_input,
                "stack_trace": stack_input,
                "language": lang_input
            })
            res.raise_for_status()
            result = res.json()

            st.success("Analysis Completed")

            # === CLASSIFICATION OUTPUT ===
            st.subheader("📍 Classification")
            classification = result.get("classification", {})
            st.markdown(f"- **Cause**: `{classification.get('cause', '-')}`")
            st.markdown(f"- **Component**: `{classification.get('component', '-')}`")
            st.markdown(f"- **Severity**: `{classification.get('severity', '-')}`")

            # === FIX SUGGESTION OUTPUT ===
            st.subheader("🛠 Fix Suggestion")
            fix = result.get("fix_suggestion", {})
            st.markdown(f"**Explanation:**\n\n{fix.get('explanation', '-')}")
            st.markdown(f"**Suggested Fix:**\n\n{fix.get('fix', '-')}")
            st.code(fix.get("code", ""), language=lang_input.lower())

        except Exception as e:
            st.error(f"Analysis failed: {e}")
