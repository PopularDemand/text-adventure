from sys import exit

#global variables
inv = []
health = 100
power = 20

bat = 1  #have you picked up the bat
catnip = 1  #have you picked up the catnip
key = 1  #have you picked up the key
gun = 1  #have you picked up the gun

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
	if reason != "end":
		print reason
		print "And thus our story ends."
	
	choice = raw_input("Play again?")

	if choice == "y" or "yes" in choice:
		start()
	else:
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
		error_message(choice)
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
		error_message(choice)
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
		error_message(choice)
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
		error_message(choice)
		school()

###
def home():
	global home_first_time
	print "get sad and lose power and health from home"
	print "familiar shade to the west, entrance to warehouse north, people east"

	if choice == "look":
		home()
	elif "inv" in choice:
		inv_check()
		home()

	elif choice == "e" or "east" in choice:
		bad_guys()
	elif choice == "w" or "west" in choice:
		school()
	elif choice == "n" or "north" in choice:
		bad_guys_entry()

	else:
		error_message(choice)
		home()

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
			error_message(choice)
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
			error_message(choice)
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
	elif choice == "s" or "south" in choice:
		bad_guys_entry()
	else:
		error_message(choice)
		ivy_room()

def open_door():
	global key, open_door_first_time
	
	if open_door_first_time:
		print "There is a door here to the warehouse.\nTo the west there is a walkway. To the south, there is what looks like a garage."
	else:
		print "To the east, there is a shadowy room. To the west there is a walkway. To the south, there is what looks like a garage."
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
	elif choice == "e" or "east" in choice and not open_door_first_time:
		cat_room()
	
	elif "door" in choice and key == 1:
		print "This door is locked. Maybe there is a key somewhere..."
		open_door()
	elif "door" in choice and key == 0:
		print "The key opens the door"
		open_door_first_time = 0
		open_door()
	else:
		error_message(choice)
		open_door()

def cat_room():
	global indoor_cat

	if indoor_cat == 1:
		print "You enter the door. Through the darkness you can see a two entryways across the room, but there is an ornery stray cat blocking your path."
		print "You can fight the cat or flee."
		
		choice = raw_input("> ")
		
		if "inv" in choice:
			inv_check()
			cat_room()
		elif choice == "look":
			cat_room()
		
		elif "fight" in choice:
			if "bat" in inv:
				print "You break the rabid stray's back with the bat. The bat breaks and is useless now."
				inv.remove("bat")
				indoor_cat = 0
				cat_room()
			else:
				print "You tackle the cat. It scratches and bites, but eventually you overcome it."
				print "Unfortunately, you took some damage in the scrap."
				health_change(-20)
				indoor_cat = 0
				cat_room()
		elif "flee" in choice:
			print "You flee east."
			open_door()
		else:
			error_message(choice)
			cat_room()

	else:
		print "There is a door cracked open to the east. You hear scuffles and yelling. And... Is that Scotch crying out?!"

		choice = raw_input("> ")

		if "inv" in choice:
			inv_check()
			cat_room()
		elif choice == "look":
			cat_room()

		elif choice == "w" or "west" in choice:
			open_door()
		elif choice == "e" or "east" in choice:
			scotch_room()
		else:
			error_message(choice)
			cat_room()

