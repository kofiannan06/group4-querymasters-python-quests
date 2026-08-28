#!/usr/bin/python3
# A goblin has 27 gold pieces to share among 4 friends. Calculate how many pieces each friend gets and how many the goblin keeps (the remainder).
# The variables used.
Gold_per_share = 27 // 4
remainder = 27 % 4
# Showing the result.
print("The goblin shares {} gold pieces to his 4 friends and keeps {} gold pieces for himself.".format(Gold_per_share, remainder))
