import streamlit as st
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted
from google.generativeai import GenerativeModel

# Configure Streamlit page
st.set_page_config(
    page_title="Chatbot using Google",
    page_icon=":brain:",
    layout="centered"
)


GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")


def translate_role_for_streamlit(user_role):
    return "assistant" if user_role == "model" else user_role


if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])


st.title("Chandrika's Chatbot")


for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)


user_prompt = st.chat_input("Ask Chandrika's bot...")


if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    try:
        gemini_response = st.session_state.chat_session.send_message(user_prompt)
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)  
    except ResourceExhausted:
        st.error(" Quota exceeded. Please wait or upgrade your plan.")
    except Exception as e:
        st.error(f"Unexpected error: {e}")
