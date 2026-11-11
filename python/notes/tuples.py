# ============================================================
# TUPLES - quick reference
# ============================================================


# -- Create and access (same as a list) ---------------------
rgb = (255, 128, 0)
print(rgb[0])    # 255
print(rgb[-1])   # 0
print(len(rgb))  # 3


# -- Immutable: cannot be modified --------------------------
# rgb[0] = 99        # TypeError
# rgb.append(1)      # AttributeError
# To "change" one, build a new tuple:
rgb = (99,) + rgb[1:]
print(rgb)   # (99, 128, 0)   note the comma in (99,) for a 1-element tuple


# -- Unpacking: one variable per element --------------------
r, g, b = rgb
print(r, g, b)   # 99 128 0
# The variables are COPIES of the values: changing r does not change rgb
r = 1
print(rgb)       # (99, 128, 0)


# -- Return several values from a function ------------------
def rectangle(width, height):
    return width * height, 2 * (width + height)   # returns a tuple

area, perimeter = rectangle(3, 6)
print(area, perimeter)   # 18 18

# Same idea for (status, message) as in the validation function:
def validate(value):
    if value < 0:
        return False, 'Error: negative'
    return True, ''

status, message = validate(-1)
print(status, message)   # False Error: negative
# Keep the SAME shape (2 values) in every return, or unpacking fails


# -- Tuple or list? -----------------------------------------
# Tuple: data that must not change (coordinates, colors, fixed options)
# List: data that grows, shrinks or is sorted
vowels = ('a', 'e', 'i', 'o', 'u')
print('e' in vowels)   # True
