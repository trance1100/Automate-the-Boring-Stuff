def display_invetory(inventory):
    print("Invetory:")
    item_total = 0
    for k, v, in inventory.items():
        print(str(v) + " " + str(k))
        item_total += v
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for item in dragonLoot:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory.setdefault(item, 1)
    return inventory
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
display_invetory(inv)