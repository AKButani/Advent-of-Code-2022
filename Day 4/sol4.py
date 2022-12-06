f = open('Day 4\\input.txt')
def find_overlap(arr):
    if(arr[0] == arr[2] or arr[1] == arr[3]):
        return 1
    if(arr[0] <= arr[2] and arr[1] >= arr[2]):
        return 1
    if(arr[0] >= arr[2] and arr[0] <= arr[3]):
        return 1
    return 0


counter = 0
for line in f:
    line = line[:-1]
    line = line.replace('-', ',')
    arr = line.split(",")
    arr = [int(num) for num in arr] 
    """
    if(arr[0] == arr[2] and arr[1] == arr[3]):
        counter = counter + 1
        print(arr)
    elif(arr[0] <= arr[2] and arr[1] >= arr[3]):
        counter = counter + 1
        print(arr)
    elif(arr[0] >= arr[2] and arr[1] <= arr[3]):
        counter = counter + 1
        print(arr)
    """
    counter += find_overlap(arr)
    
print(counter)
   