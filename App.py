import tkinter as tk
from tkinter import ttk
from typing import Callable, Iterable, Self

import os
import re
import json

#bd = BoundDict("test.json")
#print(bd)
#bd[4] = "xd"
#print(bd)
#bd.save()
#print(bd)

class TraceableList(list):
    def __init__(self, *args, **kwargs) -> None:
        super(TraceableList, self).__init__(self, *args, **kwargs)
        self._onChangeList = []
    
    def trace_add(self, func: Callable[[list], None]):
        self._onChangeList.append(func)
    
    def __setitem__(self, key, value) -> None:
        super(TraceableList, self).__setitem__(key, value)
        for func in self._onChangeList:
            func(self)
    
    def replace(self, newList: dict) -> None:
        self.clear()
        for item in newList:
            self.append(item)
        for func in self._onChangeList:
            func(self)

class TraceableDict(dict):
    _instances = {}
    def __init__(self, *args, **kwargs) -> None:
        super(TraceableDict, self).__init__(self, *args, **kwargs)
        self.__set__("_onChangeList",  [])
    
    def __set__(self, obj, value) -> None:
        d = TraceableDict._instances.get(self)
        if d == None:
            d = {}
            TraceableDict._instances[self] = d
        d[obj] = value
    
    def __get__(self, obj):
        d = TraceableDict._instances.get(self)
        if d == None:
            return None
        return d.get(obj)
    
    def __hash__(self) -> int:
        h = 0
        i = 1
        for item in self.items():
            h += (hash(item[0]) + hash(item[1])) * i
            i *= 7817
        h = h % 4294967296
        return h
    
    def trace_add(self, func: Callable):
        self.__get__("_onChangeList").append(func)
    
    def __setattr__(self, key, value) -> None:
        try:
            super(TraceableDict, self).__setitem__(key, value)
            for func in self.__get__("_onChangeList"):
                func(self)
        except Exception as e:
            print(e)
    
    def __setitem__(self, key, value) -> None:
        try:
            super(TraceableDict, self).__setitem__(key, value)
            for func in self.__get__("_onChangeList"):
                func(self)
        except Exception as e:
            print(e)
    
    def replace(self, newDict: dict) -> None:
        self.clear()
        for item in newDict.items():
            self[item[0]] = item[1]
        for func in self.__get__("_onChangeList"):
            func(self)

class BoundDict(TraceableDict):
    def __init__(self, filepath: str | None = None) -> None:
        self.path = ""
        if filepath != None:
            self.resolvePath(filepath)
            with open(self.path, "r", encoding = "utf-8") as file:
                file = "\n".join(file)
                super(BoundDict, self).__init__(json.loads(str(file)))
        else:
            super(BoundDict, self).__init__()
    
    def resolvePath(self, filepath: str):
        base = os.path.abspath(__file__)
        base = re.split("\\\\", base)
        base.pop(len(base) - 1)
        for partialString in base:
            if partialString != "":
                self.path += partialString + "/"
        self.path += filepath
    
    def save(self) -> None:
        with open(self.path, "w", encoding = "utf-8") as file:
            json.dump(self, file, indent = 4)
    
    def changeFilepath(self, newFilepath):
        self.resolvePath(newFilepath)
        newDict = BoundDict(self.path)
        self.replace(newDict)

class Entry(tk.Frame):
    def __init__(self, master, content, key):
        pass

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        # LANGUAGE
        self.languages = ["de_DE", "en_EN"]
        self.currentLanguage = tk.StringVar(master)
        self.currentLanguage.trace_add("write", self.onChangeCurrentLanguage)
        self.languageMenu = ttk.Combobox(self, textvariable = self.currentLanguage, values = self.languages)
        self.languageMenu.pack()

        # HERO
        self.heroDict = BoundDict()
        self.heroDict.trace_add(self.onChangeHeroDict)
        self.currentHero = tk.StringVar(master)
        self.currentHero.trace_add("write", self.onChangeCurrentHero)
        self.heroMenu = ttk.Combobox(self, textvariable = self.currentHero, values = list(self.heroDict.keys()))
        self.heroMenu.pack()

        # ASPECT
        self.aspectDict = TraceableDict()
        self.aspectDict.trace_add(self.onChangeAspectDict)
        self.currentAspect = tk.StringVar(master)
        self.currentAspect.trace_add("write", self.onChangeCurrentAspect)
        self.aspectMenu = ttk.Combobox(self, textvariable = self.currentLanguage, values = list(self.aspectDict.keys()))
        self.aspectMenu.pack()

        # SPELL
        self.spellDict = TraceableDict()
        self.spellDict.trace_add(self.onChangeSpellDict)
        self.currentSpell = tk.StringVar(master)
        self.currentSpell.trace_add("write", self.onChangeCurrentSpell)
        self.spellMenu = ttk.Combobox(self, textvariable = self.currentLanguage, values = list(self.spellDict.keys()))
        self.spellMenu.pack()

        self.contents = tk.StringVar()
        self.entrythingy = tk.Entry(textvariable = self.contents)
        self.entrythingy.pack()
        self.contents.set("this is a variable")
        self.entrythingy.bind('<Key-Return>', self.print_contents)
    
    def onChangeCurrentLanguage(self, var, index, mode):
        current = self.currentLanguage.get()
        self.heroDict.changeFilepath("RES_MODIFIED/" + current + "/res.json")
    
    def onChangeHeroDict(self):
        newAspectDict: dict | None = self.heroDict.get(self.currentHero.get())
        if newAspectDict == None:
            newAspectDict = {}
        self.aspectDict.replace(newAspectDict)
        self.heroMenu['values'] = list(self.heroDict.keys())
    
    def onChangeCurrentHero(self, var, index, mode):
        currentHero = self.currentHero.get()
        newAspectDict = self.heroDict.get(currentHero)
        if type(newAspectDict) != dict:
            newAspectDict = {}
        self.aspectDict.replace(newAspectDict)
    
    def onChangeAspectDict(self):
        newSpellDict: dict | None = self.aspectDict.get(self.currentAspect.get())
        if newSpellDict == None:
            newSpellDict = {}
        self.spellDict.replace(newSpellDict)
        self.aspectMenu['values'] = list(self.aspectDict.keys())
    
    def onChangeCurrentAspect(self, var, index, mode):
        currentAspect = self.currentAspect.get()
        newSpellDict = self.aspectDict.get(currentAspect)
        if type(newSpellDict) != dict:
            newSpellDict = {}
        self.spellDict.replace(newSpellDict)
    
    def onChangeSpellDict(self):
        self.spellMenu['values'] = list(self.spellDict.keys())
    
    def onChangeCurrentSpell(self, var, index, mode):
        pass

    '''
    def update_option_menu(self, optionsMenu, value, newList):
        menu = optionsMenu["menu"]
        menu.delete(0, "end")
        for string in newList:
            menu.add_command(label=string, command=lambda val=string: value.set(val))
    '''

    def print_contents(self, event):
        print("Hi. The current entry content is:", self.contents.get())

root = tk.Tk()
myapp = App(root)
myapp.mainloop()
