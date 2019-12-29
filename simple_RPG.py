#Simple RPG

import random

def game():

	#Characters
	player = "Hero"
	enemy = "Dummy"

	#Character details
	plyr_health = 100
	enmy_health = 100

	#ItemsStats
	sword_attk = 10.0

	#Short sword
	spd_shrt_swrd = 2.0

	#Long sword
	spd_swrd = 0.5

	#Items
	short_Sword = int(sword_attk * spd_shrt_swrd)
	longsword = int(sword_attk * spd_swrd)


	#Player Item choice
	plyr_Item = input("Would you like a shortsword or a longsword? Take your pick:").lower().strip().replace(" ", "")
	if plyr_Item == "shortsword":
		print("")
		print("You took the short sword")
		plyr_Item = short_Sword
	elif plyr_Item == "longsword":
		print("")
		print("You took the longsword")
		plyr_Item = longsword

	#Computer Item choice
	comp_Item = random.randint(1, 2)
	if comp_Item == 1:
		comp_Item = short_Sword
		print("The enemy took the short sword")
		print("")
	elif comp_Item == 2:
		comp_Item = longsword
		print("The enemy took the longsword")
		print("")

	#Battle sim
	while plyr_health > 0 or enmy_health > 0:

		#Assign values to Moves	
		general_attk = 5
		plyr_attack = general_attk + plyr_Item
		comp_attack = general_attk + comp_Item

		plyr_block = comp_attack - general_attk
		comp_block = plyr_attack - general_attk

		plyr_miss = 0
		comp_miss = 0

		#Define Computers Attack/block
		comp_Move = random.randint(1, 3)
		if comp_Move == 1:
			comp_Move = comp_attack
		elif comp_Move == 2:
			comp_Move = comp_block
		elif comp_Move == 3:
			comp_Move = comp_miss

		#Define Players Attack/block
		plyr_Move = input("Would you like to attack or block? Choose wisely: ").lower().strip()

		if plyr_Move == "attack":
			plyr_Move = random.randint(0, 1)
			if plyr_Move == 0:
				plyr_Move = plyr_attack
			elif plyr_Move == 1:
				plyr_Move = plyr_miss

		elif plyr_Move == "block":
				plyr_Move = plyr_block

		#Use of defined Moves

		#Computer and Player same moves
		if comp_Move == comp_attack and plyr_Move == plyr_attack:
			enmy_health = enmy_health - plyr_attack
			plyr_health = plyr_health - comp_attack
			print("")
			print("You chose to attack.")
			print("The enemy chose to attack.")
			print("")
			print("You dealt a damage of " + str(plyr_attack) + " points.")
			print("You received a damage of " + str(comp_attack) + " points.")
			print("...")

		elif comp_Move == comp_block and plyr_Move == plyr_block:
			print("")
			print("Nobody got hurt.")	
			print("...")

		elif comp_Move == comp_miss and plyr_Move == plyr_miss:
			print("")
			print("You missed")
			print("The enemy missed")
			print("...")

		#CP attk - PL block
		elif comp_Move == comp_attack and plyr_Move == plyr_block:
			plyr_health = plyr_health - plyr_block
			print("")
			print("You chose to block.")
			print("The enemy chose to attack.")
			print("")
			print("You received a damage of " + str(plyr_block) + " points.")
			print("...")
		#CP block - PL attack
		elif comp_Move == comp_block and plyr_Move == plyr_attack:
			enmy_health = enmy_health - comp_block
			print("")
			print("You chose to attack.")
			print("The enemy chose to block.")
			print("")
			print("You dealt a damage of " + str(comp_block) + " points.")
			print("...")
		#CP attk - PL miss
		elif comp_Move == comp_attack and plyr_Move == plyr_miss:
			plyr_health = plyr_health - comp_attack
			print("")
			print("You missed")
			print("The enemy chose to attack.")
			print("")
			print("You received a damage of " + str(comp_attack) + " points.")
			print("...")
		#CP block - PL miss
		elif comp_Move == comp_block and plyr_Move == plyr_miss:
			print("")
			print("You missed")
			print("The enemy chose to block.")
			print("...")
		#CP miss - PL attack
		elif comp_Move == comp_miss and plyr_Move == plyr_attack:
			enmy_health = enmy_health - plyr_attack
			print("")
			print("You chose to attack.")
			print("The enemy missed.")
			print("")
			print("You dealt a damage of " + str(plyr_attack) + " points.")
			print("...")
		#CP miss - PL block
		elif comp_Move == comp_miss and plyr_Move == comp_block:
			print("")
			print("You chose to block.")
			print("The enemy missed.")
			print("...")

		print("Your health is at " + str(plyr_health) + " points.")
		print("Your enemy's health is at " + str(enmy_health) + " points.")
		print("...")

		if plyr_health <= 0:
			print("The enemy won.")
			input("...")
			return
		elif enmy_health <= 0:
			print("You win!")
			input("...")
			return

answer = input("Would you like to play a simple RPG battle? Type yes or no: ").lower().strip()
if answer == "yes":
	print("")
	print("Welcome to Simple RPG.")
	print("")
	print("Choose your equipment and then attack or block. Make sure to make the wisest decision!")
	print("...")
	game()
elif answer == "no":
	print("If you want to play the game, restart the program")

print("...")
input("Press enter to exit")