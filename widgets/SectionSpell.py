from widgets.Section import SectionList
from widgets.Entry import Entry

class SectionSpell(SectionList):
    def __init__(self, master):
        super(SectionSpell, self).__init__(master = master, nameKey = "SPELLNAME", text = "Choose a spell: ")

        self.entry_spell_0 = Entry(self, self.properties, "SPELLNAME", 1, 1)
        self.entry_spell_1 = Entry(self, self.properties, "PROPERTY1", 2, 1)
        self.entry_spell_2 = Entry(self, self.properties, "PROPERTY2", 3, 1)
        self.entry_spell_3 = Entry(self, self.properties, "PROPERTY3", 4, 1)
        self.entry_spell_4 = Entry(self, self.properties, "PROPERTY4", 5, 1)
        self.entry_spell_5 = Entry(self, self.properties, "MOD1A", 6, 1)
        self.entry_spell_6 = Entry(self, self.properties, "MOD1B", 7, 1)
        self.entry_spell_7 = Entry(self, self.properties, "MOD2A", 8, 1)
        self.entry_spell_8 = Entry(self, self.properties, "MOD2B", 9, 1)
        self.entry_spell_9 = Entry(self, self.properties, "MOD3A", 10, 1)
        self.entry_spell_10 = Entry(self, self.properties, "MOD3B", 11, 1)
    
    def updateDataStructure(self, newParentProperties: dict):
        dataStructureTest = newParentProperties.get("SPELLS")
        if isinstance(dataStructureTest, list):
            self.dataStructure = dataStructureTest
        else:
            self.dataStructure = []
        super(SectionSpell, self).updateDataStructure(newParentProperties)
    
    def onChangeCurrent(self, *args, **kwargs):
        super().onChangeCurrent(*args, **kwargs)
        self.entry_spell_0.updateContent(self.properties)
        self.entry_spell_1.updateContent(self.properties)
        self.entry_spell_2.updateContent(self.properties)
        self.entry_spell_3.updateContent(self.properties)
        self.entry_spell_4.updateContent(self.properties)
        self.entry_spell_5.updateContent(self.properties)
        self.entry_spell_6.updateContent(self.properties)
        self.entry_spell_7.updateContent(self.properties)
        self.entry_spell_8.updateContent(self.properties)
        self.entry_spell_9.updateContent(self.properties)
        self.entry_spell_10.updateContent(self.properties)