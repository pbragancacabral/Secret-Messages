import string

from ciphers import Cipher


class Atbash(Cipher):
    """Atbash is a monoalphabetic substitution cipher originally used to encrypt the Hebrew alphabet. It can be modified
    for use with any known writing system with a standard collating order.

    Plain	A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z
    Cipher	Z	Y	X	W	V	U	T	S	R	Q	P	O	N	M	L	K	J	I	H	G	F	E	D	C	B	A

    Source: Wikipedia

    This implementation is case-sensitive."""
    _ALPHABET = string.ascii_letters

    @classmethod
    def __encryptdecrypt(cls, message):
        output = ""
        for character in message:
            if character in cls._ALPHABET:
                index = cls._ALPHABET.index(character)
                output += cls._ALPHABET[::-1][index]
            else:
                output += character
        return output

    """Takes one string and encrypts it based on the Atbash cipher."""
    @classmethod
    def encrypt(cls, message):
        return cls.__encryptdecrypt(message)

    """Takes one string and decrypts it based on the Atbash cipher."""
    @classmethod
    def decrypt(cls, message):
        return cls.__encryptdecrypt(message)
