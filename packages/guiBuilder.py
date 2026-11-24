import tkinter as tk
from tkinter import ttk
from tkinter import font

def buildScoreboard(players):
    for player in players:
        print()

def runGUI(scale: float):
    horizontalResolution = 680 * scale
    verticalResolution = 360 * scale
    root = tk.Tk()
    style = ttk.Style()
    sharedFont = font.Font(family = "TkDefaultFont", size = int(9 * scale))
    root.title("Scoreboard")
    root.geometry(f"{horizontalResolution}x{verticalResolution}")

    #styling
    style.configure("TLabelframe.Label", font = sharedFont)
    style.configure("Treeview.Heading", font = sharedFont)
    
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.rowconfigure(0, weight=1)

    #Scoreboard (left)
    leftBoard = ttk.LabelFrame(root, text = "Leaderboard", padding = 10 * scale)
    leftBoard.grid(row = 0, column = 0, sticky = "nsew", padx=(0, 6))
    scoreTree = ttk.Treeview(
        leftBoard, columns = ("Name", "High Score", "Hours", "Date added"), show = "headings"
    )
    columnWidth = 50 * scale
    scoreTree.heading("Name", text = "Name")
    scoreTree.heading("High Score", text = "High Score")
    scoreTree.heading("Hours", text = "Hours")
    scoreTree.heading("Date added", text = "Date added")

    scoreTree.column("Name", width = columnWidth, anchor = "w")
    scoreTree.column("High Score", width = columnWidth, anchor = "center")
    scoreTree.column("Hours", width = columnWidth, anchor = "e")
    scoreTree.column("Date added", width = columnWidth, anchor = "e")

    scoreTree.pack(fill = "both", expand = True)

    root.mainloop()