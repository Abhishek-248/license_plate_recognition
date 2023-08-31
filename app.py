from flask import Flask, render_template, request
import os
from deeplearning import OCR
# webserver gateway interface
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        upload_file = request.files['image_name']
        filename = upload_file.filename
        upload_file.save('static/upload')
        text = OCR('static/upload', filename)

        return render_template('index.html', upload=True, upload_image=filename, text=text)

    return render_template('index.html', upload=False)


if __name__ == "__main__":
    app.run(debug=True)