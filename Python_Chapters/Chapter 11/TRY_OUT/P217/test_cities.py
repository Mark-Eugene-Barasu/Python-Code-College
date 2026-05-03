# test_cities.py - Tests for 11-1/11-2
# Run with: pytest test_cities.py -v

import pytest # type: ignore
from city_functions import city_country


def test_city_country():
    # Test 11-1: basic city, country format
    result = city_country('santiago', 'chile')
    assert result == 'Santiago, Chile'


def test_city_country_population():
    # Test 11-2: city, country, population format
    result = city_country('santiago', 'chile', 5000000)
    assert result == 'Santiago, Chile - population 5,000,000'


# Run tests
if __name__ == '__main__':
    pytest.main([__file__, '-v'])
