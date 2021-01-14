def to_dec(number):
    """Convert octal to decimal"""
    return int(number, 8)

def to_bin(number):
    """Convert octal to binary"""
    return bin(to_dec(number))[2:]

def to_hex(number):
    """Convert octal to hexadecimal"""
    return hex(to_dec(number))[2:]
    