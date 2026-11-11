# ============================================================
# FUNCTIONS - quick reference
# ============================================================


# -- Parameters, default values, return ---------------------
def greet(name, greeting='Hello'):
    return f'{greeting}, {name}!'

print(greet('Hippolyte'))             # Hello, Hippolyte!
print(greet('Hippolyte', 'Bonjour'))  # Bonjour, Hippolyte!
print(greet('Hippolyte', greeting='Hi'))   # Hi, Hippolyte!
# Defaults go AFTER parameters without default:
# def bad(optional='x', required): SyntaxError

# Without return, a function returns None
def no_return():
    x = 1

print(no_return())   # None


# -- print vs return ----------------------------------------
# print shows something on screen. return gives a value back to the caller
# (tests and other functions can only use what is returned).


# -- Several return values (tuple) --------------------------
def area_perimeter(w, h):
    return w * h, 2 * (w + h)

area, perimeter = area_perimeter(3, 6)
print(area, perimeter)   # 18 18


# -- Early return -------------------------------------------
def safe_divide(a, b):
    if b == 0:
        return 'Error: division by zero'
    return a / b          # no else needed

print(safe_divide(10, 2), safe_divide(1, 0))   # 5.0 Error: division by zero


# -- One function = one job ---------------------------------
# validation(problems) -> (status, message)
# format_problems(problems) -> string
# calculate(problems) -> list of results
# The main function calls them in order and decides when to stop.
# Name functions so they don't hide Python's: `format`, `max`, `list`...
# Docstring = fiche of the function: what it receives, what it returns.


# -- Function calling another -------------------------------
def width(parts):                       # parts = ['32', '+', '698']
    return len(max(parts[::2], key=len)) + 2

print(width('32 + 698'.split()))        # 5


# -- Lambda: anonymous one-line function --------------------
double = lambda x: x * 2
print(double(5))   # 10
# Mostly passed directly to sorted / map / filter / min / max


# -- sorted / min / max with key ----------------------------
expenses = [{'amount': 30}, {'amount': 10}, {'amount': 50}]
print(sorted(expenses, key=lambda e: e['amount']))   # ascending by amount
print(max(['a', 'bbb', 'cc'], key=len))              # 'bbb'


# -- map and filter (functions taking a function) -----------
expenses = [
    {'amount': 30, 'category': 'food'},
    {'amount': 10, 'category': 'transport'},
    {'amount': 50, 'category': 'food'},
]
amounts = list(map(lambda e: e['amount'], expenses))
food = list(filter(lambda e: e['category'] == 'food', expenses))
print(amounts)   # [30, 10, 50]
print(food)      # the two food expenses
# map and filter return iterators: wrap them in list()
# The list comprehension does the same and is usually preferred:
print([e['amount'] for e in expenses])                   # [30, 10, 50]
print([e for e in expenses if e['category'] == 'food'])  # same as `food`
