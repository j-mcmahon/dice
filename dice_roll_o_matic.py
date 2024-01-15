import re
from random import randint
from time import sleep

def bleep_bloop(pause = 0.2):
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
sleep(0.5)

print("""---
To end your session, type 'end'
To roll 4 d23s type '4d23'
To roll 1 d40 type '1d40' or '40'
Shortcuts: 1d20 = 't' 1d100 = 'h' 1d6 = 's' 1d8 = 'e'
---\n""")


x = ""
while x != "end":
	x = input("What do you want roll? ").lower()
	if bool(re.search("^[0-9]*$", x)):
		x = '1d' + str(x)
		print(f"Rolling {x}")
	elif x == 't':
		x = '1d20'
		print(f"Rolling {x}")
	elif x == 'h':
		x = '1d100'
		print(f"Rolling {x}")
	elif x == 's':
		x = '1d6'
		print(f"Rolling {x}")
	elif x == 'e':
		x = '1d8'
		print(f"Rolling {x}")
	if bool(re.search("^[0-9]*d[0-9]*$", x)):
		split_x = x.split("d")
		n = int(split_x[0])
		die = int(split_x[1])

		results_ints = []
		results_strings = []
		for i in range(0,n):
			result = randint(1,die)
			results_ints.append(result)
			results_strings.append(str(result))
			if die == 20 and result == 20:
				print("Rolled a 20! Let's goooooooo!")
			elif die == 20 and result == 1:
				print("Rolled a 1! Oh no!")
			else:
				print(f"Rolled a {result}")
		print("---")
		if n != 1:
			print(f"Final result: {' + '.join(results_strings)} = {sum(results_ints)}")
			print(f"Highest roll was: {max(results_ints)} | Lowest roll was: {min(results_ints)}")
	elif x == "end":
		print("Goodbye. Thank you for choosing DICE-ROLL-O-MATIC!")
	else:
		print("Invalid roll! YOU FOOL!")
	print("")