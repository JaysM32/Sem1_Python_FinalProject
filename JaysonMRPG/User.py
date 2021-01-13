# User creation and checking of levels
import os


class User: #User class and account when playing.
    def __init__(self, name , gender, attr):
        self.name = name
        self.gender = gender
        self.attr = attr #attributes : Intelligence, Strength, Agility, and Luck
        self.Health = 50.0 #start health is half
        self.Armor = 0.25 #damage reduction ( change with armor )
        self.Level = 1
        self.EXP = 0 #for every 10 EXP = 1 level
        self.UserInventory = {"Sword":1, "Shield":1, "Leather Armor": 1, "Health Potion": 1, "Iron Ingots": 5, "Wood": 10, "Gold Coins": 50, "Food":2, "Drink":1}
        self.Equipped = "Sword"
        self.EqArmor = "Leather Armor"
        self.story = 0
        self.objective = 20
        self.strComplt = False


#testuser = user.User("Jude", "Male", {"INT":3, "STR":3, "AGI":3, "LCK":3})




def createUser (): #UserCreation
    os.system('cls')
    name = str(input("Please Create a name = "))
    gender = str(input("Pick a gender. ( Female or Male )\n( write exactly as shown ): "))
    currentpoints = 12
    Attr = {"INT":0, "STR":0, "AGI":0, "LCK":0} #attributes helps in dungeon
    while True:
        if currentpoints <= 0:
            print("are you sure ? (Y/N)")
            makesure = str(input("input either Y or N: "))
            if makesure.lower() == "y":
                break
            elif makesure.lower()=="n":
                pass
        print("-----------------------------------------------")
        print("You currently have", currentpoints, "points to spend on attributes")
        print(Attr)
        pick = str(input("Pick an Attribute to spend Points on: "))#attribute maker
        if pick.upper() not in Attr.keys():
            print("error input")
        else:
            spend = int(input("Change / Add to: "))
            if spend <= currentpoints:
                if Attr[pick.upper()] >= spend:
                    currentpoints = currentpoints + Attr[pick.upper()]
                    Attr[pick.upper()] = spend
                else:
                    Attr[pick.upper()] = Attr[pick.upper()] + spend
            else: print("not enough points")
            currentpoints = currentpoints - spend



    user1 = User(name, gender, Attr)
    os.system('cls')
    print("-----------------------------------------------")
    print("User Created !")
    print("Name : ",name)
    print("Gender : ", gender)
    print("Attributes : ", Attr)
    print("-----------------------------------------------")
    print("Welcome to Cloud RPG !")

    return user1


def checklevel(userobj): # checks the level of the user and add 1 attr point when level up
    if userobj.EXP >= 10:
        userobj.EXP = userobj.EXP - 10
        userobj.Level += 1
        print("-----------------------------------------------")
        print("You currently have 1 points to spend on attributes")
        print(userobj.Attr)
        pick = str(input("Pick an Attribute to spend Points on: "))
        if pick.upper() not in userobj.Attr.keys():
            print("error input")
        else:
            userobj.Attr[pick.upper()] += 1
        print("-----------------------------------------------")
    else: pass
