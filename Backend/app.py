from flask import Flask, request, send_file
from br_client.main import removeImageBackgound

app = Flask(__name__)

# Configuration for file upload
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/api/uploadimage', methods=['POST'])
def background_remover():
    # Check method
    if request.method == "POST":
        # Check file
        if 'file' not in request.files:
            return 'No image found!', 404
        
        # Check file type
        if not allowed_file(request.files['file'].filename):
            return 'Invalid image extension!', 400
        
        # Remove image background and save image
        file_save_path = str('./imagers/' + str(request.files['file'].filename).split(".")[-2].split("/")[-1] + '-output.png')
        removeImageBackgound(request.files['file']).save(file_save_path, 'PNG')

        return send_file(file_save_path, mimetype='image/jpeg')

    return 'Invalid method!', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
