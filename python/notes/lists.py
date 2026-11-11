# ============================================================
# LISTS - quick reference
# ============================================================


# -- Create and access --------------------------------------
fruits = ['apple', 'banana', 'kiwi']
print(fruits[0])      # 'apple'  (first)
print(fruits[-1])     # 'kiwi'   (last)
print(len(fruits))    # 3


# -- Add ----------------------------------------------------
fruits.append('mango')           # one element at the end
fruits.insert(1, 'pear')         # at index 1
fruits.extend(['plum', 'fig'])   # several elements at the end
print(fruits)   # ['apple', 'pear', 'banana', 'kiwi', 'mango', 'plum', 'fig']


# -- Remove -------------------------------------------------
fruits.remove('pear')    # by value (first match only)
last = fruits.pop()      # removes AND returns the last one -> 'fig'
first = fruits.pop(0)    # removes AND returns index 0 -> 'apple'
del fruits[0]            # removes index 0 (returns nothing)
print(fruits)            # ['kiwi', 'mango', 'plum']


# -- Search -------------------------------------------------
print('kiwi' in fruits)             # True
print(fruits.index('mango'))        # 1  (ValueError if missing)
print(['a', 'b', 'a'].count('a'))   # 2


# -- Sort ---------------------------------------------------
numbers = [3, 1, 4, 1, 5]
print(sorted(numbers))   # [1, 1, 3, 4, 5]  NEW list, original unchanged
print(numbers)           # [3, 1, 4, 1, 5]
numbers.sort()           # sorts IN PLACE, returns None
print(numbers)           # [1, 1, 3, 4, 5]
numbers.sort(reverse=True)
print(numbers)           # [5, 4, 3, 1, 1]


# -- Slicing: list[start:stop:step] -------------------------
n = [10, 20, 30, 40, 50]
print(n[1:-1])   # [20, 30, 40]  without first and last
print(n[::-1])   # [50, 40, 30, 20, 10]  reversed
print(n[::2])    # [10, 30, 50]  every 2nd element (index 0, 2, 4)
print(n[1::2])   # [20, 40]      every 2nd element from index 1

# Sum without min and max (kata): sort, cut both ends, sum
print(sum(sorted(n)[1:-1]))   # 90


# -- min / max / sum ----------------------------------------
print(min(n), max(n), sum(n))   # 10 50 150

# On strings, min/max compare ALPHABETICALLY, not by length
words = ['abc', 'de', 'z']
print(min(words))              # 'abc'
print(min(words, key=len))     # 'z'   key=len -> compare by length
print(len(min(words, key=len)))   # 1  length of the shortest word


# -- Nested lists -------------------------------------------
grid = [[1, 2], [3, 4]]
print(grid[1][0])   # 3  (row 1, column 0)
for row in grid:
    for value in row:
        print(value)   # 1, 2, 3, 4

# split() gives a list: pick operands with a step of 2
parts = '32 + 698'.split()
print(parts)        # ['32', '+', '698']
print(parts[::2])   # ['32', '698']  operands only


# -- Pitfalls -----------------------------------------------

# 1. append() / sort() / reverse() return None
result = [1].append(2)
print(result)   # None  -> never write x = my_list.append(...)

# 2. Never remove from a list while looping over it
data = ['a', 'b', 1]
for x in data:
    if type(x) != int:
        data.remove(x)
print(data)   # ['b', 1]  'b' was skipped!

# Build a new list instead
data = ['a', 'b', 1]
print([x for x in data if type(x) == int])   # [1]

# 3. b = a does NOT copy: both names point to the same list
a = [1, 2]
b = a
b.append(3)
print(a)   # [1, 2, 3]
c = a.copy()
c.append(4)
print(a)   # [1, 2, 3]  unchanged: c is a real copy

# See also: comprehensions.py (build lists in one line)
