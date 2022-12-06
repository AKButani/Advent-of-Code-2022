f = open('Day 1\\input.txt')
curr = 0
arr = []
for line in f:
    if line == '\n':
        arr.append(curr)
        curr = 0
    else:
        line = line[:-1]
        curr = curr + int(line)
    
arr.sort()


print(arr[len(arr)- 1] + arr[len(arr) -2] + arr[len(arr) - 3])
