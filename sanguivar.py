print("Welcome to Sanguivar, Adventure Awaits! Please state your name to enter")

name = input("What is your name?")

print(f"Hello {name}, enter at your own risk")
#Player wakes up in dark dusty cell
inventory = []
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
    

