import string

from ciphers import Cipher


class Atbash(Cipher):
    ALPHABET = string.ascii_letters

    @classmethod
    def __encryptdecrypt(cls, message):
        output = ""
        for character in message:
            if character in cls.ALPHABET:
                index = cls.ALPHABET.index(character)
                output += cls.ALPHABET[::-1][index].swapcase()
            else:
                output += character
        return output

    """Takes one string and encrypts it
    based on the Atbash cipher.
    """
    @classmethod
    def encrypt(cls, message):
        return cls.__encryptdecrypt(message)

    """Takes one string and decrypts it
    based on the Atbash cipher.
    """
    @classmethod
    def decrypt(cls, message):
        return cls.__encryptdecrypt(message)
