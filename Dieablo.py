"""
Dieablo - a die rolling action role playing game

Obtain lucky loot so that you can get luckier and obtain luckier loot. Thinking outside the Skinner Box.

Notes:
1) Rewrote and cleaned code to incorporate helper functions. Added proof for rolls on item generation for testing.
2) To do: add functionality to "save"/"equip" items under equipped_items
3) To do: once items are saved/equipped, add this value to rolls as a sort of "player power level"
4) To do: add "weighting" to item rolls (may involve considerable rewrite to item rolling code)
5) To do: make player power level affect item roll weighting
6) To do: add functionality to save games

See sample equipped item code below:
    # Dictionary which records equipped items
    equipped_items = {
    "weapon_name": "0",
    "weapon_power": 0,
    "armour_name": "0",
    "armour_power": 0,
    "jewellery_name": "0",
    "jewellery_power": 0
    }

 Extra note to self: Draft weighting code saved in separate file, to incorporate.

"""

import random

# Program version and tagline
VERSION = "Pre-alpha 0.3"
TAGLINE = "Stay a while, and roll..."

def main():

 # Dictionary which lists item types and assigns them a number
    item_types = {
    "Weapon": 1,
    "Armour": 2,
    "Jewellery": 3
    }

 # Dictionary which contains item prefixes and their associated dice modifiers
    item_prefixes = {
    "Cursed": -10,
    "Unlucky": -5,
    "Trusty": 1,
    "Fortunate": 2,
    "Lucky" : 3,
    "Uncanny" : 4,
    "Weighted": 5,
    "Blessed": 10
    }

 # Dictionary which contains material types and their associated dice modifiers
    item_materials = {
    "Stone": -10,
    "Wooden": -5,
    "Copper": 1,
    "Bronze": 2,
    "Iron" : 3,
    "Steel" : 4,
    "Obsidian": 5,
    "Mythril": 10
    }

 # Dictionary which contains weapon types and their associated dice modifiers
    weapon_types = {
    "Pebble": -10,
    "Stick": -5,
    "Sword": 1,
    "Axe": 2,
    "Mace" : 3,
    "Longbow" : 4,
    "Katana": 5,
    "Staff": 10
    }

 # Dictionary which contains armour types and their associated dice modifiers
    armour_types = {
    "Pants": -10,
    "Shirt": -5,
    "Garb": 1,
    "Tunic": 2,
    "Cuirass" : 3,
    "Hauberk" : 4,
    "Mail": 5,
    "Plate": 10
    }

 # Dictionary which contains jewellery types and their associated dice modifiers
    jewellery_types = {
    "Trinket": -10,
    "Charm": -5,
    "Bangle": 1,
    "Bracelet": 2,
    "Earring" : 3,
    "Ring" : 4,
    "Amulet": 5,
    "Crown": 10
    }

 # Dictionary which contains item suffixes and their associated dice modifiers
    item_suffixes = {
    "Sloth": -10,
    "Lemming": -5,
    "Mouse": 1,
    "Rabbit": 2,
    "Dog" : 3,
    "Cat" : 4,
    "Parrot": 5,
    "Dragon": 10
    }

    # Prints a welcome message
    print(end='\n')
    print("Dieablo", VERSION, ":", TAGLINE)
    print("---------------------------------------------------")
    print(end='\n')

    # Input prompt which commences and/or restarts the code
    while input("Roll the dice? Press enter.") == "":

        # Generates an item tuple from the dictionary
        def get_item(d):
            random_key = random.choice(list(d.keys()))
            return random_key, d[random_key]

        # Generate item attributes and corresponding power values
        prefix, prefix_value = get_item(item_prefixes)
        material, material_value = get_item(item_materials)
        weapon, weapon_value = get_item(weapon_types)
        armour, armour_value = get_item(armour_types)
        jewellery, jewellery_value = get_item(jewellery_types)
        suffix, suffix_value = get_item(item_suffixes)

        # Generate complete names for items
        raw_weapon_name = (prefix, material, weapon, "of the", suffix)
        weapon_name = ' '.join(raw_weapon_name)

        raw_armour_name = (prefix, material, armour, "of the", suffix)
        armour_name = ' '.join(raw_armour_name)

        raw_jewellery_name = (prefix, material, jewellery, "of the", suffix)
        jewellery_name = ' '.join(raw_jewellery_name)

        # Random power value to be added to item power
        random_power = random.randint(1, 20)

        # Compute combined powers for each item
        weapon_power = prefix_value + material_value + weapon_value + suffix_value + random_power
        armour_power = prefix_value + material_value + armour_value + suffix_value + random_power
        jewellery_power = prefix_value + material_value + jewellery_value + suffix_value + random_power

        # Picks an item type
        rolled_item_type = get_item(item_types)[0]

        # Defines the function which prints the resulting item
        def print_final_item():
            if rolled_item_type == "Weapon":
                print(end='\n')
                print(weapon_name)
                print("Item type:", rolled_item_type)
                print("Power level:", weapon_power)
                print(end='\n')
                print("(",prefix, prefix_value, "+", material, material_value, "+", weapon, weapon_value, "+",
                suffix, suffix_value, "+", "Random Power (1-20)", random_power, "=", weapon_power,")")

            elif rolled_item_type == "Armour":
                print(end='\n')
                print(armour_name)
                print("Item type:", rolled_item_type)
                print("Power level:", armour_power)
                print(end='\n')
                print("(",prefix, prefix_value, "+", material, material_value, "+", armour, armour_value, "+",
                      suffix, suffix_value, "+", "Random Power (1-20)", random_power, "=", armour_power,")")

            elif rolled_item_type == "Jewellery":
                print(end='\n')
                print(jewellery_name)
                print("Item type:", rolled_item_type)
                print("Power level:", jewellery_power)
                print(end='\n')
                print("(",prefix, prefix_value, "+", material, material_value, "+", jewellery, jewellery_value, "+",
                      suffix, suffix_value, "+", "Random Power (1-20)", random_power, "=", jewellery_power,")")

        # Call the function to print the resulting item
        print_final_item()

if __name__ == "__main__":
    main()