def bad_guys_entry():
	global entry_bad_guys
	global bat
	global gun

	if entry_bad_guys:
		print "You follow the shadowy figures. It's two big men dressed in the greys of Mustafa's cronies."
		print "They stand in front of a door to a warehouse smoking cigarettes and talking about..."
		print "'The girl that was dumb enough to return'?! Could they mean Scotch?"
		print "Apparently, she is being held captive in the warehouse the two are guarding."
		print "You measure up the cronies and think you can take them while maybe sustaining significant injuries."
		print "Maybe there's another entry somewhere...\n"
		print "Do you fight through the bad guys or go back?"

		choice = raw_input("> ")

		if "fight" in choice:
			print "\nYou need to get to Scotch as soon as possible. And if that means taking some damage, so be it."
			if "bat" in inv:
				print "You sneak through the shadows until you are within bat's reach of the men."
				print "You swiftly bring the bat over one of the men's head. He buckles and the bat splinters."
				print "The other guys unholsters his gun and fires a shot. It misses."
				print "You rush towards him and plunge what's left of the bat into his gut."
				print "He gasps and falls backward, freeing the bat. You then jam it into his neck. He's not getting back up.\n"
				print "The first man grabs you from behind. He hooks his arm under yours and pulls until your shoulder pops."
				print "Pain erupts through your chest. Your head flinches backward, fortunatly knocking the man off of you."
				print "You spring forward and grab the pistol from the fallen crony."
				print "While the first man is fumbling for his own pistol, you fire one shot straight to his face. He falls.\n"
				print "You hide in the shadows in case more cronies follow the gunshots."
				print "As you wait, you pop your dislocated shoulder back into place. No more bad guys arrive."
				print "You've won. Barely.\n"
				get("gun")
				inv.remove('bat')
				gun = 0
				health_change(-40)
				power_change(-5)
			elif "bat" not in inv:
				print "You sneak through the shadows until you are in reach of the men. They don't see you."
				print "The man farther away from you receives a call. 'Hey, babe,' he answers and walks away.\n"
				print "With one distracted, you lunge forward and grab the remaining one around the neck."
				print "He claws at your face, getting one good scratch above your right eye. Maintaining control, you twist his head until you hear a crack."
				print "You drag his lifeless body to the shadows.\n"
				print "Before you have a chance to set him down, you hear 'HEY HEY HEY'."
				print "The other man is off of his phone and sprinting toward you with his pistol drawn! He fires a shot and hits you in the shoulder."
				print "Two more shots come in, but they lodge in the man you are dragging. As you dodge and fumble, you notice a holster on the dead man."
				print "You pull the gun out and hope it's loaded.\n"
				print "You drop the man your dragging and juke into the shadows faster than the shooter can comprehend."
				print "As he fires in you general direction, you take three shots at his and all hit the center of mass. He falls back crying in agony."
				print "His cries are soon drowned in blood and stop coming altogether.\n"
				print "You hide behind some trashcans in case the gunshots caught the attention of more cronies."
				print "As you wait, you inspect your shoulder wound. Doc would probably say it's superficial, but it still hurts like hell."
				print "Blood is pouring down the right side of your face from the scratch above your eye."
				print "After concluding no one else was coming to investigate the commotion, you powder the wounds to stop the bleeding. And look around.\n"
				get("gun")
				gun = 0
				health_change(-50)
				power_change(-5)
			raw_input("Press [Enter]")
			entry_bad_guys = 0
			bad_guys_entry()
		elif "inv" in choice:
			inv_check()
			bad_guys_entry()
		elif choice == "look":
			bad_guys_entry()
		elif choice == "e" or "east" in choice or "back" in choice:
			print "You decide to head back the way you came. As you slide back into the shadows, though, you trip over some loose rubble."
			print "The guys hear you! They unholster their guns and head your way shouting 'WHO'S THERE?' Welp.\n..."
			print "Fight or flee?"

			choice = raw_input("> ")

			if "flee" in choice:
				fleeing()
			elif "fight" in choice:
				if "bat" in inv:
					print "You hide behind a dumpster, out of the line of sight of the men."
					print "As they pass you, you swiftly bring the bat over one of the men's head. He buckles, and the bat splinters."
					print "The other guys unholsters his gun and fires a shot. It misses."
					print "You rush towards him and plunge what's left of the bat into his gut."
					print "He gasps and falls backward, freeing the bat. You then jam it into his neck. He's not getting back up.\n"
					print "The first man tackles you. He hooks his arm under yours and pulls until your shoulder pops."
					print "Pain erupts through your chest. Your head flinches backward, fortunatly knocking the man off of you.\n"
					print "You spring forward and grab the pistol from the fallen crony."
					print "While the first man is fumbling for his own pistol, you fire one shot straight to his face. He falls.\n"
					print "You hide in the shadows in case more cronies follow the gunshots."
					print "As you wait, you pop your dislocated shoulder back into place. No more bad guys arrive."
					print "You've won. Barely.\n"
					get("gun")
					gun = 0
					inv.remove("bat")
					health_change(-40)
					power_change(-5)

				elif "bat" not in inv:
					print "You hide behind a dumpster, out of the line of sight of the men."
					print "The two men pass you in tandem. You swiftly grab the second one around the neck from behind."
					print "He claws at your face, getting one good scratch above your right eye. Maintaining control, you twist his head until you hear a crack."
					print "You drag his lifeless body into the shadows.\n"
					print "Before you have a chance to set his down, you hear 'HEY HEY HEY'."
					print "The other man is sprinting toward you with his pistol drawn! He fires a shot and hits you in the shoulder."
					print "Two more shots come in, but they lodge in the man you are dragging. As you dodge and fumble, you notice the dead man dropped his gun."
					print "You pick it up and hope it's loaded.\n"
					print "You drop the man your dragging and juke into the shadows faster than the shooter can comprehend."
					print "As he fires in you general direction, you take three shots at him and all hit the center of mass. He falls back, crying in agony."
					print "His cries are soon drowned in blood and stop coming altogether."
					print "You hide behind some trashcans in case the gunshots caught the attention of more cronies.\n"
					print "As you wait, you inspect your wound. Doc would probably say it's superficial, but it still hurts like hell."
					print "Blood is pouring down the right side of your face from the scratch above your eye."
					print "After concluding no one else was coming to investigate the commotion, you powder the wounds to stop the bleeding. And look around.\n"
					get("gun")
					gun = 0
					health_change(-50)
					power_change(-5)
				raw_input("Press [Enter]")
				entry_bad_guys = 0
				bad_guys_entry()
			else:
				error_message(choice)
				fleeing()
		else: 
			error_message(choice)
			bad_guys_entry()

	else:
		print "There is a courtyard to the west and an entry to a warehouse to the east."

		choice = raw_input("> ")

		if "inv" in choice:
			inv_check()
			bad_guys_entry()
		elif choice == "look":
			bad_guys_entry()

		elif choice == "w" or "west" in choice:
			key_room()
		elif choice == "e" or "east" in choice:
			chem_lab()
		else:
			error_message(choice)
			bad_guys_entry()

