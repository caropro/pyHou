# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0

import numpy as np
import json
from scipy import stats
import PIL.Image as Image
import matplotlib

testValue = 1

# create base grid
def wfc_Grid():
    print("Gen Base Grid")
    #Base Size of Grid
    SizeX = 9
    SizeY = 9

    #Create Grid
    grid = np.zeros((SizeX,SizeY))

    #Set Grid Value
    for x in range(SizeX):
        for y in range(SizeY):
            grid[x][y] = 9

    #display Grid
    print(grid)
    return grid


def Solve(inputGrid):
    #init Record
    record = []

    #randStart
    randStart_row = np.random.randint(0,9)
    randStart_col = np.random.randint(0,9)
    randStart_Value = np.random.randint(0,9)
    record.append([randStart_row,randStart_col,randStart_Value])

    inputGrid[randStart_row][randStart_col] = randStart_Value
    update(inputGrid,record[-1])
    # while(len(record) != inputGrid.size):
    #     #find the next point
    #     nextPoint = findNextPoint(inputGrid,record)
    #     if nextPoint == []:
    #         print("No Next Point")
    #         break
    #     else:
    #         record.append(nextPoint)
    #         inputGrid[nextPoint[0]][nextPoint[1]] = nextPoint[2]

    print(inputGrid)

def update(inputGrid,cell):
    pos = [cell[0],cell[1]]
    up = [pos[0],pos[1]-1]
    down = [pos[0],pos[1]+1]
    left = [pos[0]-1,pos[1]]
    right = [pos[0]+1,pos[1]]






class wfc_object():
    def __init__(self):
        pass


def run():
    init_grid = wfc_Grid()
    print("*"*100)
    Solve(init_grid)


if __name__ == '__main__':
    run()