import unittest

from cipher_methods import (
    decrypt_des_cbc,
    decrypt_safer_k64_cbc,
    decrypt_twofish128_cbc,
    des_encrypt_block,
    encrypt_des_cbc,
    encrypt_safer_k64_cbc,
    encrypt_twofish128_cbc,
    safer_k64_decrypt_block,
    safer_k64_encrypt_block,
    twofish128_decrypt_block,
    twofish128_encrypt_block,
)


class CipherMethodsTests(unittest.TestCase):
    def test_des_known_answer(self):
        key = bytes.fromhex("133457799BBCDFF1")
        plaintext = bytes.fromhex("0123456789ABCDEF")
        ciphertext = bytes.fromhex("85E813540F0AB405")

        self.assertEqual(des_encrypt_block(key, plaintext), ciphertext)

    def test_twofish_128_known_answer(self):
        key = bytes(16)
        plaintext = bytes(16)
        ciphertext = bytes.fromhex("9F589F5CF6122C32B6BFEC2F2AE8C35A")

        self.assertEqual(twofish128_encrypt_block(key, plaintext), ciphertext)
        self.assertEqual(twofish128_decrypt_block(key, ciphertext), plaintext)

    def test_safer_k64_known_answer(self):
        key = bytes(8)
        plaintext = bytes(8)
        ciphertext = bytes.fromhex("032808C90EE7AB7F")

        self.assertEqual(safer_k64_encrypt_block(key, plaintext), ciphertext)
        self.assertEqual(safer_k64_decrypt_block(key, ciphertext), plaintext)

    def test_cbc_roundtrips_utf8(self):
        message = "Cifras: ação, UTF-8 e 🔐"
        test_cases = (
            (encrypt_des_cbc, decrypt_des_cbc, bytes.fromhex("133457799BBCDFF1"), bytes.fromhex("0123456789ABCDEF")),
            (encrypt_twofish128_cbc, decrypt_twofish128_cbc, bytes(16), bytes(16)),
            (encrypt_safer_k64_cbc, decrypt_safer_k64_cbc, bytes(8), bytes.fromhex("0123456789ABCDEF")),
        )

        for encrypt, decrypt, key, iv in test_cases:
            with self.subTest(cipher=encrypt.__name__):
                ciphertext, returned_key, returned_iv = encrypt(message, key, iv)
                self.assertEqual(returned_key, key)
                self.assertEqual(returned_iv, iv)
                self.assertEqual(decrypt(ciphertext, key, iv).decode("utf-8"), message)


if __name__ == "__main__":
    unittest.main()
