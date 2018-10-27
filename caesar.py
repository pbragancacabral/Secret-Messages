import random
import string

from ciphers import Cipher


class Caesar(Cipher):
    """In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift,
    is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which
    each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example,
    with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius
    Caesar, who used it in his private correspondence.

    Source: Wikipedia

    This implementation is case-insensitive."""

    _ALPHABET = string.ascii_uppercase

    def __init__(self, offset=random.randint(1, 26)):
        self.CIPHER = self._ALPHABET[offset:] + self._ALPHABET[:offset]

    """Takes one string and encrypts it based on the Caesar cipher."""
    def encrypt(self, text):
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self._ALPHABET.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.CIPHER[index])
        return "".join(output)

    """Takes one string and decrypts it based on the Caesar cipher."""
    def decrypt(self, text):
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.CIPHER.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self._ALPHABET[index])
        return "".join(output)
