# chatbot
chatgpt for finding answers for our queries

# Chandrika's Chatbot

Chandrika's Chatbot is a simple yet powerful conversational AI application built with Streamlit and powered by Google's Gemini 1.5 Pro model. It provides an interactive chat interface where users can ask questions and receive intelligent responses.

## Features

* **Interactive Chat Interface**: A user-friendly chat window for seamless conversations.
* **Google Gemini 1.5 Pro**: Leverages the latest Gemini model for high-quality, relevant responses.
* **Streamlit Powered**: Built with Streamlit for easy deployment and a beautiful UI.
* **API Key Management**: Securely handles your Google API key using Streamlit's `secrets` management.

## Getting Started

Follow these steps to set up and run Chandrika's Chatbot locally.

### Prerequisites

Before you begin, ensure you have the following:

* **Python 3.7+**: [Download Python](https://www.python.org/downloads/)
* **Google API Key**: You'll need an API key from the Google AI Studio. If you don't have one, you can get it [here](https://aistudio.google.com/app/apikey).

### Installation

1.  **Clone the Repository (or create the files manually):**
    If you're creating a new repository, you'll copy the code into your `app.py` file. If you're cloning:
    ```bash
    git clone <your-repository-url>
    cd <your-repository-name>
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure your Google API Key:**
    Streamlit applications use a `secrets.toml` file to manage sensitive information like API keys. Create a folder named `.streamlit` in the root directory of your project, and inside it, create a file named `secrets.toml`.

    Your project structure should look like this:
    ```
    your-project-name/
    ├── .streamlit/
    │   └── secrets.toml
    ├── chatbot_app.py
    ├── requirements.txt
    └── README.md
    ```

    Open `.streamlit/secrets.toml` and add your Google API key:
    ```toml
    GOOGLE_API_KEY="YOUR_API_KEY_HERE"
    ```
    **Replace `YOUR_API_KEY_HERE` with your actual Google API key.**

### Running the Application

Once everything is set up, run the Streamlit application from your terminal:

```bash
streamlit run chatbot_app.py
