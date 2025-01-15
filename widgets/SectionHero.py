from widgets.Section import SectionDict
from widgets.SectionAspect import SectionAspect
from widgets.Entry import Entry

class SectionHero(SectionDict):
    def __init__(self, master, child: SectionAspect):
        super(SectionHero, self).__init__(master = master, text = "Choose a hero: ", child = child)

        self.entry_hero_0 = Entry(self, self.properties, "DESC_GOOD", 1, 1)
        self.entry_hero_1 = Entry(self, self.properties, "DESC_BAD", 2, 1)

    def updateDataStructure(self, newParentProperties: dict):
        self.dataStructure.clear()
        self.dataStructure.update(newParentProperties) # type: ignore
        super(SectionHero, self).updateDataStructure(newParentProperties)
    
    def onChangeCurrent(self, *args, **kwargs):
        super().onChangeCurrent(*args, **kwargs)
        self.entry_hero_0.updateContent(self.properties)
        self.entry_hero_1.updateContent(self.properties)