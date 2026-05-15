
# 🛡️ Brand Guardian

> **An AI-powered compliance pipeline that audits micro-influencer video content for brand safety and sentiment using Azure Video Indexer and Multimodal LLMs.**

Brand Guardian acts as an automated internal tool to scale organic marketing campaigns. It programmatically ingests unstructured creator videos, analyzes them for brand alignment, and outputs structured compliance metadata—completely eliminating the need for manual video reviews.

---

## ✨ Key Features
* **Automated Video Auditing:** Integrates with Azure Video Indexer to scan high-volume creator content.
* **Compliance & Safety Checks:** Uses Multimodal LLMs to score visual and audio sentiment against strict brand guidelines.
* **Agentic QA Pipeline:** Built with a graph-based workflow for cross-verified, hallucination-free auditing.
* **Structured Data Output:** Converts unstructured video streams into clean, actionable JSON metadata.
* **Full Observability:** Integrated with LangSmith and Azure Application Insights for real-time monitoring.

## 🛠️ Tech Stack
* **Language:** Python 3.13
* **API Framework:** FastAPI / Uvicorn
* **Package Manager:** `uv`
* **Cloud & AI:** Azure Video Indexer, Azure AI Services
* **Database:** OpenSearch (Vector Database)
* **Telemetry:** LangSmith, Azure Monitor Opentelemetry

---

## 🚀 Getting Started

### Prerequisites
Make sure you have the following installed:
* [Python 3.13+](https://www.python.org/downloads/)
* [`uv`](https://github.com/astral-sh/uv) (for lightning-fast dependency management)
* Git

### 1. Clone the Repository

git clone [https://github.com/YOUR_USERNAME/Brand-Guardian.git](https://github.com/YOUR_USERNAME/Brand-Guardian.git)
cd Brand-Guardian/complianceqapipeline

### 2. Environment Variables
Create a .env file in the root directory and add your secret keys. (Never commit this file to GitHub!)

Code snippet
# Azure Storage
AZURE_STORAGE_ACCOUNT_ACCESS_KEY=your_key_here

# Azure AI & Search Services
AZURE_AI_SERVICES_KEY=your_key_here
AZURE_SEARCH_ADMIN_KEY=your_key_here

# LangSmith Telemetry
LANGCHAIN_API_KEY=your_langsmith_pat_here
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=Brand-Guardian

### 3. Install Dependencies
Using uv, you can quickly sync and lock your environment:

Bash
uv sync

### 4. Run the Application
Start the local API server with live reloading:

Bash
uv run uvicorn backend.src.api.server:app --reload
The server will start at: http://127.0.0.1:8000


# 📂 Project Structure

complianceqapipeline/
├── backend/
│   ├── data/                  # Reference documents and guidelines
│   ├── scripts/               # Ingestion and database indexing scripts
│   ├── src/
│   │   ├── api/               # FastAPI server and telemetry setup
│   │   ├── graph/             # Workflow states, nodes, and routing logic
│   │   └── services/          # External API integrations (Azure Video Indexer)
│   └── tests/                 # Unit and integration tests
├── .env                       # Local secrets (ignored by Git)
├── .gitignore                 # Git ignore rules
├── pyproject.toml             # Python dependencies and project metadata
├── uv.lock                    # Dependency lockfile
└── README.md                  # Project documentation

# 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.
