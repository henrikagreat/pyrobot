class ButtonEvent():
    def __init__(self, action, name):
        self.action = action
        self.name = name
    
    def getAction(self):
        return self.action
    
    def getName(self):
        return self.name
