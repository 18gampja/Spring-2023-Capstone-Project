import random
import math
import operator

# Target Class
class Target:
    xCoord = 0
    yCoord = 0
    closest_m5 = None

# M5 Class
class M5:
    id = ""

    xCoord = 0
    yCoord = 0

    luciferin = 0
    last_luciferin = []

    next_direction = 0
    prior_directions = []

    def generate_luciferin(self):
        self.luciferin = math.sqrt((math.pow((self.xCoord - targ.xCoord), 2)) + (math.pow((self.yCoord - targ.yCoord), 2)))

    def generate_next_direction(self):
        xDelta = targ.xCoord - self.xCoord
        yDelta = targ.yCoord - self.yCoord
        desired_angle_r = math.atan2(yDelta, xDelta)
        desired_angle_d = 90 - (desired_angle_r * (180/math.pi))
        print(desired_angle_d)

# Divider Function
def divider():
    print("-------------------------")

# Function to make the grid
def makeGrid(w, h):
    grid = []
    row = f"{' ' * w}"
    for i in range(h):
        grid.append(row)
    return grid

# Function to print the grid
def printGrid(grid):
    print(f"{'_' * 42}")
    for row in grid[::-1]:
        print(f"|{row}|")
    print(f"{'‾' * 42}")

# Function to place an item
def setItem(item, itemName, xVal=0, yVal=0):
    if xVal and yVal:
        targetX = xVal
        targetY = yVal
        print(f"The coordinates of the {itemName} are: ({targetX}, {targetY})")
    else:
        print(f"Enter the X coordinate of {itemName}: (1-20): ", end="")
        targetX = int(input())
        print(f"Enter the Y coordinate of {itemName}: (1-40): ", end="")
        targetY = int(input())
        print(f"The coordinates of the {itemName} are: ({targetX}, {targetY})")
    row = list(grid[targetX-1])
    row[targetY-1] = item
    grid[targetX-1] = "".join(row)
    return targetX, targetY

# Produces the next step in the Simulation
def runSimulation(m5s):
    # Check if any M5s have made contact with the Target
    for i in range (0, m5_count):
        if m5s[i].xCoord == targ.xCoord and m5s[i].yCoord == targ.yCoord:
            print(f"The M5 \"{m5s[i]}\" has hit the target!")
    # If no M5s have hit the Target...
    else:
        m5s.sort(key=lambda x: x.luciferin)
        closestM5 = m5s[0]
        print(f"The closest M5 is: {closestM5.id}")

# Option to manually input item coordinates
random_target_location = True
random_m5_location = True
m5_count = 5


# Set size for Grid and call print
grid = makeGrid(40, 20)[::-1]
printGrid(grid)

# Create Target and M5s
targ = Target
m5s = []
for i in range(0, m5_count):
    m5 = M5()
    m5s.append(m5)

# Populate Item with Coordinates
if random_target_location:
    targ.xCoord,targ.yCoord = setItem('X', "Target", random.randint(1, 20), random.randint(1, 40))
else:
    targ.xCoord,targ.yCoord = setItem('X', "Target")

if random_m5_location:
    for i in range (0, m5_count):
        m5s[i].xCoord, m5s[i].yCoord = setItem(f"{i+1}", f"M5 #{i+1}", random.randint(1, 20), random.randint(1, 40))
        m5s[i].id = f"M5_{i+1}"
        print(m5s[i].id)
else:
    for i in range (0, m5_count):
        m5s[i].xCoord, m5s[i].yCoord = setItem(f"{i+1}", f"M5 #{i+1}")
        m5s[i].id = f"M5_{i+1}"
        print(m5s[i].id)

divider()
printGrid(grid)

print(f"The Target is at: {targ.xCoord, targ.yCoord}")

for i in range(0, m5_count):
    divider()
    print(f"{m5s[i].id} is at: {m5s[i].xCoord, m5s[i].yCoord}")
    m5s[i].generate_luciferin()
    print(f"{m5s[i].id}'s Luciferan Value is: {round(m5s[i].luciferin, 2)}")
    m5s[i].generate_next_direction()
    #print(f"The next direction of {m5s[i].id} is {m5s[i].next_direction}")

divider()

runSimulation(m5s)

dontExit = input()