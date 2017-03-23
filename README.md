# nfc2server

nfc2server is an open-source software for the Raspberry Pi that detects NFC/RFID tags and sends HTTP requests when a new tag is detected or removed.

## About
nfc2server is developed by [Interaktiva rum (Interactive rooms)](http://www.interaktivarum.se/en) and is initiated and funded by [The Nordic Museum](http://www.nordiskamuseet.se/en) in Sweden.

### Museum exhibitions
nfc2server was designed and developed as part of the exhibition [Nordic Light](http://www.nordiskamuseet.se/en/utstallningar/nordic-light), on display from 2016 at the Nordic Museum.
When entering the exhibition, each visitor gets a LED candlestick that she carries with her throughtout the exhibition and uses to switch on and off lights by simply holding it against ”light switch surfaces”.
The candlestick contains a small NFC tag.
The active hardware (see list below) is hidden behind the ”light switch surfaces” and detects whenever a tag/candlestick is held against it.
When a NFC tag is detected a message is sent to the server (as a HTTP request) with tag and station/surface IDs, upon which the correct action can be carried out, for instance *turn on the red spotlight*.

Any museum/science center (or simply anyone that wants to) is encouraged to download the software code and use it in their own interactive projects! If you do, please let us know - we will be happy to hear about your work and help share your project!

*Note*: nfc2server does not provide the server side code to receive and handle the HTTP requests - it simply sends a message to the server with the information specified by the user. The server side code will be provided in a separate repository.

## Hardware

The following hardware is needed in order to run the application.

### Raspberry Pi
http://raspberrypi.org

Any model should work, but these are the models that are tested and confirmed to be working:
* Raspberry Pi 3 Model B v1.2

### Adafruit PN532 NFC/RFID controller breakout board
http://www.adafruit.com/products/364

Any version should work, but these are the models that are tested and confirmed to be working:
* Adafruit PN532 NFC/RFID controller breakout board - v1.6

### NFC/RFID tag
Several tag types should work; these are the tag types that are tested and confirmed to be working:
* Adafruit 13.56MHz RFID/NFC Clear Tag - 1KB
* Adafruit 13.56MHz RFID/NFC Card - 1KB
* Adafruit Micro NFC/RFID Transponder - NTAG203 13.56MHz

### GPIO breakout wires and soldering equipment
In order to connect the PN532 breakout board to the Raspberry Pi you need six GPIO breakout wires.
For the best result, you also need to do some basic soldering - if you are new to soldering, see this great guide by Adafruit: http://learn.adafruit.com/adafruit-guide-excellent-soldering

## Setup

### Raspberry Pi and PN532 breakout board
Although this is not a Minecraft related project, Adafruit provides a great Minecraft related beginners tutorial on how to download and setup the Raspberry Pi with the PN532 breakout board: http://learn.adafruit.com/raspberry-pi-nfc-minecraft-blocks. 
The following terminal commands should properly install the dependency libraries:
```
sudo apt-get update
sudo apt-get install build-essential python-dev git
cd ~
git clone https://github.com/adafruit/Adafruit_Python_PN532.git
cd Adafruit_Python_PN532
sudo python setup.py install
``` 
but we recommend to follow the full tutorial to properly setup the hardware and dependencies.

### Download the source files
The project source files are publically available at: http://github.com/nordicmuseum/nfc2server. No installation is needed, just download the files to your prefered directory.

Clone with Git:
```
git clone https://github.com/nordicmuseum/nfc2server.git
``` 

### Server
The server can either be online or on a local network. For instructions on how to setup your own local server, please refer to http://apache.org. 
For instructions how to setup PHP to parse the request data, please refer to http://php.net.

If you do not have your own server, you can use a HTTP request inspect service, such as http://requestb.in, for testing and verifying your requests.

## Settings: settings.json

* **server** - server settings
	* **host** *optional (leave empty)* - the server host name
	* **ip** - *optional (leave empty)* - the server IP address
	* **endpoint** - the endpoint (without the server host name) for the HTTP request, e.g. *api/touches*
* **staticUserData** *optional (leave empty)* - static data to be sent to the server with each message

## Run

### Start the application
#### From the terminal
* Browse to the nfc2server directory 
* Run the following command: ``` sudo python nfc2server.py ```

#### From the Linux desktop
* Browse to the nfc2server directory
* Double-click on the nfc2server.py script and select *Run in terminal*

The terminal should output: Application is running. Ready.

### Send NFC data
* When you hold a NFC tag close to the PN532 breakout board, the terminal should output: *Found card with UID: xxxx*
* Each time a new tag is detected or an old tag is removed an HTTP request is sent to the server with the following data: 
	* The performed action: *touch* or *remove*
	* All static user data, as defined in settings.json
	* The NFC tag UID
	* The client time in format YYYY-MM-DD HH:MM:SS
* The terminal outputs the server response message.

## Contact

### Bug reports
Please use the Issues tab on Github https://www.github.com/nordicmuseum/nfc2server/issues to report any bugs or issues that you encounter.

### Feature requests
If you have any requests or suggestions on how nfc2server can be improved or even customized to suit your project needs, please send an email to: martin@interaktivarum.se, robert.ziherl@nordiskamuseet.se and/or aron.ambrosiani@nordiskamuseet.se.

### Share your project
Are you using nfc2server in your own project? Great! We will be happy to hear about your work and to help share your project!
Please send an email to martin@interaktivarum.se, robert.ziherl@nordiskamuseet.se and/or aron.ambrosiani@nordiskamuseet.se.

