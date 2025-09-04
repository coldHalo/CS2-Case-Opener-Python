from random import randint, choices, random

# Rarity distribution for items in the case
# The sum of these values should equal 1

rarity = {
    "Common" : 0.79, # Blue
    "Uncommon" : 0.15, # Purple
    "Rare" : 0.04, # Pink
    "Mythical" : 0.009, # Red
    "Legendary" : 0.001 # Gold
}

# All case common items, uncommon items, rare items, mythical items, and legendary items with their weights
# Weights are arbitrary and can be adjusted to change the likelihood of getting a specific item within its rarity category
# The sum of weights in each category does not need to equal 1, as they are relative weights

common1 = {
    "USP-S / Desert Mant" : 0.26,
    "P250 /  ForBorealest" : 0.26,
    "Negev / Jancle Urban" : 0.26,
    "Tec-9 / Groundwater" : 0.26,
    "Dual Berettas / Colony" : 0.26,
    "Glock-18 / Groundwater" : 0.26,
    "Five-SeveN / Forest Night" : 0.26,
    "MP9 / Sand Dashed" : 0.26,
    "PP-Bizon / Graphical Sunset" : 0.26,
}

uncommon1 = {
    "P90 / Ash Wood" : 0.20,
    "MAC-10 / Palm" : 0.20,
    "UMP-45 / Bone Pile" : 0.20,
    "FAMAS / Prototype 5" : 0.20,
    "SG 553 / Tornado" : 0.20,
}

rare1 = {
    "AWP / Worm God" : 0.25,
    "M4A1-S / Kracken" : 0.25,
    "AK-47 / Elite Build" : 0.25,
    "Desert Eagle / Bronze Deco" : 0.25,
}

mythical1 = {
    "M4A4 / The Emperor" : 0.33,
    "AWP / Dark Matter Reimagined" : 0.33,
    "AK-47 / Neon Rider" : 0.33,
}

legendary1 = {
    "★ Karambit / Case Hardened" : 1.0,
    "★ M9 Bayonet / Doppler" : 1.0,
    "★ Butterfly Knife / Fade" : 1.0,
    "★ Bayonet / Marble Fade" : 1.0,
    "★ Flip Knife / Tiger Tooth" : 1.0,
    "★ Gut Knife / Slaughter" : 1.0,
    "★ Huntsman Knife / Crimson Web" : 1.0,
    "★ Shadow Daggers / Doppler" : 1.0,
    "★ Talon Knife / Fade" : 1.0,
    "★ Bowie Knife / Marble Fade" : 1.0,
    "★ Navaja Knife / Tiger Tooth" : 1.0,
    "★ Stiletto Knife / Slaughter" : 1.0,
}

common2 = {
    "CZ75-Auto / Tigris" : 0.16,
    "R8 Revolver / Amber Fade" : 0.16,
    "MP7 / Cirrus" : 0.26,
    "P2000 / Oceanic" : 0.1,
    "Sawed-Off / Forest DDPAT" : 0.2,
    "MAG-7 / Memento" : 0.2,
    "SSG 08 / Blue Spruce" : 0.26,
    "MP5-SD / Lab Rats" : 0.26,
}

uncommon2 = {
    "AUG / Storm" : 0.20,
    "SG 553 / Cyrex" : 0.30,
    "FAMAS / Styx" : 0.25,
    "UMP-45 / Primal Saber" : 0.25,
}

rare2 = {
    "Desert Eagle / Code Red" : 0.33,
    "AK-47 / Neon Revolution" : 0.33,
    "M4A1-S / Hot Rod" : 0.33,
}

mythical2 = {
    "AWP / Medusa" : 0.33,
    "AK-47 / Fire Serpent" : 0.33,
    "M4A4 / Howl" : 0.33,
}

legendary2 = {
    "★ Karambit / Doppler" : 1.0,
    "★ M9 Bayonet / Marble Fade" : 1.0,
    "★ Butterfly Knife / Tiger Tooth" : 1.0,
    "★ Bayonet / Fade" : 1.0,
    "★ Flip Knife / Slaughter" : 1.0,
    "★ Gut Knife / Crimson Web" : 1.0,
    "★ Huntsman Knife / Tiger Tooth" : 1.0,
    "★ Shadow Daggers / Fade" : 1.0,
    "★ Talon Knife / Slaughter" : 1.0,
    "★ Bowie Knife / Doppler" : 1.0,
    "★ Navaja Knife / Marble Fade" : 1.0,
    "★ Stiletto Knife / Crimson Web" : 1.0,
    "★ Ursus Knife / Tiger Tooth" : 1.0,
    "★ Skeleton Knife / Fade" : 1.0,
    "★ Paracord Knife / Slaughter" : 1.0,
    "★ Survival Knife / Crimson Web" : 1.0,
    "★ Nomad Knife / Doppler" : 1.0,
    "★ Classic Knife / Marble Fade" : 1.0,
    "★ CQC Knife / Tiger Tooth" : 1.0,
    "★ Push Dagger / Slaughter" : 1.0,
}

# Wear distribution for items
# The sum of these values should equal 1

wear = {
    "Factory New" : 0.10,
    "Minimal Wear" : 0.22,
    "Field-Tested": 0.30,
    "Well-Worn": 0.25,
    "Battle-Scarred": 0.13
}

# Function to open a case and return the item obtained
# There are 2 cases currently implemented, each with its own set of items

def open_case_1():
    rarity_choice = choices(list(rarity.keys()), weights=list(rarity.values()))[0]
    if rarity_choice == "Common":
        item = choices(list(common1.keys()), weights=list(common1.values()))[0]
    elif rarity_choice == "Uncommon":
        item = choices(list(uncommon1.keys()), weights=list(uncommon1.values()))[0]
    elif rarity_choice == "Rare":
        item = choices(list(rare1.keys()), weights=list(rare1.values()))[0]
    elif rarity_choice == "Mythical":
        item = choices(list(mythical1.keys()), weights=list(mythical1.values()))[0]
    else:
        item = choices(list(legendary1.keys()), weights=list(legendary1.values()))[0]

    # 10% chance for the item to be a StatTrak™ version
    # StatTrak™ items track the number of kills made with that weapon

    if random() < 0.1:
        item = "StatTrak™ " + item

    return f"{item} ({rarity_choice})"

def open_case_2():
    rarity_choice = choices(list(rarity.keys()), weights=list(rarity.values()))[0]
    if rarity_choice == "Common":
        item = choices(list(common2.keys()), weights=list(common2.values()))[0]
    elif rarity_choice == "Uncommon":
        item = choices(list(uncommon2.keys()), weights=list(uncommon2.values()))[0]
    elif rarity_choice == "Rare":
        item = choices(list(rare2.keys()), weights=list(rare2.values()))[0]
    elif rarity_choice == "Mythical":
        item = choices(list(mythical2.keys()), weights=list(mythical2.values()))[0]
    else:
        item = choices(list(legendary2.keys()), weights=list(legendary2.values()))[0]
    
    if random() < 0.1:
        item = "StatTrak™ " + item
    
    return f"{item} ({rarity_choice})"

# This feature is only for debugging purposes and is not part of the actual game
# It simulates opening 100 cases of case 1 and 2 and prints the results, displaying the item and its wear condition

print("Case 1 Results:")
print("")

for i in range(100):
    print(open_case_1() + " | Wear: " + choices(list(wear.keys()), weights=list(wear.values()))[0])

print("")
print("---")
print("")
print("Case 2 Results:")
print("")

for i in range(100):
    print(open_case_2() + " | Wear: " + choices(list(wear.keys()), weights=list(wear.values()))[0])