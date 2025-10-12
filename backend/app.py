from flask import Flask, request, jsonify
import subprocess
from extractor import extract_text_from_file
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Extract text from the document
    text = extract_text_from_file(file_path)

    # Run Node.js script with Puter.js
    result = subprocess.run(
        ["node", "run_puter.js", text],
        capture_output=True,
        text=True
    )

    return jsonify({"response": result.stdout})

if __name__ == '__main__':
    app.run(debug=True)
