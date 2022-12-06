f = open('Day 3\\input.txt')
def sol1(f):
    res = 0
    for line in f:
        str1 = line[:len(line)//2]
        str2 = line[len(line)//2:]
        set1 = set(str1)
        set2 = set(str2)
        inter = set1.intersection(set2)
        for el in inter:
            
            if(el.islower()):
                #print(el + " " + str(ord(el) - 96))
                res = res + (ord(el) - 96)
            else:
                #print(el + " " + str(ord(el) - 64))
                res = res + (ord(el) - 38)
    return res


    
def sol2(f):
    res = 0
    i = 0
    arr = ['', '', '']
    for line in f:
        if(i != 0 and i%3 == 0):
            set1 = set(arr[0])
            set2 = set(arr[1])
            set3 = set(arr[2])
            inter = set1.intersection(set2)
            inter = inter.intersection(set3)
            inter.remove('\n')
            for el in inter:
                if(el.islower()):
                    #print(el + " " + str(ord(el) - 96))
                    res = res + (ord(el) - 96)
                else:
                    #print(el + " " + str(ord(el) - 64))
                    res = res + (ord(el) - 38)
            arr[0] = line
        else:
            arr[i%3] = line
        i = i + 1
    return res

print(str(sol2(f)))

