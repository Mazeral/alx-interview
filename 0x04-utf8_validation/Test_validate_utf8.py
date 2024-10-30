import unittest
check_utf8 = __import__("0-validate_utf8").validUTF8

class TestCheckUTF8(unittest.TestCase):

    def test_single_byte_sequence(self):
        # ASCII characters (1 byte)
        self.assertTrue(check_utf8([0x48]))  # H
        self.assertTrue(check_utf8([0x65]))  # e
        self.assertTrue(check_utf8([0x6C]))  # l
        self.assertTrue(check_utf8([0x6C]))  # l
        self.assertTrue(check_utf8([0x6F]))  # o

    def test_multi_byte_sequences(self):
        # 2-byte sequence
        self.assertTrue(check_utf8([0xC3, 0xB1]))  # ñ
        # 3-byte sequence
        self.assertTrue(check_utf8([0xE2, 0x82, 0xAC]))  # €
        # 4-byte sequence
        self.assertTrue(check_utf8([0xF0, 0x9F, 0x98, 0x80]))  # 

    def test_invalid_byte_sequences(self):
        # Invalid starter byte
        self.assertFalse(check_utf8([0x80]))  
        # Starter byte without enough continuation bytes
        self.assertFalse(check_utf8([0xC3]))  # ñ (missing continuation byte)
        self.assertFalse(check_utf8([0xE2, 0x82]))  # € (missing continuation byte)
        self.assertFalse(check_utf8([0xF0, 0x9F, 0x98]))  #  (missing continuation byte)
        # Continuation byte without a starter byte
        self.assertFalse(check_utf8([0x80, 0x80, 0x80]))  
        # Incorrect continuation byte
        self.assertFalse(check_utf8([0xC3, 0xC3]))  # ñ (incorrect continuation byte)

    def test_edge_cases(self):
        # Empty input
        self.assertTrue(check_utf8([]))  
        # Single invalid byte
        self.assertFalse(check_utf8([0xFF]))  

    def test_real_world_text(self):
        # Hello, World! in English (all ASCII)
        hello_world_en = [0x48, 0x65, 0x6C, 0x6C, 0x6F, 0x2C, 0x20, 0x57, 0x6F, 0x72, 0x6C, 0x64, 0x21]
        self.assertTrue(check_utf8(hello_world_en))
        # Hola, Mundo! in Spanish (contains non-ASCII characters)
        hello_world_es = [0x48, 0x6F, 0x6C, 0x61, 0x2C, 0x20, 0x4D, 0x75, 0x6E, 0x64, 0x6F, 0x21, 0xC3, 0xB1, 0xC3, 0xB3, 0xC2, 0xA1]
        self.assertTrue(check_utf8(hello_world_es))

if __name__ == '__main__':
    unittest.main()
