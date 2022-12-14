f = open('Day 14\\input.txt')
grid = []
maxy = 0
for i in range(700):
    grid.append([])
    for j in range(200):
        grid[i].append(".")
for line in f:
    line = line[:-1]
    line = line.replace("->", " ")
    line = line.split()
    for i in range(len(line) - 1):
        from_ = line[i].replace(",", " ")
        from_ = from_.split()
        to = line[i+1].replace(",", " ")
        to = to.split()
        for j in range(min(int(from_[0]),int(to[0])), max(int(from_[0]),int(to[0]))+1):
            grid[j][int(to[1])] = "#"
        for j in range(min(int(from_[1]),int(to[1])), max(int(from_[1]),int(to[1]))+1):
            grid[int(to[0])][j] = "#"
        maxy = max(maxy, max(int(from_[1]), int(to[1])))

for i in range(700):
    grid[i][maxy+2] = "#"

done = False
counter = 0
while(not done):
    x = 500
    y = 0
    resting = False
    while y < maxy + 3 and not resting:
        if grid[x][y+1] == ".":
            y+=1
            continue
        elif grid[x-1][y+1] == ".":
            y+= 1
            x-= 1 
            continue
        elif grid[x+1][y+1] == ".":
            x += 1
            y += 1
            continue
        else:
            resting = True
    grid[x][y] = "o"
    counter += 1
    if x == 500 and y == 0:
        done = True

print(counter)




