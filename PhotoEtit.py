from PIL import Image, ImageDraw


class Photo:
    def __init__(self, name):
        self.image = Image.open(name)
        self.draw = ImageDraw.Draw(self.image)
        self.width = self.image.size[0]
        self.height = self.image.size[1]
        self.pix = self.image.load()