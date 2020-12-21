
def GetTileBorders(tile):
    borders = []
    borders += [tile[0]] #top
    right = []
    for row in tile:
        right += [row[-1]]
    borders += [right] #right
    borders += [tile[9]] #bottom
    left = []
    for row in tile:
        left += [row[0]]
    borders += [left] #left
    return borders

def UpdateTileBorders(TILES, TILE_BORDERS, tilename):
    borders = GetTileBorders(TILES.get(tilename))
    TILE_BORDERS.update({tilename:borders})

def SearchBorders(TILE_BORDERS, tilename, side):
    testborder = TILE_BORDERS.get(tilename)[side]
    teststr = "".join(testborder)
    teststrflipped = teststr[::-1]
    foundmatch = False
    for key in TILE_BORDERS.keys():
        if key == tilename:
            continue
        borders = TILE_BORDERS.get(key)
        for i in range(4):
            borderstr = "".join(borders[i])
            if borderstr == teststr:
                foundmatch = True
                break
            elif borderstr == teststrflipped:
                foundmatch = True
                break
        if foundmatch:
            break
    return foundmatch

def CorrectTileOrientation(TILES,t,operation):
    tilename = t.name
    tile = TILES.get(tilename)
    if operation == 0: #flip vertical
        tile = tile[::-1]
        TILES.update({tilename: tile})
        if t.unique.__contains__(0):
            t.unique.remove(0)
            t.unique += [2]
        elif t.unique.__contains__(2):
            t.unique.remove(2)
            t.unique += [0]
    elif operation == 1: #flip horizontal
        for i,line in enumerate(tile):
            tile[i] = line[::-1]
        TILES.update({tilename: tile})
        if t.unique.__contains__(1):
            t.unique.remove(1)
            t.unique += [3]
        elif t.unique.__contains__(3):
            t.unique.remove(3)
            t.unique += [1]
    elif operation == 2: #rotate clockwise
        for i,line in enumerate(tile):
            for j, c in enumerate(line):
                if i>=j:
                    continue
                else:
                    temp = tile[i][j]
                    tile[i][j] = tile[j][i]
                    tile[j][i] = temp
        TILES.update({tilename: tile})
        if t.unique.__contains__(0):
            t.unique.remove(0)
            if t.unique.__contains__(3):
                t.unique.remove(3)
                t.unique += [0]
            t.unique += [3]
        elif t.unique.__contains__(3):
            t.unique.remove(3)
            if t.unique.__contains__(0):
                t.unique.remove(0)
                t.unique += [3]
            t.unique += [0]
        elif t.unique.__contains__(1):
            t.unique.remove(1)
            if t.unique.__contains__(2):
                t.unique.remove(2)
                t.unique += [1]
            t.unique += [2]
        elif t.unique.__contains__(2):
            t.unique.remove(2)
            if t.unique.__contains__(1):
                t.unique.remove(1)
                t.unique += [2]
            t.unique += [1]
        CorrectTileOrientation(TILES, t, 1)
    else: #rotate counter clock wise
        for i,line in enumerate(tile):
            for j, c in enumerate(line):
                if i>=j:
                    continue
                else:
                    temp = tile[i][j]
                    tile[i][j] = tile[j][i]
                    tile[j][i] = temp
        TILES.update({tilename: tile})
        if t.unique.__contains__(0):
            t.unique.remove(0)
            if t.unique.__contains__(3):
                t.unique.remove(3)
                t.unique += [0]
            t.unique += [3]
        elif t.unique.__contains__(3):
            t.unique.remove(3)
            if t.unique.__contains__(0):
                t.unique.remove(0)
                t.unique += [3]
            t.unique += [0]
        elif t.unique.__contains__(1):
            t.unique.remove(1)
            if t.unique.__contains__(2):
                t.unique.remove(2)
                t.unique += [1]
            t.unique += [2]
        elif t.unique.__contains__(2):
            t.unique.remove(2)
            if t.unique.__contains__(1):
                t.unique.remove(1)
                t.unique += [2]
            t.unique += [1]
        CorrectTileOrientation(TILES, t, 0)
    return



file = open("input.txt","r")
lines = file.readlines()

TILES = {}
TILE_BORDERS = {}

tilenum = 0
tile = []
for i,line in enumerate(lines):
    if i%12 == 0:
        tilenum = line[5:9]
    elif i%12 == 11:
        TILES[tilenum] = tile
        tile = []
    elif line != '\n':
        tile += [list(line.strip())]

# find all borders
for key in TILES.keys():
    borders = GetTileBorders(TILES.get(key))
    TILE_BORDERS[key] = borders

class Tile():
     def __init__(self,name,unique):
         self.name = name
         self.unique = unique

def GetCommonBorder(tile1,tile,side):
    borders1 = TILE_BORDERS.get(tile1.name)
    borders2 = TILE_BORDERS.get(tile.name)
    common = -1
    flipped = False
    teststr = "".join(borders1[side])
    teststrflipped = teststr[::-1]
    for i in range(4):
        if "".join(borders2[i]) == teststr:
            common = i
        elif "".join(borders2[i]) == teststrflipped:
            common = i
            flipped = True
    return common, flipped

