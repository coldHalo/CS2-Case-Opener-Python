from random import randint, choices, random
import pygame
import sys

# Initialize Pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Counter-Strike Case Opening Simulator V0.1 TEST")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
inventory_font = pygame.font.SysFont(None, 24)


# Inventory to hold opened items

inventory = []

# Rarity distribution for items in Case 1

rarity1 = {
    "Common" : 0.79, # Blue
    "Uncommon" : 0.15, # Purple
    "Rare" : 0.04, # Pink
    "Mythical" : 0.009, # Red
    "Legendary" : 0.001 # Gold
}

rarity2 = {
    "Common" : 0.70, # Blue
    "Uncommon" : 0.22, # Purple
    "Rare" : 0.06, # Pink
    "Mythical" : 0.014, # Red
    "Legendary" : 0.001 # Gold
}

# Colors for each rarity (for UI)

rarity_colors = {
    "Common": (0, 112, 221),
    "Uncommon": (163, 53, 238),
    "Rare": (255, 105, 180),
    "Mythical": (255, 69, 58),
    "Legendary": (255, 215, 0),
}


# All case common items, uncommon items, rare items, mythical items, and legendary items with their weights for Case 1

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

# All case common items, uncommon items, rare items, mythical items, and legendary items with their weights for Case 2

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

wear = {
    "Factory New" : 0.10,
    "Minimal Wear" : 0.22,
    "Field-Tested": 0.30,
    "Well-Worn": 0.25,
    "Battle-Scarred": 0.13
}

# Function to open a case and return the item obtained
# There are 2 cases currently implemented, each with its own set of items
# Case 2 is currently better than the Case 1, but this will be compensated by adding a higher price for the keys

def open_case_1():
    rarity_choice = choices(list(rarity1.keys()), weights=list(rarity1.values()))[0]
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
    # StatTrak™ items track the number of kills made with that weapon, increasing the value of the item

    if random() < 0.1:
        item = "StatTrak™ " + item

    return f"{item} ({rarity_choice})"

def open_case_2():
    rarity_choice = choices(list(rarity2.keys()), weights=list(rarity2.values()))[0]
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
# It simulates opening 100 cases of Case 1 and 2 and prints the results, displaying the item and its wear condition

"""

THIS LINE IS DESIGNED FOR DEBUGGING AND/OR TESTING PURPOSES ONLY
REMOVE OR COMMENT OUT WHEN NOT NEEDED

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

"""

# Pygame UI Loop - NOT TO BE CHANGED

current_screen = "main_menu"

state = True
while state == True:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:

            state = False
        if current_screen == "main_menu":

            casebutton_color = (70, 130, 180)
            casebutton_hover = (100, 160, 210)
            casebutton_rect = pygame.Rect(300, 400, 200, 60)

            inventorybutton_color = (70, 130, 180)
            inventorybutton_hover = (100, 160, 210)
            inventorybutton_rect = pygame.Rect(650, 20, 130, 40)

            screen.fill((30, 30, 30))
            title = font.render("Counter-Strike Case Opening Simulator V0.1 TEST", True, (255, 255, 255))
            subtitle = font.render("Made by coldHalo", True, (255, 255, 255))
            screen.blit(subtitle, (275, 100))
            screen.blit(title, (100, 50))

            mouse_pos = pygame.mouse.get_pos()
            color = casebutton_hover if casebutton_rect.collidepoint(mouse_pos) else casebutton_color
            pygame.draw.rect(screen, color, casebutton_rect, border_radius=10)

            casebutton_text = font.render("Open Case", True, (255, 255, 255))
            screen.blit(casebutton_text, (casebutton_rect.x + 35, casebutton_rect.y + 17))

            if event.type == pygame.MOUSEBUTTONDOWN:

                if inventorybutton_rect.collidepoint(event.pos):
                    current_screen = "inventory"

                if casebutton_rect.collidepoint(event.pos):

                    caseresult = open_case_1() + " | Wear: " + choices(list(wear.keys()), weights=list(wear.values()))[0]
                    inventory.append(caseresult)
                    print("You have obtained: " + caseresult)

        if current_screen == "inventory":

            screen.fill((30, 30, 30))
            title = font.render("Inventory", True, (255, 255, 255))
            screen.blit(title, (350, 20))

            for idx, item in enumerate(inventory):
                item_text = inventory_font.render(f"{idx + 1}. {item}", True, (255, 255, 255))
                screen.blit(item_text, (50, 70 + idx * 30))

        pygame.display.flip()
        clock.tick(60)

pygame.quit()