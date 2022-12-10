f = open('Day 10\\input.txt')
strength = []
for i in range(300):
    strength.append(0) 
i = 1
for line in f:
    line = line[:-1]
    line = line.split()
    if len(line) > 1:
        strength[i+2] += int(line[1])
        i+=1
    i+=1
'''
sol = 0
temp = 1
for i in range(221):
    temp += strength[i]
    if(i % 40 == 20):
        sol += temp * i
        print(temp)

print(strength)
print(sol)
'''

#part 2
CRT = []
sprite = 1
pixel_draw = 0
for i in range(6):
    CRT.append([])


for i in range(6):
    pixel_draw = 0
    for j in range(40):
        sprite += strength[i*40 + j + 1]
        if pixel_draw in range(sprite- 1 , sprite + 2):
            CRT[i].append('#')
        else:
            CRT[i].append('.')
        pixel_draw += 1

for i in range(6):
    string = ''.join(CRT[i])
    print(string)




