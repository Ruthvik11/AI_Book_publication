import streamlit as st
import os


def load_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "File not found."


def save_final_edit(text):
    with open("data/chapter_final.txt", "w", encoding="utf-8") as f:
        f.write(text)

st.set_page_config(page_title="AI Book Workflow", layout="wide")

st.title(" Automated Book Publication: Human-in-the-Loop")

col1, col2 = st.columns(2)


with col1:
    st.subheader(" Original Chapter")
    original_text = load_file("data/chapter1.txt")
    st.text_area("Original Chapter", original_text, height=300, disabled=True)

    st.subheader(" AI-Written Chapter (Editable)")
    ai_text = load_file("data/chapter_spun.txt")
    ai_written_edit = st.text_area("AI Written Output", ai_text, height=300)


with col2:
    st.subheader("AI Reviewer Feedback")
    review_text = load_file("data/chapter_review.txt")
    st.text_area("AI Review", review_text, height=300, disabled=True)

    st.subheader(" Human Editor Final Version")
    human_edit = st.text_area("Your Edited Version", ai_written_edit, height=300)

    if st.button("Save Final Version"):
        save_final_edit(human_edit)
        st.success(" Final version saved to data/chapter_final.txt!")
