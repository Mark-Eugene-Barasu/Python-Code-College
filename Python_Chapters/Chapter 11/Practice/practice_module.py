def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b


def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b


def get_greeting(name):
    """Return a personalized greeting message."""
    if not name:
        raise ValueError("Name cannot be empty")
    return f"Hello, {name.title()}!"
