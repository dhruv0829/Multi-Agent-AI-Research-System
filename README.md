<div align="center">

# 🧠 ResearchMind

### Autonomous Multi-Agent AI Research Assistant

Build research reports using a collaborative team of AI agents powered by LangChain, LangGraph, Mistral AI, Tavily Search, and Streamlit.

---

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![LangChain](https://img.shields.io/badge/LangChain-Agentic-green?style=for-the-badge)
![LangGraph](https://img.shields.io/badge/LangGraph-MultiAgent-orange?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-red?style=for-the-badge&logo=streamlit)
![Mistral AI](https://img.shields.io/badge/Mistral-AI-black?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

</div>

---

# 🚀 Homepage

![Homepage](assets/homepage.png)

---

# 📖 Project Overview

ResearchMind is an **Autonomous Multi-Agent Research System** that performs real-time web research using multiple specialized AI agents working together.

Instead of relying on a single Large Language Model, ResearchMind divides the task into multiple intelligent agents.

Each agent has a specialized responsibility, making the research pipeline modular, scalable, and production-oriented.

---

# ⚡ Features

✅ Live Internet Research

✅ Multi-Agent Architecture

✅ Autonomous Web Scraping

✅ AI Generated Research Reports

✅ AI Critic & Report Evaluation

✅ Download Reports

✅ Modular LangChain Architecture

✅ Production Ready Streamlit UI

---

# 🏗 Architecture

```
              User
                │
                ▼
        Search Agent
                │
                ▼
        Reader Agent
                │
                ▼
        Writer Chain
                │
                ▼
        Critic Chain
                │
                ▼
         Final Research Report
```

---

# 🤖 AI Pipeline

| Agent | Responsibility |
|--------|---------------|
| 🔍 Search Agent | Searches the latest information using Tavily |
| 📄 Reader Agent | Scrapes webpages using BeautifulSoup |
| ✍ Writer Chain | Generates a professional research report |
| 🧐 Critic Chain | Reviews and scores the generated report |

---

# ⚙ Tech Stack

- Python
- LangChain
- LangGraph
- LCEL (Runnable Pipelines)
- Mistral AI
- Tavily Search API
- BeautifulSoup
- Streamlit

---

# 📸 Pipeline

![Pipeline](assets/pipeline.png)

---

# 📄 Generated Report

![Report](assets/report.png)

---

# 🧐 AI Critic Feedback

![Critic](assets/critic.png)

---

# 📂 Project Structure

```
ResearchMind/

│── assets/
│── app.py
│── agents.py
│── pipeline.py
│── tools.py
│── requirements.txt
│── README.md
│── .gitignore
│── .env (not included)
```

---

# 💻 Installation

Clone the repository

```bash
git clone https://github.com/dhruv0829/Multi-Agent-AI-Research-System.git
```

Go inside the project

```bash
cd Multi-Agent-AI-Research-System
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env`

```env
MISTRAL_API_KEY=YOUR_KEY
TAVILY_API_KEY=YOUR_KEY
```

Run

```bash
streamlit run app.py
```

---

# 🔮 Future Improvements

- PDF Export
- Citation Generator
- Multi-LLM Support
- Memory
- RAG Integration
- Agent Monitoring Dashboard
- Report Versioning
- Authentication

---

# 🤝 Contributing

Contributions are welcome.

Feel free to fork this repository and submit a Pull Request.

---

# ⭐ Support

If you found this project useful,

⭐ Star this repository.

---

<div align="center">

Made with ❤️ by **Dhruv**

</div>