import sys
from pathlib import Path
import streamlit as st
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from src.factuality import evaluate_pair

st.set_page_config(page_title="AI Factuality Evaluator",layout="wide")
st.title("AI Hallucination & Factuality Evaluator")
st.warning("Screening aid only: text similarity cannot establish truth. Verify important claims against trusted sources.")
reference=st.text_area("Reference answer",height=150)
answer=st.text_area("AI-generated answer",height=150)
if st.button("Evaluate"):
    if not reference.strip() or not answer.strip():
        st.error("Please provide both answers.")
    else:
        r=evaluate_pair(reference,answer)
        a,b,c=st.columns(3)
        a.metric("Support score",f"{r['support_score']:.2f}")
        b.metric("Similarity",f"{r['similarity']:.2f}")
        c.metric("Lexical overlap",f"{r['lexical_overlap']:.2f}")
        st.subheader("Assessment signal")
        st.write(r["label"])
        if r["contradiction_signal"]:
            st.error("Potential contradiction detected; verify against a trusted source.")
