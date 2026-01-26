from PIL import Image, ImageEnhance



class ImageProcessingService:


    def __init__(self):
        pass


    def processImage(self, unprocessedImage):
        # resize / rotate depending on height and width
        image = Image.open(unprocessedImage)
        width, height = image.size
        if (height > width):
            image = image.rotate(270, expand=True)
        resizedImage = image.resize((800,480))
        enhancer = ImageEnhance.Contrast(resizedImage)
        return enhancer.enhance(2)