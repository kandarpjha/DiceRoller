import random

global exit_chk
exit_chk = "n"

def start():
	print "*-" * 17
	print "Welcome to Die Rolling Simulator!"
	print "-*" * 17
	
	roll()

def bye():
	print "Thank you for using Rolling Die Simulator. :-)"

def roll():
	print "Please select the die face (6 or 8 or 12) you want to roll:\n"
	choice = int(raw_input(">"))

	if choice == 6:
		rolling_6()
	elif choice == 8:
		rolling_8()
	elif choice == 12:
		rolling_12()
	else:
		print "Please select a valid die."
		roll()

def rolling_6():
	result = random.randint(1, 6)
	print "You Rolled %s." % result
	
	exit_chk_raw = raw_input("Do you want to roll once more? Y/N\n")
	exit_chk == exit_chk_raw.lower()
	if exit_chk == "y":
		start()
	else:
		bye()

def rolling_8():
	result = random.randint(1, 8)
	print "You Rolled %s." % result
	
	exit_chk_raw = raw_input("Do you want to roll once more? Y/N\n")
	exit_chk == exit_chk_raw.lower()
	if exit_chk == "y":
		start()
	else:
		bye()

def rolling_12():
	result = random.randint(1, 12)
	print "You Rolled %s." % result
	
	exit_chk_raw = raw_input("Do you want to roll once more? Y/N\n")
	exit_chk == exit_chk_raw.lower()
	if exit_chk == "y":
		start()
	else:
		bye()

start()