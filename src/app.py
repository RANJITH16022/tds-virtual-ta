from flask import Flask, request, jsonify
from flask_cors import CORS
from src.process_data import answer_question
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Virtual TA is running!"

@app.route("/api/", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question")
    image = data.get("image_path")  # Optional

    if not question:
        return jsonify({"error": "Question is required."}), 400

    answer, links = answer_question(question, image_path=image)
    return jsonify({"answer": answer, "links": links})

if __name__ == "__main__":
    app.run(debug=True)
