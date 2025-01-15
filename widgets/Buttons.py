import tkinter as tk
from tkinter import Tk
from widgets.SectionLanguage import SectionLanguage
from scripts.Utils import BoundDict, reset
from scripts.Export import export

class Buttons(tk.Frame):
    def __init__(self, master, root: Tk, content: dict, sectionLanguage: SectionLanguage):
        super(Buttons, self).__init__(master, highlightbackground = "black", highlightthickness = 1, padx = 5, pady = 5)

        self.root = root
        self.content = content
        self.sectionLanguage = sectionLanguage

        self.labelButton = tk.Label(self, text = " ")
        self.labelButton.grid(row = 0, column = 0, sticky = "w")
        self.buttonFrame = tk.Frame(self)
        self.buttonFrame.grid(row = 1, column = 0, sticky = "w")

        self.buttonSaveCurrent = tk.Button(self.buttonFrame, text ="Save current language", command = self.saveCurrentLanguage)
        self.buttonSaveCurrent.grid(row = 0, column = 0, sticky = "w")

        self.buttonSaveAll = tk.Button(self.buttonFrame, text ="Save all languages", command = self.saveAll)
        self.buttonSaveAll.grid(row = 0, column = 1, sticky = "w")

        self.buttonExportCurrent = tk.Button(self.buttonFrame, text ="Export current language", command = self.exportCurrentLanguage)
        self.buttonExportCurrent.grid(row = 1, column = 0, sticky = "w")

        self.buttonExportAll = tk.Button(self.buttonFrame, text ="Export all languages", command = self.exportAll)
        self.buttonExportAll.grid(row = 1, column = 1, sticky = "w")

        self.buttonResetCurrent = tk.Button(self.buttonFrame, text ="Reset current language to MODIFIED", command = self.resetCurrentToMODIFIED)
        self.buttonResetCurrent.grid(row = 2, column = 0, sticky = "w")

        self.buttonResetAll = tk.Button(self.buttonFrame, text ="Reset all languages to MODIFIED", command = self.resetAllToMODIFIED)
        self.buttonResetAll.grid(row = 2, column = 1, sticky = "w")

        self.buttonResetCurrent = tk.Button(self.buttonFrame, text ="Reset current language to BASE", command = self.resetCurrentToBASE)
        self.buttonResetCurrent.grid(row = 3, column = 0, sticky = "w")

        self.buttonResetAll = tk.Button(self.buttonFrame, text ="Reset all languages to BASE", command = self.resetAllToBASE)
        self.buttonResetAll.grid(row = 3, column = 1, sticky = "w")

        self.buttonExit = tk.Button(self.buttonFrame, text ="Exit", command = self.exit)
        self.buttonExit.grid(row = 4, column = 0, sticky = "w")
    
    def display(self, text):
        self.labelButton["text"] = text
    
    def displayTimed(self, text):
        self.display(text)
        self.root.after(5000, self.display, " ")
    
    def saveCurrentLanguage(self):
        self.display("Saving...")
        d = self.content.get(self.sectionLanguage.current.get())
        if isinstance(d, BoundDict):
            d.save()
            self.displayTimed("Successfully saved current language!")
        else:
            self.displayTimed("No valid language selected!")
    
    def saveAll(self):
        self.display("Saving...")
        for d in self.content.values():
            if isinstance(d, BoundDict):
                d.save()
        self.displayTimed("Successfully saved all languages!")
    
    def exportCurrentLanguage(self):
        self.display("Exporting...")
        l = self.sectionLanguage.current.get()
        d = self.content.get(l)
        if isinstance(l, str) and isinstance(d, BoundDict):
            export(d, l)
            self.displayTimed("Successfully exported current language!")
        else:
            self.displayTimed("No valid language selected!")
    
    def exportAll(self):
        self.display("Exporting...")
        for item in self.content.items():
            l = item[0]
            d = item[1]
            if isinstance(l, str) and isinstance(d, BoundDict):
                export(d, l)
        self.displayTimed("Successfully exported all languages!")
    
    def resetCurrentToMODIFIED(self):
        self.display("Resetting...")
        l = self.sectionLanguage.current.get()
        d = self.content.get(l)
        if isinstance(d, BoundDict):
            d.load()
            self.sectionLanguage.onChangeCurrent()
            self.displayTimed("Successfully reset current language to MODIFIED!")
        else:
            self.displayTimed("No valid language selected!")
    
    def resetAllToMODIFIED(self):
        self.display("Resetting...")
        for item in self.content.items():
            l = item[0]
            d = item[1]
            if isinstance(l, str) and isinstance(d, BoundDict):
                d.load()
        self.sectionLanguage.onChangeCurrent()
        self.displayTimed("Successfully reset all languages to MODIFIED!")
    
    def resetCurrentToBASE(self):
        self.display("Resetting...")
        l = self.sectionLanguage.current.get()
        d = self.content.get(l)
        if isinstance(d, BoundDict):
            reset(l, d)
            self.sectionLanguage.onChangeCurrent()
            self.displayTimed("Successfully reset current language to MODIFIED!")
        else:
            self.displayTimed("No valid language selected!")
    
    def resetAllToBASE(self):
        self.display("Resetting...")
        for item in self.content.items():
            l = item[0]
            d = item[1]
            if isinstance(l, str) and isinstance(d, BoundDict):
                reset(l, d)
        self.sectionLanguage.onChangeCurrent()
        self.displayTimed("Successfully reset all languages to BASE!")
    
    def exit(self):
        self.root.destroy()