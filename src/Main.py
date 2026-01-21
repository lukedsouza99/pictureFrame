from flask import Flask, request, render_template, redirect, url_for
from ImageProcessingService import ImageProcessingService

ImageProcessingService = ImageProcessingService()


app = Flask(__name__)



@app.route('/')
def index():
   return render_template("FileUpload.html")


@app.route('/', methods=['POST'])
def upload_file():
    file = request.files['file']
    ImageProcessingService.processImage(file)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0')

