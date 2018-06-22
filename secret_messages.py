import helpers

from atbash import Atbash
from ciphers import Cipher
from keywordd import Keywordd
from polybius import Polybius

ciphers = ["Atbash", "Caesar", "Polybius", "Keyword"]


def select_cipher():
    helpers.clear_screen()
    print("Please pick one of the following ciphers:")
    print()
    for cipher in ciphers:
        print("- {}".format(cipher))
    print()
    
    while True:
        try:
            cipher = input("Which cipher would you like to use? ")
            if cipher.upper() == "ATBASH":
                cipher = Atbash()
            elif cipher.upper() == "CAESAR":
                cipher = Caesar()
            elif cipher.upper() == "POLYBIUS":
                cipher = Polybius()
            elif cipher.upper() == "KEYWORD":
                cipher = Keywordd()
            else:
                raise ValueError("That cipher doesn't exist or has not yet been implemented.")
        except ValueError as error:
            print(error)
            print()
        else:
            break
    return cipher
            
def select_encrypt_or_decrypt():
    while True:
            helpers.clear_screen()
            try:
                action = input("Whould you like to encrypt and decrypt? ")
                if action != "decrypt" and action != "encrypt":
                    raise ValueError("You must pick between encrypt and decrypt")
            except ValueError as error:
                print(error)
            else:
                break
    return action


def print_message(cipher, action):
    helpers.clear_screen()    
    message = input("Type the message to {}: ".format(action))
        
    helpers.clear_screen()
    if action == "encrypt":
        input("Encrypted message: {}".format(cipher.encrypt(message)))
    else:
        input("Encrypted message: {}".format(cipher.encrypt(message)))

        
def prompt_for_restart():
    print()
    restart = input("Would you like to restart? yes/no: ").upper()
    return restart
    
        
def run():
    restart = "YES"
    while restart != "NO":
        cipher = select_cipher()
        action = select_encrypt_or_decrypt()    
        print_message(cipher, action)
        restart = prompt_for_restart()
    print("Quitting...")
    
    
if __name__ == "__main__":    
    run()