from scripts import __basepath__
import json
import shutil

class BoundDict(dict):
    def __init__(self, filepath: str | None = None) -> None:
        if filepath != None:
            self.path = __basepath__ + filepath
            with open(self.path, "r", encoding = "utf-8") as file:
                file = "\n".join(file)
                super(BoundDict, self).__init__(json.loads(str(file)))
        else:
            super(BoundDict, self).__init__()
    
    def load(self):
        with open(self.path, "r", encoding = "utf-8") as file:
            file = "\n".join(file)
            super(BoundDict, self).clear()
            super(BoundDict, self).update(json.loads(str(file)))
    
    def save(self) -> None:
        with open(self.path, "w", encoding = "utf-8") as file:
            json.dump(self, file, indent = 4)
    
    def updateFilepath(self, newFilepath: str):
        self.path = __basepath__ + newFilepath
        self.load()

def reset(lang: str, d: BoundDict):
    pathResBase = __basepath__ + "ressources/BASE/"
    pathResMod = __basepath__ + "ressources/MODIFIED/"

    pathResBaseLang = pathResBase + lang + "/res.json"
    pathResModLang = pathResMod + lang + "/res.json"

    shutil.copy(pathResBaseLang, pathResModLang)
    d.load()