from widgets.Section import SectionList
from widgets.SectionSpell import SectionSpell
from widgets.Entry import Entry

class SectionAspect(SectionList):
    def __init__(self, master, child: SectionSpell):
        super(SectionAspect, self).__init__(master = master, nameKey = "ASPECTNAME", text = "Choose an aspect: ", child = child)

        self.entry_aspect_0 = Entry(self, self.properties, "ASPECTNAME", 1, 1)
        self.entry_aspect_1 = Entry(self, self.properties, "LORE_NAME", 2, 1)
        self.entry_aspect_2 = Entry(self, self.properties, "LORE_DESCRIPTION", 3, 1)
        self.entry_aspect_3 = Entry(self, self.properties, "LORE_MASTERY_NAME", 4, 1)
        self.entry_aspect_4 = Entry(self, self.properties, "LORE_MASTERY_ATMO_SHORT", 5, 1)
        self.entry_aspect_5 = Entry(self, self.properties, "LORE_MASTERY_ATMO_LONG", 6, 1)
        self.entry_aspect_6 = Entry(self, self.properties, "LORE_PROPERTIES_1", 7, 1)
        self.entry_aspect_7 = Entry(self, self.properties, "LORE_PROPERTIES_2", 8, 1)
        self.entry_aspect_8 = Entry(self, self.properties, "LORE_PROPERTIES_3", 9, 1)
        self.entry_aspect_9 = Entry(self, self.properties, "LORE_PROPERTIES_MASTERY", 10, 1)
        self.entry_aspect_10 = Entry(self, self.properties, "FOCUS_NAME", 11, 1)
        self.entry_aspect_11 = Entry(self, self.properties, "FOCUS_DESCRIPTION", 12, 1)
        self.entry_aspect_12 = Entry(self, self.properties, "FOCUS_MASTERY_NAME", 13, 1)
        self.entry_aspect_13 = Entry(self, self.properties, "FOCUS_MASTERY_ATMO_SHORT", 14, 1)
        self.entry_aspect_14 = Entry(self, self.properties, "FOCUS_MASTERY_ATMO_LONG", 15, 1)
        self.entry_aspect_15 = Entry(self, self.properties, "FOCUS_PROPERTIES_1", 16, 1)
        self.entry_aspect_16 = Entry(self, self.properties, "FOCUS_PROPERTIES_2", 17, 1)
        self.entry_aspect_17 = Entry(self, self.properties, "FOCUS_PROPERTIES_3", 18, 1)
        self.entry_aspect_18 = Entry(self, self.properties, "FOCUS_PROPERTIES_MASTERY", 19, 1)
    
    def updateDataStructure(self, newParentProperties: dict):
        dataStructureTest = newParentProperties.get("ASPECTS")
        if isinstance(dataStructureTest, list):
            self.dataStructure = dataStructureTest
        else:
            self.dataStructure = []
        super(SectionAspect, self).updateDataStructure(newParentProperties)
    
    def onChangeCurrent(self, *args, **kwargs):
        super().onChangeCurrent(*args, **kwargs)
        self.entry_aspect_0.updateContent(self.properties)
        self.entry_aspect_1.updateContent(self.properties)
        self.entry_aspect_2.updateContent(self.properties)
        self.entry_aspect_3.updateContent(self.properties)
        self.entry_aspect_4.updateContent(self.properties)
        self.entry_aspect_5.updateContent(self.properties)
        self.entry_aspect_6.updateContent(self.properties)
        self.entry_aspect_7.updateContent(self.properties)
        self.entry_aspect_8.updateContent(self.properties)
        self.entry_aspect_9.updateContent(self.properties)
        self.entry_aspect_10.updateContent(self.properties)
        self.entry_aspect_11.updateContent(self.properties)
        self.entry_aspect_12.updateContent(self.properties)
        self.entry_aspect_13.updateContent(self.properties)
        self.entry_aspect_14.updateContent(self.properties)
        self.entry_aspect_15.updateContent(self.properties)
        self.entry_aspect_16.updateContent(self.properties)
        self.entry_aspect_17.updateContent(self.properties)
        self.entry_aspect_18.updateContent(self.properties)