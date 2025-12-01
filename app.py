import streamlit as st

st.title("NLP Harmful Prompt Classifier")
st.write("Upload text and get predictions")

text = st.text_area("Enter a comment")

if st.button("Predict"):
    st.write("Prediction will appear here")
