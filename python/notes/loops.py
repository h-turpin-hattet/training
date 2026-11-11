# ============================================================
# LOOPS - quick reference
# ============================================================


# -- for over elements --------------------------------------
for fruit in ['apple', 'kiwi']:
    print(fruit)   # apple, kiwi

for char in 'abc':
    print(char)    # a, b, c  (a string is iterable too)


# -- range ---------------------------------------------------
print(list(range(3)))        # [0, 1, 2]   stops BEFORE 3
print(list(range(2, 5)))     # [2, 3, 4]
print(list(range(0, 10, 3))) # [0, 3, 6, 9]

for _ in range(3):           # _ = counter not used
    print('Repeating...')


# -- Index needed: range(len()) or enumerate ----------------
names = ['apple', 'kiwi']
prices = [3, 10]

for i in range(len(names)):          # i = 0, 1 -> valid indexes
    print(names[i], prices[i])       # two lists in parallel

for i, name in enumerate(names):     # index AND value together
    print(i, name)                   # 0 apple / 1 kiwi
# enumerate gives no benefit if you never use the index


# -- Nested loops -------------------------------------------
problems = ['32 + 8', '1 - 3801']
for problem in problems:             # outer: each problem
    for operand in problem.split()[::2]:   # inner: its two operands
        print(operand)               # 32, 8, 1, 3801

# Inner loop only on the right elements: don't loop over '+' / '-'
for problem in problems:
    parts = problem.split()
    if parts[1] == '+':
        print('addition')


# -- Accumulate results (3 lists, 1 per output line) --------
top, bottom = [], []
for problem in problems:
    a, op, b = problem.split()
    top.append(a)
    bottom.append(op + b)
print(top, bottom)   # ['32', '1'] ['+8', '-3801']
# Create the lists BEFORE the loop. No `x = my_list.append(...)`.


# -- Counter / total in a loop ------------------------------
count = 0
total = 0
for n in [1, 2, -6, -3]:
    if n > 0:
        count += 1
    elif n < 0:
        total += n
print(count, total)   # 2 -9
# Start at 0 for a sum, at 1 for a product (1 is neutral for *)


# -- return inside a loop exits the function ----------------
def first_negative(numbers):
    for n in numbers:
        if n < 0:
            return n      # stops at the first one
    return None           # after the loop: nothing found

print(first_negative([3, -1, -5]))   # -1


# -- while True + break -------------------------------------
counter = 0
while True:
    counter += 1
    if counter == 3:
        break             # only exit point
print(counter)            # 3

# Menu pattern:
# while True:
#     show_menu()
#     choice = input('Enter your choice: ')
#     if choice == '5':
#         break


# -- Never modify a list while looping over it --------------
# See lists.py (pitfalls). Build a new list instead.
