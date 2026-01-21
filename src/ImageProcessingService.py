from PIL import Image



class ImageProcessingService:


    def __init__(self):
        pass


    def processImage(self, unprocessedImage):
        # resize / rotate depending on height and width
        image = Image.open(unprocessedImage)
        resizedImage = image.resize((100,100))
        return resizedImage