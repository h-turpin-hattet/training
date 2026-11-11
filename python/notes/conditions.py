# ============================================================
# CONDITIONS - quick reference
# ============================================================


# -- Comparison operators always return a bool --------------
print(5 > 3, 5 == 5, 5 != 5, 5 >= 6)   # True True False False

# So no need for if/else just to return True/False
def is_adult(age):
    return age >= 18      # instead of if age >= 18: return True else: ...

def opposites(a, b):
    return a % 2 != b % 2   # one even and one odd

print(is_adult(20), opposites(3, 4), opposites(2, 4))   # True True False


# -- and / or / not -----------------------------------------
x = 5
print(x > 0 and x < 10)   # True  both must be true
print(x < 0 or x > 3)     # True  one is enough
print(not x > 3)          # False


# -- Classic trap: "different from A or from B" is always True
op = '+'
print(op != '+' or op != '-')      # True  (wrong: always true)
print(op != '+' and op != '-')     # False (right)
print(op not in ['+', '-'])        # False (right, and easier to extend)


# -- in / not in --------------------------------------------
print('a' in 'banana')            # True
print(3 in [1, 2, 3])             # True
print('title' in {'title': 1})    # True (dictionary: tests the keys)


# -- any / all (take a list or a generator) -----------------
print(all([True, True, False]))   # False  every element must be true
print(any([True, False, False]))  # True   at least one is true

problems = ['32 + 8', '1 - 3801']
# Is there at least one invalid operator?
print(any(p.split()[1] not in ['+', '-'] for p in problems))   # False
# Are all operands digits? (two `for` in one expression)
print(all(
    operand.isdigit()
    for problem in problems
    for operand in problem.split()[::2]
))   # True
# Error condition "not all valid" = `if not all(...)`


# -- Truthy / falsy -----------------------------------------
# Falsy: '' [] {} () 0 None False. Everything else is truthy.
print(bool(''), bool([]), bool(0), bool(None))   # False False False False
print(bool('a'), bool([0]), bool(' '))           # True True True
# So `if not my_list:` tests "empty or None". Beware: ' ' is truthy.


# -- Early return (no else needed) --------------------------
def check(value):
    if value is None:
        return 'None'
    if value == '':
        return 'empty'
    return 'ok'          # reached only if the checks above failed

print(check(None), check(''), check('a'))   # None empty ok


# -- Order of checks: the most dangerous first --------------
# `or` stops at the first True (short-circuit), so None goes first
def valid(arr):
    return not (arr is None or len(arr) < 3)   # len(None) never evaluated

print(valid(None), valid([1, 2]), valid([1, 2, 3]))   # False False True


# -- Inline if/else (ternary) -------------------------------
print('Even' if 4 % 2 == 0 else 'Odd')   # Even
