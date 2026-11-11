# ============================================================
# COMPREHENSIONS - quick reference
# ============================================================
# A comprehension is a loop + append written on one line.


# -- Transform: [expression for x in iterable] --------------
numbers = [1, 2, 3, 4, 5]
print([n ** 2 for n in numbers])         # [1, 4, 9, 16, 25]
print([w.upper() for w in ['ab', 'cd']]) # ['AB', 'CD']
print([int(c) for c in '123'])           # [1, 2, 3]


# -- Filter: [expression for x in iterable if condition] ----
# Elements that do not match are DROPPED
print([n for n in numbers if n % 2 == 0])   # [2, 4]
print([x for x in ['a', 1, 'b', 2] if type(x) == int])   # [1, 2]
print(len([n for n in numbers if n > 2]))   # 3  (count the matches)


# -- Filter + transform -------------------------------------
print([n ** 2 for n in [-3, -1, 0, 1, 2] if n > 0])   # [1, 4]


# -- Ternary: [a if condition else b for x in iterable] -----
# ALL elements are kept, transformed differently
print(['even' if n % 2 == 0 else 'odd' for n in numbers])
# ['odd', 'even', 'odd', 'even', 'odd']

text = 'CamelCase'
snake = [
    '_' + c.lower() if c.isupper()   # uppercase -> '_' + lowercase
    else c                           # otherwise unchanged
    for c in text
]
print(''.join(snake).strip('_'))   # 'camel_case'

# Filter: `if` AT THE END (drops).  Ternary: `if ... else` AT THE START (keeps).


# -- Equivalent loop (to understand it) ---------------------
result = []
for n in numbers:
    if n % 2 == 0:
        result.append(n ** 2)
print(result)                                      # [4, 16]
print([n ** 2 for n in numbers if n % 2 == 0])     # same thing


# -- Two `for` in one comprehension -------------------------
# Same ORDER as nested loops: outer first, inner second
problems = ['32 + 8', '1 - 3801']
print([op for p in problems for op in p.split()[::2]])
# ['32', '8', '1', '3801']


# -- Generator expression (no brackets) ---------------------
# Lazy: nothing is computed until something consumes it
gen = (n for n in numbers)
print(gen)                 # <generator object ...>   not a list
print(list(gen))           # [1, 2, 3, 4, 5]
print([n for n in numbers])   # with [] you get the list straight away

# Perfect inside sum / any / all / min / max:
print(sum(n ** 2 for n in numbers if n % 2 == 0))   # 20
print(any(n > 4 for n in numbers))                   # True
print(all(n > 0 for n in numbers))                   # True


# -- Do NOT use append in a comprehension -------------------
# [result.append(i) for i in data]  -> list of None (append returns None)
# The comprehension builds the list by itself.
