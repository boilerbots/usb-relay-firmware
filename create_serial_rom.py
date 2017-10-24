#!/usr/bin/python3

import sys
import os
import argparse
import string
import array
from struct import *


def main(argv=None):

  if argv is None:
      argv = sys.argv

  parser = argparse.ArgumentParser()
  parser.add_argument('--serial', dest='serial', type=str, help='The relay serial number, 6 characters')
  parser.add_argument('output', type=argparse.FileType('w'), default=sys.stdout, help='output file name')


  args = parser.parse_args()

  print("serial=", args.serial[0:6])

  crc = int(0)
  s = bytes(args.serial[0:6], 'utf-8')
  packed_data = pack('<{}sB'.format(len(args.serial)), s, 0)

  args.output.write('\n')
  for c in packed_data:
    args.output.write('{0:02x} '.format(c)),
  args.output.write("\n")
  args.output.write('')
  args.output.close()

if __name__ == '__main__':
  main()

