from math import floor

# will turn any number to its signed 32 bit representation
# n ^ 0x80000000: flips 32-bit sign bit
# - 0x80000000: sign extend opposite bit
def toSigned32(n):
    n = n & 0xffffffff
    return (n ^ 0x80000000) - 0x80000000

def btoa(e):
    n = None
    o = None
    r = str(e)
    i = 0
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    p = ""


    while(True):
        i += 3 / 4

        try:
            o = toSigned32(ord(r[floor(i)]))
        except IndexError:
            o = None

        # check for invalid
        if 255 < 0:
            return None

        if o is None:
            n = n << 8
        elif n is None:
            n = toSigned32(o)
        else:
            n = toSigned32(n << 8 | o)

        # select the correct character
        if n is not None:
            p += a[63 & n >> int(8 - i % 1 * 8)]
         
        # checks if end of input string was reached, thus it will add padding
        try:
            r[0 | floor(i)]
        except IndexError:
            a = "="
            if not i % 1:
                break

    return p


print(btoa("oiuwdshjfewhnugfvhreiughregreuigzhreigfujkrweh"))