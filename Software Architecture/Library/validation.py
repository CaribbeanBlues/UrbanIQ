def validate_yesno_input():
    """
    Prompts for a binary yes/no input. If not 0 or 1, re-prompt for entry
    Returns:
         1 for yes, 0 for no

    """
    while True:
        try:
            request = int(input())
        except ValueError:
            print("*    Please only enter 1 for Yes or 0 for No.")
            continue
        else:
            while request not in (0, 1):
                print("*    Please only enter 1 for Yes or 0 for No.")
                request = int(input())
        return request


def validate_reconfirmation(entry_name):
    """
    Displays input and confirms entry with user. User presses 1 to confirm, or 0 to renter
    Args:
        entry_name:

    Returns:
        validated user input
    """
    while True:
        print(f"*   What is your {entry_name}:")
        entry = input()
        print(f"*   Is this your {entry_name}: {entry}")
        print("*    Please enter 1 for Yes, 0 for no")
        confirm = validate_yesno_input()
        if confirm == 1:
            return entry

def validate_standard_string():
    entries = input()
    entries = entries.rstrip()
    entries = entries.lstrip()