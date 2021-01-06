# non-town and dungoen story draws

import os, time

def statusbar(userobj):
    os.system('cls')
    print("-----------------------------------------------")
    print("HitPoints : ", userobj.Health)
    print("level : ",userobj.Level)
    print("Exp : ",userobj.EXP)
    print("Currently equipped weapon = ", userobj.Equipped)
    print("Currently equipped armor = ", userobj.EqArmor)
    print("-----------------------------------------------")

def mainmenu():

    print("-----------------------------------------------")
    print("       --------   CLOUD RPG   --------         ")
    print("-----------------------------------------------")
    print("   A Text-Based RPG created by Jayson Mikael   ")
    print("           Created using Python3 ")
    print("-----------------------------------------------")
    print("1. Play")
    print("2. Help")
    print("3. Exit")
    print("-----------------------------------------------")



def help():
    os.system('cls')
    print("-----------------------------------------------")
    print("       --------   CLOUD RPG   --------         ")
    print("-----------------------------------------------")
    print("   A Text-Based RPG created by Jayson Mikael   ")
    print("           Created using Python3 ")
    print("-----------------------------------------------")
    print("Follow each command in order to continue")
    print("usually by either inputing numbers or specific ")
    print("words")
    print("This is created as i am unable to draw for the ")
    print("sake of my life")
    print("-----------------------------------------------")
    print("press 'enter' to continue")
    input()  # to continue after reading



def startstory():
    os.system('cls')
    print("-----------------------------------------------")
    print("current location: Forest")
    print("you are currently running away from what it \n"
          "seems to be a bear. ")
    print("you're tired and your sword and armor has taken")
    print("some damage. ")
    print("In front, you see a town with guards on the entrance.")
    print("-----------------------------------------------")
    print("your current choices ")
    print("1. run torwards the town and ask help from the guard")
    print("2. fight the bear")

def introstory1(name):
    os.system('cls')
    print("-----------------------------------------------")
    print("You ran straight to the entrance and the guards")
    print("sees the bear and helps you. ")
    print("The bear decided to ran away after seeing the guards")
    print("You are now safe")
    print("Guard1 = 'What is your name, adventurer ? '")
    print(f"{name} = my name is {name}.")
    print("guard2 = 'You might want to head inside and take a break.'")
    print("you head inside...")
    print("Inside you saw a shop, the blacksmith and the inn.")
    print("-----------------------------------------------")
    print("Where will you go ?")
    print("1. Shop")
    print("2. Blacksmith ( craft )")
    print("3. Inn")
    print("-----------------------------------------------")

def introstory2():
    print("-----------------------------------------------")
    print("""you decided to fight the bear. the bear was very strong 
but you still had some fight left inside. you fought the bear,
yet the bear was overwhelming you. in the end, you werent able to 
defeat the bear, and you died. """)
    print("-----------------------------------------------")
    print("                 Game Over")

def insidetown(introdone):
    os.system('cls')
    print("You are currently in the town. ")
    print("-----------------------------------------------")
    print("Where will you go ?")
    print("0. Exit to Main Menu")
    print("1. Shop")
    print("2. Blacksmith ( craft )")
    print("3. Inn")
    print("4. Dungeon")
    print("5. Recycle")
    if introdone == True:
        print("6. Adeventure's Guild ( story ) ")
    print("-----------------------------------------------")


