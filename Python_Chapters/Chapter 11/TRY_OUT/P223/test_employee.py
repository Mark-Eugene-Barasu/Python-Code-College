# test_employee.py - Tests for Employee class (11-3)
# First: Tests without fixture
# Second: Tests with fixture (employee fixture)
# Run with pytest test_employee.py -v

import pytest
from employee import Employee


def test_give_default_raise():
    """Test default raise of $5000."""
    emp = Employee('John', 'Doe', 50000)
    emp.give_raise()
    assert emp.annual_salary == 55000


def test_give_custom_raise():
    """Test custom raise of $10000."""
    emp = Employee('Jane', 'Smith', 60000)
    emp.give_raise(10000)
    assert emp.annual_salary == 70000


# Fixture added - provides employee instance for tests


@pytest.fixture
def employee():
    """Fixture returning Employee instance with $50000 salary."""
    return Employee('John', 'Doe', 50000)


def test_give_default_raise_fixture(employee):
    """Test default raise using fixture."""
    employee.give_raise()
    assert employee.annual_salary == 55000


def test_give_custom_raise_fixture(employee):
    """Test custom raise using fixture."""
    employee.give_raise(10000)
    assert employee.annual_salary == 60000
