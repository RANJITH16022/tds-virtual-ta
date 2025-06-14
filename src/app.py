from flask import Flask, request, jsonify
import base64
import os
from process_data import answer_question

app = Flask(__name__)

@app.route('/api/', methods=['POST'])
def handle_question():
    data = request.get_json()
    if not data or 'question' not in data:
        return jsonify({"error": "Missing question"}), 400

    question = data['question']
    image = data.get('image', None)
    image_path = None

    if image:
        try:
            image_data = base64.b64decode(image)
            image_path = 'temp_image.webp'
            with open(image_path, 'wb') as f:
                f.write(image_data)
        except:
            return jsonify({"error": "Invalid image"}), 400

    answer, links = answer_question(question, image_path)

    if image_path and os.path.exists(image_path):
        os.remove(image_path)

    return jsonify({"answer": answer, "links": links}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
    