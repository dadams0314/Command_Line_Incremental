import time
import random
import json
import os

# Startup Art
Startup_Art =  """
▄████████  ▄██████▄    ▄▄▄▄███▄▄▄▄     ▄▄▄▄███▄▄▄▄      ▄████████ ███▄▄▄▄   ████████▄        ▄█        ▄█  ███▄▄▄▄      ▄████████ 
███    ███ ███    ███ ▄██▀▀▀███▀▀▀██▄ ▄██▀▀▀███▀▀▀██▄   ███    ███ ███▀▀▀██▄ ███   ▀███      ███       ███  ███▀▀▀██▄   ███    ███ 
███    █▀  ███    ███ ███   ███   ███ ███   ███   ███   ███    ███ ███   ███ ███    ███      ███       ███▌ ███   ███   ███    █▀  
███        ███    ███ ███   ███   ███ ███   ███   ███   ███    ███ ███   ███ ███    ███      ███       ███▌ ███   ███  ▄███▄▄▄     
███        ███    ███ ███   ███   ███ ███   ███   ███ ▀███████████ ███   ███ ███    ███      ███       ███▌ ███   ███ ▀▀███▀▀▀     
███    █▄  ███    ███ ███   ███   ███ ███   ███   ███   ███    ███ ███   ███ ███    ███      ███       ███  ███   ███   ███    █▄  
███    ███ ███    ███ ███   ███   ███ ███   ███   ███   ███    ███ ███   ███ ███   ▄███      ███▌    ▄ ███  ███   ███   ███    ███ 
████████▀   ▀██████▀   ▀█   ███   █▀   ▀█   ███   █▀    ███    █▀   ▀█   █▀  ████████▀       █████▄▄██ █▀    ▀█   █▀    ██████████ 
                                                                                             ▀                                     
 ▄█  ███▄▄▄▄    ▄████████    ▄████████    ▄████████   ▄▄▄▄███▄▄▄▄      ▄████████ ███▄▄▄▄       ███        ▄████████  ▄█            
███  ███▀▀▀██▄ ███    ███   ███    ███   ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███ ███▀▀▀██▄ ▀█████████▄   ███    ███ ███            
███▌ ███   ███ ███    █▀    ███    ███   ███    █▀  ███   ███   ███   ███    █▀  ███   ███    ▀███▀▀██   ███    ███ ███            
███▌ ███   ███ ███         ▄███▄▄▄▄██▀  ▄███▄▄▄     ███   ███   ███  ▄███▄▄▄     ███   ███     ███   ▀   ███    ███ ███            
███▌ ███   ███ ███        ▀▀███▀▀▀▀▀   ▀▀███▀▀▀     ███   ███   ███ ▀▀███▀▀▀     ███   ███     ███     ▀███████████ ███            
███  ███   ███ ███    █▄  ▀███████████   ███    █▄  ███   ███   ███   ███    █▄  ███   ███     ███       ███    ███ ███            
███  ███   ███ ███    ███   ███    ███   ███    ███ ███   ███   ███   ███    ███ ███   ███     ███       ███    ███ ███▌    ▄      
█▀    ▀█   █▀  ████████▀    ███    ███   ██████████  ▀█   ███   █▀    ██████████  ▀█   █▀     ▄████▀     ███    █▀  █████▄▄██      
                            ███    ███                                                                              ▀            
"""
# Mana Resources
default_resources = [
    {
        "Mana": {
            "Amount": 0,
            "Description": "The Life-blood of all magic, stripped from the aether which veils our world and all other planes.",
            "Discovered": 1,
            "Purchasable": False,
        },
        "Runes": {
            "Amount": 0,
            "Cost": 10,
            "Description" : "Ancient writing that harnesses the mana to take action in the real world.S",
            "Delta": 1.1,
            "Purchasable": True,
            "Discovered": 0,
        },
        "Mirror Images": {
            "Amount": 0,
            "Cost": 100,
            "Description": "Command your reflection to generate more " ,
            "Delta": 1.25,
            "Purchasable": True,
            "Discovered": 0,
        },
        "Simulacrum": {
            "Amount": 0,
            "Cost": 10000,
            "Description": "Use pure mana to form a facimile, a second body for yourself.",
            "Delta": 1.5,
            "Purchasable": True,
            "Discovered": 0,
        },
    }
]

resources = list(default_resources)

# Starting Values
duration = 1
gain = 1
max_mana = 1_000_000_000

# Functions

def Storage():
    print("--------Storage--------")
    for resource_dict in resources:
        for resource_name, resource_data in resource_dict.items():
            if resource_data["Discovered"] == 1:
                pass
            else:
                continue
            print(f"{resource_name}:")
            print(f"  Amount: {resource_data['Amount']}")
            if "Cost" in resource_data:
                print(f"  Cost: {resource_data['Cost']} mana")
            print(f"  Description: {resource_data['Description']}")
            print()
    print("------------------------")


def check_resource(resource_name_input):
    for resource_dict in resources:
        for resource_name, resource_data in resource_dict.items():
            if resource_name.lower() == resource_name_input.lower():
                print(f"{resource_name}:")
                print(f"  Amount: {resource_data['Amount']}")
                print(f"  Description: {resource_data['Description']}")
                return
    print(f"Resource '{resource_name_input}' not found.")

