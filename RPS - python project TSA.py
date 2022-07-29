#Rock-Paper-Scissors Game - TSA Python Project
import random as r
import time
import os

menu = "y"
def player_choice(user_pick):
    global u_pick
    if user_pick < 1 or user_pick > 3:
        print("Invalid: choose any one -- rock, paper, scissors")
        exit()
    elif user_pick == 1:
        u_pick = 'rock'
    elif user_pick == 2:
        u_pick = 'paper'
    elif user_pick == 3:
        u_pick = 'scissors'
    else:
        print("Invalid Selected!")

def computer_choice(comp_pick):
    global choice
    if comp_pick == 1:
        choice = 'rock'
    elif comp_pick == 2:
        choice = 'paper'
    else:
        choice = 'scissors'

def result(u_pick, choice):
    if choice == u_pick:
        print("tie, you both select same")
    elif choice == 'rock' and u_pick == 'rock':
        print("tie, you both select same")
    elif choice == 'rock' and u_pick == 'paper':
        print("You win, Computer select rock")
    elif choice == 'rock' and u_pick == 'scissors':
        print("Computer win, Computer select rock")
    elif choice == 'paper' and u_pick == 'rock':
        print("Computer win, Computer select paper")
    elif choice == 'paper' and u_pick == 'scissors':
        print("You win, Computer select paper")
    elif choice == 'scissors' and u_pick == 'rock':
        print("You win, Computer select rock")
    elif choice == 'scissors' and u_pick == 'paper':
        print("Computer win, Computer select scissors")
    else:
        print("Invalid: choose any one -- rock, paper, scissors")

while (menu == "y"):
    comp_pick = r.randint(1, 3)
    while True:
        try:
            os.system('cls')
            print("Rock-Paper-Scissors Game")
            print("options: \n[1] Rock \n[2] Paper \n[3] Scissors")
            user_pick = int(input("Select your choice [1/2/3]: "))
            player_choice(user_pick)
            computer_choice(comp_pick)
            time.sleep(1)
            print("\nYou choose, " + u_pick)
            result(u_pick, choice)
            break
        except ValueError:
            print("That was no valid number.  Try again...")
            time.sleep(2)

    time.sleep(2)
    menu = input("\ndo you want to continue the game? (y/n) \n")
