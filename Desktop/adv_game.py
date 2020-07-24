import time
import random


def print_pause(message, wait_time):
    print(message)
    time.sleep(wait_time)


def start():
    print_pause("Help John to reach his home, which is 3 streets away.", 1)
    print_pause("Its late night,John should reach his home asap!", 1)
    print_pause("John is walking on the road alone.", 1)
    print_pause("walking alone, John has two options either left or  right", 1)
    home()


def home():
    print_pause("1.Left \t 2.Right .", 2)
    while True:
        option = input("Enter a number.")
        if option == '1':
            left()
        elif option == '2':
            right()
        else:
            print("Please enter a valid input.")
            home()


def left():
    print_pause("After a while. John saw stray dogs staring at him.", 1)
    print_pause("Little john is scared of them.", 1)
    print_pause("He decided to either walk along the road or runaway.", 1)
    print_pause("1.Walk along the road \t 2.Runaway .", 1)
    while True:
        decision = input("Enter a number.")
        if decision == '1':
            walkalong()
        elif decision == '2':
            runaway()
        else:
            print("Please enter a valid input.")


def walkalong():
    print_pause("As John moved forward. Dogs started to bark at him. ", 1)
    print_pause("Little John is very scared and started to run.", 1)
    print_pause("Dogs chased him for few streets and finally bite John.", 1)
    print_pause("John fell unconsious.", 1)
    print_pause("GAME OVER! Retry.", 1)
    restart()


def runaway():
    print_pause("John ran few streets away from dogs.", 1)
    print_pause("he was deeply tensed about his location now.", 1)
    print_pause("He finds his neighbours searching for him.", 1)
    print_pause("They brought John home safe.", 1)
    print_pause("Hurrayy! you won the game. Better decision.", 1)
    restart()


def restart():
    while True:
        a = input("Do you want to play again (y/n) ? ")
        if a == 'y':
            start()
        elif a == 'n':
            print("Bye! Thank you for playing")
        else:
            print("Bye! Thank you for playing")

y = ['Uncle', 'Nephew', 'Neighbour', 'Father']
z = random.choice(y)


def right():
    print_pause("It was dark here. There were no street lights.", 2)
    print_pause("with lots of fear John walked along the road.", 2)
    print_pause("He turned left and walked for a while.", 2)
    print_pause(f"He saw his {z} .", 2)
    print_pause(f"His {z} safely took him home.", 2)
    print_pause("YOU WON!", 1)
    restart()


start()
