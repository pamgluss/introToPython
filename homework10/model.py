class Model:
    def __init__(self):
        self.temperature_ = 0
    def convertToFar(self):
        return ((9 * self.temperature_) / 5.0) +32
    def convertToCel(self):
        return (self.temperature_ - 32) * 5/9.0