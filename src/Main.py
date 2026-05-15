from flask import Flask, request, render_template, redirect, url_for
from ImageProcessingService import ImageProcessingService
from EpdService import EPD
from ImageService import ImageService
from StartUpService import StartUpService

startUpService = StartUpService()
startUpService.setUp()
ImageProcessingService = ImageProcessingService()
imageService = ImageService()
epdService = EPD()
epdService.init()
# check if file exists
epdService.display(epdService.getbuffer(imageService.load()))


app = Flask(__name__)



@app.route('/')
def index():
   return render_template("FileUpload.html")


@app.route('/', methods=['POST'])
def upload_file():
    if request.form.get('clear') == 'Clear':
        epdService.Clear()
    else:
        file = request.files['file']
        processedImage = ImageProcessingService.processImage(file)
        imageService.save(processedImage)
        print(processedImage)
        epdService.display(epdService.getbuffer(imageService.load()))
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0')

