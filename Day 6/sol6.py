

f = open('Day 6\\input6.txt')
counter = 0
arr = []
for line in f:
    line = line[:-1]
    for char in line:
        counter += 1
        arr.append(char)
        if len(arr) > 14:
            arr.pop(0)
        if len(arr) == 14:
            if(len(arr) == len(set(arr))):
                print(counter)
                break
            

        
        