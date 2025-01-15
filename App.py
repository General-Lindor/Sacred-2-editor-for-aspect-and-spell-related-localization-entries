import tkinter as tk
from tkinter import Tk, Widget, Event
from scripts.Utils import BoundDict
from widgets import SectionLanguage, SectionHero, SectionAspect, SectionSpell, Buttons

class App(tk.Frame):
    def __init__(self, root: Tk):
        super(App, self).__init__(root)
        self.root = root
        self.content = {
            "de_DE" : BoundDict("ressources/MODIFIED/de_DE/res.json"),
            "en_EN" : BoundDict("ressources/MODIFIED/en_EN/res.json"),
        }

        # create in reverse order
        self.sectionSpell = SectionSpell.SectionSpell(self)
        self.sectionAspect = SectionAspect.SectionAspect(self, self.sectionSpell)
        self.sectionHero = SectionHero.SectionHero(self, self.sectionAspect)
        self.sectionLanguage = SectionLanguage.SectionLanguage(self, self.content, self.sectionHero)

        # grid in forwards order
        self.sectionLanguage.grid(row = 0, column = 0, sticky = "nw", padx = 10, pady = 5)
        self.sectionHero.grid(row = 1, column = 0, sticky = "nw", padx = 10, pady = 5)
        self.sectionAspect.grid(row = 2, column = 0, sticky = "nw", padx = 10, pady = 5)
        self.sectionSpell.grid(row = 3, column = 0, sticky = "nw", padx = 10, pady = 5)

        # create and grid buttons
        self.Buttons = Buttons.Buttons(self, self.root, self.content, self.sectionLanguage)
        self.Buttons.grid(row = 4, column = 0, sticky = "nw", padx = 10, pady = 5)

class Window():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("Sacred 2 Aspects & Spells ressources Editor")

        #screen_width = root.winfo_screenwidth()
        #screen_height = root.winfo_screenheight()

        self.content = App(self.root)

        self.scrollbarVertical = tk.Scrollbar(self.root, orient = "vertical", command = self.onSrollY)
        self.scrollbarHorizontal = tk.Scrollbar(self.root, orient = "horizontal", command = self.onSrollX)

        self.scX: float = 0.0
        self.scY: float = 0.0
            
        self.root.update_idletasks()

        self.widthScrollBar:    float = self.scrollbarVertical.winfo_width()
        self.widthRoot:         float = self.root.winfo_width()
        self.widthContent:      float = self.content.winfo_width()
        self.widthEff:          float = self.widthRoot - self.widthScrollBar

        self.heightScrollBar:   float = self.scrollbarHorizontal.winfo_height()
        self.heightRoot:        float = self.root.winfo_height()
        self.heightContent:     float = self.content.winfo_height()
        self.heightEff:         float = self.heightRoot - self.heightScrollBar

        self.scW: float = self.widthEff / self.widthContent
        self.scH: float = self.heightEff / self.heightContent

        self.root.bind('<Configure>', self.onResizeRoot, add = False)
        self.content.bind('<Configure>', self.onResizeContent, add = False)
        self.scrollbarVertical.bind('<Configure>', self.onResizeScrollY, add = False)
        self.scrollbarHorizontal.bind('<Configure>', self.onResizeScrollX, add = False)
    
        self.placeWidgets()
    
    def onResizeContent(self, event: tk.Event | None, *args, **kwargs):
        if event == None:
            return
        if event.widget != self.content:
            return
        self.root.update_idletasks()
        self.widthContent = self.content.winfo_width()
        self.heightContent = self.content.winfo_height()
        self.scW = self.widthEff / self.widthContent
        self.scH = self.heightEff / self.heightContent
        self.placeWidgets()
    
    def onResizeRoot(self, event: tk.Event | None, *args, **kwargs):
        if event == None:
            return
        if event.widget != self.root:
            return
        self.root.update_idletasks()
        self.widthRoot = self.root.winfo_width()
        self.widthEff = self.widthRoot - self.widthScrollBar
        self.heightRoot = self.root.winfo_height()
        self.heightEff = self.heightRoot - self.heightScrollBar
        self.scW = self.widthEff / self.widthContent
        self.scH = self.heightEff / self.heightContent
        self.placeWidgets()
    
    def onResizeScrollX(self, event: tk.Event | None, *args, **kwargs):
        if event == None:
            return
        if event.widget != self.scrollbarHorizontal:
            return
        self.root.update_idletasks()
        self.heightScrollBar = self.scrollbarHorizontal.winfo_height()
        self.heightEff = self.heightRoot - self.heightScrollBar
        self.scH = self.heightEff / self.heightContent
        self.placeWidgets()
    
    def onResizeScrollY(self, event: tk.Event | None, *args, **kwargs):
        if event == None:
            return
        if event.widget != self.scrollbarVertical:
            return
        self.root.update_idletasks()
        self.widthScrollBar = self.scrollbarVertical.winfo_width()
        self.widthEff = self.widthRoot - self.widthScrollBar
        self.scW = self.widthEff / self.widthContent
        self.placeWidgets()
    
    def placeWidgets(self):

        #a: list[float | int] = [(self.widthEff - self.widthContent) * 0.5, 0.0]
        #px = max(a)
        px = 0
        offsetX = (((self.widthEff - self.widthContent) / (1.0 - self.scW)) * self.scX)
        px = px + offsetX

        b: list[float | int] = [(self.heightEff - self.heightContent) * 0.5, 0.0]
        py = max(b)
        offsetY = (((self.heightEff - self.heightContent) / (1.0 - self.scH)) * self.scY)
        py = py + offsetY
        
        self.content.place(x = px, y = py)
        self.scrollbarVertical.place(x = self.widthEff, y = 0, height = self.heightRoot)
        self.scrollbarHorizontal.place(x = 0, y = self.heightEff, width = self.widthRoot)
        self.calcScrollX()
        self.calcScrollY()
    
    def calcScrollX(self):
        left = self.scX
        right = left + self.scW
        self.scrollbarHorizontal.set(left, right)
    
    def calcScrollY(self):
        top = self.scY
        bottom = top + self.scH
        self.scrollbarVertical.set(top, bottom)

    def onSrollX(self, *args):
        try:
            self.scX = float(args[1])
            self.placeWidgets()
        except Exception:
            pass

    def onSrollY(self, *args):
        try:
            self.scY = float(args[1])
            self.placeWidgets()
        except Exception:
            pass

W = Window()
W.root.mainloop()
