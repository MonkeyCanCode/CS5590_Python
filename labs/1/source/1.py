#!/usr/bin/python3
# Lab assignment 1: part 1


def valid_width(password):
    """
    Check if password contains number
    """
    return True if 6 <= len(password) <= 16 else False


def contain_number(password):
    """
    Check if password contains number
    """
    return any(char.isdigit() for char in password)


def contain_special_char(password):
    """
    Check if password contains special character
    """
    special_chars = "$@!*"
    return any((char in special_chars) for char in password)


def contains_both_cases(password):
    """
    check if password contains both upper and lower case characters
    """
    return any(char.isupper() for char in password) and any(char.islower() for char in password)


def password_validator(password):
    """
    Check if password is valid
    """
    return True if (valid_width(password) and
                    contain_number(password) and
                    contain_special_char(password) and
                    contains_both_cases(password)) else False


# Get user's password
input_password = input("Enter your password: ")
# Perform password validation
print("Valid password" if password_validator(input_password) else "Invalid password")

