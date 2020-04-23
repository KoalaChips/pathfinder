import tkinter as tk
import tkinter.messagebox as mbox

import math

w, h = 30, 30
tiles = [[0 for x in range(w)] for y in range(h)]
state = 'w'
start = [-1, -1]
end = [-1, -1]
pos = [-1, -1]

def makeWall(tile, event):
    global tiles, state, start, end
    i = int((tile.i * tile.w + event.y) / tile.w)
    j = int((tile.j * tile.w + event.x) / tile.w)

    if state == 's':
        if start != [-1,-1]:
            tiles[start[0]][start[1]].frame.config(bg='white')
            tiles[start[0]][start[1]].state = 'p'
        start[0] = i
        start[1] = j
    elif state == 'f':
        if end != [-1,-1]:
            tiles[end[0]][end[1]].frame.config(bg='white')
            tiles[end[0]][end[1]].state = 'p'
        end[0] = i
        end[1] = j

    states = {
        'w': 'black', 
        'p': 'white', 
        's': 'green', 
        'f': 'red'
    }
    tiles[i][j].state = state
    tiles[i][j].frame.config(bg=states[state])

def setstate(event):
    global state
    char = event.char
    states = ['w', 'p', 's', 'f']
    if char in states:
        state = char

class tile(tk.Frame):
    def __init__(self, h, w, i, j, state):
        self.frame = tk.Frame(root, 
                              height=h, 
                              width=w, 
                              bg='ghostwhite',
                              highlightbackground= 'gray15',
                              highlightcolor="black", 
                              highlightthickness=1, 
                              bd=10)
        self.frame.grid(row=i, column=j)
        self.state = state
        self.frame.bind('<Button-1>', lambda e: makeWall(self, e))
        self.frame.bind("<B1-Motion>", lambda e: makeWall(self, e))
        self.i = i
        self.j = j
        self.w = w


if __name__ == '__main__':
    root = tk.Tk(className="A* Pathfinding")
    width = 600
    height = 600
    size = str(width) + 'x' + str(height)
    root.geometry(size)
    root.bind("<Key>", setstate)
    
    for i in range(w):
        for j in range(h):
            tiles[i][j] = tile(w, h, i, j, 'p')

    root.mainloop()

'''
colour list:
    calculated: green3
    been to: red2
    walkable: ghostwhite
    wall: gray5
    path: mediumturquoise
'''
