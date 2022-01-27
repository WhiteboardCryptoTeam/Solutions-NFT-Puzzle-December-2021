#!/usr/bin/env python3

"""This script is created for Whiteboard crypto to solve the monthly NFT puzzle.
This script outputs the flag needed to solve Puzzle 01 for the December 2021 puzzle.

The "File Modification Date/Time" of some images are different than others. When you check
the modification date/time, the date for some images its 01:00:00 and 01:01:00. The minute
represents a 0 or 1. Once you get all the 0's and 1's, you will get the flag in binary form.
"""

__author__ = "Whiteboard Crypto"
__copyright__ = "Copyright 2021, Whiteboard Crypto"
__credits__ = ["Theodore"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Whiteboard Crypto"
__email__ = "whiteboardcryptoteam@gmail.com"
__status__ = "Development"

import os, time

def main():

  flag = ""

  imageNumbers = [46, 54, 59, 64, 66, 76, 81, 84, 101, 107, 121, 127, 138, 144, 166, 180, 201, 222, 244, 250, 256, 280, 288, 290, 300, 322, 344, 360, 366, 380, 381, 389, 410, 422, 444, 446, 460, 468, 480, 499, 506, 510, 520, 522, 540, 546, 550, 575, 580, 588, 591, 600, 610, 665, 680, 691, 702, 709, 722, 740, 744, 760, 777, 782, 801, 822, 825, 840, 844, 860, 877, 888, 900, 911, 922, 930, 933, 940, 950, 966, 1090, 1100, 1122, 1144, 1180, 1190, 1210, 1244, 1280, 1301, 1310, 1344, 1450, 1490, 1560, 1590, 1666, 1690, 1700, 1801, 1888, 1901, 1977, 1999, 2007, 2021, 2080, 2083, 2091, 2096, 2099, 2101, 2110, 2121, 2144, 2150, 2166, 2169, 2176, 2180, 2203, 2210, 2233, 2244, 2251, 2266, 2278, 2290, 2300, 2310, 2340, 2344, 2350, 2355, 2366, 2367, 2380, 2383, 2391, 2394, 2398, 2399, 2401, 2411, 2414, 2418, 2423, 2425, 2431, 2433, 2442, 2451, 2466, 2478, 2480, 2484, 2491, 2493, 2498, 2499, 2510, 2513, 2544, 2566, 2577, 2581, 2584, 2592, 2609, 2613, 2644, 2672, 2681, 2693, 2698, 2701, 2703, 2709, 2713, 2718, 2721, 2730, 2734, 2741, 2753, 2758, 2761, 2771, 2781, 2786, 2790, 2793, 2803, 2813, 2823, 2833, 2838, 2841, 2846, 2849, 2856, 2859, 2863, 2871, 2876, 2884, 2888, 2893, 2901, 2912, 3001, 3013, 3024, 3037, 3057, 3080, 3209, 3224, 3233, 3269, 3290, 3291, 3296, 3300, 3490, 3493, 3511, 3523, 3544, 3569, 3612, 3624, 3801, 3813, 3858, 3862, 3877, 3901, 3913, 4000]

  for x in imageNumbers:
    modTimesinceEpoc = os.path.getmtime("../images/{}.png".format(x))
    modificationTime = time.strftime('%M', time.localtime(modTimesinceEpoc))
    flag += modificationTime[1:]

  print (flag)

if __name__ == '__main__' :
  main()
