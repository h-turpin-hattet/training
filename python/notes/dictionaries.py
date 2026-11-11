# ============================================================
# DICTIONARIES - quick reference
# ============================================================


# -- Create and access --------------------------------------
film = {'title': 'Pulp Fiction', 'year': 1994, 'rating': 9}
print(film['title'])         # 'Pulp Fiction'
print(film.get('year'))      # 1994
print(film.get('genre'))     # None  (no error if the key is missing)
# film['genre']              # KeyError if the key is missing


# -- Add / modify / delete ----------------------------------
film['genre'] = 'Thriller'   # new key
film['rating'] = 10          # existing key: value replaced
del film['year']             # delete a key
print(film.pop('genre'))     # 'Thriller'  (removes AND returns the value)
print(film)                  # {'title': 'Pulp Fiction', 'rating': 10}


# -- Loop ---------------------------------------------------
for key, value in film.items():
    print(f'{key}: {value}')   # title: Pulp Fiction / rating: 10

print(list(film.keys()))     # ['title', 'rating']
print(list(film.values()))   # ['Pulp Fiction', 10]
print('title' in film)       # True  (tests KEYS, not values)


# -- List of dictionaries (most common structure) -----------
expenses = [
    {'amount': 30, 'category': 'food'},
    {'amount': 10, 'category': 'transport'},
    {'amount': 50, 'category': 'food'},
]
print(expenses[0]['amount'])   # 30
print(sum(e['amount'] for e in expenses))   # 90
print([e for e in expenses if e['category'] == 'food'])   # the 2 food ones


# -- Dictionary instead of a long if/elif -------------------
# Key = what player 1 plays, value = what it beats
wins = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}

def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    if wins[p1] == p2:    # wins[p1] looks up the VALUE of the key p1
        return 'Player 1 won!'
    return 'Player 2 won!'

print(rps('rock', 'scissors'))   # Player 1 won!
print(rps('rock', 'paper'))      # Player 2 won!

# Rule: if all values would be the same (e.g. vowels), a dictionary is
# the wrong tool: use a string or a tuple and test with `in`.
