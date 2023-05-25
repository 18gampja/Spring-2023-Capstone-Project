import socket
import hashlib
import struct
import socket
import time
import json
import os
import threading
from pymongo import MongoClient

try:
     client = MongoClient(os.getenv('SERVER_HOST'), 27017)
     db = client.db
except Exception as e:
     print("Error: " + str(e))

def updateM5(query, new_data):
	collection = db.m5
	data_id = collection.update_one(query, new_data)

def insertPOI(new_data):
	collection = db.algo
	data_id = collection.insert_one(new_data)
	#{"poi":"coord"} 


ipID = [{'192.168.8.73' : '1'}, {'192.168.8.220' : '2'}, {'192.168.8.100' : '3'}, {'192.168.8.217' : '4'}, {'192.168.1.119', '5'}]
key = "password"
turtleIP = '192.168.8.209' #change IP's as needed
compIP = '192.168.1.197'

# Fix first ip here
m5stacks = [('192.168.8.73', 8000), ('192.168.1.247', 8001), ('192.168.8.100', 8002), ('192.168.8.217', 8003), ('192.168.1.119', 8004)]
# m5stacks = [('192.168.1.247', 8005)]

recvSockets = []
# sendSockets = []
pointsOfInterest = []


# This will theoretically connect all m5s at the same time

count = 0

for m5 in m5stacks:

    recv_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    recv_sock.bind((compIP, m5[1]))
    recv_sock.setblocking(False)
    recvSockets.append(recv_sock)
    
    # send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # send_sock.connect((m5[0], 8080))
    # sendSockets.append(send_sock)
    count += 1

# Not sure what to do with this yet but it's here
M5_StickCam = '10.254.239.1'

# Receives and unpacks the message from m5
def recvMsg():

    for i, recv_sock in enumerate(recvSockets):
        try:
            data, addr = recv_sock.recvfrom(1024)

            # print(f'Received message from {addr}: {data}')
            recvMessageLength, = struct.unpack('I', data[:4])
            try:
                recvMessage = (struct.unpack('%ds' % recvMessageLength, data[4:4+recvMessageLength])[0])
                recvMessageHash = struct.unpack('32s', data[4+recvMessageLength:])[0]
                checkHash = hashlib.sha256((key + recvMessage.decode()).encode()).digest()
                if recvMessageHash == checkHash:
                    
                    interpMess = json.loads(recvMessage.decode())
                    
                    # # Message interpretation here
                    if interpMess["foundObject"] == True:
                        pointsOfInterest = [interpMess["xPos"], interpMess["yPos"]]
                        print(pointsOfInterest)
                        insertPOI({"poi" : str(pointsOfInterest)})
                        updateM5({"owner": int(interpMess["owner"])}, {"xPos": interpMess["xPos"], "yPos": interpMess["yPos"], "foundObject": interpMess["foundObject"],"active": interpMess["active"]})
                    else:
                        updateM5({"owner": int(interpMess["owner"])}, {"xPos": interpMess["xPos"], "yPos": interpMess["yPos"], "foundObject": interpMess["foundObject"],"active": interpMess["active"]})
                        print(interpMess)
                    time.sleep(1)

                else:
                    print("Hashes did not match!")
                    print("Recieved: ", recvMessageHash)
                    print("Calculated: ", checkHash)

            except Exception as e:
                print(e)
            
        except Exception as e:
            pass

# Declaring our threads then starting them
receiveThread = threading.Thread(target = recvMsg)
receiveThread.start()

while True:

    if (receiveThread.is_alive() == False):
         receiveThread.join()
         time.sleep(1)
         receiveThread = threading.Thread(target = recvMsg)
         receiveThread.start()
