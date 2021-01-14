def to_dec(number):
    """Convert binary to decimal"""
    return int(number, 2)

def to_oct(number):
    """Convert binary to octal"""
    return oct(to_dec(number))[2:]

def to_hex(number):
    """Convert binary to hexadecimal"""
    return hex(to_dec(number))[2:]
    