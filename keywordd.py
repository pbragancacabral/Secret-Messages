import string

from ciphers import Cipher


class Keyword(Cipher):
    ALPHABET = string.ascii_letters

    def __init__(self, keyword):
        self.keyword = keyword
        self.ALPHABET_REVERSED = list(self.keyword)
        for character in self.ALPHABET:
            if character not in self.ALPHABET_REVERSED:
                self.ALPHABET_REVERSED.append(character)

    """Takes one string and encrypts it
    based on the Keyword cipher.
    """
    def encrypt(self, message):
        encrypted = ""
        for character in message:
            if character in self.ALPHABET:
                index = self.ALPHABET.index(character)
                encrypted += self.ALPHABET_REVERSED[index]
            else:
                encrypted += character
        return encrypted

    """Takes one string and decrypts it
    based on the Keyword cipher.
    """
    def decrypt(self, message):
        decrypted = ""
        for character in message:
            if character in self.ALPHABET:
                index = self.ALPHABET_REVERSED.index(character)
                decrypted += self.ALPHABET[index]
            else:
                decrypted += character
        return decrypted
