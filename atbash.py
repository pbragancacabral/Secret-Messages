import string

from ciphers import Cipher


class Atbash(Cipher):
    ALPHABET = string.ascii_uppercase
    ALPHABET_REVERSED = ALPHABET[::-1]

    """Takes one string and encrypts it
    based on the Atbash cipher.
    """
    def encrypt(self, message):
        encrypted = ""
        for character in message.upper():
            index = self.ALPHABET.index(character)
            encrypted += self.ALPHABET_REVERSED[index]
        return encrypted

    """Takes one string and decrypts it
    based on the Atbash cipher.
    """
    def decrypt(self, message):
        decrypted = ""
        for character in message.upper():
            index = self.ALPHABET_REVERSED.index(character)
            decrypted += self.ALPHABET[index]
        return decrypted
