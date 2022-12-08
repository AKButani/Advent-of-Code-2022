f = open('Day 8\\input.txt')
def isvisible(i,j,grid):
    if i == 0 or i == len(grid)-1 or j == 0 or j == len(grid[0]) - 1:
        return True
    val = grid[i][j]
    hidden = False
    for row in range(i): # from above
        if(grid[row][j] >= val):
            hidden = True
    if not hidden:
        return True
    hidden = False
    for row in range(i+1, len(grid)): #from below
        if(grid[row][j] >= val):
            hidden = True
    if not hidden:
        return True
    hidden = False
    for col in range(j):
        if grid[i][col] >= val:
            hidden = True
    if not hidden:
        return True
    hidden = False   
    for col in range(j+1, len(grid[0])):
        if grid[i][col] >= val:
            hidden = True
    if not hidden:
        return True
    return False

def scenicscore(i,j,grid):
    if i == 0 or i == len(grid)-1 or j == 0 or j == len(grid[0]) - 1:
        return 0
    val = grid[i][j]
    up = 0
    for row in range(i-1,-1,-1):
        up += 1
        if(grid[row][j] >= val):
            break
    down = 0
    for row in range(i+1, len(grid)):
        down += 1
        if(grid[row][j] >= val):
            break
    left = 0
    for col in range(j-1, -1, -1):
        left += 1
        if grid[i][col] >= val:
            break
    right = 0
    for col in range(j+1, len(grid[0])):
        right += 1
        if grid[i][col] >= val:
            break
    return up * down * left * right

grid = []
for line in f:
    line = line[:-1]
    line = [*line]
    line = [int(num) for num in line]
    grid.append(line)

sol = 0
#print(grid)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        #if(isvisible(i, j, grid)):
        #    sol += 1
        sol = max(sol, scenicscore(i, j, grid))
print(sol)

