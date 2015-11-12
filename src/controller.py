class Controller:
    def __init__(self):
        self.pathList = []
        self.run = False
    def addPath(self, path):
        self.pathList.append(path)
    def getPaths(self):
        return self.pathList
    def run(self):
        self.run = True
        #while HERE
