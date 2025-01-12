import tkinter as tk
from tkinter import ttk
from typing import Callable
#import tkinter.font as tkfont

import os
import re
import json

class TraceableList(list):
    def __init__(self, *args, **kwargs) -> None:
        super(TraceableList, self).__init__(self, *args, **kwargs)
        self._onChangeList = []
    
    def trace_add(self, func: Callable):
        self._onChangeList.append(func)
    
    #def __setitem__(self, key, value) -> None:
    #    super(TraceableList, self).__setitem__(key, value)
    #    for func in self._onChangeList:
    #        func()
    
    def __set__(self, newList: list) -> None:
        self.clear()
        for item in newList:
            self.append(item)
        for func in self._onChangeList:
            func()

class TraceableDict(dict):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._onChangeList = []
    
    def trace_add(self, func: Callable):
        self._onChangeList.append(func)
    
    #def __setitem__(self, key, value) -> None:
    #    super(TraceableDict, self).__setitem__(key, value)
    #    for func in self._onChangeList:
    #        func()

    def __set__(self, newDict: dict) -> None:
        self.clear()
        for item in newDict.items():
            self[item[0]] = item[1]
        for func in self._onChangeList:
            func()

class BoundDict(dict):
    def __init__(self, filepath: str | None = None) -> None:
        if filepath != None:
            self.resolvePath(filepath)
            print(self.path)
            with open(self.path, "r", encoding = "utf-8") as file:
                file = "\n".join(file)
                super(BoundDict, self).__init__(json.loads(str(file)))
        else:
            super(BoundDict, self).__init__()
    
    def resolvePath(self, filepath: str):
        #print("RESOLVING", filepath)
        self.path = ""
        base = os.path.abspath(__file__)
        base = re.split("\\\\", base)
        base.pop(len(base) - 1)
        for partialString in base:
            if partialString != "":
                self.path += partialString + "/"
        self.path += filepath
        #print("DONE", self.path)
    
    def save(self) -> None:
        with open(self.path, "w", encoding = "utf-8") as file:
            json.dump(self, file, indent = 4)
    
    def changeFilepath(self, newFilepath: str):
        self.resolvePath(newFilepath)
        newDict = BoundDict(newFilepath)
        self.replace(newDict)

