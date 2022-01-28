#!/usr/bin/env python3

"""This script is created for Whiteboard crypto to solve the monthly NFT puzzle.
This script outputs the flag needed to solve Puzzle 03 for the December 2021 puzzle.
This puzzle took the longest to solve. For files 0.png and 4095.png there are some
appended bytes. If you take both bytes and you compare them, the matching bytes
represents the flag.
"""

__author__ = "Whiteboard Crypto"
__copyright__ = "Copyright 2021, Whiteboard Crypto"
__credits__ = ["Theodore"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Whiteboard Crypto"
__email__ = "whiteboardcryptoteam@gmail.com"
__status__ = "Development"

def main():

  flag = []

  with open("extractedBytesImage0.bin", "rb") as f1, open("extractedBytesImage4095.bin", "rb") as f2:
    byte1 = f1.read(1)
    byte2 = f2.read(1)

    while byte1:
      if (byte1 == byte2):
        print (byte1)
      byte1 = f1.read(1)
      byte2 = f2.read(1)

if __name__ == '__main__' :
  main()
