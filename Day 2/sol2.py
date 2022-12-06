def pointcalc(first, second):
    if(first == 'A'): #rock
        if(second == 'X'):
            return 3 + 1
        elif(second == 'Y'):
            return 6 + 2
        else:
            return 0 + 3
    elif(first == 'B'): #paper
        if(second == 'X'):
            return 0 + 1
        elif(second == 'Y'):
            return 3 + 2
        else:
            return 6 + 3
    else: #scissors
        if(second == 'X'): 
            return 6 + 1
        elif(second == 'Y'):
            return 0 + 2
        else:
            return 3 + 3
        
def parttwo(first, second):
   # points = [1, 2, 3] #rock, paper, scissors
    if(first == 'A'): #rock
        if(second == 'X'):
            return 0 + 3
        elif(second == 'Y'):
            return 3 + 1
        else:
            return 6 + 2
    elif(first == 'B'): #paper
        if(second == 'X'):
            return 0 + 1
        elif(second == 'Y'):
            return 3 + 2
        else:
            return 6 + 3
    else: #scissors
        if(second == 'X'): 
            return 0 + 2
        elif(second == 'Y'):
            return 3 + 3
        else:
            return 6 + 1



f = open('Day 2\\input.txt')
score = 0
for line in f:
    line = line[:-1]
    line = line.split()
    score = score + parttwo(line[0], line[1])

print(score)