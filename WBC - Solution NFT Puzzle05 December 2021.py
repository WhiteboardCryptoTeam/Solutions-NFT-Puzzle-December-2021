#!/usr/bin/env python3

"""This script is created for Whiteboard crypto to solve the monthly NFT puzzle.
This script outputs the flag needed to solve Puzzle 05 for the December 2021 puzzle.
For this puzzle you had to find the image with a ZIP file appended to it (667.png).
A compressed file starts with PK, so i should be easy to identify that the appended
bytes is a compressed file. If you extract the appended bytes and name it to .zip, you
can try to extract the compressed file. Unfortunately, the zip file is password-protected.
Since the password can't be found anywhere, you have to brute-force the password. I used
a password which can be found in most wordlists "comicbooks". Extracting the file and you
will find the flag.

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

  

if __name__ == '__main__' :
  main()
