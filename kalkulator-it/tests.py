import unittest
from bin import binary
from dec import decimal
from oct import octal
from hex import hexdec


class TestCalculator(unittest.TestCase):
    """
    I have decimal number with value "100" an the result will be:
    Binary      : 1100100
    Octal       : 144
    Hexadecimal : 64
    """

    def test_bin(self):
        # Binary to decimal
        result = binary.to_dec('1100100')
        self.assertEqual(str(result), '100')

        # Binary to octal
        result = binary.to_oct('1100100')
        self.assertEqual(str(result), '144')
                
        # Binary to hexadecimal
        result = binary.to_hex('1100100')
        self.assertEqual(str(result), '64')

    def test_dec(self):
        # Decimal to binary
        result = decimal.to_bin(100)
        self.assertEqual(result, '1100100')

        # Decimal to octal
        result = decimal.to_oct(100)
        self.assertEqual(result, '144')

        # Decimal to hexadecimal
        result = decimal.to_hex(100)
        self.assertEqual(result, '64')

    def test_oct(self):
        # Octal to binary
        result = octal.to_bin('144')
        self.assertEqual(str(result), '1100100')

        # Octal to decimal
        result = octal.to_dec('144')
        self.assertEqual(str(result), '100')

        # Octal to hexadecimal
        result = octal.to_hex('144')
        self.assertEqual(str(result), '64')

    def test_hex(self):
        # Hexadecimal to binary
        result = hexdec.to_bin('64')
        self.assertEqual(str(result), '1100100')

        # Hexadecimal to decimal
        result = hexdec.to_dec('64')
        self.assertEqual(str(result), '100')

        # Hexadecimal to octal
        result = hexdec.to_oct('64')
        self.assertEqual(str(result), '144')

if __name__ == "__main__":
    unittest.main()