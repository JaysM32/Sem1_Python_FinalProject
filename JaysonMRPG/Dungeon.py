#fight enemies and recieve loot.
#import JaysonMRPG.User as user
import Draw as draw
import random, os, time

availloot = ["Sword","Bow","Shield", "Health Potion"]
fixedloot = ["Iron", "Wood", "Red Liquids"]



def rare(userobj): # recieve rare treasure
    os.system('cls')
    recieve1 = random.choice(availloot)
    userobj.UserInventory.setdefault(recieve1, 0)
    userobj.UserInventory[recieve1] += 1
    userobj.UserInventory.setdefault("Gold Coins", 0)
    userobj.UserInventory["Gold Coins"] += 30
    userobj.UserInventory.setdefault("Iron Ingots", 0)
    userobj.UserInventory["Iron Ingots"] += 15
    userobj.UserInventory.setdefault("Wood", 0)
    userobj.UserInventory["Wood"] += 10
    userobj.UserInventory.setdefault("Red Liquids", 0)
    userobj.UserInventory["Red Liquids"] += 10
    print("----------------------------------------")
    print("You found rare loot")
    print("You found :")
    print(f"1. 1x {recieve1}")
    print("2. 15x Iron")
    print("3. 10x Wood")
    print("4. 10x Red Liquids")
    print("5. 30x Gold coins")
    print("----------------------------------------")
    print("your current inventory:")
    print(userobj.UserInventory)
    print("----------------------------------------")


def treasure(userobj): #recieve normal treasure
    os.system('cls')
    userobj.UserInventory.setdefault("Iron Ingots", 0)
    userobj.UserInventory["Iron Ingots"] += 5
    userobj.UserInventory.setdefault("Gold Coins", 0)
    userobj.UserInventory["Gold Coins"] += 10
    userobj.UserInventory.setdefault("Wood", 0)
    userobj.UserInventory["Wood"] += 5
    userobj.UserInventory.setdefault("Red Liquids", 0)
    userobj.UserInventory["Red Liquids"] += 2
    print("----------------------------------------")
    print("You found a treasure chest !")
    print("You recieved :")
    print("1. 5x Iron")
    print("2. 5x Wood")
    print("3. 2x Red Liquids")
    print("4. 10x Gold coins")
    print("----------------------------------------")
    print("your current inventory:")
    print(userobj.UserInventory)
    print("----------------------------------------")


def battle(userobj): # battle the enemy ( this will happen most of the time )
    os.system('cls')
    enemyhp = 100
    enemyAGI = 4
    print("you encountered an enemy !")
    while True:
        if enemyhp <= 0:
            userobj.objective = userobj.objective - 1
            treasure(userobj)
            if userobj.story >= 1 and userobj.objective <= 0:
                userobj.strComplt = True
            break
        draw.statusbar(userobj.Health, userobj.Level, userobj.EXP, userobj.Equipped)
        print("----------------------------------------")
        print(f"Enemy Health = {enemyhp}")
        print(f"Player Health = {userobj.Health}")
        print("----------------------------------------")
        print("1. Attack")
        print("2. Defend")
        print("3. Heal")
        print("4. Flee")
        print("----------------------------------------")
        battleChoice = int(input("input the number to continue : "))
        if battleChoice == 1: #attack
            if userobj.Equipped == "Sword":#currently equipped is sword
                print("you dealt damage yet you also received some")
                enemyhp = enemyhp - 50*(userobj.Attr["STR"]*0.1)
                userobj.Health = userobj.Health - 4*(1-userobj.Armor)
            elif userobj.Equipped == "Bow":#currently equipped is bow, there will be 3 scenarios / possibility
                hitProb = random.randint(1, 3)
                if hitProb == 1:
                    print("you dealt damage")
                    enemyhp = enemyhp - 10 * (userobj.Attr["STR"] * 0.2)
                elif hitProb == 2:
                    print("you dealt damage yet you also received some")
                    enemyhp = enemyhp - 10 * (userobj.Attr["STR"] * 0.2)
                    userobj.Health = userobj.Health - 8 * (1 - userobj.Armor)
                else:
                    print("You missed and you got hit!")
                    userobj.Health = userobj.Health - 8 * (1 - userobj.Armor)

        elif battleChoice == 2:#defend
            print("you defended the enemy's attack")

        elif battleChoice == 3:#heal
            if userobj.Health >= 100:
                print("max health !")
            elif userobj.UserInventory["Health Potion"] >= 1:
                print("you used a health potion")
                userobj.Health += 10
                userobj.UserInventory["Health Potion"] = userobj.UserInventory["Health Potion"] - 1
                if userobj.Health >= 100: userobj.Health = 100 #cant go above 100
            else:
                print("no health potion left")

        elif battleChoice == 4:#flee. success depends on the lck attribute
            if userobj.attr["AGI"] >= enemyAGI:
                if userobj.attr["LCK"] >= 6:
                    chance = random.random(1,100)
                    if chance >= 49:
                        print("You've escaped !")
                        break
                    else:
                        print("Unable to escape !")
                elif userobj.attr["LCK"] >= 5:
                    chance = random.random(1,100)
                    if chance >= 43:
                        print("You've escaped !")
                        break
                    else:
                        print("Unable to escape !")
                elif userobj.attr["LCK"] >= 4:
                    chance = random.random(1,100)
                    if chance >= 34:
                        print("You've escaped !")
                        break
                    else:
                        print("Unable to escape !")
                else:
                    chance = random.random(1, 100)
                    if chance >= 25:
                        print("You've escaped !")
                        break
                    else:
                        print("Unable to escape !")
            else: print("Unable to escape!")


def dungeon(userobj):
    os.system('cls')
    print("You enter the dungeon")
    while True:
        print("------------The Dungeon---------------")
        print("would you like to search deeper ?")
        print("1. Yes")
        print("2. No")
        print("--------------------------------------")
        searchChoice = int(input("Input number to continue : "))
        if searchChoice == 1:
            path = [1,2,3]
            randompath = random.choices(path, weights=[50,5,1])
            if randompath == [1]:
                battle(userobj)
            elif randompath == [2]:
                treasure(userobj)
            elif randompath == [3]:
                rare(userobj)
        elif searchChoice == 2: break
        else: print("Error input")
        time.sleep(1)
        os.system('cls')
