# Game of Nim
# This game of NIM consists of 16 matches in 4 rows arranged as follows:
#
#           1-   |
#           2-   | | |
#           3-   | | | | |
#           4-   | | | | | | |
#
# The players alternately pick a certain number of matches (at least 1) in only one row, and the one who takes
# the last matches wins.
# A winning game (for the player who has to play) is a game for which the result of the Vertical XOR is Non Zero,
# otherwise it is a loosing game. From any winning game the current player can obtain a loosing game for the
# other player zwinkernd. From any loosing game one obtains a winning game for the other player what ever one
# does traurig.
#
#
#           Binary Conversion
#           1-                        ===>          0 0 0
#           2-   | | |                ===>          0 1 1
#           3-   | | | | |            ===>          1 0 1
#           4-   | | | | |            ===>          1 0 1
#
#                                                   | | |   Vertical XOR
#                                                   V V V
#
#                                                   0 1 1   Non Zero "winning"
#
# Implement the game for a player and your program.
# Tip: represent the board as a list of integer [1, 3, 5, 7] where the content represents the number
# of matches per line.
# Try to use as less as possible side effects.
# Make use of this partial implementation: nim-partial.py

#Author: TimHuerzeler
#Date: 06.10.2022