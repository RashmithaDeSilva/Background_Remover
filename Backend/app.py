from flask import Flask, request, send_file
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)


# Configuration for file upload
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/api/uploadimage', methods=['POST'])
def background_remover():
    if request.methods == POST:
        # Check if the POST request has the file part
        if 'file' not in request.files:
            return 'No file part'

    return 'Hello, World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
