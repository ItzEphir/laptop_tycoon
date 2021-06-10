class Levels:
    def __init__(self):
        self.maxWidth = 1
        self.maxHeight = 1
        self.maxWidthScreen = 1
        self.maxHeightScreen = 1

    def refresh(self):
        self.originalMaxWidth = self.maxWidth
        self.originalMaxHeight = self.maxHeight
        self.originalMaxWidthScreen = self.maxWidthScreen
        self.originalMaxHeightScreen = self.maxHeightScreen