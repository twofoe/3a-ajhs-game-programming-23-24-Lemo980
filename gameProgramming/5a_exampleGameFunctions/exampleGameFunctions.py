# Example Game Functions, Eliot Blanton, v0.0
import random

#Variable Declarations
weaponList = ["Wooden club", "Stone hammer", "Bone spear", "Magic staff of flame", "Steel greatsword", "Silver dagger", "Magical ice mace" ] #List of items in inventory
hitPoints = 500.5 #how much total health a player has
enemyList = ["Skeleton warrior", "Giant hog", "Dark mage", "Venomous serpent", "Goblin warrior", "Giant warrior", "Tree monster", "Werewolf"] #List of possible enemies






#Function Definitions

def enemyEncounter(weaponList,enemyList): #Randomly selects an enemy and allows the user to choose a weapon based on what enemy is selected
    enemy = enemyList[random.randint(0, 7)]
    print(f"A {enemy} crosses your path and begins battle")
    print("""Your weapon options are:
        1: Wooden club
        2: Stone hammer
        3: Bone spear
        4: Magic staff of flame
        5: Steel greatsword
        6: Silver dagger
        7: Magical ice mace""")
    equippedWeapon = weaponList[int(input("Please choose a weapon using a number 1 - 7 \n")) - 1]
    return equippedWeapon, enemy


def damage(equippedWeapon, enemy): #Determines how much damage an enemy will take when hit with different weapons then returns damage value
    if equippedWeapon == "Wooden club":
        if enemy == "Skeleton warrior":
            damage = 25
        elif enemy == "Giant hog":
            damage = 30
        elif enemy == "Dark mage":
            damage = 20
        elif enemy == "Venomous serpent":
            damage = 50
        elif enemy == "Goblin warrior":
            damage = 21
        elif enemy == "Giant warrior":
            damage = 10
        elif enemy == "Tree monster":
            damage = 5
        elif enemy == "Werewolf":
            damage = 15
    elif equippedWeapon == "Stone hammer":
        if enemy == "Skeleton warrior":
            damage = 30
        elif enemy == "Giant hog":
            damage = 35
        elif enemy == "Dark mage":
            damage = 25
        elif enemy == "Venomous serpent":
            damage = 60
        elif enemy == "Goblin warrior":
            damage = 21
        elif enemy == "Giant warrior":
            damage = 15
        elif enemy == "Tree monster":
            damage = 10
        elif enemy == "Werewolf":
            damage = 18
    elif equippedWeapon == "Bone spear":
        if enemy == "Skeleton warrior":
            damage = 10
        elif enemy == "Giant hog":
            damage = 60
        elif enemy == "Dark mage":
            damage = 30
        elif enemy == "Venomous serpent":
            damage = 20
        elif enemy == "Goblin warrior":
            damage = 24
        elif enemy == "Giant warrior":
            damage = 15
        elif enemy == "Tree monster":
            damage = 5
        elif enemy == "Werewolf":
            damage = 20
    elif equippedWeapon == "Magic staff of flame":
        if enemy == "Skeleton warrior":
            damage = 20
        elif enemy == "Giant hog":
            damage = 40
        elif enemy == "Dark mage":
            damage = 50
        elif enemy == "Venomous serpent":
            damage = 30
        elif enemy == "Goblin warrior":
            damage = 30
        elif enemy == "Giant warrior":
            damage = 35
        elif enemy == "Tree monster":
            damage = 90
        elif enemy == "Werewolf":
            damage = 30
    elif equippedWeapon == "Steel greatsword":
        if enemy == "Skeleton warrior":
            damage = 50
        elif enemy == "Giant hog":
            damage = 35
        elif enemy == "Dark mage":
            damage = 35
        elif enemy == "Venomous serpent":
            damage = 30
        elif enemy == "Goblin warrior":
            damage = 60
        elif enemy == "Giant warrior":
            damage = 50
        elif enemy == "Tree monster":
            damage = 30
        elif enemy == "Werewolf":
            damage = 30
    elif equippedWeapon == "Silver dagger":
        if enemy == "Skeleton warrior":
            damage = 15
        elif enemy == "Giant hog":
            damage = 15
        elif enemy == "Dark mage":
            damage = 15
        elif enemy == "Venomous serpent":
            damage = 20
        elif enemy == "Goblin warrior":
            damage = 18
        elif enemy == "Giant warrior":
            damage = 5
        elif enemy == "Tree monster":
            damage = 5
        elif enemy == "Werewolf":
            damage = 100
    elif equippedWeapon == "Magical ice mace":
        if enemy == "Skeleton warrior":
            damage = 30
        elif enemy == "Giant hog":
            damage = 35
        elif enemy == "Dark mage":
            damage = 60
        elif enemy == "Venomous serpent":
            damage = 30
        elif enemy == "Goblin warrior":
            damage = 50
        elif enemy == "Giant warrior":
            damage = 20
        elif enemy == "Tree monster":
            damage = 20
        elif enemy == "Werewolf":
            damage = 20
    return damage

def enemyAttack(enemy):
    if enemy == "Skeleton warrior":
        enemyAttack = 40
    elif enemy == "Giant hog":
        enemyAttack = 35
    elif enemy == "Dark mage":
        enemyAttack = 50
    elif enemy == "Venomous serpent":
        enemyAttack = 60
    elif enemy == "Goblin warrior":
        enemyAttack = 50
    elif enemy == "Giant warrior":
        enemyAttack = 90
    elif enemy == "Tree monster":
        enemyAttack = 100
    elif enemy == "Werewolf":
        enemyAttack = 300
    return enemyAttack

def gameFunction(hitPoints):
    if hitPoints > 500.5:
        playerAlive = True
    while playerAlive:
        enemyEncounter(weaponList, enemyList)
        








































def func3():
    pass

def func3():
    pass






























































