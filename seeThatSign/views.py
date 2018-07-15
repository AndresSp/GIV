import os
from flask import flash, send_from_directory, render_template, request
from werkzeug import secure_filename, exceptions
from werkzeug.exceptions import HTTPException
from seeThatSign import app

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['UPLOAD_FOLDER']='./uploads'

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    upload = None
    if request.method == 'POST':
        try:
            f = request.files['file']
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            upload = 'Upload Succesfully'
        except HTTPException: ##Upload Fails
            upload = 'Upload a file'
    return render_template('index.html',upload=upload)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/generated', methods = ['GET'])
def getGeneratedImages():
    return 'Generated Images'