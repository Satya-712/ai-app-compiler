import streamlit as st
import requests
import json

st.title("AI App Compiler")

prompt = st.text_area("Enter your app idea")

if st.button("Generate"):

    response = requests.post(
        "http://127.0.0.1:8000/generate",
        json={"prompt": prompt}
    )

    result = response.json()

    parsed = json.loads(result["result"])

    st.subheader("Generated Configuration")

    st.json(parsed)

    json_data = json.dumps(parsed, indent=2)

    st.download_button(
        label="Download JSON",
        data=json_data,
        file_name="app_config.json",
        mime="application/json"
    )