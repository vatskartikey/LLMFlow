from flask import Flask, request, jsonify, send_from_directory
import subprocess
from extractor import extract_text_from_file
import os
import tempfile

app = Flask(__name__, static_folder="../client", static_url_path="/")
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return send_from_directory('../client', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('../client', path)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    text = extract_text_from_file(file)
    
    # Fake AI output
    response = f"Analysis of {file.filename}:\nSink: line 12\nSource: line 5\nSanitizer: line 20"
    
    return jsonify({"response": response})


if __name__ == '__main__':
    app.run(debug=True)
