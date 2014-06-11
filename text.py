import time
import random

spider_damage = 10
inventory = []
iron_dagger_damage = random.randint(5,12)
player_damage = iron_dagger_damage


def intro():
    print("You are lost in the woods. You know that if you follow the right path, you will get to the nearest village.")
    time.sleep(1)
    print("You see that there are 2 paths ahead. In which one do you want to go(left or right)")
def left_or_right():
    choice = ""
    print("Where do you want to go, left or right?")
    choice = input()
    return choice

def intro_end(left_or_right):
    if choice == "left":
        print("You go down the path to the left and...")
        time.sleep(1)
        print("You die a horrible death")
        input()
        quit()

    elif choice == "right":
        print("You go down the path to the right and...")
        time.sleep(1)
        print("Notice that the trees are thinning out")
        time.sleep(1)

def iron_dagger():
    iron_dagger = ''
    print("You see a flash of light in the forest. Do you want to risk the forest to go see what it was?(yes or no)")
    iron_dagger = input()
    return iron_dagger

def choice1_end(iron_dagger):
    if iron_dagger == "yes":
        print("You find an iron dagger!")
        inventory.append("iron dagger")
        print(inventory)
    elif iron_dagger == "no":
        print("You continue on")
    else:
        iron_dagger

def part_1():
    print("You finally get out of the forest")
    time.sleep(1)
    print("You see a giant frost spider in the distance")
    print("""
               (
                )
               (
         /\  .-" "-.  /\
        //\\/  ,,,  \//\\
        |/\| ,;;;;;, |/\|
        //\\\;-" "-;///\\
       //  \/   .   \/  \\
      (| ,-_| \ | / |_-, |)
        //`__\.-.-./__`\\
       // /.-(() ())-.\ \\
      (\ |)   '---'   (| /)
       ` (|           |) `
         \)           (/)""")


def attack_or_run():
    choice2 = ""
    while choice2 != "1" and choice2 != "2":
        print("Do you want to attack it or run?(1 = attack, 2 = run)")
        choice2 = input()
    return choice2

def part_1_1(attack_or_run):
    if choice2 == "2":
        print("You start to run away")
        time.sleep(1)
        print("You trip on a rock and...")
        time.sleep(1)
        safe = random.randint(1, 10)
        if safe == 1:
            print("You continue on towards the nearest village")
        else:
            print("You fall into a ravine and die")
            input()
            quit()
    if choice2 == "1":
        if "iron dagger" in inventory:
            print("You run towards the spider with your iron dagger")
            time.sleep(1)
            print("You start to attack it and...")
            time.sleep(1)
        else:
            print("You desperatly try to kill the spider with your fists but fail miserably")
            input()
            quit()

def encounter_1(part_1_1):
    if choice2 == "1":
        John_Smith_hp = 50
        Giant_spider_hp = 30
        while True:
            Giant_spider_hp = Giant_spider_hp - player_damage
            John_Smith_hp = John_Smith_hp - spider_damage
            if Giant_spider_hp < 1:
                print("You kill the spider")
                break;
            print ("Spider health:", Giant_spider_hp, "/30")
            time.sleep(0.5)
            if John_Smith_hp < 1:
                print("You got killed by the spider")
                break;
            print("Your health", John_Smith_hp, "/50")
            time.sleep(0.5)


def part_1_2(attack_or_run, part_1_1):
    if choice2 == "1":
        bottle = ""
        while bottle != "yes" and bottle != "no":
            print("You find a strange bottle with some kind of potion in it. Do you want to take it with you?")
            bottle = input()
    print("You spot a giant on the road")
    time.sleep(1)
    if bottle == "yes":
        print("You know you cannot deafeat him, but perhaps the bottle could help you?")
        time.sleep(1)
        inventory.append("bottle")
    elif bottle == "no":
        print("You know you cannot deafeat him...")
        time.sleep(1)
        print("You try to run away but realize that it's hopeless as the giant closes in on you")
        time.sleep(1)
        print("Perhaps that bottle could have saved you...?")
        input()
        quit()

    else:
        print("You know you cannot deafeat him...")
        time.sleep(1)
        print("You try to run away but realize that it's hopeless as the giant closes in on you...")
        input()
        quit()

def part_1_3():
    if "bottle" in inventory:
        choice3 = ""
        print("What do you want to do?")
        print("Print HELP if you don't know what to do")
        print("1.drink, 2.run, 3.fight, 4.apply to weapon")

        choice3 = input()
        if choice3 == "drink" or choice3 == "1":
            print("You drink the potion and collapse on the ground dead. Maybe that wasn't such a good idea")
            input()
            quit()
        elif choice3 in["fight", "run", "3", "2"]:
            print("You get destroyed by the giant")
            input()
            quit()

        elif choice3 == "apply" or choice3 == "4":
            print("You apply the potion to your shortsword and charge the giant")
            time.sleep(1)
            print("You manage to cut the giant and he collapses to the ground.")
            time.sleep(1)

        else:
            part_1_3()

def part_1_4():
    print("You finally arrive to the village")










playagain = "yes"
if playagain == "yes":
    intro()
    choice = left_or_right()
    intro_end(left_or_right)
    iron_dagger()
    iron_dagger = iron_dagger()
    choice1_end(iron_dagger)
    part_1()
    choice2 = attack_or_run()
    part_1_1(attack_or_run)
    encounter_1(part_1_1)
    part_1_2(part_1_1, attack_or_run)
    part_1_3()
    part_1_4
