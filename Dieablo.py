"""
Dieablo - a dice rolling action role playing game
Obtain lucky loot so that you can get luckier and obtain luckier loot.
Thinking outside the Skinner's Box.
Notes:
1) Suceeded at pulling paired keys and items from dictionary.
2) Next task is to generate items based on a dice roll and pulling the right data pairs from each dictionary.
"""

import random

# Program version and tagline
VERSION = "Pre-alpha 0.1"
TAGLINE = "Stay a while, and roll..."

def main():

 # Dictionary which records equipped items
    equipped_items = {
    "weapon_name": "0",
    "weapon_mod": 0,
    "armour_name": "0",
    "armour_mod": 0,
    "jewellery_name": "0",
    "jewellery_mod": 0
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

 # Dictionary which contains material types and their associated dice modifiers 
    materials = {
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
    weapon_types = {
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
    weapon_types = {
    "Trinket": -10,
    "Charm": -5,
    "Bangle": 1,
    "Bracelet": 2,
    "Earring" : 3,
    "Ring" : 4,
    "Amulet": 5,
    "Crown": 10
    }

    # Prints a welcome message
    print(end='\n')
    print("Dieablo", VERSION, ":", TAGLINE)
    print("---------------------------------------------------")
    print(end='\n')

    # Input prompt which commences and/or restarts the code
    while input("Roll the dice? Press enter.") == "":
        
        # Picks a random key from the item_prefix dictionary
        def pick_random_key_from_item_prefixes(d: item_prefixes):
            keys = list(d.keys())
            random_key_from_item_prefixes = random.choice(keys)
            return random_key_from_item_prefixes

        # Picks a random value from the item_prefix dictionary (not currently used)
        def pick_random_value_from_item_prefixes(d: item_prefixes):
            _, random_value_from_item_prefixes = pick_random_item_from_item_prefixes(d)
            return random_value_from_item_prefixes
        
        # Picks a random item from the item_prefix dictionary based on the generated key
        def pick_random_item_from_item_prefixes(d: item_prefixes):
            random_key_from_item_prefixes = pick_random_key_from_item_prefixes(d)
            random_item_from_item_prefixes = random_key_from_item_prefixes, d[random_key_from_item_prefixes]
            return random_item_from_item_prefixes

        # Defines the random item from item_prefix as a variable and prints it (test)
        random_item_from_item_prefixes = pick_random_item_from_item_prefixes(item_prefixes)
        print(random_item_from_item_prefixes)
        print(end='\n')

if __name__ == "__main__":
    main()
