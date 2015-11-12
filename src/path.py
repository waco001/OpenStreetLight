class Path:
    'Base class for path'
    def __init__(self, startDir, endDir):
        self.startDir   = startDir
        self.endDir     = endDir
    def getStartDir(self):
        return self.startDir
    def getEndDir(self):
        return self.endDir
