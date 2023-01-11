# Automatic Floodlights for 3D Printer (Octoprint server)
Python scripts that turns on some LEDs to get better light in timelapse recordings.
This version uses the Octoprint Event Manager so there is no need for weird configurations.

## Requirements
### Software
* Python 3 (Should be installed by default on Raspbian - [How to install](https://www.raspberrypi.org/forums/viewtopic.php?t=181480)) 
* Python 3 RPi.GPIO package ```sudo pip install RPi.GPIO```
* (Obviously) an Octoprint server
* Works fine on Raspberry Pi OS Bullseye (Debian 11)

### Hardware
* Raspberry Pi
* 1 Channel 5V Relay [(Something like this)](https://www.amazon.com/dp/B00VRUAHLE/)
* A breadboard
* Some components (wires, LEDs and a resistor) to make the lamp

## Wiring scheme
There are two ways to wire this thing.
The first one is the recommended way.
The second one is an alternate way if, for example, you are using a fan on your Pi alongside these LEDs and don't have any spare 5V pins.
In any case, wiring is fairly straight-forward. 

### Common parts
#### LEDs
1. Put 5 LEDs on the breadboard
1. Connect them in parallel (something like in the pictures below)
1. Add a 10Ω resistor on one side (in this case I put it on the positive side - red wires on the breadboard in the images below)
1. Connect a wire from the resistor to a 5V pin on your Raspberry Pi (red wire going from the breadbord to the Raspberry Pi in the images below)

#### Relay
1. Connect the NO to the negative side of the lamp (check the pictures below, it's the cyan wire going from the relay to the breadbord)
1. Connect the signal pin on the relay to pin 7 on the Raspberry Pi (check the pictures below, it's the cyan wire going from the Raspberry Pi to the relay)
1. Connect the - pin on the relay to a ground header on your Raspberry Pi
1. Connect the COM to another ground header on your raspberry Pi

### 1 - Default
![Wiring scheme](https://github.com/StoKatze/Automatic-Floodlights-For-3D-Printer-Octoprint-server-/blob/main/Wiring%20Scheme/Lampadina%20Stampante%203D_bb_normal.png)
* Connect the + pin on the relay to the other unused 5V pin on your Raspberry Pi (red wire going from the Raspberry Pi to the relay in the picture above)

If you don't have a second 5V pin available, please follow the alternate wiring instructions.

### 2 - Alternate
![Wiring scheme Alternate](https://github.com/StoKatze/Automatic-Floodlights-For-3D-Printer-Octoprint-server-/blob/main/Wiring%20Scheme/Lampadina%20Stampante%203D_alternate.png)
* Connect the + pin on the relay to a 3.3V pin on your Raspberry Pi (white cable in the picture above)

Please note that if you have a fan, the ground pin next to the 5V one might be already occupied. This is not an issue since you can use any other ground pin.

## Usage 
Download the python scripts inside a directory, edit some parameters and set up octoprint to execute it when a print stars or ends or fails.

### Detailed instructions
#### Configuring the python script
1. Create a new directory and ```CD``` into it
1. Download the python scripts in this directory
1. Edit it using nano or any other text editor ```nano OctoprintLEDON.py```
1. Check and, if you are using another pin for the relay signal, edit line 6
1. Save and exit
1. Repeat steps 3, 4 and 5 for file OctoprintLEDOFF.py

#### Configuring Octoprint
1. Open your Octoprint Web UI
1. Open the settings (wrench icon)
1. Choose "Event Manager" on the left sidebar
1. Add these events (click close when you're done filling all the fields - also replace ```<SCRIPTS-PATH>``` with the absolute path of the scripts directory on your system):
* Event -> ```PrintStarted``` / Command -> ```python3 <SCRIPTS-PATH>/OctoprintLEDON.py``` / Type -> ```System``` / Enabled -> ```Checked```
* Event -> ```PrintDone``` / Command -> ```python3 <SCRIPTS-PATH>/OctoprintLEDOFF.py``` / Type -> ```System``` / Enabled -> ```Checked```
* Event -> ```PrintFailed``` / Command -> ```python3 <SCRIPTS-PATH>/OctoprintLEDOFF.py``` / Type -> ```System``` / Enabled -> ```Checked```
5. Click Save
6. Restart your Octoprint server (either via the web UI or from the Raspberry Pi CLI)

## Thank you
I don't know much about electronics so I tried making this circuit as easy as possible. Suggestions are welcome.
