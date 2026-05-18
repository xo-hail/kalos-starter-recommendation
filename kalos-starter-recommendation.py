# Recommendation engine that tells u what Kalos starter to choose

# Recommendations
fire = "Fennekin"
water = "Froakie"
grass = "Chespin"

print("Welcome to the world of Pokemon!")
name = input("First things first, what is your name? ")
print("Hello, " + name + "!")
gender = input("Are you a boy or a girl? ")


# Collect attributes to recommend according to user; algorithm start
rec = ""
rec_Score = 0

# Program start
region = input("What region are you from? ")
if region == "Kalos":
    print("Welcome to the Kalos region! I am Professor Sycamore!")
if region != "Kalos":
    import sys
    exit("This program only supports Kalos.")

does_want_Explore = input("Do you want to explore the world of Pokemon (yes/no)? ")
if does_want_Explore == "yes":
    print("Alright, let's get started!")
if does_want_Explore == "no":
    import sys
    exit("Terminating " + name + ".")

pokemon_choice = input("What Pokemon will you choose? Fennekin, Froakie, or Chespin? ")
if pokemon_choice == "I don't know":
    print("No worries! I'll help you decide through a series of questions.")
else:
    print("Received " + pokemon_choice + " from Professor Sycamore.")
    print("It seems to like you!")
    import sys
    exit()

rpg_class = ""
does_play_rpg = input("Do you play RPG games? ")
if does_play_rpg == "yes":
    rpg_class = input("What class do you usually play? ")
    if rpg_class == "Mage":
        rec = fire
    elif rpg_class == "Rogue":
        rec = water
    elif rpg_class == "Knight":
        rec = grass
else:
  input("That's okay. ")













