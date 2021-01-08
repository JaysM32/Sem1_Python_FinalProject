import Draw as draw
import User as user
import Town as town
import Dungeon as dugn
import Story as str
import time, os


def main():
    while True :
        draw.mainmenu()
        mainmenuchoice = int(input("enter the number to continue: "))
        if mainmenuchoice == 1:
            gameuser = user.createUser() #temporaryly create a user to be used
            print("-----------------------------------")
            print("Currently Loading")
            print("-----------------------------------")
            time.sleep(4)
            draw.startstory()
            startstorychoice = int(input())
            if startstorychoice == 1:
                draw.introstory1(gameuser.name)
                choice2 = int(input("Input the number : "))
                if choice2 == 1:
                    town.shop(gameuser) #buy and sell items
                elif choice2 == 2:
                    town.blacksmith(gameuser) #craft and recycle items
                elif choice2 == 3:
                    town.sleep(gameuser) #heal and save the game to a file.

                else:
                    print("ERROR: Unknown Input")

                count = 0
                while True:
                    count += 1
                    if count >= 2:
                        draw.insidetown(True) #mainmenu when in the game
                    else:
                        draw.insidetown(False) #mainmenu when in the game
                    choice3 = int(input("Input the number : "))
                    if choice3 == 0:
                        break
                    elif choice3 == 1:
                        town.shop(gameuser)
                    elif choice3 == 2:
                        town.blacksmith(gameuser)
                    elif choice3 == 3:
                        town.sleep(gameuser)
                    elif choice3 == 4:
                        dugn.dungeon(gameuser)
                    elif choice3 == 5:
                        town.recycle_sell(gameuser)
                    elif choice3 == 6 and count >= 2:
                        if gameuser.story == 0: str.part1(gameuser) # once executed, cant go back to here
                        elif gameuser.story == 1: str.part2(gameuser)
                        elif gameuser.story == 2: str.part3(gameuser)
                    else:
                        print("ERROR: Unknown Input")

            elif startstorychoice == 2:
                draw.introstory2()
                break

        elif mainmenuchoice == 2:
            draw.help()

        elif mainmenuchoice == 3:
            os.system('cls')
            print("Thank you for playing the Game !")
            break

        else:
            print("ERROR: Unknown Input")
            print("-----------------------------------------------")

if __name__ == '__main__':
    main()