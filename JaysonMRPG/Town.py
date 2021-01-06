#sleep,craft,shop is in here
#import JaysonMRPG.User as user

import os, time
import Draw as draw

shopinventory = { "Sword":10, "Bow":10, "Shield":10, "Health Potion":10, "Iron Armor":10, "Food":50, "Drink":50}
shoplist = list(shopinventory.keys())
shopPrice = { "Sword":7, "Bow":5, "Shield":4, "Health Potion":5, "Iron Armor":7, "Food":2, "Drink":2}
craftPrice = { "Sword":3, "Bow":2, "Shield":2, "Health Potion":5, "Iron Armor":2}
recycleavail = { "Iron Ingots":10, "Wood":10, "Red Liquids": 5, }
materials = ["Iron", "Wood", "Red Liquids"]

def inventory(userobj): # display inventory
    os.system('cls')
    print("-----------Inventory-----------")
    count = 1
    for item in userobj.UserInvetory.keys():
        count += 1
        print(f"{count}. {item} - {userobj.UserInvetory}")

def sleep(userobj): # sleep / heal
    os.system('cls')
    print("You decided to take a sleep at the nearby inn.")
    print("Health is healed to full ")
    print("Stamina and Mana are restored")
    print("----------------------------------------------")
    print("Cost : 2 gold coins")
    userobj.Health = 100
    userobj.Stamina = 100
    userobj.Mana = 50
    userobj.UserInventory["Gold Coins"] = userobj.UserInventory["Gold Coins"] - 2
    print(f"Balance : {userobj.UserInventory['Gold Coins']}")
    print("----------------------------------------------")
    time.sleep(4)
    while True:
        os.system('cls')
        print("----------------------------------------------")
        print("would you like to change inventory settings ? ")
        print("1. Yes")
        print("2. No ( exit inn )")
        print("----------------------------------------------")
        invChoice = int(input("input the NUMBER to continue : "))
        if invChoice == 1:
            draw.statusbar(userobj)
            inventory(userobj)
            print("----------------------------------------------")
            print("What would you like to do ?")
            print("1. Change weapon")
            print("2. Change Armor")
            print("3. Exit inn")
            print("----------------------------------------------")
            invChoice2 = int(input("input the NUMBER to continue : "))
            if invChoice2 == 1:
                print("change to : ")
                if "Excalibur" in userobj.UserInventory.keys() and "Bow" in userobj.UserInventory.keys():
                    print("Sword || Bow || Excalibur")
                elif "Excalibur" in userobj.UserInventory.keys():
                    print("Sword ||  Excalibur")
                elif "Bow" in userobj.UserInventory.keys():
                    print("Sword || Bow")
                else: print("You only have the Sword")
            elif invChoice2 == 2:
                print("change to : ")
                if "Iron Armor" in userobj.UserInventory.keys():
                    print("Leather Armor || Iron Armor")
                else: print("You only have Leather Armor")
            elif invChoice2 == 3: break
            else:
                print("Error Input")

        elif invChoice == 2: break

        else: print("Error Input")






def shop(userobj): # buy items
    os.system('cls')
    print("You entered the shop.")
    while True:
        print("----------Ethereal Fowl Shop-------------")
        print(f"your current gold amount : {userobj.UserInventory['Gold Coins']}")
        print("The shop is currently selling ")
        print("item : price : availability")
        count = 0
        for item in shopinventory.keys(): # display the items
            count += 1
            print(f"{count}. {item} : {shopPrice[item]} : {shopinventory[item]}")
        print("-----------------------------------------")
        print("What would you like to purchase ?")
        print("input 'exit' to exit the shop")
        buyChoice = str(input("input the exact name in the list : "))
        if buyChoice == 0: break
        amt = int(input("input purchase amount : "))
        if shopinventory[buyChoice] != 0 : #buy the selected item
            if userobj.UserInventory["Gold Coins"] >= (amt*shopPrice[buyChoice]):
                userobj.UserInventory.setdefault(buyChoice,0)
                userobj.UserInventory[buyChoice] += amt
                shopinventory[buyChoice] = shopinventory[buyChoice] - amt
            else:
                print("Not enough Gold Coins")
        else:
            print("No longer available ")


