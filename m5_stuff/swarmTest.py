from m5stack import *
import time
import random
import math
import socket 
import wifiCfg 
import hashlib
import struct
import json
import _thread
import select
from m5ui import * 
from uiflow import * 

# This just tells us where the servos are
servo_0 = unit.get(unit.SERVO, unit.PORTB)
servo_1 = unit.get(unit.SERVO, unit.PORTA)

# Set the coordinates of the central point
center_x = 7
center_y = 7

# Set the scaling factor for the distance
scaling_factor = 3  # 1 increment = 3 feet

# Set the size of each cell in the display
cell_size = 20

# Initialize the display
M5Stack.lcd.clear()

# Draw the coordinate plane
for i in range(16):
    M5Stack.lcd.hline(0, i * cell_size, 240, 0xFFFFFF)
    M5Stack.lcd.vline(i * cell_size, 0, 240, 0xFFFFFF)

# Move the M5Stack in a random direction for a random amount of time
def move_random():
    # Set a random direction and speed
    direction = random.randint(0, 360)
    speed = random.uniform(0.1, 0.3)

    # Calculate the velocity components based on the direction and speed
    vel_x = speed * math.cos(math.radians(direction))
    vel_y = speed * math.sin(math.radians(direction))

    # Scale the velocity components based on the scaling factor
    vel_x *= scaling_factor
    vel_y *= scaling_factor

    # Move the M5Stack for a random amount of time
    duration = random.uniform(1, 3)
    start_time = time.time()
    while time.time() - start_time < duration:
        # Get the distance from the ultrasonic sensor
        distance = M5Stack.uart(1).distance(ultrasonic_pin)

        # If the distance is less than 30cm, stop and move in a new random direction
        if distance < 30:
            return

        # Calculate the new position of the M5Stack based on the velocity components
        new_x = int(center_x + vel_x)
        new_y = int(center_y + vel_y)

        # Draw the M5Stack at the new position
        M5Stack.lcd.rect(new_x * cell_size - cell_size/2, new_y * cell_size - cell_size/2, cell_size, cell_size, 0xFFFFFF)

        # Erase the previous position of the M5Stack
        M5Stack.lcd.rect((new_x - vel_x/scaling_factor) * cell_size - cell_size/2, (new_y - vel_y/scaling_factor) * cell_size - cell_size/2, cell_size, cell_size, 0x000000)

        # Wait for a short amount of time to smooth out the movement
        time.sleep(0.05)

# Move the M5Stack around randomly forever
while True:
    move_random()