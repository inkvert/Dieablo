"""
Dieablo - a dice rolling action role playing game
Obtain lucky loot so that you can get luckier and obtain luckier loot.
Thinking outside the Skinner's Box.
Notes:
1) Succeeded at generating items based on a die roll and pulling the right data pairs from each dictionary.
2) To do: add functionality to "save"/"equip" items under equipped_items
3) To do: once items are saved/equipped, add this value to rolls as a sort of "player power level"
4) To do: add "weighting" to item rolls (may involve considerable rewrite to item rolling code)
5) To do: make player power level affect item roll weighting
"""

import random

# Program version and tagline
VERSION = "Pre-alpha 0.2"
TAGLINE = "Stay a while, and roll..."

def main():

 # Dictionary which lists item types and assigns them a number
    item_types = {
    "Weapon": 1,
    "Armour": 2,
    "Jewellery": 3
    }
 
 # Dictionary which records equipped items
    equipped_items = {
    "weapon_name": "0",
    "weapon_power": 0,
    "armour_name": "0",
    "armour_power": 0,
    "jewellery_name": "0",
    "jewellery_power": 0
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

        # Item rolling
        # Prefix generation
        # --------------------------------------------------
        # Picks a random key from the item_prefixes dictionary
        def pick_random_key_from_item_prefixes(d: item_prefixes):
            keys = list(d.keys())
            random_key_from_item_prefixes = random.choice(keys)
            return random_key_from_item_prefixes

        # Picks a random item from the item_prefixes dictionary based on the generated key
        def pick_random_item_from_item_prefixes(d: item_prefixes):
            random_key_from_item_prefixes = pick_random_key_from_item_prefixes(d)
            random_item_from_item_prefixes = random_key_from_item_prefixes, d[random_key_from_item_prefixes]
            return random_item_from_item_prefixes

        # Defines the random item from item_prefixes as a variable, then splits the tuple into name and number
        random_item_from_item_prefixes = pick_random_item_from_item_prefixes(item_prefixes)
        name_from_item_prefixes =  random_item_from_item_prefixes[0]
        number_from_item_prefixes = random_item_from_item_prefixes[1]

        # Suffix generation
        # --------------------------------------------------
        # Picks a random key from the item_suffixes dictionary
        def pick_random_key_from_item_suffixes(d: item_suffixes):
            keys = list(d.keys())
            random_key_from_item_suffixes = random.choice(keys)
            return random_key_from_item_suffixes

        # Picks a random item from the item_suffixes dictionary based on the generated key
        def pick_random_item_from_item_suffixes(d: item_suffixes):
            random_key_from_item_suffixes = pick_random_key_from_item_suffixes(d)
            random_item_from_item_suffixes = random_key_from_item_suffixes, d[random_key_from_item_suffixes]
            return random_item_from_item_suffixes

        # Defines the random item from item_suffixes as a variable, then splits the tuple into name and number
        random_item_from_item_suffixes = pick_random_item_from_item_suffixes(item_suffixes)
        name_from_item_suffixes =  random_item_from_item_suffixes[0]
        number_from_item_suffixes = random_item_from_item_suffixes[1]

        # Materials generation
        # --------------------------------------------------
        # Picks a random key from the item_materials dictionary
        def pick_random_key_from_item_materials(d: item_materials):
           keys = list(d.keys())
           random_key_from_item_materials = random.choice(keys)
           return random_key_from_item_materials

        # Picks a random item from the item_materials dictionary based on the generated key
        def pick_random_item_from_item_materials(d: item_materials):
           random_key_from_item_materials = pick_random_key_from_item_materials(d)
           random_item_from_item_materials = random_key_from_item_materials, d[random_key_from_item_materials]
           return random_item_from_item_materials

        # Defines the random item from item_materials as a variable, then splits the tuple into name and number
        random_item_from_item_materials = pick_random_item_from_item_materials(item_materials)
        name_from_item_materials = random_item_from_item_materials[0]
        number_from_item_materials = random_item_from_item_materials[1]

        # Weapon type generation
        # --------------------------------------------------
        # Picks a random key from the weapon_types dictionary
        def pick_random_key_from_weapon_types(d: weapon_types):
           keys = list(d.keys())
           random_key_from_weapon_types = random.choice(keys)
           return random_key_from_weapon_types

        # Picks a random item from the weapon_types dictionary based on the generated key
        def pick_random_item_from_weapon_types(d: weapon_types):
           random_key_from_weapon_types = pick_random_key_from_weapon_types(d)
           random_item_from_weapon_types = random_key_from_weapon_types, d[random_key_from_weapon_types]
           return random_item_from_weapon_types

        # Defines the random item from weapon_types as a variable, then splits the tuple into name and number
        random_item_from_weapon_types = pick_random_item_from_weapon_types(weapon_types)
        name_from_weapon_types = random_item_from_weapon_types[0]
        number_from_weapon_types = random_item_from_weapon_types[1]

        # Weapon type generation
        # --------------------------------------------------
        # Picks a random key from the weapon_types dictionary
        def pick_random_key_from_weapon_types(d: weapon_types):
           keys = list(d.keys())
           random_key_from_weapon_types = random.choice(keys)
           return random_key_from_weapon_types

        # Picks a random item from the weapon_types dictionary based on the generated key
        def pick_random_item_from_weapon_types(d: weapon_types):
           random_key_from_weapon_types = pick_random_key_from_weapon_types(d)
           random_item_from_weapon_types = random_key_from_weapon_types, d[random_key_from_weapon_types]
           return random_item_from_weapon_types

        # Defines the random item from weapon_types as a variable, then splits the tuple into name and number
        random_item_from_weapon_types = pick_random_item_from_weapon_types(weapon_types)
        name_from_weapon_types = random_item_from_weapon_types[0]
        number_from_weapon_types = random_item_from_weapon_types[1]

        # Armour type generation
        # --------------------------------------------------
        # Picks a random key from the weapon_types dictionary
        def pick_random_key_from_armour_types(d: armour_types):
           keys = list(d.keys())
           random_key_from_armour_types = random.choice(keys)
           return random_key_from_armour_types

        # Picks a random item from the armour_types dictionary based on the generated key
        def pick_random_item_from_armour_types(d: armour_types):
           random_key_from_armour_types = pick_random_key_from_armour_types(d)
           random_item_from_armour_types = random_key_from_armour_types, d[random_key_from_armour_types]
           return random_item_from_armour_types

        # Defines the random item from armour_types as a variable, then splits the tuple into name and number
        random_item_from_armour_types = pick_random_item_from_armour_types(armour_types)
        name_from_armour_types = random_item_from_armour_types[0]
        number_from_armour_types = random_item_from_armour_types[1]

        # Jewellery type generation
        # --------------------------------------------------
        # Picks a random key from the weapon_types dictionary
        def pick_random_key_from_jewellery_types(d: jewellery_types):
            keys = list(d.keys())
            random_key_from_jewellery_types = random.choice(keys)
            return random_key_from_jewellery_types

        # Picks a random item from the jewellery_types dictionary based on the generated key
        def pick_random_item_from_jewellery_types(d: jewellery_types):
            random_key_from_jewellery_types = pick_random_key_from_jewellery_types(d)
            random_item_from_jewellery_types = random_key_from_jewellery_types, d[random_key_from_jewellery_types]
            return random_item_from_jewellery_types

        # Defines the random item from jewellery_types as a variable, then splits the tuple into name and number
        random_item_from_jewellery_types = pick_random_item_from_jewellery_types(jewellery_types)
        name_from_jewellery_types = str(random_item_from_jewellery_types[0])
        number_from_jewellery_types = random_item_from_jewellery_types[1]

        # Item type generation
        # --------------------------------------------------
        # Picks a random key from the weapon_types dictionary
        def pick_random_key_from_item_types(d: item_types):
            keys = list(d.keys())
            random_key_from_item_types = random.choice(keys)
            return random_key_from_item_types

        # Picks a random item from the item_types dictionary based on the generated key
        def pick_random_item_from_item_types(d: item_types):
            random_key_from_item_types = pick_random_key_from_item_types(d)
            random_item_from_item_types = random_key_from_item_types, d[random_key_from_item_types]
            return random_item_from_item_types

        # Defines the random item from item_types as a variable, then splits the tuple into name and number
        random_item_from_item_types = pick_random_item_from_item_types(item_types)
        name_from_item_types = str(random_item_from_item_types[0])
        number_from_item_types = str(random_item_from_item_types[1])

        # Compiles and joins the rolled weapon name
        unjoined_weapon_name = (name_from_item_prefixes, name_from_item_materials, name_from_weapon_types, "of the", name_from_item_suffixes)
        weapon_name = ' '.join(unjoined_weapon_name)
        # Compiles and joins the rolled armour name
        unjoined_armour_name = (name_from_item_prefixes, name_from_item_materials, name_from_armour_types, "of the", name_from_item_suffixes)
        armour_name = ' '.join(unjoined_armour_name)
        # Compiles and joins the rolled jewellery name
        unjoined_jewellery_name = (name_from_item_prefixes, name_from_item_materials, name_from_jewellery_types, "of the", name_from_item_suffixes)
        jewellery_name = ' '.join(unjoined_jewellery_name)
        # Random power value which is added to item power
        random_power = random.randint(1,20)
        # Compiles rolled weapon power
        weapon_power = int(number_from_item_prefixes + number_from_item_materials + number_from_weapon_types + number_from_item_suffixes + random_power)
        # Compiles rolled armour power
        armour_power = int(number_from_item_prefixes + number_from_item_materials + number_from_armour_types + number_from_item_suffixes + random_power)
        # Compiles rolled weapon power
        jewellery_power = int(number_from_item_prefixes + number_from_item_materials + number_from_jewellery_types + number_from_item_suffixes + random_power)
        # Stores whether the item is a weapon, armour or jewellery
        rolled_item_type = name_from_item_types

        # Defines the function which prints the resulting item
        def print_final_item():
            if rolled_item_type == "Weapon":
                print(end='\n')
                print(weapon_name)
                print("Item type:", rolled_item_type)
                print("Power level:", weapon_power)
                print(end='\n')
            elif rolled_item_type == "Armour":
                print(end='\n')
                print(armour_name)
                print("Item type:", rolled_item_type)
                print("Power level:", armour_power)
                print(end='\n')
            elif rolled_item_type == "Jewellery":
                print(end='\n')
                print(jewellery_name)
                print("Item type:", rolled_item_type)
                print("Power level:", jewellery_power)
                print(end='\n')

        # Calls the function which prints the resulting item
        print_final_item()

if __name__ == "__main__":
    main()
