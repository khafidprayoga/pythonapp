def to_dec(number):
    """Convert hexadecimal to decimal"""
    return int(str(number), 16)

def to_bin(number):
    """Convert hexadecimal to binary"""
    
    return bin(to_dec(number))[2:]

def to_oct(number):
    """Convert hexadecimal to Octal"""
    return oct(to_dec(number))[2:]