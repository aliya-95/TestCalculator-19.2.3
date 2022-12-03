import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_adding_success(self):
        assert self.calc.adding(1, 2) == 3

    def test_subtraction_success(self):
        assert self.calc.subtraction(4, 3) == 1

    def test_division_success(self):
        assert self.calc.division(6, 2) == 3

    def test_multiply_success(self):
        assert self.calc.multiply(10, 2) == 20

    def teardown(self):
        print('Выполнение метода Teardown')