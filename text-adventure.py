from sys import exit

#global variables
inv = []
health = 100
power = 20

bat = 1  #have you picked up the bat
catnip = 1  #have you picked up the catnip
key = 1  #have you picked up the key

bakery_first_time = 1  #have you seen the bakery once
school_first_time = 1  #have you seen the school once
home_first_time = 1  #have you seen home once
open_door_first_time = 1   #have you opened the door with the key

outdoor_cat = 1  #have you beaten outdoor cat
indoor_cat = 1  #have you beaten indoor cat
entry_bad_guys = 1  #have you beaten bad guys at warehouse entry
strong_bad_guys = 1  #have you beaten the strong bad guys

def error_message(choice):
	print "Sorry, %s is not a valid option." % choice

#status functions
def inv_check():  #fix this to be more pleasing
	for i in inv:
		print i

def power_change(num):
	global power
	power = power + num
	print "Your power has changed by %d and is now %d." % (num, power)
	if power <=0:
		dead("You've lost the will to go on.")
	
def health_change(num):
	global health
	health = health + num
	print "Your health has changed by %d and is now %d." % (num, health)
	if health <= 0:
		dead("You ache. You pain. You die.")

def get(thing):
	global inv
	inv.append(thing)
	print "You now have the %s" % thing

def dead(reason):
	print reason
	print "And thus our story ends."
	exit(0)
	
#game rooms
def start():
	print "[storyline]"
	print "There is an open alley way to the south."
	
	choice = raw_input("> ")
	
	if choice == "s" or "south" in choice:
		bat_room()

def bat_room():
	global bat
	if bat == 1:
		print "There is a discarded baseball bat. There is a bakery to the south. You hear scuffling to the east."
	else:
		print "There is a bakery to the south. You hear scuffling to the east."
	
	choice = raw_input("> ")
	
	if "bat" in choice and bat == 1:
		get("bat")
		bat = 0
		print "This bat is swollen and cracked with age. You are now armed with a bat."
		bat_room()
	elif "inv" in choice:
		inv_check()
		bat_room()
	elif choice == "s" or "south" in choice:
		bakery()
	elif choice == "e" or "east" in choice:
		key_room()
	elif choice == "look":
		bat_room()
	else:
		print "What?"
		bat_room()

def bakery():
	print "Old bakery that you used to frequent. Seeing it in dilapidated state causes you to start shaking and crying."
	global bakery_first_time
	if bakery_first_time == 1:
		power_change(-5)
		bakery_first_time = 0
	print "There is a shadowy building to the east and an open alley way to the north."
	
	choice = raw_input("> ")
	
	if choice == "look":
		bakery()
	elif "inv" in choice:
		inv_check()
		bakery()
	
	elif choice == "e" or "east" in choice:
		school()
	elif choice == "n" or "north" in choice:
		bat_room()
	else:
		print "What?"
		bakery()
		
def key_room():
	global key
	print "You go through an alley and emerge into a rundown courtyard. Shadowy figures disappear to the east."
	#if you dont have key
	if key:
		print "One of the figures appears to drop an item."
	print "There is an open alley way to your west. A shadowy building to your south.\n A shaded corridor to your east. An opening to a warehouse north."
	choice = raw_input(">>> ")
	
	if choice == "look":
		key_room()
	elif "inv" in choice:
		inv_check()
		key_room()
	
	elif "item" in choice:
		print "It's a key!"
		get("key")
		key = 0
		key_room()
	elif choice == "n" or "north" in choice:
		locked_door()
	elif choice == "s" or "south" in choice:
		school()
	elif choice == "e" or "east" in choice:
		bad_guys_entry()
	elif choice == "w" or "west" in choice:
		bat_room()
	else:
		print "What?"
		key_room()

def school():
	global school_first_time
	print "On closer look, it is the old school. The statue crumbled. Everything in waste, etc. \
	Seeing it this way causes you to start shaking and crying."
	if school_first_time:
		power_change(-5)
		school_first_time = 0
	print "An odd sense draws you to the east. There is a courtyard to your north. A bakery to your west."
	
	choice = raw_input("> ")
	
	if choice == "look":
		school()
	elif "inv" in choice:
		inv_check()
		school()
	
	elif choice == "e" or "east" in choice:
		home()
	elif choice == "n" or "north" in choice:
		key_room()
	elif choice == "w" or "west" in choice:
		bakery()
	else:
		print "What?"
		school()
	
def locked_door():
	global outdoor_cat, inv
	
	if outdoor_cat == 1:
		print "You've reached the door, but there is an ornery stray cat blocking your path."
		print "You can fight the cat or flee."
		
		choice = raw_input("> ")
		
		if "inv" in choice:
			inv_check()
			locked_door()
		elif choice == "look":
			locked_door()
		
		elif "fight" in choice:
			if "bat" in inv:
				print "You break the rabid stray's back with the bat. The bat breaks and is useless now."
				inv.remove("bat")
				outdoor_cat = 0
				locked_door()
			else:
				print "You tackle the cat. It scratches and bites, but eventually you overcome it."
				print "Unfortunately, you took some damage in the scrap."
				health_change(-20)
				outdoor_cat = 0
				locked_door()
		elif "flee" in choice:
			print "You flee south."
			key_room()
		else:
			print "What?"
			locked_door()
	else:
		print "There is a door to a warehouse here. It appears to be locked."
		print "There is a courtyard to the south and a pathway to the east."
		
		choice = raw_input("> ")
		
		if "inv" in choice:
			inv_check()
			locked_door()
		elif choice == "look":
			locked_door()
		
		elif choice == "s" or "south" in choice:
			key_room()
		elif choice == "e" or "east" in choice:
			ivy_room()
		
		elif "key" in choice or "door" in choice:
			print "Well, shucks. The key doesn't open this door."
			locked_door()
		else:
			print "What?"
			locked_door()
	
def ivy_room():
	print "You walk along the warehouse. You come to a tangle of ivy along the wall that appears climbable. \n To your east and west are doors into the warehouse."
	
	choice = raw_input("> ")
	
	if "inv" in choice:
			inv_check()
			ivy_room()
	elif choice == "look":
			ivy_room()
	
	elif "ivy" in choice or "climb" in choice:
		print "You begin to climb the ivy. As you are halfway up the wall, a handful of ivy turns out to be a snake! AHH!"
		dead("You fall off the wall and die.")
	elif choice == "w" or "west" in choice:
		locked_door()
	elif choice == "e" or "east" in choice:
		open_door()
	else:
		error_message(choice)
		ivy_room()

def open_door():
	global key, open_door_first_time
	
	if open_door_first_time:
		print "There is a door here to the warehouse.\nTo the west there is a walkway. To the south, there is a free standing garage."
	else:
		print "To the east, there is a shadowy room. To the west there is a walkway. To the south, there is a free standing garage."
	choice = raw_input("> ")
	
	if "inv" in choice:
			inv_check()
			open_door()
	elif choice == "look":
			open_door()
	
	elif choice == "w" or "west" in choice:
		ivy_room()
	elif choice == "s" or "south" in choice:
		chem_lab()
	
	elif "door" in choice and key == 1:
		print "This door is locked. Maybe there is a key somewhere..."
		open_door()
	elif "door" in choice and key == 0:
		print "The key opens the door"
		open_door_first_time = 0
		open_door()
	else:
		print "What?"
start()

	
	
