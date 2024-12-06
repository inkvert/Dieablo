"""
Dieablo - a die rolling action role playing game

Obtain lucky loot so that you can get luckier and obtain luckier loot. Thinking outside the Skinner Box.

Notes:
1) Added cumulative weighting and adjusted item drop tables.
2) To do: add functionality to "save"/"equip" items under equipped_items
3) To do: once items are saved/equipped, add this value to rolls as a sort of "player power level"
4) To do: add functionality to save games

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
"""

import random

# Program version and tagline
VERSION = "Pre-alpha 0.4"
TAGLINE = "Stay a while, and roll..."

# Sets the minimum and maximum range for item weighting rolls
MIN_WEIGHT = 1
MAX_WEIGHT = 10000

# Sets the minimum and maximum range for random power added to items
MIN_POWER = 1
MAX_POWER = 5

def main():
    # Dictionary which lists item types and assigns them a number
    item_types = {
        "Weapon": 1, "Armour": 2, "Jewellery": 3
    }
    # Dictionary which records equipped items
    equipped_items = {
        "weapon_name": "0", "weapon_power": 0,
        "armour_name": "0", "armour_power": 0,
        "jewellery_name": "0", "jewellery_power": 0
    }
    # Dictionary which contains item prefixes and their associated power and drop weight (out of 10,000)
    item_prefixes = {
        "Trusty": {"tier": 1, "power": 1, "weight": 5000},
        "Fortunate": {"tier": 2, "power": 2, "weight": 3000},
        "Lucky": {"tier": 3, "power": 3, "weight": 1250},
        "Uncanny": {"tier": 4, "power": 4, "weight": 640},
        "Weighted": {"tier": 5, "power": 5, "weight": 100},
        "Blessed": {"tier": 6, "power": 10, "weight": 10},
        "Destined": {"tier": 7, "power": 20, "weight": 1}
    }
    # Dictionary which contains material types and their associated power and drop weight (out of 10,000)
    item_materials = {
        "Copper": {"tier": 1, "power": 1, "weight": 5000},
        "Bronze": {"tier": 2, "power": 2, "weight": 3000},
        "Iron": {"tier": 3, "power": 3, "weight": 1250},
        "Steel": {"tier": 4, "power": 4, "weight": 640},
        "Obsidian": {"tier": 5, "power": 5, "weight": 100},
        "Mythril": {"tier": 6, "power": 10,  "weight": 10},
        "Titanium": {"tier": 7, "power": 20, "weight": 1}
    }
    # Dictionary which contains weapon types and their associated power and drop weight (out of 10,000)
    weapon_types = {
        "Sword": {"tier": 1, "power": 1, "weight": 5000},
        "Axe": {"tier": 2,  "power": 2, "weight": 3000},
        "Mace": {"tier": 3, "power": 3, "weight": 1250},
        "Longbow": {"tier": 4, "power": 4, "weight": 640},
        "Katana": {"tier": 5, "power": 5, "weight": 100},
        "Staff": {"tier": 6, "power": 10, "weight": 9},
        "Tachi": {"tier": 7, "power": 20, "weight": 1}
    }
    # Dictionary which contains armour types and their associated power and drop weight (out of 10,000)
    armour_types = {
        "Garb": {"tier": 1, "power": 1, "weight": 5000},
        "Tunic": {"tier": 2, "power": 2, "weight": 3000},
        "Cuirass": {"tier": 3, "power": 3, "weight": 1250},
        "Hauberk": {"tier": 4, "power": 4, "weight": 640},
        "Mail": {"tier": 5, "power": 5, "weight": 100},
        "Plate": {"tier": 6, "power": 10, "weight": 9},
        "Gosoku": {"tier": 7, "power": 20, "weight": 1},
    }
    # Dictionary which contains jewellery types and their associated power and drop weight (out of 10,000)
    jewellery_types = {
        "Bangle": {"tier": 1, "power": 1, "weight": 5000},
        "Bracelet": {"tier": 2, "power": 2, "weight": 3000},
        "Earring": {"tier": 3, "power": 3, "weight": 1250},
        "Ring": {"tier": 4, "power": 4, "weight": 640},
        "Amulet": {"tier": 5, "power": 5, "weight": 100},
        "Crown": {"tier": 6, "power": 10, "weight": 10},
        "Brooch": {"tier": 7, "power": 20, "weight": 1}
    }
    # Dictionary which contains item suffixes and their associated power and drop weight (out of 10,000)
    item_suffixes = {
        "Mouse": {"tier": 1, "power": 1, "weight": 5000},
        "Rabbit": {"tier": 2, "power": 2, "weight": 3000},
        "Dog": { "tier": 3, "power": 3, "weight": 1250},
        "Cat": {"tier": 4, "power": 4, "weight": 640},
        "Parrot": {"tier": 5, "power": 5, "weight": 100},
        "Dragon": {"tier": 6, "power": 10, "weight": 10},
        "Basilisk": {"tier": 7, "power": 20, "weight": 1}
    }
    # Prints a welcome message
    print(end='\n')
    print("Dieablo", VERSION, ":", TAGLINE)
    print("---------------------------------------------------")
    print(end='\n')

    # Input prompt which commences and/or restarts the code
    while input("Roll the dice? Press enter.") == "":

        def roll_item(dic):
            # Roll a random number between defined weight range
            roll = random.randint(MIN_WEIGHT, MAX_WEIGHT)

            # Create cumulative weights
            cumulative = 0
            cumulative_weights = []

            for item, details in dic.items():
                cumulative += details['weight']
                cumulative_weights.append((cumulative, item, details['power']))

            for cumulative_weight, item, power in cumulative_weights:
                if roll <= cumulative_weight:
                    return item, power

        prefix, prefix_value = roll_item(item_prefixes)
        material, material_value = roll_item(item_materials)
        weapon, weapon_value = roll_item(weapon_types)
        armour, armour_value = roll_item(armour_types)
        jewellery, jewellery_value = roll_item(jewellery_types)
        suffix, suffix_value = roll_item(item_suffixes)
        
        # Generate complete names for items
        raw_weapon_name = (prefix, material, weapon, "of the", suffix)
        weapon_name = ' '.join(raw_weapon_name)

        raw_armour_name = (prefix, material, armour, "of the", suffix)
        armour_name = ' '.join(raw_armour_name)

        raw_jewellery_name = (prefix, material, jewellery, "of the", suffix)
        jewellery_name = ' '.join(raw_jewellery_name)

        # Random power value to be added to item power
        random_power = random.randint(1, 10)

        # Compute combined powers for each item
        weapon_power = prefix_value + material_value + weapon_value + suffix_value + random_power
        armour_power = prefix_value + material_value + armour_value + suffix_value + random_power
        jewellery_power = prefix_value + material_value + jewellery_value + suffix_value + random_power

        # Picks an item type
        rolled_item_type = random.choice(list(item_types.keys()))

        # Defines the function which prints the resulting item
        def print_final_item():
            if rolled_item_type == "Weapon":
                print(end='\n')
                print(weapon_name)
                print("Item type:", rolled_item_type)
                print("Power level:", weapon_power)
                print(end='\n')
                print("(",prefix, prefix_value, "+", material, material_value, "+", weapon, weapon_value, "+",
                suffix, suffix_value, "+", "Random Power (",MIN_POWER,"-",MAX_POWER,")",
                      random_power, "=", weapon_power,")")

            elif rolled_item_type == "Armour":
                print(end='\n')
                print(armour_name)
                print("Item type:", rolled_item_type)
                print("Power level:", armour_power)
                print(end='\n')
                print("(",prefix, prefix_value, "+", material, material_value, "+", armour, armour_value, "+",
                      suffix, suffix_value, "+", "Random Power (",MIN_POWER,"-",MAX_POWER,")",
                      random_power, "=", armour_power,")")

            elif rolled_item_type == "Jewellery":
                print(end='\n')
                print(jewellery_name)
                print("Item type:", rolled_item_type)
                print("Power level:", jewellery_power)
                print(end='\n')
                print("(",prefix, prefix_value, "+", material, material_value, "+", jewellery, jewellery_value, "+",
                      suffix, suffix_value, "+", "Random Power (",MIN_POWER,"-",MAX_POWER,")",
                      random_power, "=", jewellery_power,")")

        # Call the function to print the resulting item
        print_final_item()

if __name__ == "__main__":
    main()
