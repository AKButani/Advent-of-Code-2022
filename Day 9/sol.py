
def tail_move(current_tail, diffx, diffy):
    tail_x = current_tail[0]
    tail_y = current_tail[1]
    if(abs(diffx) > 1):
        tail_x += diffx//abs(diffx)
        if(diffy > 0):
            tail_y += 1
        elif(diffy < 0):
            tail_y -= 1
    elif(abs(diffy) > 1):
        tail_y += diffy//abs(diffy)
        if(diffx < 0):
            tail_x -= 1
        elif(diffx > 0):
            tail_x += 1
    return (tail_x,tail_y)

def move(current_head, current_tail, visited, dir, dis, istail):
    #for i in range(dis):
    head_x = current_head[0] + dir[0]
    head_y = current_head[1] + dir[1]
    current_head = (head_x, head_y)
    diffx= current_head[0] - current_tail[0]
    diffy = current_head[1] - current_tail[1]
    current_tail = tail_move(current_tail, diffx, diffy)
    if(current_tail not in visited and istail):
        visited.append(current_tail)

    return current_head, current_tail, visited



f = open('Day 9\\input.txt')
visited = [(0,0)]
starting = (0,0)
knot_locations = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
print(len(knot_locations))



directions = {'L': (-1, 0), 'R': (1,0), 'U': (0,1), 'D': (0,-1)}
for line in f:
    line = line[:-1]
    line = line.split()
    for j in range(int(line[1])):
        for i in range(len(knot_locations) - 1):
            istail = False
            if(i == 8):
                istail = True
            if(i == 0):
                knot_locations[i], knot_locations[i+1], visited = move(knot_locations[i], knot_locations[i+1], visited, directions[line[0]], int(line[1]), istail)
            if( i> 0):
                 knot_locations[i], knot_locations[i+1], visited = move(knot_locations[i], knot_locations[i+1], visited, (0,0), int(line[1]), istail)

print(len(visited))