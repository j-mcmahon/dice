import argparse
import re
import sys
from random import randint
from time import sleep

parser = argparse.ArgumentParser()

parser.add_argument("-v", "--Output", help = "bla")
 
# Read arguments from command line
args = parser.parse_args()

#import startup_messages # import local script

shortcuts = {"h": "1d100", "t": "1d20", "e": "1d8", "s": "1d6", "f": "1d4"}

def roll_dice(n, d):
	results = []
	for i in range(0,n):
		result = randint(1,d)
		results.append(result)
		if d == 20 and result == 20:
			print("Rolled a 20! Let's goooooooo!")
		elif d == 20 and result == 1:
			print("Rolled a 1! Oh no!")
		else:
			print(f"Rolled a {result}")
	print("---")
	return results

def summarise_results(results):
	results_strings = [ str(x) for x in results]
	print(f"Final result: { ' + '.join(results_strings) } = { sum(results) }")
	print(f"Highest roll was: {max(results)} | Lowest roll was: {min(results)}")

def interpret_input(x, variant = "standard"):
	if bool(re.search("^[0-9]*$", x)):
		x = "1d" + str(x)
		print(f"Rolling {x}")
	elif x in shortcuts.keys():
		x = shortcuts[x]
		print(f"Rolling {x}")
	if bool(re.search("^[0-9]*d[0-9]*$", x)):
		split_x = x.split("d")
		n = int(split_x[0])
		d = int(split_x[1])
		results = roll_dice(n, d)
		if n != 1:
			summarise_results(results)
	elif x == "end":
		print("Goodbye. Thank you for choosing DICE-ROLL-O-MATIC!")
	else:
		print("Invalid roll! YOU FOOL!")

x = ""
while x != "end":
	x = input("What do you want roll? ").lower()
	interpret_input(x)
	print("")