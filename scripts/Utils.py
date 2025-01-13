
from scripts import __basepath__
import json

class BoundDict(dict):
    def __init__(self, filepath: str | None = None) -> None:
        if filepath != None:
            self.setFilepath(filepath)
        else:
            super(BoundDict, self).__init__()
    
    def load(self):
        with open(self.path, "r", encoding = "utf-8") as file:
            file = "\n".join(file)
            self.clear()
            super(BoundDict, self).__init__(json.loads(str(file)))
    
    def save(self) -> None:
        with open(self.path, "w", encoding = "utf-8") as file:
            json.dump(self, file, indent = 4)
    
    def setFilepath(self, filepath: str):
        self.path = __basepath__ + filepath
        self.load()