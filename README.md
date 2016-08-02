# nfc2server

nfc2server listens for nfc sensor data and sends a server message when new data is received.

##Hardware

###Raspberry Pi
http://raspberrypi.org
Any model should work, but these are the models that are tested and confirmed to be working:
* Raspberry Pi 3 Model B v1.2

###Adafruit PN532 NFC/RFID controller breakout board
http://www.adafruit.com/products/364

###NFC/RFID tag
Several tag types should work; these are the tag types that are tested and confirmed to work:
* Adafruit 13.56MHz RFID/NFC Clear Tag - 1KB
* Adafruit 13.56MHz RFID/NFC Card - 1KB
* Adafruit Micro NFC/RFID Transponder - NTAG203 13.56MHz

###*GPIO breakout wires and soldering equipment*
In order to connect the PN532 breakout board to the Raspberry Pi you need six GPIO breakout wires and preferably need to do some soldering. See below for details and setup instructions.

##Setup

###Raspberry Pi and PN532 breakout board
Although this is not a Minecraft related project, Adafruit provides a great Minecraft related beginners tutorial on how to download and setup the Raspberry Pi with the PN532 breakout board: http://learn.adafruit.com/raspberry-pi-nfc-minecraft-blocks. Please follow the tutorial's steps to properly setup the hardware and dependency libraries. 

###Download the source files
The project source files are publically available at: http://github.com/interaktivarum/nfc2server. No installation is needed, just download the files to your prefered directory.

###Server
The server can either be online or limited to a local network. For instructions on how to setup your own local server, please refer to http://apache.org. 
For instructions how to setup PHP to parse the request data, please refer to http://php.net.

##Settings: settings.json

* **server** - server settings
	* **host** *optional (leave empty)* - the server host name, e.g. *interaktivarum.se* or *DESKTOP-FR67JBO*   
	* **ip** - *optional (leave empty)* - the server IP address, e.g. *46.30.213.125* or *192.168.1.110*
	* **endpoint** - the endpoint for the request, e.g. *endpoints/request_test.php*
* **staticUserData** *optional (leave empty)* - static data to be sent to the server with each message
	* **userData0** - any number, string, boolean, array, object or null
	* **userData1** - any number, string, boolean, array, object or null
	* **...**
	* **userDataX** - any number, string, boolean, array, object or null

##Run

### Start the application
#### From the terminal
* Browse to the nfc2server directory 
* Run the following command: ``` sudo python nfc2server.py ```

#### From the Linux desktop
* Browse to the nfc2server directory
* Double-click on the nfc2server.py script and select *Run in terminal*

### Send NFC data
* Hold a NFC tag close to the PN532 breakout board, the terminal should write: *Found card with UID: xxxx*
* Each time a new tag is detected or an old tag is removed a request is sent to the server with the following data: 
	* The performed action: *touch* or *remove*
	* All static user data, as defined in settings.json
	* The NFC tag UID
	* The client time in format YYYY-MM-DD HH:MM:SS
* The terminal writes the server response message. 