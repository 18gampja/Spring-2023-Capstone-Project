# Import the necessary libraries
import random
from m5stack import *
from m5ui import *
import unit
import math

# Initialize the M5 device
m5setup()

# Instantiate the servos
servo_0 = unit.get(unit.SERVO, unit.PORTB)
servo_1 = unit.get(unit.SERVO, unit.PORTA)

def moveForward():
  servo_0.write_angle(1)
  servo_1.write_angle(-1)

# Define a function to move the servos randomly
def move_random():
  # Generate a random angle for each servo
  angle_0 = random.randint(0, 180)
  angle_1 = random.randint(0, 180)
  
  # Move the servos to the selected angles
  servo_0.write_angle(angle_0)
  servo_1.write_angle(angle_1)

  def rot_deg(deg): #deg is in degrees clockwise
    global servo_0, servo_1
    global current_direction
    
    if deg != 0 and deg % 360 == 0:
        turnAround()
    
    else:
        deg %= 360

        if deg > 180:
            servo_0.write_angle(0) #left
            servo_1.write_angle(0)
            d = 360 - deg
            current_direction = current_direction + deg

        else:
            servo_0.write_angle(180) #right
            servo_1.write_angle(180)
            d = deg
            current_direction = current_direction - deg
        slep = d*.3931/90 #works, +-1 deg
        time.sleep(slep)
        stop()
        if current_direction < 0:
          current_direction = current_direction + 360
        lcd.print("\n" + str(current_direction) + " degrees")
    
    
def turnAround():
    global servo_0, servo_1
    servo_0.write_angle(0) #180
    servo_1.write_angle(0)
    slep = 1.615 #works, +-1 deg
    time.sleep(slep)
    stop()

def get_angle(curr_coord, target_coord):
    # Calculate the difference between the points
    x1 = curr_coord[0]
    y1 = curr_coord[1]
    x2 = target_coord[0]
    y2 = target_coord[1]
    dx = x2 - x1
    dy = y2 - y1
    
    # Calculate the angle in radians
    radians = math.atan2(dy, dx)
    
    # Convert radians to degrees
    degrees = math.degrees(radians)
    
    # Ensure the angle is between 0 and 360 degrees
    if degrees < 0:
        degrees += 360
        
    return degrees

# Loop through and move the servos randomly
while True:
  move_random()
  wait_ms(500)