def loading_bar(duration):
    progress_bar_length = 100
    for i in range(progress_bar_length + 1):
        percent_complete = (i / progress_bar_length) * 100
        bar = "[" + "=" * i + ">" + "." * (progress_bar_length - i) + "]"
        print(f"\rCondensing Mana: {bar} {percent_complete:.0f}%", end="")
        time.sleep(duration / progress_bar_length)
    print()

def purchase_resource(resource_name_input):
    purchased = False
    for resource_dict in resources:
        for resource_name, resource_data in resource_dict.items():
            if resource_name.lower() == resource_name_input.lower():
                if resource_data["Purchasable"]:
                    if resource_data["Cost"] <= resources[0]["Mana"]["Amount"]:
                        resources[0]["Mana"]["Amount"] -= resource_data["Cost"]
                        resource_data["Amount"] += 1
                        resource_data["Cost"] = round(resource_data["Cost"] * resource_data["Delta"])
                        print(f"{resource_name} purchased!")
                        purchased = True
                        break
                    else:
                        print("Not enough Mana to purchase this resource.")
                        purchased = True
                        break
                else:
                    print(f"{resource_name} is not purchasable. Perhaps there's another way I could find it...")
                    purchased = True
                    break
        if purchased:
            break
    if purchased:
        save_game()
    elif not purchased and not any(resource_name.lower() == resource_name_input.lower() for resource_dict in resources for resource_name in resource_dict):
        print(f"'{resource_name_input}'? I'm uncertain of what this may be.")

def condense_mana():
    global duration, gain

    condense_duration = 0
    condense_gain = 0

    condense_duration = duration * (1 + resources[0]['Runes']['Amount']) / (1 + resources[0]['Simulacrum']['Amount'])
    condense_gain = (gain + ((1 * resources[0]['Runes']['Amount'])) * (1 + (1.5 * resources[0]['Mirror Images']['Amount'])))
    print(f"Condensing Mana for {condense_duration} seconds to gain {condense_gain} Mana...")
    loading_bar(condense_duration)

    for resource_dict in resources:
        if "Mana" in resource_dict:
            resource_dict["Mana"]["Amount"] += condense_gain
            if resource_dict["Mana"]["Amount"] > max_mana:
                resource_dict["Mana"]["Amount"] = max_mana
    save_game()
    print(f"Mana Condensation Complete! Gained {int(condense_gain)} Mana.  You now have {int(resource_dict['Mana']['Amount'])} Mana")
    check_discovered_status()

def check_discovered_status():
    if resources[0]["Mana"]["Amount"] >= resources[0]["Runes"]["Cost"]:
        resources[0]["Runes"]["Discovered"] = True
        print("New resource discovered!  Runes!")
    if resources[0]["Mana"]["Amount"] >= resources[0]["Mirror Images"]["Cost"]:
        resources[0]["Mirror Images"]["Discovered"] = True
        print("New resource discovered!  Mirror Images!")
    if resources[0]["Mana"]["Amount"] >= resources[0]["Simulacrum"]["Cost"]:
        resources[0]["Simulacrum"]["Discovered"] = True
        print("New resource discovered!  Simulacrum!")
    save_game()
    return



def save_game():
    with open("save.json", "w") as save_file:
        json.dump(resources, save_file)

def load_game():
    if os.path.exists("save.json"):
        with open("save.json", "r") as save_file:
            global resources
            resources = json.load(save_file)
            print("Game Loaded")
    else:
        print("No save file found. Starting new game.")

def reset_game():
    global resources
    resources[:] = list(default_resources)
    save_game()

def help_command():
    print("Available commands:")
    print("  storage - Display all resources.")
    print("  check <resource_name> - Check amount of a specific resource (e.g., check mana)")
    print("  purchase <resource_name> - Purchase a resource.")
    print("  condense - Begin condensing mana.")
    print("  help - Display this help message.")
    print("  exit - Quit the program.")

def main():

    # Startup Splash
    print(Startup_Art)
    print("Welcome to the game... Command Line Incremental!")
    print("Type 'help' to see available commands.")
    print()

    load_game()

    # Main Gameplay
    while True:
        command = input("Enter Command: ")
        command_parts = command.split()

        if command_parts[0] == "storage":
            Storage()
        elif command_parts[0] == "check":
            if len(command_parts) > 1:
                resource_name_to_check = command_parts[1]
                check_resource(resource_name_to_check)
            else:
                print("Available resources: ")
                for resource_dict in resources:
                    for resource_name, resource_data in resource_dict.items():
                        if resource_data["Discovered"] == 1:
                            pass
                        else:
                            continue
                        print(f"{resource_name}")
        elif command_parts[0] == "condense":
            if len(command_parts) == 1:
                condense_mana()
            else:
                print("Usage: condense")
        elif command_parts[0] == "reset":
            print("Are you absolutely sure you want to reset?  This will return the game to the very beginning. (Yes / anything else... please...)")
            confirmation = input().lower()
            if confirmation == "yes":
                reset_game()
                print("Game has been reset.")
            else:
                print("Game has not been reset.")
        elif command_parts[0] == "purchase":
            if len(command_parts) > 1:
                resource_name_to_purchase = command_parts[1]
                purchase_resource(resource_name_to_purchase)
            else:
                print("What are you trying to purchase?")
                response = input()
                purchase_resource(response)
        elif command_parts[0] == "help":
            help_command()
        elif command_parts[0] == "exit":
            print("Exiting...")
            break
        else:
            print("Invalid Command. Type 'help' for available commands.")
        print()


if __name__ == "__main__":
    main()