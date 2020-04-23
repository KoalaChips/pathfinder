import tkinter as tk
import math
import time

root = tk.Tk(className="A* Pathfinding")
cellX, cellY = 20, 20
w, h = 30, 30
tiles = [[0 for x in range(w)] for y in range(h)]
state = 'w'
start = {'i':-1, 'j':-1}
finish = {'i':-1, 'j':-1}
path = []
visited = []
found = []
status = False

def astaralgo():
    global start, finish, tiles, visited, path, found, w, h, root
    finished = False
    i = start['i']
    j = start['j'] 

    while finished == False:
        tilesaround(tiles, i, j, w, h, found, visited)
        nextPath = tiles[found[0][0]][found[0][1]]
        for tile in found:
            if tiles[tile[0]][tile[1]].fcost < nextPath.fcost:
                nextPath = tiles[tile[0]][tile[1]]
            elif tiles[tile[0]][tile[1]].fcost == nextPath.fcost:
                if tiles[tile[0]][tile[1]].hcost < nextPath.hcost:
                    nextPath = tiles[tile[0]][tile[1]]
        
        print(i, j)
        for tile in found:
            f = tiles[tile[0]][tile[1]].fcost
            g = tiles[tile[0]][tile[1]].gcost
            h = tiles[tile[0]][tile[1]].hcost
            print(f"{tile[0]} {tile[1]}  f:{f}  g:{g}  h{h}")
        
        if nextPath.row == finish['i'] and nextPath.column == finish['j']: 
            finished = True
        else:
            nextPath.frame.config(bg='red2')
            found.remove((nextPath.row, nextPath.column))
            visited.append(nextPath)
            i = nextPath.row
            j = nextPath.column
        root.update()
        time.sleep(.1)
        

def tilesaround(tiles, i, j, w, h, found, visited):
    # calculates g-cost(d from start), h-cost(d from finish), f-cost(total of g and h) 
    # of the surrounding tiles
    columns = [i-1 , i, i+1]
    rows = [j-1, j, j+1]
    if i == 0:
        del rows[0]
    if i == w - 1:
        del rows[-1]
    if j == 0:
        del columns[0]
    if j == h - 1:
        del columns[-1]

    for row in rows:
        for column in columns:
            tile = tiles[row][column]
            if not(row == i and column == j) and tile.state != 'w':
                if tile.frame.cget('bg') != 'red2' and tile.frame.cget('bg') != 'orange' and tile.frame.cget('bg') != 'purple':
                        tile.frame.config(bg='green3')

                tile.gcost = int(math.sqrt(((i - row)* 10)**2 + ((j - column)* 10)**2))
                tile.hcost = calculateHCost(row, column)
                tile.label.config(text=str(tile.hcost))
                tile.fcost = tile.gcost + tile.hcost
                if ((row, column) not in found) and (tile not in visited):
                    found.append((row, column))

def calculateHCost(i, j):
    global finish
    dis = [finish['i'] - i, i-finish['i'], finish['j'] - j, j - finish['j']]
    tileI = finish['i']
    tileJ = finish['j']
    hcost = 0

    if dis[0] < dis[1]:
        if dis[2] < dis[3]:
            # going SE
            while tileI != i and tileJ != j:
                hcost += 14
                tileI += 1
                tileJ += 1
            hcost += (i - tileI) * 10 + (j - tileJ) * 10 

        elif dis[3] < dis[2]:
            # going NE
            while tileI != i and tileJ != j:
                hcost += 14
                tileI += 1
                tileJ -= 1
            hcost += (i - tileI) * 10 + (tileJ - j) * 10
        else:
            # going E
            hcost = (i - tileI) * 10

    elif dis[1] < dis[0]:
        if dis[2] < dis[3]:
            # going SW
            while tileI != i and tileJ != j:
                hcost += 14
                tileI -= 1
                tileJ += 1
            hcost += (tileI - i) * 10 + (j - tileJ) * 10

        elif dis[3] < dis[2]:
            # going NW
            while tileI != i and tileJ != j:
                hcost += 14
                tileI -= 1
                tileJ -= 1
            hcost += (tileI - i) * 10 + (tileJ - j) * 10
        else:
            # going W
            hcost = (tileI - i) * 10
        
    else:
        # vertial from the finish 
        hcost = abs(tileI-i) * 10

    return hcost

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
        self.label = tk.Label(self.frame, text='')                      
        self.frame.grid(row=i, column=j)
        self.state = 'p'
        self.gcost = 0
        self.hcost = 0
        self.fcost = 0
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
