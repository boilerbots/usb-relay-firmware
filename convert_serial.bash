#!/bin/bash

if [ $#  -ne 1 ]; then
  echo "$0 [serial]"
  exit
fi

SERIAL=$1

echo "create serial rom file"
./create_serial_rom.py --serial ${SERIAL} /tmp/serial.txt
echo "convert rom file to intel hex"
srec_cat /tmp/serial.txt -ascii_hex -output /tmp/serial.hex -intel
echo "program to device"
avrdude -P /dev/ttyUSB0 -c jtagkey -p t45 -U eeprom:w:/tmp/serial.hex

