# story line

# Currently developing

import os, time


def part1(userobj):
    os.system('cls')
    userobj.strComplt = False
    print("---------------------The Quest----------------------")
    print("you decided to meet with the adventurer guild")
    print("to see whether there are any quests that can be")
    print("done. you stumbled upon one quests that asks  you ")
    print("to clear a certain part of the dungeon. But you need")
    print("meet with the person who will give you the area location")
    print("----------------------------------------------------")
    input("press enter to continue")
    print("----------------------------------------------------")
    print("you meet with the person and talked about the location")
    print(f"{userobj.name}: you must be the person who put up the quest")
    print("Nate: yes, this is the quest that i put up. its easy to go to")
    print("      location. just go to the left after you enter. ")
    print(f"{userobj.name}: any ideas on how many there will be ?")
    print("Nate: probably around 20 enemies in there.")
    print(f"{userobj.name}: OK, great. shouldn't be to hard ")
    print("---------------------------------------------------")
    print("Current Obejctive : kill 20 enemies")
    input("press enter to continue")
    userobj.story = 1




def part2(userobj):
    if userobj.strComplt == True:
        os.system('cls')
        userobj.strComplt = False
        print("---------------------The Quest----------------------")
        print("you've completed the quest and went to see Nate, the")
        print("person who hired you on this quest.")
        print("you go to his house only to find that it is empty...")
        print("a note was left behind saying that he have left to see")
        print("the part of the dungeon that you've cleared. you go back")
        print("only to find that he has died due to a trap.")
        print("----------------------------------------------------")
        input("press enter to continue")
        print("----------------------------------------------------")
        print("you found another note saying that he found another part")
        print("of the dungoen that ends with a valued treasure, called")
        print("-------------------- EXCALIBUR ---------------------")
        print("and thus you decided to go back to town first to prepare")
        print("---------------------------------------------------")
        print("Current Obejctive : kill 35 enemies")
        input("press enter to continue")
        userobj.story = 2
        userobj.objective = 35

    else:
        os.system('cls')
        print("----------You have yet to complete the mission------------")
        time.sleep(5)
        pass

def part3(userobj):
    if userobj.strComplt == True and userobj.story == 2:
        os.system('cls')
        userobj.strComplt = False
        print("---------------------The Quest----------------------")
        print("You've completed the dungeon and found the valued treasure!")
        print("you recieved : ")
        print("-------------------- EXCALIBUR ---------------------")
        print("with this the story comes to an end but this does not mean")
        print("it ends as a new chapter starts a new !")
        print("----------------------------------------------------")
        input("press enter to continue")
        print("----------------------------------------------------")
        print("Congratulations for making it this far ! ")
        userobj.story = 3
        userobj.UserInventory.setdefault("Excalibur", 0)
        userobj.UserInventory["Excalibur"] += 1

    else:
        os.system('cls')
        print("----------You have yet to complete the mission------------")
        time.sleep(5)
        pass