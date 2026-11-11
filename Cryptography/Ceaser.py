## Evan Anderson
## Intro to CyberSecurity
## Tanjila Manwala

## This program takes user input to determine 
## if the user would like to encrypt or decrypt
## their inputed text. They must decide on a key
## to encrypt and use the same key to decrypt.

import sys #to quit the program with sys.exit()

_line = "+-" * 30


def valid_menu_selection(selection):
    ## verifies menu input is valid
    if selection == "1":
        print("You selected Encryption")
        print(_line)
        return True
    elif selection == "2":
        print("You selected Decryption")
        print(_line)
        return True
    elif selection == "3":
        print ("Quitting Program")
        sys.exit()
    else:
        return False

def check_valid_txt(text):
    return bool(text) and all("A" <= character <= "Z" or character == " " for character in text)

def menu():
    ## prints the menu to choose which function will run
    print("1: Encrypt a message using Ceaser Cipher")
    print("2: Decrypt a message using Ceaser Cipher")
    print("3: Quit")
    print(_line)
    return input("Enter your choice: ")

def _encrypt():
    while True:
        print("Enter the text using A-Z that you wish to encrypt.")
        text = input().upper()
        valid = check_valid_txt(text)
        if valid:
            break
    while True:
        print("Enter Secret Key (a number)")
        key = input()
        if key.isdigit() and key.isascii():
            shift = int(key)
            break
        else:
            print("Invalid key.")

    encrypted_text = ceaser_cipher(text, shift)
    print("Encrypted message:", encrypted_text)

def _decrypt():
    while True:
        print("Enter the text using A-Z that you wish to decrypt.")
        text = input().upper()
        valid = check_valid_txt(text)
        if valid:
            break
    while True:
        print("Enter Secret Key (a number)")
        key = input()
        if key.isdigit()and key.isascii():
            shift = int(key)
            break
        else:
            print("Invalid key.")

    encrypted_text = ceaser_cipher(text, -(shift))
    print("Decrypted message:", encrypted_text)
            
def ceaser_cipher(text, shift):
    result = ""

    for character in text:
        if character == " ":
            result += " "
        else:
            position = ord(character) - 65
            shifted_character = (position + shift) % 26
            result += chr(shifted_character +65)

    return result

def main():
    print("Welcome to the Ceaser Encryption/Decryption Program\n")

    selection = menu()
    
    while not valid_menu_selection(selection):
        print("That is not a valid input. Please enter 1, 2, or 3")
        selection = menu()

    if selection == "1":
        _encrypt()
    elif selection == "2":
        _decrypt()

    return 0
    
    


if __name__ == '__main__':
    main()