class Sensor:
    def __init__(self, x, y, beacon_dist):
        self.x = x
        self.y = y
        self.beacon_dist = beacon_dist


def beacon_possible(sensors, i, j):
    for sensor in sensors:
        dist_from_sen = abs(sensor.x - i) + abs(sensor.y - j)
        if sensor.beacon_dist >= dist_from_sen:
            return False, sensor
        
    return True, sensor



f = open('Day 15\\input.txt')
sensors = []
beacons = []
minx = Sensor(100000000000, 1000000, -1)
maxx = Sensor(-1000000, 1000000, -1)
for line in f:
    line = line[:-1]
    line = line.split()
    x = int(line[2][2:-1])
    
    y = int(line[3][2:-1])
    beac_x = int(line[8][2:-1])
    beac_y = int(line[9][2:])
    beacons.append((beac_x, beac_y))
    #print(beac_x)
    #print(beac_y)
    dis = abs(beac_x - x) + abs(beac_y - y)
    sensors.append(Sensor(x, y, dis))
    if x > maxx.x:
        maxx = Sensor(x, y, dis)
    if x < minx.x:
        minx = Sensor(x, y, dis)
'''
counter = 0
for i in range(minx.x - minx.beacon_dist, maxx.x + maxx.beacon_dist):
    if (i, 2_000_000) not in beacons:
        for sensor in sensors:
            dist_from_sen = abs(sensor.x - i) + abs(sensor.y - 2_000_000)
            if sensor.beacon_dist >= dist_from_sen:
                #print(i)
                counter += 1
                break

print(counter)
'''


done = False
for i in range(4_000_001):
    #print("AT:" + str(i))
    if done:
        break
    j = 0
    while j < 4_000_001:
        #print("AT: " + str(i) + ", " + str(j))
        if (i,j) not in beacons:
            boolean, sensor = beacon_possible(sensors, i, j)
            if not boolean:
                j = sensor.y + sensor.beacon_dist - abs(sensor.x - i) + 1
            else:
                print(i)
                print(j)
                done = True
                break
