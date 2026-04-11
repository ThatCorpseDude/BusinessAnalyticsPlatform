import streamlit as st
import requests

# Backend URL
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Consulting Assistant")

st.title("AI Consulting Assistant")


# Dropdown menu
option = st.selectbox(
    "Select a tool",
    [
        "Analyze Requirements",
        "Recommend Architecture",
        "Migrate Code"
    ]
)


# User input
user_input = st.text_area("Enter your input here")


# Button
if st.button("Run"):
    if not user_input.strip():
        st.warning("Please enter some input")
    else:
        if option == "Analyze Requirements":
            endpoint = "/analyze"
        elif option == "Recommend Architecture":
            endpoint = "/recommend"
        else:
            endpoint = "/migrate"

        try:
            response = requests.post(
                f"{API_URL}{endpoint}",
                json={"text": user_input}
            )

            if response.status_code == 200:
                result = response.json().get("result", "")
                st.subheader("Result")
                st.write(result)
            else:
                st.error("Error from backend")

        except Exception as e:
            st.error(f"Could not connect to backend: {e}")