#!/usr/bin/env python

import Adafruit_PN532
import binascii, sys, time, json
from functions import sendToServer 

read_sleep = 0.1;

# Create an instance of the PN532 class.
pn532 = Adafruit_PN532.PN532(cs=18, sclk=25, mosi=23, miso=24)

# Call begin to initialize communication with the PN532.
pn532.begin()

# Configure PN532 to communicate with MiFare cards.
pn532.SAM_configuration()

#Read json
print("Data folder: " + sys.path[0])
with open(sys.path[0]+'/settings.json') as data_file:
    settings = json.load(data_file)

#Static user data
ip = settings["server"]["ip"]
host = settings["server"]["host"]
endpoint = settings["server"]["endpoint"]
static_user_data = settings["staticUserData"];

#Tag uid variables
uid = None;
uid_last = uid;

# Main loop to detect cards and send server requests
print('Waiting for MiFare card...')
while True:
    # Check if a card is available to read.
    uid = pn532.read_passive_target()

    if uid != None:
        print('Found card with UID: 0x{0}'.format(binascii.hexlify(uid)))

    #If tag uid has changed from previous iteration 
    if uid_last != uid:

        #If old tag has been removed
        if uid_last != None:
            #Send HTTP request to server 
            sendToServer(ip,host,endpoint,static_user_data,uid_last,"remove")

        #If new tag is detected
        if uid != None:
            #Send HTTP request to server   
            sendToServer(ip,host,endpoint,static_user_data,uid,"touch")

        #Update uid_last
        uid_last = uid

    time.sleep(read_sleep)
        
sys.exit(0)
