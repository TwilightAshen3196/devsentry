import matplotlib.pyplot as plt
import streamlit as st
from fpdf import FPDF
import tempfile

def render_xrd_chart():
    # Dummy data for demonstration
    x = [20, 30, 40, 50, 60]
    y = [100, 20, 80, 40, 10]

    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o')
    ax.set_title("XRD Pattern")
    ax.set_xlabel("Angle (2θ)")
    ax.set_ylabel("Intensity")

    st.pyplot(fig)

def generate_pdf_report(structure: dict, recommendation: str):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="XRD Analysis Report", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 10, f"Structure: {structure.get('structure', 'N/A')}")
    pdf.multi_cell(0, 10, f"Confidence: {structure.get('confidence', 'N/A')}")
    pdf.multi_cell(0, 10, f"Justification: {structure.get('justification', 'N/A')}")
    pdf.ln(5)
    pdf.multi_cell(0, 10, f"Recommendation: {recommendation}")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        pdf.output(tmp.name)
        st.download_button(
            label="Download Report as PDF",
            data=open(tmp.name, "rb").read(),
            file_name="XRD_Report.pdf",
            mime="application/pdf"
        )