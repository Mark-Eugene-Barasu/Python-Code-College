import pytest
from practice_module import add_numbers, multiply, get_greeting


@pytest.fixture
def sample_data():
    """Fixture providing sample test data."""
    return {
        'numbers': (3, 5),
        'name': 'alice'
    }


def test_add_numbers_basic(sample_data):
    """Test add_numbers with positive integers."""
    result = add_numbers(sample_data['numbers'][0], sample_data['numbers'][1])
    assert result == 8


def test_add_numbers_zero():
    """Test add_numbers with zero."""
    result = add_numbers(0, 5)
    assert result == 5


def test_add_numbers_negative():
    """Test add_numbers with negative numbers."""
    result = add_numbers(-1, 3)
    assert result == 2


@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6),
    (0, 7, 0),
    (-2, 4, -8)
])
def test_multiply(a, b, expected):
    """Parametrized tests for multiply function."""
    result = multiply(a, b)
    assert result == expected



def test_get_greeting(sample_data):
    """Test get_greeting with valid name."""
    result = get_greeting(sample_data['name'])
    assert result == "Hello, Alice!"


def test_get_greeting_empty():
    """Test get_greeting raises ValueError for empty name."""
    with pytest.raises(ValueError):
        get_greeting("")


def test_get_greeting_mixed_case():
    """Test get_greeting handles mixed case names."""
    result = get_greeting("jOhN")
    assert result == "Hello, John!"


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
