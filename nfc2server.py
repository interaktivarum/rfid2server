#!/usr/bin/env python

import Adafruit_PN532
import binascii, sys, time, json
from functions import sendRequest 

read_sleep = 0.1;

# Instantiate and configure the PN532
pn532 = Adafruit_PN532.PN532(cs=18, sclk=25, mosi=23, miso=24)
pn532.begin()
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
print('Application running')
while True:
    
    # Read card, if available
    uid = pn532.read_passive_target()

    #If tag uid has changed from previous iteration 
    if uid_last != uid:

        # If old tag has been removed
        if uid_last != None:
            print('Removed card with UID: 0x{0}'.format(binascii.hexlify(uid_last)))
            # Send HTTP request to server 
            sendRequest(ip,host,endpoint,static_user_data,uid_last,"remove")

        # If new tag is detected
        if uid != None:
            print('Found card with UID: 0x{0}'.format(binascii.hexlify(uid)))
            # Send HTTP request to server  
            sendRequest(ip,host,endpoint,static_user_data,uid,"touch")

        #Update uid_last
        uid_last = uid

    time.sleep(read_sleep)
        
sys.exit(0)