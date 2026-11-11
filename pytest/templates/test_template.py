"""Tests for <module>."""
import pytest

from module_name import function_name


def test_<scenario>_<expected>():
    # Arrange
    # Act
    # Assert
    assert function_name(...) == ...


def test_<invalid_input>_raises():
    with pytest.raises(ValueError, match='message'):
        function_name(None)