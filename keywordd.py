import string

from ciphers import Cipher


class Keywordd(Cipher):
    KEYWORD = "KRYPTOS"
    ALPHABET = string.ascii_uppercase
    ALPHABET_REVERSED = []

    def __init__(self):
        self.ALPHABET_REVERSED = list(self.KEYWORD)
        for character in self.ALPHABET:
            if character not in self.ALPHABET_REVERSED:
                self.ALPHABET_REVERSED.append(character)

    """Takes one string and encrypts it
    based on the Keyword cipher.
    """
    def encrypt(self, message):
        encrypted = ""
        for character in message.upper():
            index = self.ALPHABET.index(character)
            encrypted += self.ALPHABET_REVERSED[index]
        return encrypted

    """Takes one string and decrypts it
    based on the Keyword cipher.
    """
    def decrypt(self, message):
        decrypted = ""
        for character in message.upper():
            index = self.ALPHABET_REVERSED.index(character)
            decrypted += self.ALPHABET[index]
        return decrypted