cornertiles = []
edgetiles = []
centertiles = []
# find unique borders
for key in TILE_BORDERS.keys():
    unique = []
    for i in range(4):
        foundmatch = SearchBorders(TILE_BORDERS, key, i)
        if not foundmatch:
            unique += [i]
    if len(unique) == 1:
        edgetiles += [Tile(key,unique)]
    elif len(unique) == 2:
        cornertiles += [Tile(key,unique)]
    else:
        centertiles += [Tile(key,[])]

framewidth = 12
image_frame = [[Tile("",[]) for i in range(framewidth)]for j in range(framewidth)]
#first fill in the edge and corner frames
curr_tile = cornertiles[0]
if curr_tile.unique.__contains__(2):
    CorrectTileOrientation(TILES,curr_tile,0)
if curr_tile.unique.__contains__(1):
    CorrectTileOrientation(TILES,curr_tile,1)
UpdateTileBorders(TILES, TILE_BORDERS, curr_tile.name)
image_frame[0][0] = curr_tile
cornertiles.remove(cornertiles[0])
print(curr_tile.unique)
print(curr_tile.name)
for col in range(1,framewidth-1):
    for tile in edgetiles:
        common_side, isflipped = GetCommonBorder(curr_tile,tile,1)
        if common_side != -1:
            if common_side == 1:
                CorrectTileOrientation(TILES, tile, 1)
            elif common_side == 0:
                CorrectTileOrientation(TILES, tile, 3)
                CorrectTileOrientation(TILES, tile, 0)
            elif common_side == 2:
                CorrectTileOrientation(TILES, tile, 2)
            if isflipped:
                CorrectTileOrientation(TILES, tile, 0)
            UpdateTileBorders(TILES, TILE_BORDERS, tile.name)
            image_frame[0][col] = tile
            curr_tile = tile
            edgetiles.remove(tile)
            print(tile.unique)
            break
    print(curr_tile.name)
for tile in cornertiles:
    common_side, isflipped = GetCommonBorder(curr_tile, tile, 1)
    if common_side != -1:
        if common_side == 1:
            CorrectTileOrientation(TILES, tile, 1)
        elif common_side == 0:
            CorrectTileOrientation(TILES, tile, 3)
            CorrectTileOrientation(TILES, tile, 0)
        elif common_side == 2:
            CorrectTileOrientation(TILES, tile, 2)
        if isflipped:
            CorrectTileOrientation(TILES, tile, 0)
        UpdateTileBorders(TILES, TILE_BORDERS, tile.name)
        image_frame[0][framewidth-1] = tile
        curr_tile = tile
        cornertiles.remove(tile)
        print(tile.unique)
        break
print(curr_tile.name)
for row in range(1,framewidth-1):
    for tile in edgetiles:
        common_side, isflipped = GetCommonBorder(curr_tile,tile,2)
        if common_side != -1:
            if common_side == 2:
                CorrectTileOrientation(TILES, tile, 0)
            elif common_side == 1:
                CorrectTileOrientation(TILES, tile, 3)
            elif common_side == 3:
                CorrectTileOrientation(TILES, tile, 2)
                CorrectTileOrientation(TILES, tile, 1)
            if isflipped:
                CorrectTileOrientation(TILES, tile, 1)
            UpdateTileBorders(TILES, TILE_BORDERS, tile.name)
            image_frame[row][framewidth-1] = tile
            curr_tile = tile
            edgetiles.remove(tile)
            print(tile.unique)
            break
    print(curr_tile.name)
for tile in cornertiles:
    common_side, isflipped = GetCommonBorder(curr_tile, tile, 2)
    if common_side != -1:
        if common_side == 2:
            CorrectTileOrientation(TILES, tile, 0)
        elif common_side == 1:
            CorrectTileOrientation(TILES, tile, 3)
        elif common_side == 3:
            CorrectTileOrientation(TILES, tile, 2)
            CorrectTileOrientation(TILES, tile, 1)
        if isflipped:
            CorrectTileOrientation(TILES, tile, 1)
        UpdateTileBorders(TILES, TILE_BORDERS, tile.name)
        image_frame[framewidth-1][framewidth-1] = tile
        curr_tile = tile
        cornertiles.remove(tile)
        print(tile.unique)
        break
print(curr_tile.name)
for col in range(1,framewidth-1):
    for tile in edgetiles:
        common_side, isflipped = GetCommonBorder(curr_tile,tile,3)
        if common_side != -1:
            if common_side == 3:
                CorrectTileOrientation(TILES, tile, 1)
            elif common_side == 2:
                CorrectTileOrientation(TILES, tile, 3)
                CorrectTileOrientation(TILES, tile, 0)
            elif common_side == 0:
                CorrectTileOrientation(TILES, tile, 2)
            if isflipped:
                CorrectTileOrientation(TILES, tile, 0)
            UpdateTileBorders(TILES, TILE_BORDERS, tile.name)
            image_frame[framewidth-1][framewidth-col-1] = tile
            curr_tile = tile
            edgetiles.remove(tile)
            print(tile.unique)
            break
    print(curr_tile.name)
