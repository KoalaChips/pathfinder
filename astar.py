import tkinter as tk
import math

root = tk.Tk(className="A* Pathfinding")
w, h = 30, 30
tiles = [[0 for x in range(w)] for y in range(h)]
state = 'w'
start = {'i':-1, 'j':-1}
finish = {'i':-1, 'j':-1}
status = False

def changeStatus(event):
    global status
    if str(event.type) == "ButtonRelease":
        status = False
    elif str(event.type) == "ButtonPress":
        status = True
    print(status)


def makeState(event, tile):
    global tiles, start, finish, state, status, root
    print(tile.row, tile.column)
    if status:
        i = tile.row
        j = tile.column

        if state == 'w':
            colour = 'gray5'
        elif state == 'p':
            colour = 'ghostwhite'
        elif state == 's':

            if start['i'] != -1:
                tiles[start['i']][start['j']].frame.config(bg='ghostwhite')
                tiles[start['i']][start['j']].state = 'p'
                start['i'] = i
                start['j'] = j
            else:
                start['i'] = i
                start['j'] = j
            colour = 'purple'

        elif state == 'f':
            if finish['i'] != -1:
                tiles[finish['i']][finish['j']].frame.config(bg='ghostwhite')
                tiles[finish['i']][finish['j']].state = 'p'
                finish['i'] = i
                finish['j'] = j
            else:
                finish['i'] = i
                finish['j'] = j
            colour = 'orange'

        tiles[i][j].frame.config(bg=colour)
        tiles[i][j].state = state

def setstate(event):
    global state
    if event.char == '1':
        state = 'w'
    elif event.char == '2':
        state = 'p'
    elif event.char == '3':
        state = 's'
    elif event.char == '4':
        state = 'f'


class tile(tk.Frame):
    def __init__(self, h, w, i, j):
        self.frame = tk.Frame(root, 
                              height=h, 
                              width=w,
                              bg='ghostwhite',
                              highlightbackground= 'gray15',
                              highlightcolor="black", 
                              highlightthickness=1, 
                              bd=10)
        self.frame.grid(row=i, column=j)
        self.state = 'p'
        self.frame.bind("<Enter>", lambda event, obj=self: makeState(event, obj))
        self.row = i
        self.column = j


if __name__ == '__main__':
    width = 600
    height = 600
    size = str(width) + 'x' + str(height)
    root.geometry(size)
    root.bind("<Key>", setstate)

    
    root.bind("<Button-1>", changeStatus)
    root.bind("<ButtonRelease-1>", changeStatus)


    w, h = 30, 30
    tiles = [[0 for x in range(w)] for y in range(h)]
    for i in range(w):
        for j in range(h):
            tiles[i][j] = tile(20, 20, i, j)

    root.mainloop()

    '''
    colour list:
    calculated: green3
    been to: red2
    walkable: ghostwhite
    wall: gray5
    path: mediumturquoise
    '''
