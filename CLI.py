import time
import random
import json

resources = [
    {
        "Mana": {
            "Amount": 0,
            "Description": "The Life-blood of all magic, stripped from the aether which veils our world and all other planes."
        },
        "Runes": {
            "Amount": 0,
            "Cost": 0,
            "Description" : "Ancient writing that harnesses the mana to take action in the real world.S"
        }
    }
]

Startup_Art = """
.sSSSSs.                                                                                                SSSSS                                        
SSSSSSSSSs. .sSSSSs.    .sSSSsSS SSsSSSSS .sSSSsSS SSsSSSSS .sSSSSs.    .sSSSs.  SSSSS .sSSSSs.         SSSSS       SSSSS .sSSSs.  SSSSS .sSSSSs.    
S SSS SSSSS S SSSSSSSs. S SSS  SSS  SSSSS S SSS  SSS  SSSSS S SSSSSSSs. S SSS SS SSSSS S SSSSSSSs.      S SSS       S SSS S SSS SS SSSSS S SSSSSSSs. 
S  SS SSSS' S  SS SSSSS S  SS   S   SSSSS S  SS   S   SSSSS S  SS SSSSS S  SS  `sSSSSS S  SS SSSSS      S  SS       S  SS S  SS  `sSSSSS S  SS SSSS' 
S..SS       S..SS SSSSS S..SS       SSSSS S..SS       SSSSS S..SSsSSSSS S..SS    SSSSS S..SS SSSSS      S..SS       S..SS S..SS    SSSSS S..SS       
S:::S SSSSS S:::S SSSSS S:::S       SSSSS S:::S       SSSSS S:::S SSSSS S:::S    SSSSS S:::S SSSSS      S:::S       S:::S S:::S    SSSSS S:::SSSS    
S;;;S SSSSS S;;;S SSSSS S;;;S       SSSSS S;;;S       SSSSS S;;;S SSSSS S;;;S    SSSSS S;;;S SSSSS      S;;;S       S;;;S S;;;S    SSSSS S;;;S       
S%%%S SSSSS S%%%S SSSSS S%%%S       SSSSS S%%%S       SSSSS S%%%S SSSSS S%%%S    SSSSS S%%%S SSSS'      S%%%S SSSSS S%%%S S%%%S    SSSSS S%%%S SSSSS 
SSSSSsSSSSS SSSSSsSSSSS SSSSS       SSSSS SSSSS       SSSSS SSSSS SSSSS SSSSS    SSSSS SSSSSsS;:'       SSSSSsSS;:' SSSSS SSSSS    SSSSS SSSSSsSS;:' 
                                                                                                                                                     
SSSSS                                                                                                                                                
SSSSS .sSSSs.  SSSSS .sSSSSs.    .sSSSSSSSs. .sSSSSs.    .sSSSsSS SSsSSSSS .sSSSSs.    .sSSSs.  SSSSS .sSSSSSSSSSSSSSs. .sSSSSs.    SSSSS            
S SSS S SSS SS SSSSS S SSSSSSSs. S SSS SSSSS S SSSSSSSs. S SSS  SSS  SSSSS S SSSSSSSs. S SSS SS SSSSS SSSSS S SSS SSSSS S SSSSSSSs. S SSS            
S  SS S  SS  `sSSSSS S  SS SSSS' S  SS SSSS' S  SS SSSS' S  SS   S   SSSSS S  SS SSSS' S  SS  `sSSSSS SSSSS S  SS SSSSS S  SS SSSSS S  SS            
S..SS S..SS    SSSSS S..SS       S..SSsSSSa. S..SS       S..SS       SSSSS S..SS       S..SS    SSSSS `:S:' S..SS `:S:' S..SSsSSSSS S..SS            
S:::S S:::S    SSSSS S:::S SSSSS S:::S SSSSS S:::SSSS    S:::S       SSSSS S:::SSSS    S:::S    SSSSS       S:::S       S:::S SSSSS S:::S            
S;;;S S;;;S    SSSSS S;;;S SSSSS S;;;S SSSSS S;;;S       S;;;S       SSSSS S;;;S       S;;;S    SSSSS       S;;;S       S;;;S SSSSS S;;;S            
S%%%S S%%%S    SSSSS S%%%S SSSSS S%%%S SSSSS S%%%S SSSSS S%%%S       SSSSS S%%%S SSSSS S%%%S    SSSSS       S%%%S       S%%%S SSSSS S%%%S SSSSS      
SSSSS SSSSS    SSSSS SSSSSsSSSSS SSSSS SSSSS SSSSSsSS;:' SSSSS       SSSSS SSSSSsSS;:' SSSSS    SSSSS       SSSSS       SSSSS SSSSS SSSSSsSS;:' 
"""

# Starting Values
duration = 1
gain = 1

def Storage():
    print("--------Storage--------")
    for resource_dict in resources:
        for resource_name, resource_data in resource_dict.items():
            print(f"{resource_name}:")
            print(f"  Amount: {resource_data['Amount']}")
            print(f"  Cost: {resource_data['Cost']}")
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

def condense_mana():
    print(f"Condensing Mana for {duration} seconds to gain {gain} Mana...")
    loading_bar(duration)

    for resource_dict in resources:
        if "Mana" in resource_dict:
            resource_dict["Mana"]["Amount"] += gain
            break

    print(f"Mana Condensation Complete! Gained {gain} Mana.")

def help_command():
    print("Available commands:")
    print("  storage - Display all resources.")
    print("  check <resource_name> - Check amount of a specific resource (e.g., check mana)")
    print("  condense - Begin condensing mana.")
    print("  help - Display this help message.")
    print("  exit - Quit the program.")

def main():

    print(Startup_Art)
    print("Welcome to the game... Command Line Incremental!")
    print("Type 'help' to see available commands.")
    print()

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
                print("Usage: check <resource_name>")
        elif command_parts[0] == "condense":
            if len(command_parts) == 1:
                condense_mana()
            else:
                print("Usage: condense")
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