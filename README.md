# RAG Flask API for Geospatial Technology

A Retrieval-Augmented Generation (RAG) system built with Flask that answers questions about geospatial technology using PDF documents as knowledge base.

## 🚀 Features

- **Document Retrieval**: Find relevant content from PDF documents
- **AI Generation**: Generate answers using Groq/Mixtral LLM
- **Comparative Analysis**: Compare different geospatial technologies
- **Vector Search**: Powered by Qdrant vector database
- **RESTful API**: Easy-to-use endpoints for different query modes

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Vector Database**: Qdrant Cloud
- **Embeddings**: FastEmbed
- **LLM**: Groq (Mixtral-8x7b-32768)
- **Document Processing**: LangChain, PyPDF

## 📋 Prerequisites

- Python 3.8+
- Qdrant Cloud account
- Groq API key

## 🔧 Installation

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/rag-flask-api.git
cd rag-flask-api
```

2. **Create virtual environment**:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**:
Create a `.env` file:
```env
QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_api_key
GROQ_API_KEY=your_groq_api_key
COLLECTION_NAME=geospatial_docs
DEBUG=True
```

5. **Ingest documents**:
```bash
python ingest_data.py
```

6. **Run the application**:
```bash
python app.py
```

## 🌐 API Endpoints

### Main Query Endpoint
```http
POST /api/query
Content-Type: application/json

{
  "mode": "retrieval|generation|comparative",
  "query": "Your question here"
}
```

### Direct Endpoints
- `POST /api/retrieval/retrieve` - Document retrieval
- `POST /api/generation/generate` - Text generation
- `POST /api/comparative/compare` - Comparative analysis

## 💡 Usage Examples

### Retrieval Mode
```bash
curl -X POST http://localhost:5000/api/query \
  -H "Content-Type: application/json" \
  -d '{"mode": "retrieval", "query": "What is GIS?"}'
```

### Generation Mode
```bash
curl -X POST http://localhost:5000/api/query \
  -H "Content-Type: application/json" \
  -d '{"mode": "generation", "query": "Explain GIS technology"}'
```

### Comparative Mode
```bash
curl -X POST http://localhost:5000/api/query \
  -H "Content-Type: application/json" \
  -d '{"mode": "comparative", "query": "Compare GIS and GPS"}'
```

## 📁 Project Structure

```
rag-flask-api/
├── api/
│   ├── __init__.py
│   ├── retrieval.py          # Document retrieval logic
│   ├── generation.py         # AI text generation
│   ├── comparative_analysis.py  # Comparative analysis
│   └── common.py            # Shared utilities
├── data/                    # PDF documents
├── app.py                   # Main Flask application
├── config.py               # Configuration settings
├── ingest_data.py          # Data ingestion script
├── requirements.txt        # Python dependencies
└── .env                    # Environment variables (not in repo)
```

## 🔑 Environment Setup

1. **Qdrant Cloud**: Sign up at https://cloud.qdrant.io
2. **Groq API**: Get free API key at https://console.groq.com
3. **Add your API keys** to `.env` file

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

For questions or issues, please open an issue on GitHub.