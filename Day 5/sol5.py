f = open('Day 5\\input.txt')
def stack_modify(stack, count, num_from, num_to):
    for i in range(count):
        stack[num_to].append(stack[num_from].pop())
        #print(stack)

def stack_modify2(stack, count, num_from, num_to):
    if count == 1:
        stack_modify(stack, count, num_from, num_to)
    else:
        temp = []
        for i in range(count):
            temp.append(stack[num_from].pop())
        for i in range(count):
            stack[num_to].append(temp.pop())



stack = []
str0 = ["TPZCSLQN", "LPTVHCG", "DCZF", "GWTDLMVC", "PWC", "PFJDCTSZ", "VWGBD", "NJSQHW", "RCQFSLV"]
for string in str0:
    stack.append([*string])
#print(stack)
for line in f:
    line = line[:-1]
    if line.startswith('m'):
        line = line.split()
        line.remove('move')
        line.remove('from')
        line.remove('to')
        #print(line)
        stack_modify2(stack, int(line[0]), int(line[1]) - 1, int(line[2]) - 1)





for i in range(9):
    print(stack[i].pop())           