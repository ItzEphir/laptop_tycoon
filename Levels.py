class Levels:
    def __init__(self):
        self.maxWidth = 1
        self.maxHeight = 1
        self.maxWidthScreen = 1
        self.maxHeightScreen = 1

    def refresh(self):
        self.originalMaxWidth = self.maxWidth
        self.originalMaxHeight = 1
        self.originalMaxWidthScreen = 1
        self.originalMaxHeightScreen = 1
