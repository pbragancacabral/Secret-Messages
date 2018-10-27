import string

from ciphers import Cipher


class Keyword(Cipher):
    """A keyword cipher is a form of monoalphabetic substitution. A keyword is used as the key, and it determines the
    letter matchings of the cipher alphabet to the plain alphabet.

    Plaintext: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
    Encrypted: K R Y P T O S A B C D E F G H I J L M N Q U V W X Z

    Source: Wikipedia"""
    ALPHABET = string.ascii_uppercase

    def __init__(self, keyword=None):
        if keyword is None:
            raise ValueError("A 'keyword' is required.")
        if not all(character.isalpha() for character in keyword):
            raise ValueError("'keyword' must be a single word: [A-Z]")
        self.keyword = keyword.upper()
        self.ALPHABET_REVERSED = []
        for character in list(self.keyword):
            if character not in self.ALPHABET_REVERSED:
                self.ALPHABET_REVERSED.append(character)
        for character in self.ALPHABET:
            if character not in self.ALPHABET_REVERSED:
                self.ALPHABET_REVERSED.append(character)

    """Takes one string and encrypts it based on the Keyword cipher."""
    def encrypt(self, message):
        message = message.upper()
        encrypted = ""
        for character in message:
            try:
                index = self.ALPHABET_REVERSED.index(character)
                encrypted += self.ALPHABET[index]
            except ValueError:
                encrypted += character
        return encrypted

    """Takes one string and decrypts it based on the Keyword cipher."""
    def decrypt(self, message):
        message = message.upper()
        decrypted = ""
        for character in message:
            try:
                index = self.ALPHABET.index(character)
                decrypted += self.ALPHABET_REVERSED[index]
            except ValueError:
                decrypted += character
        return decrypted
