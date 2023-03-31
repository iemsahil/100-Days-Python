print('''
*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


first = input("You`re at a crossroad,where do you want to go?Left or Right?\n").lower()
if first == "left":
    second = input("You`ve come to lake.There is a island in the middle of the lake.Type wait to wait for a boat or type swim to swim across.\n").lower()
    if second == "wait":
        third= input("You arrive at the island unharmed. There is house with 3 doors. One red,one blue and one yellow.\n").lower()
        if third == "red":
            print("Burned by fire.Game Over.")
        elif third == "blue":
            print("Eaten by beasts.Game Over.")
        elif third == "yellow":
            print ("You found the treasure! You Win!")
        else :
            print("You choose a door that doesn`t exist.Game Over.")
        
    else:
        print("Attacked by trout.Game Over")
    
else:
    print("Fall into a hole.Game Over")