This is a basic firmware for the cheap USB relay boards that are sold on eBay
and report themselves as being from www.dcttech.com. They're based on an Atmel
ATtiny chip and run [V-USB](https://www.obdev.at/products/vusb/) as the core of
their firmware. 

This project deviates from the basic firmware in 2 ways.

* Implement reading the serial number from the eeprom area.
* Added a watchdog timer

The HID driver sends a byte array to the device. Use the first byte to control the state of the relay, byte[0]=0 de-energize and byte[0]=1 energize.
The second byte enables a watchdog timer count down with the value in seconds, byte[1]=5 would time out after approximately 5 seconds. The relay opens when decrementing to zero so if you leave the timer at zero it is effectively disabled.

`apt install avr-libc avrdude` should install the appropriate build requirements on Debian (`gcc-avr` will be automatically pulled in) assuming you already have `build-essential` installed for `make`.

`make` will then build you a main.hex which you can program to your device using
`avrdude`. With my cheap [USBASP](http://www.fischl.de/usbasp/) I use:

    avrdude -P /dev/ttyUSB0 -c usbasp -p t45 -U flash:w:main.elf:e


Pin outs on the 1 port relay board look like:

<pre>
  |RELAY|
  +-----+               [USBASP connections]
           o RESET      RST
           o SCK        CLK
   +--+    o MISO       MISO
   |AT|    □ MOSI       MOSI
   +--+
           □ 5V         +5V
           o GND        GND
  | USB |
  +-----+
</pre>

USB D- is connected to Port B pin 1, USB D+ to Port B pin 2 (INT0) and the relay is hanging off Port B pin 3.

Given that V-USB is GPLv2+ or commercial all of my code is released as GPLv3+, available at [https://the.earth.li/gitweb/?p=usb-relay-firmware.git;a=summary](https://the.earth.li/gitweb/?p=usb-relay-firmware.git;a=summary) or on GitHub for easy whatever at [https://github.com/u1f35c/usb-relay-firmware](https://github.com/u1f35c/usb-relay-firmware)