class Entry():
    def __init__(self, master, content: dict, key: str, row: int, column: int):
        
        self.content = content
        self.key = key
        #self.font = tkfont.Font(family="Helvetica", size=8, weight="normal")
        
        self.textLength = 0
        self.value = tk.StringVar(master = master)
        #self.value.trace_add("write", self.onWrite)
        self.value.trace_add("write", self.updateWidth)
        
        self.label = tk.Label(master = master, text = key)
        self.label.grid(row = row, column = column, sticky = "w")

        self.entry = tk.Entry(master = master, textvariable = self.value, font = "Helvetica 10 normal")
        self.entry.grid(row = row, column = column + 1, sticky = "w")

        self.update()
    
    def onWrite(self, *args, **kwargs):
        pass
        #d = self.content.get(self.key)
        #print(d)
        #if not isinstance(d, dict):
        #    d = {}
        #d["VALUE"] = self.value.get()
        #print(d)
        #self.content[self.key] = d
    
    def updateWidth(self, *args, **kwargs):
        #pxWidth = self.font.measure(text = self.value.get())
        #avgWidth = self.font.measure("0")
        #width = round(pxWidth / avgWidth)
        width = len(self.value.get())
        self.entry["width"] = width
    
    def update(self):
        d = self.content.get(self.key)
        if isinstance(d, dict):
            s = d.get("VALUE")
            if isinstance(s, str):
                self.value.set(s)
                return
        self.value.set("")
    
    def updateContent(self, newContent: dict):
        self.content = newContent
        self.update()

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.content = {
            "de_DE" : BoundDict("RES_MODIFIED/de_DE/res.json"),
            "en_EN" : BoundDict("RES_MODIFIED/en_EN/res.json"),
        }

        # LANGUAGE
        self.languageChoices = list(self.content.keys())
        self.currentLanguage = tk.StringVar(master = self)
        self.currentLanguage.trace_add("write", self.onChangeCurrentLanguage)
        self.currentLanguageProperties = {}

        tk.Label(master = self, text="Choose a language: ").grid(row = 0, column = 0, sticky = "w")
        self.languageMenu = ttk.Combobox(master = self, textvariable = self.currentLanguage, values = self.languageChoices)
        self.languageMenu.grid(row = 0, column = 1)

        # HERO
        self.heroChoices = []
        self.currentHero = tk.StringVar(master = self)
        self.currentHero.trace_add("write", self.onChangeCurrentHero)
        self.currentHeroProperties = {}

        tk.Label(master = self, text="Choose a hero: ").grid(row = 1, column = 0, sticky = "w")
        self.heroMenu = ttk.Combobox(master = self, textvariable = self.currentHero, values = [])
        self.heroMenu.grid(row = 1, column = 1)

        self.entry_hero_0 = Entry(self, self.currentHeroProperties, "DESC_GOOD", 2, 1)
        self.entry_hero_1 = Entry(self, self.currentHeroProperties, "DESC_BAD", 3, 1)

        # ASPECT
        self.aspectChoices = {}
        self.currentAspect = tk.StringVar(master = self)
        self.currentAspect.trace_add("write", self.onChangeCurrentAspect)
        self.currentAspectProperties = {}

        tk.Label(master = self, text="Choose an aspect: ").grid(row = 4, column = 0, sticky = "w")
        self.aspectMenu = ttk.Combobox(master = self, textvariable = self.currentAspect, values = [])
        self.aspectMenu.grid(row = 4, column = 1)

        self.entry_aspect_0 = Entry(self, self.currentAspectProperties, "ASPECTNAME", 5, 1)
        self.entry_aspect_1 = Entry(self, self.currentAspectProperties, "LORE_NAME", 6, 1)
        self.entry_aspect_2 = Entry(self, self.currentAspectProperties, "LORE_DESCRIPTION", 7, 1)
        self.entry_aspect_3 = Entry(self, self.currentAspectProperties, "LORE_MASTERY_NAME", 8, 1)
        self.entry_aspect_4 = Entry(self, self.currentAspectProperties, "LORE_MASTERY_ATMO_SHORT", 9, 1)
        self.entry_aspect_5 = Entry(self, self.currentAspectProperties, "LORE_MASTERY_ATMO_LONG", 10, 1)
        self.entry_aspect_6 = Entry(self, self.currentAspectProperties, "LORE_PROPERTIES_1", 11, 1)
        self.entry_aspect_7 = Entry(self, self.currentAspectProperties, "LORE_PROPERTIES_2", 12, 1)
        self.entry_aspect_8 = Entry(self, self.currentAspectProperties, "LORE_PROPERTIES_3", 13, 1)
        self.entry_aspect_9 = Entry(self, self.currentAspectProperties, "LORE_PROPERTIES_MASTERY", 14, 1)
        self.entry_aspect_10 = Entry(self, self.currentAspectProperties, "FOCUS_NAME", 15, 1)
        self.entry_aspect_11 = Entry(self, self.currentAspectProperties, "FOCUS_DESCRIPTION", 16, 1)
        self.entry_aspect_12 = Entry(self, self.currentAspectProperties, "FOCUS_MASTERY_NAME", 17, 1)
        self.entry_aspect_13 = Entry(self, self.currentAspectProperties, "FOCUS_MASTERY_ATMO_SHORT", 18, 1)
        self.entry_aspect_14 = Entry(self, self.currentAspectProperties, "FOCUS_MASTERY_ATMO_LONG", 19, 1)
        self.entry_aspect_15 = Entry(self, self.currentAspectProperties, "FOCUS_PROPERTIES_1", 20, 1)
        self.entry_aspect_16 = Entry(self, self.currentAspectProperties, "FOCUS_PROPERTIES_2", 21, 1)
        self.entry_aspect_17 = Entry(self, self.currentAspectProperties, "FOCUS_PROPERTIES_3", 22, 1)
        self.entry_aspect_18 = Entry(self, self.currentAspectProperties, "FOCUS_PROPERTIES_MASTERY", 23, 1)

        # SPELL
        self.spellChoices = {}
        self.currentSpell = tk.StringVar(master = self)
        self.currentSpell.trace_add("write", self.onChangeCurrentSpell)
        self.currentSpellProperties = {}

        tk.Label(master = self, text="Choose a spell: ").grid(row = 24, column = 0, sticky = "w")
        self.spellMenu = ttk.Combobox(master = self, textvariable = self.currentSpell, values = [])
        self.spellMenu.grid(row = 24, column = 1)

        self.entry_spell_0 = Entry(self, self.currentSpellProperties, "SPELLNAME", 25, 1)
        self.entry_spell_1 = Entry(self, self.currentSpellProperties, "PROPERTY1", 26, 1)
        self.entry_spell_2 = Entry(self, self.currentSpellProperties, "PROPERTY2", 27, 1)
        self.entry_spell_3 = Entry(self, self.currentSpellProperties, "PROPERTY3", 28, 1)
        self.entry_spell_4 = Entry(self, self.currentSpellProperties, "PROPERTY4", 29, 1)
        self.entry_spell_5 = Entry(self, self.currentSpellProperties, "MOD1A", 30, 1)
        self.entry_spell_6 = Entry(self, self.currentSpellProperties, "MOD1B", 31, 1)
        self.entry_spell_7 = Entry(self, self.currentSpellProperties, "MOD2A", 32, 1)
        self.entry_spell_8 = Entry(self, self.currentSpellProperties, "MOD2B", 33, 1)
        self.entry_spell_9 = Entry(self, self.currentSpellProperties, "MOD3A", 34, 1)
        self.entry_spell_10 = Entry(self, self.currentSpellProperties, "MOD3B", 35, 1)
    
    def onChangeCurrentLanguage(self, *args, **kwargs):
        #print("onChangeCurrentLanguage")
        languagePropertiesTest = self.content.get(self.currentLanguage.get())
        if isinstance(languagePropertiesTest, dict):
            self.currentLanguageProperties = languagePropertiesTest
        else:
            self.currentLanguageProperties = {}
        self.resetHero()
    
    def onChangeCurrentHero(self, *args, **kwargs):
        #print("onChangeCurrentHero")
        heroPropertiesTest = self.currentLanguageProperties.get(self.currentHero.get())
        if isinstance(heroPropertiesTest, dict):
            self.currentHeroProperties = heroPropertiesTest
        else:
            self.currentHeroProperties = {}
        self.entry_hero_0.updateContent(self.currentHeroProperties)
        self.entry_hero_1.updateContent(self.currentHeroProperties)
        self.resetAspect()
    
    def onChangeCurrentAspect(self, *args, **kwargs):
        #print("onChangeCurrentAspect")
        self.currentAspectProperties = {}
        currentAspectIndexTest = self.aspectChoices.get(self.currentAspect.get())
        if isinstance(currentAspectIndexTest, int):
            if isinstance(self.currentHeroProperties, dict):
                aspectList = self.currentHeroProperties.get("ASPECTS")
                if isinstance(aspectList, list):
                    try:
                        self.currentAspectProperties = aspectList[currentAspectIndexTest]
                    except IndexError as e:
                        print(aspectList)
                        print(currentAspectIndexTest)
                        print(e)
        self.entry_aspect_0.updateContent(self.currentAspectProperties)
        self.entry_aspect_1.updateContent(self.currentAspectProperties)
        self.entry_aspect_2.updateContent(self.currentAspectProperties)
        self.entry_aspect_3.updateContent(self.currentAspectProperties)
        self.entry_aspect_4.updateContent(self.currentAspectProperties)
        self.entry_aspect_5.updateContent(self.currentAspectProperties)
        self.entry_aspect_6.updateContent(self.currentAspectProperties)
        self.entry_aspect_7.updateContent(self.currentAspectProperties)
        self.entry_aspect_8.updateContent(self.currentAspectProperties)
        self.entry_aspect_9.updateContent(self.currentAspectProperties)
        self.entry_aspect_10.updateContent(self.currentAspectProperties)
        self.entry_aspect_11.updateContent(self.currentAspectProperties)
        self.entry_aspect_12.updateContent(self.currentAspectProperties)
        self.entry_aspect_13.updateContent(self.currentAspectProperties)
        self.entry_aspect_14.updateContent(self.currentAspectProperties)
        self.entry_aspect_15.updateContent(self.currentAspectProperties)
        self.entry_aspect_16.updateContent(self.currentAspectProperties)
        self.entry_aspect_17.updateContent(self.currentAspectProperties)
        self.entry_aspect_18.updateContent(self.currentAspectProperties)
        self.resetSpell()
    
    def onChangeCurrentSpell(self, *args, **kwargs):
        #print("onChangeCurrentSpell")
        self.currentSpellProperties = {}
        currentSpellIndexTest = self.spellChoices.get(self.currentSpell.get())
        if isinstance(currentSpellIndexTest, int):
            if isinstance(self.currentAspectProperties, dict):
                spellList = self.currentAspectProperties.get("SPELLS")
                if isinstance(spellList, list):
                    try:
                        self.currentSpellProperties = spellList[currentSpellIndexTest]
                    except IndexError as e:
                        pass
        self.entry_spell_0.updateContent(self.currentSpellProperties)
        self.entry_spell_1.updateContent(self.currentSpellProperties)
        self.entry_spell_2.updateContent(self.currentSpellProperties)
        self.entry_spell_3.updateContent(self.currentSpellProperties)
        self.entry_spell_4.updateContent(self.currentSpellProperties)
        self.entry_spell_5.updateContent(self.currentSpellProperties)
        self.entry_spell_6.updateContent(self.currentSpellProperties)
        self.entry_spell_7.updateContent(self.currentSpellProperties)
        self.entry_spell_8.updateContent(self.currentSpellProperties)
        self.entry_spell_9.updateContent(self.currentSpellProperties)
        self.entry_spell_10.updateContent(self.currentSpellProperties)

    def resetHero(self):
        #print("resetHero")
        # heroChoices
        if isinstance(self.currentLanguageProperties, dict):
            self.heroChoices = list(self.currentLanguageProperties.keys())
        else:
            self.heroChoices = []
        # currentHero
        if not (self.currentHero.get() in self.heroChoices):
            self.currentHero.set("")
        else:
            self.onChangeCurrentHero()
        # Widgets
        self.heroMenu["values"] = self.heroChoices

    def resetAspect(self):
        #print("resetAspect")
        # aspectChoices
        aspectList = []
        if isinstance(self.currentHeroProperties, dict):
            aspectList = self.currentHeroProperties.get("ASPECTS")
        self.aspectChoices = {}
        if isinstance(aspectList, list):
            aspectIndex = 0
            for aspect in aspectList:
                aspectnameEntry = aspect.get("ASPECTNAME")
                print(aspectnameEntry)
                if isinstance(aspectnameEntry, dict):
                    aspectname = aspectnameEntry.get("VALUE")
                    if isinstance(aspectname, str):
                        self.aspectChoices[aspectname] = aspectIndex
                        print(aspectname, aspectIndex)
                else:
                    print(aspect)
                aspectIndex += 1
        # currentAspect
        if not (self.currentAspect.get() in self.aspectChoices.keys()):
            self.currentAspect.set("")
        else:
            self.onChangeCurrentAspect()
        # Widgets
        self.aspectMenu["values"] = list(self.aspectChoices.keys())
            
    def resetSpell(self):
        #print("resetSpell")
        # spellChoices
        spellList = []
        if isinstance(self.currentAspectProperties, dict):
            spellList = self.currentAspectProperties.get("SPELLS")
        self.spellChoices = {}
        if isinstance(spellList, list):
            spellIndex = 0
            for spell in spellList:
                spellnameEntry = spell.get("SPELLNAME")
                if isinstance(spellnameEntry, dict):
                    spellname = spellnameEntry.get("VALUE")
                    if isinstance(spellname, str):
                        self.spellChoices[spellname] = spellIndex
                spellIndex += 1
        # currentSpell
        if not (self.currentSpell.get() in self.spellChoices.keys()):
            self.currentSpell.set("")
        else:
            self.onChangeCurrentSpell()
        self.spellMenu["values"] = list(self.spellChoices.keys())

    '''
    def update_option_menu(self, optionsMenu, value, newList):
        menu = optionsMenu["menu"]
        menu.delete(0, "end")
        for string in newList:
            menu.add_command(label=string, command=lambda val=string: value.set(val))
    '''


root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
#root.geometry("500x500")

# main
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=1)

# tob
top_frame = tk.Frame(main_frame)
top_frame.pack(side="top", fill="both", expand=1)

# canvas
my_canvas = tk.Canvas(top_frame)
my_canvas.pack(side="left", fill="both", expand=1)

# scrollbar
scrollbarVertical = tk.Scrollbar(top_frame, orient="vertical", command=my_canvas.yview)
scrollbarVertical.pack(side="right", fill="y")
my_canvas.configure(yscrollcommand=scrollbarVertical.set)
my_canvas.bind(
    '<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all"))
)

scrollbarHorizontal = tk.Scrollbar(main_frame, orient="horizontal", command=my_canvas.xview)
scrollbarHorizontal.pack(side="bottom", fill="x")
my_canvas.configure(xscrollcommand=scrollbarHorizontal.set)
my_canvas.bind(
    '<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all"))
)



myApp = App(my_canvas)

my_canvas.create_window((0, 0), window=myApp, anchor="nw")
root.mainloop()
