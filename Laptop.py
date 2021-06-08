class Laptop:
    def __init__(self, name):
        self.name = name
        self.price = 50
        self.salePrice = int(self.price * 1.3)
        self.width = 600
        self.height = 300
        self.originalWidth = self.width
        self.originalHeight = self.height
        self.depth = 24
        self.widthScreen = 540
        self.heightScreen = 270
        self.originalWidthScreen = self.widthScreen
        self.originalHeightScreen = self.heightScreen
        self.resolutionX = 1366
        self.resolutionY = 768
        self.color = (40, 40, 40)
        self.colorNumber = 7
        self.screenTech = "TN"
        self.markFirst = 0
        self.mark = 0


    def countMark(self):
        self.markFirst += self.width / 60
        self.markFirst += self.height / 30
        self.markFirst += self.widthScreen / 54
        self.markFirst += self.heightScreen / 27
        if self.screenTech == "VA":
            self.markFirst += 100
        elif self.screenTech == "IPS":
            self.markFirst += 290
        elif self.screenTech == "OLED":
            self.markFirst += 280
        self.mark = self.markFirst / self.price
