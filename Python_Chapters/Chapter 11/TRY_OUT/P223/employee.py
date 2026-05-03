# employee.py - Exercise 11-3: Employee class
# This class represents an employee with name and salary attributes.
# Supports default ($5000) and custom raises via give_raise().

class Employee:
    """A simple class to model an employee."""

    def __init__(self, first_name, last_name, annual_salary):
        """Initialize employee with first name, last name, and salary."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Increase salary by default $5000 or custom amount."""
        self.annual_salary += amount
