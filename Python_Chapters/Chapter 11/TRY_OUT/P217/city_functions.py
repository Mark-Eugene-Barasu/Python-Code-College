# city_functions.py - Chapter 11 Exercise 11-1/11-2
# Module containing city_country() function for formatting city/country/population

def city_country(city, country, population=None):
    """Return formatted string 'City, Country' or 'City, Country - population XXX'.

    Args:
        city (str): City name
        country (str): Country name  
        population (int, optional): Population number. Defaults to None.

    Returns:
        str: Formatted location string
    """
    if population is None:
        # 11-1 format: 'City, Country'
        return f"{city.title()}, {country.title()}"
    else:
        # 11-2 format: 'City, Country - population XXX'
        return f"{city.title()}, {country.title()} - population {population:,}"
