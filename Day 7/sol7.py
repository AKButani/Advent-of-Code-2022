f = open('Day 7\\input.txt')



curr_dir = []
dictionary = {}

for line in f:
    line = line[:-1]
    line = line.split()
    #print(line)
    if(line[0] == '$'):
        if(line[1] == 'cd'):
            if(line[2] == '/'):
                curr_dir = []
            elif(line[2] == '..'):
                curr_dir.pop()
            else:
                direc = ','.join(curr_dir) + ',' + line[2]
                curr_dir.append(direc)
    elif(line[0] == 'dir'):
        directory = ','.join(curr_dir) + ',' + line[1]
        if(directory not in dictionary.keys()):
            dictionary[directory] = 0
    elif(line[0] != '$'):
        for el in curr_dir:
            dictionary[el] += int(line[0])
'''
part1
sol = 0
for key in dictionary.keys():
    if(dictionary[key] < 100_000):
        sol += dictionary[key]
print(sol)
'''
#part2
sol = 100_000_000
sum = 0
for key in dictionary.keys(): #sum of outer most 
    if(str(key).count(',') == 1):
        sum += dictionary[key]
ununsed = 70_000_000 - sum
required = 30_000_000
for key in dictionary.keys():
    if dictionary[key] >= required - ununsed:
        sol = min(sol, dictionary[key])

print(sum)
print(sol)





        

        
    