def blacksmith(userobj): #craft items
    os.system('cls')
    print("You entered the Blacksmith ")
    while True:
        print("----------Curious Forge-------------")
        print("Current inventory:")
        print(f"Gold Coins : {userobj.UserInventory['Gold Coins']}")
        print(f"Iron Ingots : {userobj.UserInventory['Iron Ingots']}")
        print(f"Wood : {userobj.UserInventory['Wood']}")
        print("-------------------------------------")
        print("------------Part 1--------------")
        print("Item : Cost : Iron : Wood")
        print("1. Sword : 3 : 2 : 1")
        print("2. Bow : 2 : 0 : 2")
        print("3. Shield : 2 : 3 : 2")
        print("4. Iron Armor : 2 : 3 : 0")
        print("------------Part 2--------------")
        print("Item : Cost : Red Liquids : Yellow Liquid")
        print("5. Health Potion : 5 : 4 : 0")
        print("-------------------------------------")
        print("What will you Craft ? ")
        print("type 'exit' to exit the blacksmith")
        craftChoice = str(input("input the EXACT name of the item : "))

        if craftChoice == "exit": break # exit the blacksmith
        amount = int(input("amount to craft : "))
        # crafting program below
        if craftChoice == "Sword" and userobj.UserInventory["Iron Ingots"] >= amount*2 and userobj.UserInventory["Wood"] >= amount*1 and userobj.UserInventory["Gold Coins"] >= amount*3:
            userobj.UserInventory["Gold Coins"] = userobj.UserInventory["Gold Coins"] - amount*3
            userobj.UserInventory["Iron Ingots"] = userobj.UserInventory["Iron Ingots"]  - amount*2
            userobj.UserInventory["Wood"] = userobj.UserInventory["Wood"] - amount*1
            userobj.UserInventory.setdefault(craftChoice, 0)
            userobj.UserInventory[craftChoice] += amount

        elif craftChoice == "Bow" and userobj.UserInventory["Wood"] >= 2 and userobj.UserInventory["Gold Coins"] >= amount*2:
            userobj.UserInventory["Gold Coins"] = userobj.UserInventory["Gold Coins"] - amount*2
            userobj.UserInventory["Wood"] = userobj.UserInventory["Wood"] - amount*2
            userobj.UserInventory.setdefault(craftChoice, 0)
            userobj.UserInventory[craftChoice] += amount

        elif craftChoice == "Shield" and userobj.UserInventory["Iron Ingots"] >= amount*3 and userobj.UserInventory["Wood"] >= amount*2 and userobj.UserInventory["Gold Coins"] >= amount*2:
            userobj.UserInventory["Gold Coins"] = userobj.UserInventory["Gold Coins"] - amount*2
            userobj.UserInventory["Iron Ingots"] = userobj.UserInventory["Iron Ingots"] - amount*3
            userobj.UserInventory["Wood"] = userobj.UserInventory["Wood"] - amount*2
            userobj.UserInventory.setdefault(craftChoice, 0)
            userobj.UserInventory[craftChoice] += amount

        elif craftChoice == "Iron Armor" and userobj.UserInventory["Iron Ingots"] >= amount*3 and userobj.UserInventory["Gold Coins"] >= amount*2:
            userobj.UserInventory["Gold Coins"] = userobj.UserInventory["Gold Coins"] - amount*2
            userobj.UserInventory["Iron Ingots"] = userobj.UserInventory["Iron Ingots"] - amount*3
            userobj.UserInventory.setdefault(craftChoice, 0)
            userobj.UserInventory[craftChoice] += amount

        elif craftChoice == "Health Potion" and userobj.UserInventory["Red Liquids"] >= amount*4 and userobj.UserInventory["Gold Coins"] >= amount*5:
            userobj.UserInventory["Gold Coins"] = userobj.UserInventory["Gold Coins"] - amount*5
            userobj.UserInventory["Red Liquids"] = userobj.UserInventory["Red Liquids"] - amount*4
            userobj.UserInventory.setdefault(craftChoice, 0)
            userobj.UserInventory[craftChoice] += amount

        else: #error checking
            if craftChoice not in shoplist:
                print("Incorrect input")
            else:
                print("Insufficient Materials")

        os.system('cls')
        print(userobj.UserInventory)


def recycle_sell(userobj): # recycle items
    print("----------The Recycle Station-------------")
    inventory()
    print("------------------------------------------")
    print("Current shop inventory:")
    print(recycleavail)
    print("------------------------------------------")
    print("Able to Recycle: ")
    print("Sword | Bow | Iron Armor | Health Potion")
    print("what do you wish to recycle ?")
    cycleChoice = input("type the EXACT name: ")
    if cycleChoice in userobj.UserInventory.keys(): #recycle the selected item
        if cycleChoice == "Sword":
            if recycleavail["Iron Ingots"] >= 1:
                userobj.UserInventory.setdefault("Iron Ingots", 0)
                userobj.UserInventory["Iron Ingots"] += 1
        elif cycleChoice == "Bow":
            if recycleavail["Wood"] >= 1:
                userobj.UserInventory.setdefault("Wood", 0)
                userobj.UserInventory["Wood"] += 1
        elif cycleChoice == "Iron Armor":
            if recycleavail["Iron Ingots"] >= 2:
                userobj.UserInventory.setdefault("Iron Ingots", 0)
                userobj.UserInventory["Iron Ingots"] += 2
        elif cycleChoice == "Health Potion":
            if recycleavail["Red Liquids"] >= 1:
                userobj.UserInventory.setdefault("Red Liquids", 0)
                userobj.UserInventory["Red Liquids"] += 1
        else:
                print("not enough materials from the Station")
                print("------------------------------------------")
    else:
        print("Incorrect Input !")
        print("------------------------------------------")


