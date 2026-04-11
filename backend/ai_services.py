import requests

# Local Ollama API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"


def ask_llm(prompt: str) -> str:
    """
    Sends a prompt to the local LLM (Ollama) and returns the response.
    """
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "mistral",   # or "llama3"
            "prompt": prompt,
            "stream": False
        }
    )

    if response.status_code != 200:
        return "Error: Unable to reach AI model"

    return response.json().get("response", "")


# -------------------------------
# Feature 1: Requirements Analysis
# -------------------------------
def analyze_requirements(text: str) -> str:
    prompt = f"""
    You are a software consultant.

    Extract the following from the input:
    - Functional requirements
    - Non-functional requirements
    - Risks

    Input:
    {text}
    """

    return ask_llm(prompt)


# -------------------------------
# Feature 2: Architecture Recommendation
# -------------------------------
def recommend_architecture(use_case: str) -> str:
    prompt = f"""
    You are a cloud architect.

    Suggest a system architecture using free or open-source tools.

    Include:
    - Backend
    - Frontend
    - Database
    - Deployment approach

    Use case:
    {use_case}
    """

    return ask_llm(prompt)


# -------------------------------
# Feature 3: Code Migration
# -------------------------------
def migrate_code(code: str) -> str:
    prompt = f"""
    You are a senior software engineer.

    Convert the following code into clean Python.
    Improve readability and structure.

    Code:
    {code}
    """

    return ask_llm(prompt)