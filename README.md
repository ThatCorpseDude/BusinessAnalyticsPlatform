# AI Consulting Assistant (Free and Open Source)
## Overview

AI Consulting Assistant is a full-stack application that simulates real consulting workflows using AI-driven insights. It allows users to analyze business requirements, generate system architecture recommendations, and modernize legacy code using a fully free and open-source technology stack.

This project demonstrates practical experience in application engineering, AI integration, and full-stack development.
Please note that the title of the project does not accurately convey its purpose. This project initially used azure but I thought it would be more helpful to try it with a non-paid option

## Features

### Requirements Analyzer

Extracts functional and non-functional requirements from input text
Identifies risks and assumptions

### Architecture Recommender

Suggests cloud-native architectures
Recommends backend, frontend, and database technologies

### Code Migration Tool

Converts legacy code (e.g., Java, .NET) into Python
Improves readability and structure

### AI Copilot (Local)

Provides development assistance using a locally hosted language model
Works without paid APIs or external dependencies

### Tech Stack

Backend: FastAPI (Python) Frontend: Streamlit
AI Engine: Ollama (Mistral or LLaMA3) 
Database: SQLite 
Vector Store: FAISS 
Deployment: Render, Railway, or local environment

### Project Structure
```
BusinessAnalyticsPlatform/
│
├── backend/
│   ├── main.py
│   ├── ai_service.py
│   ├── routes.py
│
├── frontend/
│   └── app.py
│
├── requirements.txt
├── README.md
└── .gitignore
```
## Setup Instructions

Clone the repository
```
git clone https://github.com/ThatCorpseDude/BusinessAnalyticsPlatform.git

cd ai-consulting-assistant
```


Install dependencies
```
pip install -r requirements.txt
Install and run Ollama
curl -fsSL https://ollama.com/install.sh | sh
ollama run mistral
```
Ensure Ollama is running before starting the backend.

Start the backend
```
uvicorn backend.main:app --reload

```
Start the frontend
```
streamlit run frontend/app.py

```

Example Use Case

Input: A company wants to migrate a legacy .NET monolithic application to a scalable cloud-based system.

Output:

Structured requirements
Suggested architecture (e.g., microservices)
Migration approach and recommendations
Deployment

This project can be deployed using free-tier platforms such as Render or Railway. It can also be run locally for demonstration purposes.

Resume Description

Developed an AI-powered consulting assistant using FastAPI and locally hosted language models to support requirement analysis, architecture design, and legacy system migration using a fully open-source stack.

Future Improvements
Authentication and user management
Dashboard and analytics features
Document export (PDF or PowerPoint)
Retrieval-augmented generation (RAG)
Public deployment of frontend
Contributing

Contributions are welcome. Please fork the repository and submit a pull request for review.

License

This project is licensed under the MIT License.

Author

ThatCorpseDude (AKA Ahmed H. Elkady)
