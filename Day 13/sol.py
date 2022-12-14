from functools import cmp_to_key
f = open('Day 13\\input.txt')

def compare(left, right):
    for i in range(min(len(left), len(right))):
        if isinstance(left[i], int):
            if isinstance(right[i], int):
                if left[i] < right[i]:
                    return "t"
                if left[i] > right[i]:
                    return "f"
            else:
                res = compare([left[i]], right[i])
                if res == "t":
                    return "t"
                elif res == "f":
                    return "f"
        else:
            if isinstance(right[i], int):
                res = compare(left[i], [right[i]])
                if res == "t":
                    return "t"
                elif res == "f":
                    return "f"
            else:
                res = compare(left[i], right[i])
                if res == "t":
                    return "t"
                elif res == "f":
                    return "f"


    if len(left) < len(right):
        return "t"
    if len(left) > len(right):
        return "f"
    if len(left) == len(right):
        return "s"
    
def check(left, right):
    if compare(left, right) == "t":
        return -1
    else:
        return 1
                    
                

input = f.readlines()


sol = 0
index = 1
packets = []
packets.append([[2]])
packets.append([[6]])
for i in range(0,len(input),3):
    
    left = eval(input[i])
    right = eval(input[i+1])
    packets.append(left)
    packets.append(right)
    '''
    if compare(left, right) == "t":
        sol += index
    '''
    index += 1

packets = sorted(packets, key=cmp_to_key(check))
print(packets)
res = 1
for i in range(len(packets)):
    if packets[i] == [[2]] or packets[i] == [[6]]:
        res *= i+1
print(res)