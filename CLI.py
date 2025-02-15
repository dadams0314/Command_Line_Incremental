import time
import random
import json

resources = [
    {
        "Mana": {
            "Amount": 100,
            "Cost": 0,
            "Description": "The Life-blood of all magic, stripped from the aether which veils our world and all other planes."
        },
        "Runes": {
            "Amount": 100,
            "Cost": 0,
            "Description" : "Ancient writing that harnesses the mana to take action in the real world.S"
        }
    }
]

def Storage():
    for resource_dict in resources:
        for resource_name, resource_data in resource_dict.items():
            print(f"{resource_name}:")
            print(f"  Amount: {resource_data['Amount']}")
            print(f"  Cost: {resource_data['Cost']}")
            print(f"  Description: {resource_data['Description']}")
            print()

def check_resource(resource_name_input):
    for resource_dict in resources:
        for resource_name, resource_data in resource_dict.items():
            if resource_name.lower() == resource_name_input.lower():
                print(f"{resource_name}:")
                print(f"  Amount: {resource_data['Amount']}")
                print(f"  Description: {resource_data['Description']}")
                return  # Exit function after finding resource
    print(f"Resource '{resource_name_input}' not found.")

def loading_bar(duration):
    progress_bar_length = 20
    for i in range(progress_bar_length + 1):
        percent_complete = (i / progress_bar_length) * 100
        bar = "[" + "=" * i + ">" + "." * (progress_bar_length - i) + "]"
        print(f"\rCondensing Mana: {bar} {percent_complete:.0f}%", end="")
        time.sleep(duration / progress_bar_length)
    print()

def condense_mana(): # Removed seconds and amount parameters
    condensation_duration = 5  # Fixed duration in seconds - can be changed later
    mana_gain_amount = 10      # Fixed mana gain amount - can be changed later

    print(f"Condensing Mana for {condensation_duration} seconds to gain {mana_gain_amount} Mana...") # Updated message
    loading_bar(condensation_duration)

    # Find Mana resource and add amount
    for resource_dict in resources:
        if "Mana" in resource_dict:
            resource_dict["Mana"]["Amount"] += mana_gain_amount
            break

    print(f"Mana Condensation Complete! Gained {mana_gain_amount} Mana.") # Updated message

def help_command():
    print("Available commands:")
    print("  storage - Display all resources.")
    print("  check <resource_name> - Check amount of a specific resource (e.g., check mana)")
    print("  condense_mana - Begin condensing mana.")
    print("  help - Display this help message.")
    print("  exit - Quit the program.")

def main():
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
        elif command_parts[0] == "condense_mana":
            if len(command_parts) == 1: # Check for just "condense_mana"
                condense_mana() # Call condense_mana without arguments
            else:
                print("Usage: condense_mana") # Updated Usage message
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