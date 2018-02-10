#!/usr/bin/python3
# Lab assignment 2: part 2


# User data from the lab
data = [
    {"name": "Rashmi", "number": "8797989821", "email": "rr@gmail.com"},
    {"name": "Saria", "number": "9897989821", "email": "ss@gmail.com"}
]


def greeting():
    """
    Greeting function.
    """
    print("============================================")
    print("Select a-d to perform an operation:")
    print("a) Display contact by name")
    print("b) Display contact by number")
    print("c) Edit contact by name")
    print("d) Exit")
    print("============================================")


def find_contact_by_name(contact_list, name):
    """
    Find the contact record from dictionary by name.
    """
    # Loop through dictionary
    for row in contact_list:
        # Return record if match found with key "name"
        if name == row["name"]:
            return row
    # Record not found
    return None


def find_contact_by_number(contact_list, number):
    """
    Find the contact record from dictionary by number
    """
    # Loop through dictionary
    for row in contact_list:
        # Return record if match found with key "number"
        if number == row["number"]:
            return row
    # Record not found
    return None


def edit_contact_by_name(contact_list, name, field, new_data):
    """
    Edit the contact record from dictionary by name and field
    """
    # Loop through dictionary
    for row in contact_list:
        # Modify record if match found with key "name"
        if name == row["name"]:
            # Check if field exist in the keys
            if field in row.keys():
                # Modify data and return if match found
                row[field] = new_data
                return row
            else:
                # Field not found
                return None
    # Record not found
    return None

# Infinite loop
while True:
    # Print greeting
    greeting()
    # Get user's choice from options display in greeting
    choice = input("Enter your choice: ").lower()
    # User's choice validation
    if choice not in "abcd":
        print("Invalid choice. Please try again.")
        continue
    # User picks "Display contact by name"
    if choice == "a":
        input_name = input("Enter name for search: ")
        output_data = find_contact_by_name(data, input_name)
        if output_data:
            print(output_data)
        else:
            print("User not found. Please try again.")
    # User picks "Display contact by number"
    elif choice == "b":
        input_number = input("Enter number for search: ")
        output_data = find_contact_by_number(data, input_number)
        if output_data:
            print(output_data)
        else:
            print("User not found. Please try again.")
    # User picks "Edit contact by name"
    elif choice == "c":
        input_name = input("Enter name for search: ")
        input_field = input("Enter the edit field: ")
        input_data = input("Enter the new data: ")
        output_data = edit_contact_by_name(data, input_name, input_field, input_data)
        if output_data:
            print("Edit completed")
            print(output_data)
        else:
            print("Edit failed")
    # User picks "Exit"
    elif choice == "d":
        print("Thanks for using the app. Bye...")
        break
# Print the final data
print(data)
