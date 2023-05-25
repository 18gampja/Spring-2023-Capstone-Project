import socket 
import wifiCfg 
import hashlib
import struct
import json
import _thread
import select
from m5stack import * 
from m5ui import * 
from uiflow import * 
import random
import network
import time
import math

# List of M5 ips and their corresponding ID
ipID = [{'192.168.8.73' : '1'}, {'192.168.8.220' : '2'}, {'192.168.8.100' : '3'},
        {'192.168.8.217' : '4'}, {'192.168.167', '5'}]

# This just tells us where the servos are
servo_0 = unit.get(unit.SERVO, unit.PORTB)
servo_1 = unit.get(unit.SERVO, unit.PORTC)
ultrasonic = unit.get(unit.ULTRASONIC, unit.PORTA)


# Send message, wait before sending another one too quick
def send(payloadMess):

  #Get Hash and pack payload
  messkey = key+payloadMess 
  hashValueM5 = hashlib.sha256(messkey.encode())
  payloadHash = hashValueM5.digest()
  payload = struct.pack('I%ds32s' % len(payloadMess), len(payloadMess), payloadMess.encode('utf-8'), payloadHash)
  message = payload
  sock.sendto(message, server_address)
  print("Sent message: {}".format(message))
  wait(1)

# Receive message
def receive():
  try:
    recvSocket.settimeout(0)
    recvPayload = recvSocket.recv(1024)
    #Unpacks payload
    recvMessageLength, = struct.unpack('I', recvPayload[:4])
    recvMessage = struct.unpack('%ds' % recvMessageLength, recvPayload[4:4+recvMessageLength])[0]
    recvMessageHash = struct.unpack('32s', recvPayload[4+recvMessageLength:])[0]
    #Creates hash
    checkHash = hashlib.sha256((key + recvMessage.decode()).encode()).digest()
    #Verifies hash
    
    if recvMessageHash == checkHash:
      package = recvMessage.decode()
      lcd.clear()
      lcd.print("\nRecieved Message: " + package, 45, 120, 0xffffff) 
      
      if package.lower() == 'forward':
        randomMove = False
        moveForward()
        return randomMove

      elif package.lower() == 'back':
        randomMove = False
        stop()
        return randomMove

      elif package.lower() == 'stop':
        randomMove = False
        stop()
        return randomMove

      elif package.lower() == 'right':
        randomMove = False
        turnRight()
        return randomMove
  
      elif package.lower() == 'reset':
        randomMove = False
        reset()
        return randomMove
        
      elif package.lower() == 'left':
        randomMove = False
        turnLeft()
        return randomMove

      elif package.lower() == 'swarm':
        randomMove = True
        return randomMove
      
    else:
      lcd.print("Hashes did not match!")
      lcd.print("Recieved: "+ recvMessageHash)
      lcd.print("Calculat: "+ checkHash)
    #This function will not complete until a signal is recieved

  except:
    pass

def moveForward():
  servo_0.write_angle(1)
  servo_1.write_angle(-1)

def moveBackward():
  servo_0.write_angle(-1)
  servo_1.write_angle(1)

def turnLeft():
  rot_deg(270)

def turnRight():
  rot_deg(90)

def stop():
  servo_0.write_angle(90)
  servo_1.write_angle(90)
  

def reset():
  machine.reset()  

def rot_deg(deg): #deg is in degrees clockwise
  
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
          if current_direction < 0:
            current_direction += 360

      else:
          servo_0.write_angle(180) #right
          servo_1.write_angle(180)
          d = deg
          current_direction = current_direction + deg
          if current_direction > 360:
            current_direction -= 360
      slep = d*.3931/90 #works, +-1 deg
      time.sleep(slep)
      if current_direction > 360:
        current_direction -= 360
    
    
def turnAround():
    servo_0.write_angle(0) #180
    servo_1.write_angle(0)
    slep = 1.615 #works, +-1 deg

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

def scan_wifi():
    for i in beacons:
        ssid = i[0]
        rssi = i[3]
        #lcd.print("\nAccess point:" + str(ssid))
        #lcd.print("\nSignal strength:"+ str(rssi))
        

rssi_ref = -55
path_loss = 2
side_length = 5

def get_distance():
    distances = []
    for rssi in beacons:
        distance = math.pow(10,(rssi_ref - rssi[3])/(10 * path_loss))
        distances.append([rssi[0].decode(), distance])
    return distances
    
