from flask import Flask, request, render_template, redirect, url_for
from ImageProcessingService import ImageProcessingService
from EpdService import EPD

ImageProcessingService = ImageProcessingService()
epdService = EPD()
epdService.init()
epdService.Clear()


app = Flask(__name__)



@app.route('/')
def index():
   return render_template("FileUpload.html")


@app.route('/', methods=['POST'])
def upload_file():
    file = request.files['file']
    processedImage = ImageProcessingService.processImage(file)
    print(processedImage)
    epdService.display(epdService.getbuffer(processedImage))
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0')

