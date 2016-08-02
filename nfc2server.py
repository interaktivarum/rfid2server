#!/usr/bin/env python

import binascii
import sys

import Adafruit_PN532
import requests, time, json

read_sleep = 0.1;

# Create an instance of the PN532 class.
pn532 = Adafruit_PN532.PN532(cs=18, sclk=25, mosi=23, miso=24)

# Call begin to initialize communication with the PN532.  Must be done before
# any other calls to the PN532!
pn532.begin()

# Get the firmware version from the chip and print(it out.)
#ic, ver, rev, support = pn532.get_firmware_version()
#print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))

# Configure PN532 to communicate with MiFare cards.
pn532.SAM_configuration()

#Read json
print("Data folder: " + sys.path[0])
with open(sys.path[0]+'/settings.json') as data_file:
    settings = json.load(data_file)

#Set user variables
ip = settings["server"]["ip"]
host = settings["server"]["host"]
endpoint = settings["server"]["endpoint"]
static_user_data = settings["staticUserData"];
uid = None;
uid_last = uid;

# Main loop to detect cards and read a block.
print('Waiting for MiFare card...')
while True:
    
    # Check if a card is available to read.
    uid = pn532.read_passive_target()
    # Try again if no card is available.
    if uid is None:
        time.sleep(read_sleep)
        continue
    print('Found card with UID: 0x{0}'.format(binascii.hexlify(uid)))

    #If new uid was detected
    if uid_last != uid:

        #Update uid
        uid_last = uid
        
        #Send user data to server   
        params = {'static':static_user_data, 'dynamic':{'chipId':binascii.hexlify(uid)}}

        if ip != '':
            #Post request with ip and host name
            r = requests.post('http://' + ip + '/' + endpoint, params=json.dumps(params), headers={'host': host})        
        else:
            #Post request with host name
            r = requests.post('http://' + host + '/' + endpoint, params=json.dumps(params), headers={})

        if r.status_code == 200:
            print r.content
        else:
            print 'REQUEST ERROR! Status code: ' + str(r.status_code)
            print r.content

    time.sleep(read_sleep)
        
sys.exit(0)
