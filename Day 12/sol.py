f = open('Day 12\\input.txt')

grid = []
adj = {}
i = 0
start = (0,0)
end = (0,0)
for line in f:
    line = line[:-1]
    grid.append([])
    j = 0
    for char in line:
        if char.islower():
            grid[i].append(ord(char) - 97)
        else:
            if char == 'S':
                grid[i].append(0)
                #start = (i, j) part1
            else:
                grid[i].append(26)
                end = (i,j)
        j += 1
    i += 1

for i in range(len(grid)):
    for j in range(len(grid[i])):
        adj[(i,j)] = []
        if i > 0:
            if grid[i][j] - grid[i-1][j] >= -1: # up
                adj[(i,j)].append((i-1,j))
        if j > 0:
            if grid[i][j] - grid[i][j-1] >= -1: #left
                adj[(i,j)].append((i, j-1))
        if i < len(grid) - 1:
            if grid[i][j] - grid[i+1][j] >= -1: #right
                adj[(i,j)].append((i+1, j))
        if j < len(grid[i]) - 1:
            if grid[i][j] - grid[i][j+1] >= -1: #down
               adj[(i,j)].append((i, j+1))
mindist = 110000000000000
#print(adj)
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if(grid[i][j] == 0):
            start = (i,j)
            q = []
            q.append(start)
            dist = {}
            dist[start] = 0
            while len(q) > 0:
                curr = q.pop(0)
                for neighbours in adj[curr]:
                    if neighbours not in dist.keys():
                        dist[neighbours] = dist[curr] + 1
                        q.append(neighbours)
            
            if end in dist.keys():
                mindist = min(dist[end], mindist)
                

print(mindist)