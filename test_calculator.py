"""
Unit tests for the calculator library
NB. unit test file must be name test_.. that pytest can pick it up

Shell: pytest -v --cov
-v nicer output
--cov coverage report
"""

import calculator

class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)