# inventory.py

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_invetory(inventory):
    print("Invetory:")
    item_total = 0
    for k, v, in inventory.items():
        print(str(v) + " " + str(k))
        item_total += v
    print("Total number of items: " + str(item_total))

display_invetory(stuff)