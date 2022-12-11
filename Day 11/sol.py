f = open('Day 11\\input.txt')

items = []
operations = []
tests = []
where_to_true = []
where_to_false = []
counter = []
for line in f:
    line = line[:-1]
    line = line.split()
    if(len(line) == 0):
        continue
    if line[0] == 'Monkey':
        items.append([])
        counter.append(0)
    elif line[0] == 'Starting':
        line.remove('Starting')
        line.remove('items:')
        for num in line:
            num = num.replace(',', '')
            items[len(items)-1].append(int(num))
        #print(items[len(items)-1])
    elif line[0] == 'Operation:':
        line.remove('Operation:')
        line.remove('new')
        line.remove('=')
        operations.append(line)
    elif line[0] == 'Test:':
        tests.append(int(line[3]))
    else:
        if line[1] == 'true:':
            where_to_true.append(int(line[5]))
        else:
            where_to_false.append(int(line[5]))
prod = 1
for num in tests:
    prod *= num
for i in range(10000):
    monkey_index = 0
    for monkey in items:
        j = 0
        for item in monkey:
            #print(''.join(operations[j]))
            
            old = item
            new = eval(''.join(operations[monkey_index]))
            #new = new // 3
            counter[monkey_index] += 1
            if new % tests[monkey_index] == 0:
                items[where_to_true[monkey_index]].append(new % prod)
            else:
                items[where_to_false[monkey_index]].append(new % prod)

            #print(new)
            j+=1
        monkey.clear()
        monkey_index += 1

counter.sort()
print(counter)
print(160567 * 161523)
