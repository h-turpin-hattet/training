# ============================================================
# ALGORITHMS - quick reference
# ============================================================
# Only reusable patterns here, not exercise solutions.


# -- Bisection: narrow a range by half until close enough ---
# Example: approximate a square root

target = 16
low = 0
high = max(1, target)   # max(1, target) handles targets between 0 and 1
tolerance = 1e-7        # acceptable margin of error

for _ in range(100):    # safety cap: avoids an infinite loop
    mid = (low + high) / 2
    square_mid = mid ** 2

    if abs(square_mid - target) < tolerance:
        print(f'sqrt({target}) is about {mid}')   # sqrt(16) is about 4.0
        break
    elif square_mid < target:
        low = mid    # too small -> search the upper half
    else:
        high = mid   # too large -> search the lower half

# Trace: low=0, high=16 -> mid=8, 8**2=64 > 16 -> high=8
#        low=0, high=8  -> mid=4, 4**2=16 = 16 -> found

# Pattern: low / high / mid + compare + move one bound + stop condition.
# Related notes: numbers.py (abs, 1e-7), loops.py (for _ in range).
