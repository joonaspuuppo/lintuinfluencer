class Tweet:
    text = ""
    time = ""
    img = ""

    def _init_(self):
        return

    def __init__(self, text, time):
        self.text = text
        self.time = time

    def _init_(self, text):
        text = text

    def getText(self):
        return self.text

    def getTime(self):
        return self.time

