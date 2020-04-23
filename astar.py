import tkinter as tk
import math

root = tk.Tk(className="A* Pathfinding")
cellX, cellY = 20, 20
w, h = 30, 30
tiles = [[0 for x in range(w)] for y in range(h)]
state = 'w'
start = {'i':-1, 'j':-1}
finish = {'i':-1, 'j':-1}
path = []
found = []
status = False

def astaralgo():
    global start, finish, tiles, path, found
    finished = False
    i = start['i']
    j = start['j'] 

    while finished == False:
        tilesaround(tiles, i, j)
        finished = True

def tilesaround(tiles, i, j):
    # calculates g-cost(d from start), h-cost(d from finish), f-cost(total of g and h) 
    # of the surrounding tiles
    rows = [i-1 , i, i+1]
    columns = [j-1, j, j+1]
    print(i, j)
    for row in rows:
        for column in columns:
            if not(row == i and column == j):
                tiles[row][column].frame.config(bg='green3')
            



def makeState(event, tile):
    global tiles, start, finish, state, root, width, height
    x = tile.column * cellX + event.x
    y = tile.row * cellY + event.y
    i = math.floor(y/cellY)
    j = math.floor(x/cellX)

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
    elif event.char == 'g':
        if finish['i'] != -1 and start['i'] != -1:
            astaralgo()
    elif event.char == 'x':
        createtiles()


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
        self.gcost = -1
        self.hcost = -1
        self.fcost = -1
        self.frame.bind("<Button-1>", lambda event, obj=self: makeState(event, obj))
        self.frame.bind("<B1-Motion>", lambda event, obj=self: makeState(event, obj))
        self.row = i
        self.column = j

def createtiles():
    global w, h, tiles
    for i in range(w):
        for j in range(h):
            tiles[i][j] = tile(20, 20, i, j)


if __name__ == '__main__':
    size = str(w * cellX) + 'x' + str(h * cellY)
    root.geometry(size)
    root.bind("<Key>", setstate)

    createtiles()

    root.mainloop()

    '''
    colour list:
    calculated: green3
    been to: red2
    walkable: ghostwhite
    wall: gray5
    path: mediumturquoise
    '''
