from random import randint
from time import sleep

def bleep_bloop(pause = 0.2):
	# print either Bleep or Bloop
	sound = ["Bleep","Bloop"][randint(1,2) - 1]
	print(sound)
	sleep(pause)

bleep_bloop()
bleep_bloop()
bleep_bloop()
bleep_bloop()

print("""---\n
WELCOME TO DICE-ROLL-O-MATIC
(c) Applied Dice Applications Labs 1971
""")

bleep_bloop()
bleep_bloop()

print("""\n---
To end your session, type 'end'
To roll 4 d23s type '4d23'
To roll 1 d40 type '1d40' or '40'
Shortcuts: 1d20 = 't' 1d100 = 'h' 1d8 = 'e' 1d6 = 's' 1d4 = 'f'
---\n""")
