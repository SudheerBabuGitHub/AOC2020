file = open("input.txt")
lines = file.readlines()
coordinates = []
colour = {}
for line in lines:
    x_coord = 0
    y_coord = 0
    chararray = list(line)
    c_prev = 'e'
    while True:
        c = chararray.pop(0)
        if c=='e':
            x_coord += 1
            if c_prev == 'e' or c_prev == 'w':
                x_coord += 1
        elif c=='w':
            x_coord -= 1
            if c_prev == 'e' or c_prev == 'w':
                x_coord -= 1
        elif c=='n':
            y_coord += 3
        elif c=='s':
            y_coord -= 3
        else:
            break
        c_prev = c
    if coordinates.__contains__((x_coord,y_coord)):
        curr_colour = colour.get((x_coord,y_coord))
        colour.update({(x_coord,y_coord):1-curr_colour})
    else:
        coordinates += [(x_coord,y_coord)]
        colour[(x_coord,y_coord)] = 1
black_coordinates = set()
for key in colour.keys():
    if colour.get(key) == 1:
        black_coordinates.add(key)
print(len(black_coordinates))

itr = 0
while itr < 100:
    #find neighbours
    neighbours = set()
    set_white = set()
    for coordinate in black_coordinates:
        x_coord = coordinate[0]
        y_coord = coordinate[1]
        black_neighbours = 0
        #e
        neighbour = (x_coord+2,y_coord)
        if black_coordinates.__contains__(neighbour):
            black_neighbours += 1
        else:
            neighbours.add(neighbour)
        #w
        neighbour = (x_coord-2,y_coord)
        if black_coordinates.__contains__(neighbour):
            black_neighbours += 1
        else:
            neighbours.add(neighbour)
        #ne
        neighbour = (x_coord+1,y_coord+3)
        if black_coordinates.__contains__(neighbour):
            black_neighbours += 1
        else:
            neighbours.add(neighbour)
        #nw
        neighbour = (x_coord-1,y_coord+3)
        if black_coordinates.__contains__(neighbour):
            black_neighbours += 1
        else:
            neighbours.add(neighbour)
        #se
        neighbour = (x_coord+1,y_coord-3)
        if black_coordinates.__contains__(neighbour):
            black_neighbours += 1
        else:
            neighbours.add(neighbour)
        #sw
        neighbour = (x_coord-1,y_coord-3)
        if black_coordinates.__contains__(neighbour):
            black_neighbours += 1
        else:
            neighbours.add(neighbour)
        if black_neighbours==0 or black_neighbours>2:
            set_white.add(coordinate)
    set_black = set()
    #iterate through neighbours
    for coordinate in neighbours:
        x_coord = coordinate[0]
        y_coord = coordinate[1]
        black_neighbours = 0
        # e
        neighbour = (x_coord + 2, y_coord)
        if black_coordinates.__contains__(neighbour):
            black_neighbours += 1
        # w
        neighbour = (x_coord - 2, y_coord)
        if black_coordinates.__contains__(neighbour):
            black_neighbours += 1
        # ne
        neighbour = (x_coord + 1, y_coord + 3)
        if black_coordinates.__contains__(neighbour):
            black_neighbours += 1
        # nw
        neighbour = (x_coord - 1, y_coord + 3)
        if black_coordinates.__contains__(neighbour):
            black_neighbours += 1
        # se
        neighbour = (x_coord + 1, y_coord - 3)
        if black_coordinates.__contains__(neighbour):
            black_neighbours += 1
        # sw
        neighbour = (x_coord - 1, y_coord - 3)
        if black_coordinates.__contains__(neighbour):
            black_neighbours += 1
        if black_neighbours == 2:
            set_black.add(coordinate)

    #update colour
    for coordinate in set_white:
        black_coordinates.remove(coordinate)
    for coordinate in set_black:
        black_coordinates.add(coordinate)

    itr += 1

    print(itr, len(black_coordinates))

