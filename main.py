ascii = '''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************'''

print("WELCOME TO THE TREASURE ISLAND!")
print("Your mission is to find the TREASURE following the instructions.")

print("You arrive at the island with your boat. You can go FORWARD, LEFT, or RIGHT...")
choice = input()

if choice.lower() == "forward":
    print("You arrived in a dense forest. The sound of animals make you have a few goosebumps. This time you can go LEFT, RIGHT OR FORWARD.")
    choice = input()
    if choice.lower() == "left":
        print("You found a group of wolves, that immediately attacked you.")
        print("GAME OVER!")
    elif choice.lower() == "right":
        print("You found a cub bear. He tried to attack you, so you smacked him. Because of that he cried and the mama bear appeared behind you.")
        print("GAME OVER!")
    elif choice.lower() == "forward":
        print("You went too deep in the woods and got lost forever.")
        print("GAME OVER!")
    else:
        print("COMMAND NOT FOUND. RESTART THE GAME")
elif choice.lower() == "left":
    print("You fell into a hole and broke both legs. You had no option other than wait.")
    print("GAME OVER!")
elif choice.lower() == "right":
    print("You know what they say: X marks the spot. But this was too easy. Do you DIG or KEEP GOING?")
    choice = input()
    if choice.lower() == "dig":
        print("You dug and dug, until you hit a landmine, which of course, exploded")
        print("GAME OVER!")
    elif choice.lower() == "keep going":
        print("You found a cabin. Looks abandoned. Do you go IN or KEEP GOING?")
        choice = input()
        if choice.lower() == "in":
            print("You find inside the cabin many bags of gold.")
            print("CONGRATULATIONS!")
        elif choice.lower() == "keep going":
            print("You keep going in circles for eternity and lost the way back.")
            print("GAME OVER!")
        else:
            print("COMMAND NOT FOUND. RESTART THE GAME")
    else:
        print("COMMAND NOT FOUND. RESTART THE GAME")
else:
    print("COMMAND NOT FOUND. RESTART THE GAME")