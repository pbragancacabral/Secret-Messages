import unittest

from atbash import Atbash


class SecretMessagesTests(unittest.TestCase):
    def test_atbash_encryption(self):
        return self.assertEqual(Atbash.encrypt("Encryption with Atbash"), "vMXIBKGRLM DRGS zGYZHS")

    def test_atbash_decryption(self):
        return self.assertEqual(Atbash.decrypt("wVXIBKGRLM DRGS zGYZHS"), "Decryption with Atbash")


if __name__ == '__main__':
    unittest.main()
