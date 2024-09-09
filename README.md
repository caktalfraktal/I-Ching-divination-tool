"threecoins.exe" as a standalone program or download the whole code with "threecoins.py"


This program simulates tossing 3 virtual coins using the os.urandom function, which generates truly random "coin" flips of 0 (tails) or 1 (heads).

Coin Flip Values:
If the flip is 0, it represents tails and is assigned a value of 2.
If the flip is 1, it represents heads and is assigned a value of 3.

Line Generation:
This coin-flipping process is repeated 3 times to form one line of the hexagram. The values from the three coin flips are summed to create a total for the line. 
For example:

Three tosses:
0, 1, 0 = tails, heads, tails = 2, 3, 2 = 7

Line Outcomes:
The possible outcomes for each line are:
6 = changing Yin line (-- --)
7 = non-changing Yang line (-----)
8 = non-changing Yin line (-- --)
9 = changing Yang line (-----)

Hexagram Construction:
This process is repeated 6 times to form a hexagram, with each result determining one of the six lines. 
If any of the lines are changing (i.e., 6 or 9), the program flips those lines to create a secondary hexagram (with Yin becoming Yang, and vice versa).

Hexagram Lookup:
The lines of the hexagram are translated into a binary format (where 0 represents a Yin line and 1 represents a Yang line). 
This binary sequence is then used to look up the corresponding hexagram from the I Ching in a pre-defined table, which provides the name, symbol, and meaning of the hexagram.
