import json


def check(item):
    """ Check if an item is in the inventory """
    # Load in json file of valid objects
    with open("inventory.json") as file:
        inven = json.load(file)

        # If the item is not in inventory, return False
        if item not in inven:
            return False
        if inven[item] == "False":
            return False

        return True


def add(item):
    """ Add an item to the inventory """
    # Read from json file
    with open("inventory.json", "r") as file:
        inven = json.load(file)

    # If item not already in inventory, add it
    if item not in inven:
        inven[item] = "True"
    if inven[item] == "False":
        inven[item] = "True"

    # Write updated inventory to file
    with open("inventory.json", "w") as file:
        json.dump(inven, file, indent=4)


def remove(item):
    """ Remove an item from the inventory """
    # Read from json file
    with open("inventory.json", "r") as file:
        inven = json.load(file)

    # Check whether the item is already in inventory, and remove it if so
    if item in inven:
        if inven[item] == "True":
            inven[item] = "False"

    # Write updated inventory to file
    with open("inventory.json", "w") as file:
        json.dump(inven, file, indent=4)


def get_inv():
    with open("inventory.json", "r") as file:
        inven = json.load(file)

    inventory = []

    for item in inven:
        if inven[item] == "True":
            inventory.append(item)

    file.close()

    return inventory


def desc():

    return


def main():
    """ Main function for debugging """
    print("\nCheck your inventory? Y/N")
    option = input(">>")
    if option.upper() == "Y":
        with open("inventory.json", "r") as file:
            inven = json.load(file)

        print("\nYou check your inventory. You are carrying...")
        for each in inven:
            if inven[each] == "True":
                print("-", each)


if __name__ == "__main__":
    main()