def get_coordinate(beacon1,beacon2):
    """
    Triangulate the position of an object utilizing area
    """
    c = side_length
      
    a = beacon1[1] 
    b = beacon2[1]
    
    a = abs(a)
    b = abs(b)
    s = (a + b + c)/2
    area = math.sqrt(abs(s*(s-a)*(s-b)*(s-c))) #filter out negatives instead of abs in the future
    height = 2*(area/c)
    yd = height
    
    if (beacon1[0] == "topleft" and beacon2[0] == "topright"): #top two points
        yd = c - yd
        xd = math.sqrt(abs(a**2 - yd**2))
    elif (beacon1[0] == "topright" and beacon2[0] == "topleft"):
        yd = c - yd
        xd = math.sqrt(abs(b**2 - yd**2))
    elif (beacon1[0] == "topleft" and beacon2[0] == "bottomleft"): #left side
        xd = yd
        yd = math.sqrt(abs(b**2 - yd**2))
    elif (beacon1[0] == "bottomleft" and beacon2[0] == "topleft"):
        xd = yd
        yd = math.sqrt(abs(a**2 - yd**2))
    elif (beacon1[0] == "topright" and beacon2[0] == "bottomright"): #right side
        xd = c - yd
        yd = math.sqrt(abs(b**2 - yd**2))
    elif (beacon1[0] == "bottomright" and beacon2[0] == "topright"):
        xd = c - yd
        yd = math.sqrt(abs(a**2 - yd**2))
    elif (beacon1[0] == "bottomleft" and beacon2[0] == "bottomright"):
        xd = math.sqrt(abs(a**2 - yd**2))
    else:
        xd = math.sqrt(abs(b**2 - yd**2))
    
    return(xd,yd)
    
def avg_coords(coords):
  if(len(coords) == 0):
    return (6, 6)
    
  #lcd.print("\nBeacon Count: "+str(len(coords)))
    
  tot_x = 0
  tot_y = 0
  
  for eachCoord in coords:
    tot_x = tot_x + eachCoord[0]
    tot_y = tot_y + eachCoord[1]
  
  return [(tot_x/len(coords)), (tot_y/len(coords))]
    

def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num
    
def isDiagnolBeacons(beacon1, beacon2):
  if (beacon1[0] == "topleft") and (beacon2[0] == "bottomright"):
    return True
  elif (beacon2[0] == "topleft") and (beacon1[0] == "bottomright"):
    return True
  elif (beacon1[0] == "bottomleft") and (beacon2[0] == "topright"):
    return True
  elif (beacon2[0] == "bottomleft") and (beacon1[0] == "topright"):
    return True
  else:
    return False

  #1855
  
def isValidCoord(coord):
   if (coord[0] > side_length) or (coord[1] > side_length):
      return False
   elif (coord[0] < 0) or (coord[1] < 0):
      return False
   else:
      return True
  
#Setup ======================================
setScreenColor(0xFF2222) 
wifiCfg.autoConnect(lcdShow=True) 
  
key = "password" #must be same key for destination
deviceIP = '192.168.1.119' #change IP's as needed
destinationIP = '192.168.1.197'

# Set up the server address and port number
server_address = (destinationIP, 8000)

# Create a socket for sending and receiving messages
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setblocking(False)

dataDict = {"owner": "", "xPos": "", "yPos": "", "foundObject": "False", "active": "True"}

count = 0
while count < len(ipID):
    
    try:
        dataDict["owner"] = ipID[count][deviceIP]
    
    except:
        pass
    count += 1
#set payloadMess to a string for testing purposes

#Setup sockets
sendingSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sendingSocket.connect((destinationIP, 5000)) #takes destination's IP
recvSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
recvSocket.bind((deviceIP, 8080)) #takes this M5's IP
recvSocket.setblocking(False)

current_direction = 0
randomFail = 0

rotations = [15, 30, 45, 240, 265, 280]
#================================================

# Sends an established connection message
send('Connection established')

#Main loop
while True: 
  
  sent = False

  wlan = network.WLAN(network.STA_IF)
  if not wlan.active():
      wlan.active(True)
  
  bssid = ["topleft", "topright", "bottomleft", "bottomright"]
  beacons = []
  coords = []
  accesspoints = wlan.scan()
  
  for i in accesspoints:

      if i[0].decode() in bssid:
          beacons.append(i)  
  distances = get_distance()
  
  for j in range(len(distances)):
    for k in range(len(distances)):
      if (k != j and not isDiagnolBeacons(distances[j],distances[k])):
        coord = get_coordinate(distances[j], distances[k])
        if isValidCoord(coord):
            coords.append(coord)
        
  final_coord = avg_coords(coords)
  
  if (btnA.isPressed()):
    send("Hello!")

  test = receive()
  
  distance = ultrasonic.distance

  if distance < 60 and distance > 0:
    stop()
    moveBackward()
    time.sleep(1)
    stop()
    time.sleep(3)
    moveForward()
    
    time.sleep(1)
    distance = ultrasonic.distance

  if distance < 60 and distance > 0:
    stop()
    dataDict["xPos"] = final_coord[0]
    dataDict["yPos"] = final_coord[1]
    dataDict["foundObject"] = True
    lcd.print(dataDict["foundObject"])
    sent = True
    moveBackward()
    time.sleep(1)
    stop()
    send(json.dumps(dataDict))

  try:
  
    if random.randint(0, 10) >= 5:
      rot_deg(rotations[random.randint(0, 5)])

    moveForward()
  
  except:
    pass

  if(btnB.isPressed()):
    machine.reset()
  

  if sent == False:
    dataDict["xPos"] = final_coord[0]
    dataDict["yPos"] = final_coord[1]
    dataDict["foundObject"] = False
    send(json.dumps(dataDict))
  scan_wifi()
  
  time.sleep(1)