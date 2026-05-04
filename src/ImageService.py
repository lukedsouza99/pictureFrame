from PIL import Image

class ImageService:

    PATH = "../resources/picture/picture.png"

    def __init__(self):
        pass


    def save(self, image):
        image.save(self.PATH)

    
    def load(self):
        return Image.open(self.PATH)