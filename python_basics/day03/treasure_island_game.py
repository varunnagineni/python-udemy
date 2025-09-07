# Three single quotes at the begining and end is to print multiple lines of String
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
    ''')

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
print("You are at a cross road. Where do you want to go?")
enter_direction = input('\tType "left" or "right"\n').lower()

if enter_direction == "right":
    print("You fell into a hole. Game Over.")
elif enter_direction == "left":
    print("You've come to lake. There is an island in the middle of the lake.")
    travel_choice = input('\tType "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if travel_choice == "swaim":
        print("You get attacked by an angry trout. Game Over.")
    elif travel_choice == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        color_choice = input("\tOne red, one yellow and one blue. Which colour do you choose?").lower()
        if color_choice == "red":
            print("Burned by fire. Game Over.")
        elif color_choice == "blue":
            print("Eaten by beasts. Game Over.")
        elif color_choice == "yellow":
            print("You Win!")
        else:
            print("Please enter red or yellow or blue only")
    else:
        print("You've selected wrong choice.")    
else:
    print("You've selected wrong choice.")