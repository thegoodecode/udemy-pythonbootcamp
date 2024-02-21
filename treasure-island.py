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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
road = input("Which way do you want to go? Left or Right? \n").lower()

if road == "left":
    print("You have reached a lake. There is an island in the middle of the lake.")
    lake = input("Do you want to swim or wait for a boat?\n").lower()

    if lake == "wait":
        print("You have successfully waited for a boat to cross the lake. You have safely reached the shore.")

        print("Now that you have reached the island, you have to choose a door. There are three doors. Red, Yellow, and Blue.")

        door = input("Which door will you choose? Red, Yellow, or Blue?\n").lower()

        if door == "yellow":
            print("You have found the treasure. You Win!")
        elif door == "blue":
            print("Did you think you'd find the treasure? You hear a pirate say... Game Over!")
        elif door == "red":
            print("You got trapped by a booby trap. Game over!")
        else: 
            print("You chose a door that doesn't exist. Game Over!")
    else:
        print("You chose to swim and got eaten by a shark. Game Over!")
else:
    print("You fell into a hole. Game Over!")





