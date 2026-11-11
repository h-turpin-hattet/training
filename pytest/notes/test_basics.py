# ============================================================
# PYTEST BASICS - quick reference
# ============================================================
# Run:  python -m pytest -v          (all tests, one line per test)
#       python -m pytest -v test_basics.py::test_add   (one test)
# Install: python -m pip install pytest
# (python -m avoids PATH problems when `pytest` is not found)


# -- Functions under test (normally imported from your module) --
# from arithmetic_arranger import arithmetic_arranger
def add(a, b):
    return a + b


def validate(value):
    """Return (status, message) like the validation function."""
    if value is None:
        raise ValueError('Input cannot be None')
    if value < 0:
        return False, 'Error: negative'
    return True, ''


# -- Naming rules -------------------------------------------
# File:     test_*.py  (or *_test.py)
# Function: test_*     -> pytest finds and runs it by itself
# Name = the scenario: test_add_negative_numbers, not test1


# -- A test = call + assert ---------------------------------
def test_add():
    assert add(2, 3) == 5


# -- Structure: Arrange / Act / Assert ----------------------
def test_add_negative_numbers():
    a, b = -2, -3                 # Arrange: prepare the data
    result = add(a, b)            # Act: call the function
    assert result == -5           # Assert: check the result


# -- Tuple results: compare the whole tuple -----------------
def test_validate_negative():
    assert validate(-1) == (False, 'Error: negative')


def test_validate_ok():
    status, message = validate(5)     # or unpack, then assert each
    assert status is True
    assert message == ''


# -- Testing an error: pytest.raises ------------------------
import pytest  # noqa: E402  (normally at the top of the file)


def test_validate_none_raises():
    with pytest.raises(ValueError):
        validate(None)


# match = regex searched in the error message (checks the message too)
def test_validate_none_message():
    with pytest.raises(ValueError, match='cannot be None'):
        validate(None)


# Use raises when the function RAISES. If it RETURNS a message
# (e.g. 'Error: Too many problems.'), a normal assert is enough.


# -- Comparing multi-line strings ---------------------------
def test_multiline():
    result = '  3\n+ 8'
    expected = '  3\n+ 8'
    assert result == expected
    # When it fails, print(repr(result)) shows spaces and \n exactly


# -- Pitfalls -----------------------------------------------
# 1. Two tests with the SAME name: the second overwrites the first,
#    only one runs and pytest says nothing. Keep names unique.
# 2. A test without `assert` always passes: it checks nothing.
# 3. Do not put print() as the check: tests need assert.
# 4. One test = one scenario. If it fails, the name tells you why.
# 5. Order of work (TDD): write the test first, see it fail (red),
#    write the code until it passes (green), then clean up.
