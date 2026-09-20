print("Welcome to Sanguivar, Adventure Awaits! Please state your name to enter")

name = input("What is your name?")
choose_class = input("Choose your class: 1.Warrior, 2.Witch, 3.Healer")
while choose_class not in ["1", "2", "3"]:
    print("Invalid class choice! Try again.")
    choose_class = input(" 1. Warrios, 2.Witch, 3. Healer")
if choose_class == "1":
    print("You have chosen the Warrior class!")
    character_class = "Warrior"
    health = 5
    strength = 6
    magic = 4
    starting_item = "Sword"

elif choose_class == "2":
    print("You have chosen the Witch class!")
    character_class = "Witch"
    health = 5
    strength = 4
    magic = 6
    starting_item = "Wand"

elif choose_class == "3":
    print("You have chosen the Healer class!")
    character_class = "Healer"
    health = 5
    strength = 5
    magic = 5
    starting_item = "Alchemy kit"


print(f"Hello {name}, the {character_class}, your adventure begins now!")
print(f"Your starting item is: {starting_item}")
print(f"Your starting stats are: Health: {health}, Strength: {strength}, Magic: {magic}")
#Player wakes up in dark dusty cell
inventory = []
inventory.append(starting_item)
door_open = False
print("You wake up in a dark dusty cell")
while door_open == False:
    print("1. Search the cell")
    print("2. Try the cell door")
    action = input("What do you do? ")

    if action == "1":
        if "rusty key" not in inventory:
            print("You find a rusty key on the floor")
            inventory.append("rusty key")
        else:
            print("You already searched the cell")
    elif action == "2":
    
        if "rusty key" in inventory: 
            print("The door creaks open")
            door_open = True
        else: 
            print("The door is locked, you need to find the key!")

print("You step outside into the dimly lit corridor")
print("1. Go left")
print("2.Go right")
action = input("What do you do?")
if action == "1":   
        print("You walk down the corridor and find a torch on the wall") 
        print("1. Take the torch")
        print("2. Leave it")
        action = input("What do you do?")

        if action == "1": 
            print("You take the torch and light it, illuminating the corridor")
            inventory.append("torch")
        elif action == "2":
            print("You leave the torch and continue down the corridor in darkness")
elif action == "2":
    print("You walk down the corridor and find a door with a strange symbol on it")
    print("1. Try open the door")
    print("2. Leave it and continue down the corridor")
    action = input("What do you do?")
    if action == "1":
        print("The door is locked, you need to find a key or another way to open it")
    elif action == "2":
        print("You continue down the corrdior and stop at the edge of a steep dark staircase leading into darkness")
    

