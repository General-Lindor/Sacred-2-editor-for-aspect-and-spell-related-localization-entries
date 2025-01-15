from typing import Self
from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import ttk

class Section(ABC, tk.Frame):
    def __init__(self, master, dataStructure: dict | list, text: str, child):
        super(Section, self).__init__(master = master, highlightbackground = "black", highlightthickness = 1, padx = 5, pady = 5)

        self.dataStructure = dataStructure
        self.child = child

        self.choices = []
        self.current = tk.StringVar(master = self)
        self.properties = {}

        self.label = tk.Label(master = self, text = text)
        self.menu = ttk.Combobox(master = self, state = "disabled", textvariable = self.current, values = self.choices)

        self.current.trace_add("write", self.onChangeCurrent)
        self.label.grid(row = 0, column = 0, sticky = "w")
        self.menu.grid(row = 0, column = 1, sticky = "w")
    
    @abstractmethod
    def onChangeCurrent(self, *args, **kwargs):
        """
            Here implement the code block to update the properties.
            It must call the super method AFTERwards.
        """
        if isinstance(self.child, Section):
            self.child.updateDataStructure(self.properties)
            if (self.current.get() in self.choices):
                self.child.menu["state"] = "readonly"
            else:
                self.child.menu["state"] = "disabled"
    
    @abstractmethod
    def updateChoices(self):
        """
            Here implement the code block to update the choices.
            This method will be called from the reset method which itself is called by the update method.
            It must call the super method AFTERwards.
        """
        self.menu["values"] = self.choices

    @abstractmethod
    def updateDataStructure(self, newParentProperties: dict):
        """
            Here implement the code block to update the datastructure from a parent's properties.
            It must call the super method AFTERwards.
        """
        self.updateChoices()
        self.menu["values"] = self.choices
        if (self.current.get() in self.choices):
            self.onChangeCurrent() # self.current didn't change absolutely, but it did change relatively to self.choices because self.choices changed
        else:
            self.current.set("")

class SectionDict(Section, ABC):
    def __init__(self, master, text: str, dataStructure: dict | None = None, child: Section | None = None):
        if isinstance(dataStructure, dict):
            super(SectionDict, self).__init__(master, dataStructure, text, child)
        else:
            super(SectionDict, self).__init__(master, {}, text, child)
    
    def onChangeCurrent(self, *args, **kwargs):
        propertiesTest = self.dataStructure.get(self.current.get()) # type: ignore
        self.properties.clear()
        if isinstance(propertiesTest, dict):
            self.properties.update(propertiesTest)
        super(SectionDict, self).onChangeCurrent()
    
    def updateChoices(self):
        self.choices = list(self.dataStructure.keys()) # type: ignore
        super(SectionDict, self).updateChoices()

class SectionList(Section, ABC):
    def __init__(self, master, nameKey: str, text: str, dataStructure: list | None = None, child: Section | None = None):
        if isinstance(dataStructure, dict):
            super(SectionList, self).__init__(master, dataStructure, text, child)
        else:
            super(SectionList, self).__init__(master, [], text, child)
        self.nameKey = nameKey
        self.choiceDict = {}
    
    def onChangeCurrent(self, *args, **kwargs):
        self.properties.clear()
        currentChoiceIndexTest = self.choiceDict.get(self.current.get())
        if isinstance(currentChoiceIndexTest, int):
            try:
                self.properties.update(self.dataStructure[currentChoiceIndexTest])
            except IndexError as e:
                pass
        super(SectionList, self).onChangeCurrent()
    
    def updateChoices(self):
        self.choiceDict.clear()
        choiceIndex = 0
        for choiceObject in self.dataStructure:
            if isinstance(choiceObject, dict):
                choiceEntry = choiceObject.get(self.nameKey) # choiceEntry is a properties dict and name is a property
                if isinstance(choiceEntry, dict):
                    choice = choiceEntry.get("VALUE")
                    if isinstance(choice, str):
                        self.choiceDict[choice] = choiceIndex
            choiceIndex += 1
        self.choices = list(self.choiceDict.keys())
        super(SectionList, self).updateChoices()