for tile in cornertiles:
    common_side, isflipped = GetCommonBorder(curr_tile, tile, 3)
    if common_side != -1:
        if common_side == 3:
            CorrectTileOrientation(TILES, tile, 1)
        elif common_side == 2:
            CorrectTileOrientation(TILES, tile, 3)
            CorrectTileOrientation(TILES, tile, 0)
        elif common_side == 0:
            CorrectTileOrientation(TILES, tile, 2)
        if isflipped:
            CorrectTileOrientation(TILES, tile, 0)
        UpdateTileBorders(TILES, TILE_BORDERS, tile.name)
        image_frame[framewidth-1][0] = tile
        curr_tile = tile
        cornertiles.remove(tile)
        print(tile.unique)
        break
print(curr_tile.name)
for row in range(1,framewidth-1):
    for tile in edgetiles:
        common_side, isflipped = GetCommonBorder(curr_tile,tile,0)
        if common_side != -1:
            if common_side == 0:
                CorrectTileOrientation(TILES, tile, 0)
            elif common_side == 3:
                CorrectTileOrientation(TILES, tile, 3)
            elif common_side == 1:
                CorrectTileOrientation(TILES, tile, 2)
                CorrectTileOrientation(TILES, tile, 1)
            if isflipped:
                CorrectTileOrientation(TILES, tile, 1)
            UpdateTileBorders(TILES, TILE_BORDERS, tile.name)
            image_frame[framewidth-row-1][0] = tile
            curr_tile = tile
            edgetiles.remove(tile)
            print(tile.unique)
            break
    print(curr_tile.name)

#fill in the center nodes
for row in range(1,framewidth-1):
    for col in range(1,framewidth-1):
        curr_tile1 = image_frame[row][col-1]
        curr_tile2 = image_frame[row-1][col]
        for tile in centertiles:
            common_side1, isflipped1 = GetCommonBorder(curr_tile1, tile, 1)
            #common_side2, isflipped2 = GetCommonBorder(curr_tile2, tile, 2)
            if common_side1 != -1:
                if common_side1 == 1:
                    CorrectTileOrientation(TILES, tile, 1)
                elif common_side1 == 0:
                    CorrectTileOrientation(TILES, tile, 3)
                    CorrectTileOrientation(TILES, tile, 0)
                elif common_side1 == 2:
                    CorrectTileOrientation(TILES, tile, 2)
                if isflipped1:
                    CorrectTileOrientation(TILES, tile, 0)
                UpdateTileBorders(TILES, TILE_BORDERS, tile.name)
                image_frame[row][col] = tile
                centertiles.remove(tile)
                break
"""
image_with_frame = [['0' for i in range(framewidth * 11)] for j in range(framewidth * 11)]
for r0 in range(framewidth):
    for c0 in range(framewidth):
        if image_frame[r0][c0].name == "":
            continue
        image_tile = TILES.get(image_frame[r0][c0].name)
        for i, line in enumerate(image_tile):
            for j, c in enumerate(line):
                image_with_frame[r0 * 10 + i + r0][c0 * 10 + j + c0] = c
for line in image_with_frame:
    print(line)
"""
#construct full image
image = [['0' for i in range(framewidth*8)] for j in range(framewidth*8)]
for row in range(framewidth):
    for col in range(framewidth):
        image_tile = TILES.get(image_frame[row][col].name)
        for i,line in enumerate(image_tile):
            if i==0 or i==9:
                continue
            for j,c in enumerate(line):
                if j==0 or j==9:
                    continue
                image[row*8+i-1][col*8+j-1] = c
TILES['full'] = image
FullImageTile = Tile("full",[])
#CorrectTileOrientation(TILES,FullImageTile,0)
import numpy as np
npimage = np.zeros((len(image),len(image[0])))
for i,row in enumerate(image):
    for j,col in enumerate(row):
        if col=='#':
            npimage[i,j] = 1

#read the sea monster
file = open("sea_monster.txt")
lines = file.readlines()
sea_monster = np.zeros((len(lines),len(lines[0])-1))
for i,line in enumerate(lines):
    for j,c in enumerate(line):
        if c=='#':
            sea_monster[i,j] = 1
sea_monster_image = np.zeros(npimage.shape)
sea_monster_sum = np.sum(sea_monster)

monster_cnt = 0
for i in range(npimage.shape[0]-sea_monster.shape[0]+1):
    for j in range(npimage.shape[1]-sea_monster.shape[1]+1):
        if np.sum(np.multiply(sea_monster,npimage[i:i+sea_monster.shape[0],j:j+sea_monster.shape[1]])) == sea_monster_sum:
            #npimage[i:i + sea_monster.shape[0], j:j + sea_monster.shape[1]][sea_monster>0] = 0
            sea_monster_image[i:i+sea_monster.shape[0],j:j+sea_monster.shape[1]] += sea_monster
            monster_cnt += 1
print("monster_cnt=",monster_cnt)
print("monster_sum=",np.size(sea_monster_image[sea_monster_image>0]))
print("total_hash=",np.sum(npimage))