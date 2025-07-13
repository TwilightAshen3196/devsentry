import streamlit as st
import requests
import time
from app.utils import render_xrd_chart, generate_pdf_report

st.set_page_config(page_title="StructSentry", layout="wide", page_icon="🧪")

st.session_state.setdefault("pattern", "")
st.session_state.setdefault("notes", "")
st.session_state.setdefault("language", "english")

# === HEADER ===
st.markdown('<h1 style="text-align:center;">🧪 StructSentry</h1>', unsafe_allow_html=True)
st.markdown('<h3 style="text-align:center; color:gray;">AI-Powered XRD Decoder with GitHub Integration</h3>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("### 📥 Submit XRD Pattern")

if st.button("🎯 Try Demo"):
    st.session_state["pattern"] = "20, 100\n30, 20\n40, 80\n50, 40\n60, 10"
    st.session_state["notes"] = "Sample is aluminum-based. Peaks around 40 suggest FCC."
    st.session_state["language"] = "english"

pattern = st.text_area("📈 XRD Pattern", height=200, value=st.session_state["pattern"])
notes = st.text_area("🗒️ Additional Notes", height=100, value=st.session_state["notes"])

lang_options = ["english", "urdu", "french", "german"]
lang_default = st.session_state.get("language") or "english"
language = st.selectbox("🌐 Output Language", lang_options, index=lang_options.index(lang_default))
st.session_state["language"] = language

structure = recommendation = github_issues = None

if st.button("🔍 Analyze Structure", use_container_width=True):
    with st.spinner("Analyzing using Gemini..."):
        try:
            response = requests.post(
                "http://localhost:8000/analyze",
                data={"xrd_pattern": pattern, "notes": notes, "language": language}
            )
            result = response.json()
            structure = result.get("structure")
            recommendation = result.get("recommendation")
            github_issues = result.get("github_issues", [])
        except Exception as e:
            st.error(f"API error: {e}")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🔬 Structure Analysis")
        if structure:
            st.markdown(f"""
            - **Structure:** {structure.get("structure", "N/A")}
            - **Confidence:** {structure.get("confidence", "N/A")}
            - **Justification:** {structure.get("justification", "N/A")}
            """)
        else:
            st.warning("No structure identified.")

    with col2:
        st.markdown("### 📦 Recommendation")
        if recommendation:
            st.markdown(recommendation)
        else:
            st.warning("No recommendation returned.")

    if github_issues:
        st.markdown("### 🔎 Related GitHub Issues")
        for issue in github_issues:
            if "error" in issue:
                st.error(issue["error"])
            else:
                st.markdown(f"- [{issue['title']}]({issue['url']})")

if st.button("📉 Visualize Pattern"):
    render_xrd_chart()

if structure and recommendation:
    st.markdown("### 📄 PDF Report")
    generate_pdf_report(structure, recommendation)

st.markdown("---")
st.markdown("#### 🙋 Feedback")
col1, col2 = st.columns(2)
with col1:
    st.button("👍 Yes", use_container_width=True)
with col2:
    st.button("👎 No", use_container_width=True)