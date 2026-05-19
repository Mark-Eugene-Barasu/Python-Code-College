# test_cities.py - Tests for city_country()
# Run with: pytest test_cities.py -v

import pytest  # type: ignore

from city_functions import city_country


def test_city_country():
    # 11-1: basic city, country format
    result = city_country('santiago', 'chile')
    assert result == 'Santiago, Chile'

    # 11-2: population optional; calling without population should work
    result = city_country('santiago', 'chile')
    assert result == 'Santiago, Chile'



def test_city_country_population():
    # 11-2: population optional; can be provided
    result = city_country('santiago', 'chile', population=5000000)
    assert result == 'Santiago, Chile - population 5,000,000'



if __name__ == '__main__':
    pytest.main([__file__, '-v'])

