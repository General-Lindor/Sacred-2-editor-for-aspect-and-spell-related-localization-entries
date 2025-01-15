from widgets.Section import SectionDict
from widgets.SectionHero import SectionHero

class SectionLanguage(SectionDict):
    def __init__(self, master, content: dict, child: SectionHero):
        super(SectionLanguage, self).__init__(master = master, text = "Choose a language: ", dataStructure = content, child = child)
        self.updateChoices()
        self.menu["state"] = "readonly"
    
    def updateDataStructure(self, newParentProperties: dict):
        self.dataStructure.clear()
        self.dataStructure.update(newParentProperties) # type: ignore
        super(SectionLanguage, self).updateDataStructure(newParentProperties)