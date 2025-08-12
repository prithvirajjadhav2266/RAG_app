from flask import Flask, jsonify, request
from api.retrieval import retrieval_blueprint, retriever
from api.generation import generation_blueprint
from api.comparative_analysis import comparative_blueprint
from api.common import run_chain, get_prompt_template, format_docs
from config import config

app = Flask(__name__)
app.config.from_object(config)

# Register the blueprints
app.register_blueprint(retrieval_blueprint, url_prefix="/api/retrieval")
app.register_blueprint(generation_blueprint, url_prefix="/api/generation")
app.register_blueprint(comparative_blueprint, url_prefix="/api/comparative")

@app.route('/')
def home():
    return jsonify({
        "message": "RAG Flask API is running!",
        "endpoints": {
            "query": "/api/query",
            "retrieval": "/api/retrieval/*",
            "generation": "/api/generation/*",
            "comparative": "/api/comparative/*"
        }
    })

@app.route('/api/query', methods=['POST'])
def query():
    """
    Route to handle user choice between retrieval-only, generalized query modes, comparative analysis, and formatted retrieval.
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400

        mode = data.get("mode", "retrieval").lower()
        query_text = data.get("query", "What is the purpose of this document?")

        if mode == "retrieval":
            # Get more documents for better context
            results = retriever.get_relevant_documents(query_text, k=10)  # Increase number of results
            serialized_results = [{"page_content": doc.page_content, "metadata": doc.metadata} for doc in results]
            return jsonify({
                "mode": mode, 
                "query": query_text, 
                "results": serialized_results,
                "total_results": len(serialized_results)
            })

        elif mode == "generation":
            # Direct function call instead of test_client
            docs = retriever.get_relevant_documents(query_text, k=8)  # Get more context
            context = format_docs(docs)
            
            prompt_template = get_prompt_template("generation")
            inputs = {"context": context, "question": query_text}
            
            response = run_chain(prompt_template, inputs)
            
            return jsonify({
                "mode": mode,
                "query": query_text,
                "response": response,
                "sources_used": len(docs)
            })
        
        elif mode == "comparative":
            # Direct function call instead of test_client
            docs = retriever.get_relevant_documents(query_text, k=8)  # Get more context
            context = format_docs(docs)
            
            prompt_template = get_prompt_template("comparative")
            inputs = {"context": context, "comparison_query": query_text}
            
            response = run_chain(prompt_template, inputs)
            
            return jsonify({
                "mode": mode,
                "query": query_text,
                "response": response,
                "sources_used": len(docs)
            })
        else:
            return jsonify({"error": "Invalid mode selected. Choose 'retrieval', 'generation', or 'comparative'."}), 400
            
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=config.DEBUG, host='0.0.0.0', port=5000)