# ============================================================
# STRINGS - quick reference
# ============================================================


# -- Access and slicing: string[start:stop:step] ------------
s = 'hello'
print(s[0], s[-1])   # h o
print(s[::-1])       # 'olleh'  reversed
print(s[::2])        # 'hlo'    every 2nd char
print(s[1::2])       # 'el'     every 2nd char from index 1
print(s[1:-1])       # 'ell'    without first and last
print(len(s))        # 5


# -- split / join -------------------------------------------
print('32 + 698'.split())          # ['32', '+', '698']  splits on spaces
print('a-b-c'.split('-'))          # ['a', 'b', 'c']
print('  a   b '.split())          # ['a', 'b']   ignores extra spaces
print('  a   b '.split(' '))       # ['', '', 'a', '', '', 'b', '']  careful!
print(''.join(['a', 'b', 'c']))    # 'abc'
print('    '.join(['32', '3801']))  # '32    3801'  4 spaces between
# no_space kata: ''.join(text.split())
# split() needs a STRING: ['a b'].split() is an AttributeError


# -- strip --------------------------------------------------
print('  hello  '.strip())    # 'hello'   both ends (not the middle)
print('_hello_'.strip('_'))   # 'hello'
print('_hello_'.lstrip('_'))  # 'hello_'  left only
print('_hello_'.rstrip('_'))  # '_hello'  right only
print(len('   '.strip()) < 1)   # True  string with only spaces


# -- Replace / remove characters ----------------------------
card = '4111-1111-4555-1142'
print(card.replace('-', ''))   # '4111111145551142'
table = str.maketrans({'-': '', ' ': ''}) # table de correspondance '-' → rien, ' ' → rien
print('41-11 11'.translate(table))   # '411111'  several characters at once


# -- Tests on characters (return True / False) --------------
print('123'.isdigit(), '12b'.isdigit())    # True False
print('abc'.isalpha(), 'ab1'.isalpha())    # True False
print('A'.isupper(), 'a'.islower())        # True True
print('Hello'.isalpha())                   # True  ('Hello World' is False: space)
print(''.isalpha(), ''.isdigit())          # False False  (empty string)


# -- Case ---------------------------------------------------
print('Hello'.lower(), 'Hello'.upper())    # hello HELLO


# -- Find a position ----------------------------------------
print('hello'.index('l'))   # 2   first occurrence, ValueError if missing
print('hello'.find('l'))    # 2   same, but returns -1 if missing
print('hello'.find('z'))    # -1
print('a' in 'banana')      # True


# -- Alignment ----------------------------------------------
print('|' + '32'.rjust(5) + '|')    # |   32|   pad on the LEFT
print('|' + '32'.ljust(5) + '|')    # |32   |   pad on the RIGHT
print('|' + '-' * 5 + '|')          # |-----|
name, width = 'ab', 5
print(f'|{name:>{width}}|')         # |   ab|   right-aligned f-string
print(f'|{name:<{width}}|')         # |ab   |   left-aligned
# str(-3800).rjust(6) -> ' -3800'  the sign counts as a character


# -- f-strings ----------------------------------------------
n = 'Hippolyte'
print(f'Hello {n}, in 5 years: {30 + 5}, {n.upper()}')
# Same quotes inside an f-string only work on Python 3.12+: use ' and "
print(f"{'    '.join(['a', 'b'])}")   # a    b


# -- Newlines -----------------------------------------------
print('line1\nline2')      # two lines
print(repr('  3\n+ 8'))     # '  3\n+ 8'  repr() shows spaces and \n exactly


# -- Alphabet as a reference string -------------------------
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(alphabet.index('h'))    # 7
print(alphabet[7])            # 'h'
# Shift with wrap-around: see numbers.py


# -- Reverse a string ---------------------------------------
print('hello'[::-1])                    # 'olleh'  shortest way
print(''.join(reversed('hello')))       # 'olleh'
# reversed() returns an iterator: wrap it in join() or list()


# -- Regular expressions: re.findall ------------------------
import re
print(re.findall(r'\d+', '12-34+56'))        # ['12', '34', '56']
print(re.findall(r'\d+|[+-]', '266-66'))     # ['266', '-', '66']
# \d = one digit, \d+ = one or more, | = or, [+-] = + or -
# findall does NOT search for the characters you wrote as separators:
# it returns every piece of the string that matches the pattern
