# Version 1.0 - Sycamore Edition
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
rec_Score = 0
final_rec = ""

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

pokemon_choice = input("What Pokemon will you choose as your starter? Fennekin, Froakie, or Chespin? ")
if pokemon_choice == "I don't know":
    print("No worries! I'll help you decide through a series of questions.")
else:
    print("Received " + pokemon_choice + " from Professor Sycamore.")
    print("It seems to like you!")
    import sys
    exit()

rpg_class = ""
is_continue = "yes"
does_play_rpg = input("Do you play RPG games? ")
if does_play_rpg == "yes":
    rpg_class = input("What class do you usually play? Mage, Rogue, or Knight? ")
    if rpg_class == "Mage":
        rec_Score += 3
        final_rec = fire
    elif rpg_class == "Rogue":
        rec_Score += 2
        final_rec = water
    elif rpg_class == "Knight":
        rec_Score += 1
        final_rec = grass
    if rpg_class not in ["Mage", "Rogue", "Knight"]:
        is_continue = input("That's okay. Continue (yes/no)? ")
        if is_continue == "yes":
            print ("Alright, moving on!")
        else:
            import sys 
            exit("I see. Goodbye!")

virtues = input("What makes a good life? Intellect, pragmatism, or morality? ")
if virtues == "Intellect":
    rec_Score += 3
elif virtues == "Pragmatism":
    rec_Score += 2
elif virtues == "Morality":
    rec_Score += 1

print("I see, I see. On to the last question!")

power_pref = input("How do you prefer to face enemies? From afar, from blindspots, or head-on? ")
if power_pref == "From afar":
    rec_Score += 3
elif power_pref == "From blindspots":
    rec_Score += 2
elif power_pref == "Head-on":
    rec_Score += 1

# Evaluate the final recommendation!
if rec_Score <= 4:
    final_rec = grass
elif rec_Score <= 6:
    final_rec = water
elif rec_Score <= 9:
    final_rec = fire 

is_Ready = input("Results are in... Are you ready (yes/no)? ")
if is_Ready == "yes":
    print("Perfect! Your recommended starter is " + final_rec + "!")
    print("Received " + final_rec + " from Professor Sycamore.")
    import sys
    exit("Your Pokemon adventure begins now! Bon voyage!")




















