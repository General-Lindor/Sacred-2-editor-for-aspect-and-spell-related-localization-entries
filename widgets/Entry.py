import tkinter as tk

class Entry():
    def __init__(self, master, content: dict, key: str, row: int, column: int):
        
        self.content = content
        self.key = key
        
        self.textLength = 0
        self.value = tk.StringVar(master = master)
        self.value.trace_add("write", self.onWrite)
        self.value.trace_add("write", self.updateWidth)
        
        self.label = tk.Label(master = master, text = key)
        self.label.grid(row = row, column = column, sticky = "w")

        self.entry = tk.Entry(master = master, textvariable = self.value, font = "Helvetica 10 normal")
        self.entry.grid(row = row, column = column + 1, sticky = "w")

        self.update()
    
    def onWrite(self, *args, **kwargs):
        d = self.content.get(self.key)
        if not isinstance(d, dict):
            d = {}
        d["VALUE"] = self.value.get()
        self.content[self.key] = d
    
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