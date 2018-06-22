from ciphers import Cipher


class Polybius(Cipher):
    square = (
             ("A", "B", "C", "D", "E"),
             ("F", "G", "H", "I/J", "K"),
             ("L", "M", "N", "O", "P"),
             ("Q", "R", "S", "T", "U"),
             ("V", "W", "X", "Y", "Z")
    )

    """Takes one string and encrypts it
    based on the Polybius cipher.
    """
    def encrypt(self, message):
        encrypted = ""
        for character in message.upper():
            for row in self.square:
                for element in row:
                    if character in element:
                        encrypted += (str(self.square.index(row)+1) +
                                      str(row.index(element)+1))
        return encrypted

    """Takes one string and decrypts it
    based on the Polybius cipher.
    """
    def decrypt(self, message):
        message = message.upper()
        decrypted = ""
        digits = [message[i:i+2] for i in range(0, len(message), 2)]
        for pair_of_digits in digits:
            row, column = map(int, list(pair_of_digits))
            decrypted += self.square[row-1][column-1]
        return decrypted
