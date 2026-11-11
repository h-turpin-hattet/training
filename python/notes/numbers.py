# ============================================================
# NUMBERS - quick reference
# ============================================================


# -- Operators ----------------------------------------------
print(7 + 2, 7 - 2, 7 * 2)   # 9 5 14
print(7 / 2)    # 3.5   always a float, even 4 / 2 = 2.0
print(7 // 2)   # 3     integer division (rounds down)
print(7 % 2)    # 1     remainder (modulo)
print(2 ** 3)   # 8     power
print(16 ** 0.5)   # 4.0 square root

# Precedence: * and ** before + and -  -> use parentheses
print('-' * (3 + 2))   # '-----'   without parentheses: TypeError


# -- Even / odd ---------------------------------------------
print(4 % 2 == 0)   # True  even
print(7 % 2 == 0)   # False odd


# -- Modulo to cycle through a sequence ---------------------
key = 'happy'   # length 5
for i in range(7):
    print(i, key[i % len(key)])   # h a p p y h a   (wraps back to the start)


# -- Wrap around an alphabet (shift / cipher) ---------------
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def shift_char(char, offset, direction=1):
    index = alphabet.index(char)
    return alphabet[(index + offset * direction) % 26]

print(shift_char('z', 3))        # 'c'  wraps around
print(shift_char('c', 3, -1))    # 'z'  direction=-1 reverses the operation
# One function for two opposite operations: direction = 1 or -1


# -- Split a two-digit number -------------------------------
n = 14
print(n // 10, n % 10)        # 1 4
print(n // 10 + n % 10)       # 5   sum of the digits
print(n - 9)                  # 5   shortcut for a doubled digit >= 10


# -- Conversions --------------------------------------------
print(int('42') + 1)      # 43
print(str(42) + '!')      # '42!'
print('42'.isdigit())     # True   '4.2'.isdigit() and '-4'.isdigit() are False
print(float('1.5'))       # 1.5
# int('+') or int('abc') -> ValueError: convert only what is a number


# -- abs / round / scientific notation ----------------------
print(abs(-5))             # 5
print(round(3.14159, 2))   # 3.14
print(1e3, 1e-7)           # 1000.0 1e-07   (1e-7 = 0.0000001)

# "Close enough" comparison with a tolerance
print(abs(15.9999999 - 16) < 1e-7)   # True


# -- min / max / sum ----------------------------------------
print(min(3, 7), max(3, 7), sum([1, 2, 3]))   # 3 7 6
# Digits that are not in a list: sum(int(d) for d in '123') -> 6
print(sum(int(d) for d in '123'))             # 6
