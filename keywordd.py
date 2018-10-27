import string

from ciphers import Cipher


class Keyword(Cipher):
    """A keyword cipher is a form of monoalphabetic substitution. A keyword is used as the key, and it determines the
    letter matchings of the cipher alphabet to the plain alphabet.
    Plaintext: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
    Encrypted: K R Y P T O S A B C D E F G H I J L M N Q U V W X Z
    Source: Wikipedia"""
    ALPHABET = string.ascii_letters

    def __init__(self, keyword):
        self.keyword = keyword
        self.ALPHABET_REVERSED = list(self.keyword)
        for character in self.ALPHABET:
            if character not in self.ALPHABET_REVERSED:
                self.ALPHABET_REVERSED.append(character)

    """Takes one string and encrypts it based on the Keyword cipher."""
    def encrypt(self, message):
        encrypted = ""
        for character in message:
            if character in self.ALPHABET:
                index = self.ALPHABET.index(character)
                encrypted += self.ALPHABET_REVERSED[index]
            else:
                encrypted += character
        return encrypted

    """Takes one string and decrypts it based on the Keyword cipher."""
    def decrypt(self, message):
        decrypted = ""
        for character in message:
            if character in self.ALPHABET:
                index = self.ALPHABET_REVERSED.index(character)
                decrypted += self.ALPHABET[index]
            else:
                decrypted += character
        return decrypted
