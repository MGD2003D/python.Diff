import unittest
from src.lab2.rsa import is_prime, gcd, multiplicative_inverse, generate_keypair, encrypt, decrypt

class TestRSA(unittest.TestCase):

    def test_is_prime(self):
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(11), True)
        self.assertEqual(is_prime(8), False)

    def test_gcd(self):
        self.assertEqual(gcd(12, 15), 3)
        self.assertEqual(gcd(3, 7), 1)

    def test_multiplicative_inverse(self):
        self.assertEqual(multiplicative_inverse(7, 40), 23)

    def test_keypair_generation(self):
        public, private = generate_keypair(17, 19)
        e, n = public
        self.assertEqual(is_prime(n/e), True)
        d, n = private
        self.assertEqual(e*d % ((17-1)*(19-1)), 1)

    def test_encryption_decryption(self):
        public, private = generate_keypair(17, 19)
        message = "Hello, World!"
        encrypted_msg = encrypt(private, message)
        decrypted_msg = decrypt(public, encrypted_msg)
        self.assertEqual(message, decrypted_msg)

if __name__ == "__main__":
    unittest.main()