def fleeing():
	print "Fight or flee?"

	choice = raw_input("> ")

	if "flee" in choice:
		print "Your mortality in mind, you turn tail and run to the courtyard."
		print "Before you can catch your breath, the cronies turn the corner. One fires a shot that lands a foot away from you head!"
		print "You run to the south! There's a huge pile of rubble, and you decide to hide behind that."
		print "The two guys follow you to the field of rubble, but can't find you."
		print "They sniff around for a bit, but decide to head back to guarding the warehouse.\n"
		print "After you breathe a sigh of relief, you notice this place looks familiar..."
		school()
	elif "fight" in choice:
		if "bat" in inv:
			print "You hide behind a dumpster, out of the line of sight of the men."
			print "As they pass you, you swiftly bring the bat over one of the men's head. He buckles and the bat splinters.\n"
			print "The other guys unholsters his gun and fires a shot. It misses."
			print "You rush towards him and plunge what's left of the bat into his gut."
			print "He gasps and falls backward, freeing the bat. You then jam it into his neck. He's not getting back up.\n"
			print "The first man grabs you from behind. He hooks his arm under yours and pulls until your shoulder pops."
			print "Pain erupts through your chest. Your head flinches backward, fortunatly knocking the man off of you.\n"
			print "You spring forward and grab the pistol from the fallen crony."
			print "While the first man is fumbling for his own pistol, you fire one shot straight to his face. He falls.\n"
			print "You hide in the shadows in case more cronies follow the gunshots."
			print "As you wait, you pop your dislocated shoulder back into place. No more bad guys arrive."
			print "You've won. Barely.\n"
			get("gun")
			health_change(-40)
			power_change(-5)

		elif "bat" not in inv:
			print "You hide behind a dumpster, out of the line of sight of the men."
			print "The two men pass you in tandem. You swiftly grab the second one around the neck from behind."
			print "He claws at your face, getting one good scratch above your right eye. Maintaining control, you twist his head until you hear a crack."
			print "You drag his lifeless body into the shadows.\n"
			print "Before you have a chance to set his down, you hear 'HEY HEY HEY'."
			print "The other man is sprinting toward you with his pistol drawn! He fires a shot and hits you in the shoulder."
			print "Two more shots come in, but they lodge in the man you are dragging. As you dodge and fumble, you notice the dead man dropped his gun."
			print "You pick it up and hope it's loaded.\n"
			print "You drop the man your dragging and juke into the shadows faster than the shooter can comprehend."
			print "As he fires in you general direction, you take three shots at him and all hit the center of mass. He falls back, crying in agony."
			print "His cries are soon drowned in blood and stop coming altogether."
			print "You hide behind some trashcans in case the gunshots caught the attention of more cronies.\n"
			print "As you wait, you inspect your wound. Doc would probably say it's superficial, but it still hurts like hell."
			print "Blood is pouring down the right side of your face from the scratch above your eye."
			print "After concluding no one else was coming to investigate the commotion, you powder the wounds to stop the bleeding. And look around.\n"
			get("gun")
			health_change(-50)
			power_change(-5)
			raw_input("Press [Enter]")
		entry_bad_guys = 0
		bad_guys_entry()
	else:
		error_message(choice)
		fleeing()

###
def chem_lab():
	print "juicy chemicals that will boost health and power"
	print "if OD though, die"
	print "north is warehouse entry, east is closet, west is door outside"

	choice = raw_input("> ")

	if "inv" in choice:
		inv_check()
		chem_lab()
	elif "look" in choice:
		chem_lab()

	elif choice == "n" or "north" in choice:
		open_door()
	elif choice == "e" or "east" in choice:
		chem_closet()
	elif choice == "w" or "west" in choice:
		bad_guys_entry()
	else:
		error_message(choice)
		chem_lab()

###
def chem_closet():
	print "more drugs here. will die if OD"
	print "chem lab to the west"

	choice = raw_input("> ")

	if "inv" in choice:
		inv_check()
		chem_closet()
	elif "look" in choice:
		chem_closet()

	elif "drugs" in choice:
		dead("too mush drugs")
	elif choice == "w" or "west" in choice:
		chem_lab()
	else:
		error_message(choice)
		chem_closet()

###
def bad_guys:
	print "strong bad guys. 3 bad guys. 20 hp each hit"
	print "there's an opening to the east"

	choice = raw_input("> ")

	if "inv" in choice:
		inv_check()
		bad_guys()
	elif choice == "look":
		bad_guys()
	elif choice == "w" or "west" in choice:
		home()
	else:
		error_message(choice)
		bad_guys()

###
def scotch():
	print "finally we come to the climax"
	print "effects will negatively affect power and health, may die"
	choice = raw_input("> ")

	end()

###
def end():
	print "Before anything resolves... You hear the crack and then...\n\nNothing."
	print "Unbeknownst to you, a .50 cal bullet comes through the northern window and pierces your left temple."
	print "\n\nThis is the end."
	dead("end")

start()