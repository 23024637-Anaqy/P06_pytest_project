import pytest

from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected
        
    def test_subtract(self):
        # Arrange
        a = 10
        b = 4
        cal = Calculator()
        
        # Act
        result = cal.subtract(a, b)
        
        # Assert
        expected = 6
        assert result == expected

    def test_multiply(self):
        # Arrange
        a = 7
        b = 6
        cal = Calculator()
        
        # Act
        result = cal.multiply(a, b)
        
        # Assert
        expected = 42
        assert result == expected

    def test_divide(self):

        # Arrange
        a = 10
        b = 2
        cal = Calculator()
        
        # Act
        result = cal.divide(a, b)
        
        # Assert
        expected = 5
        assert result == expected

    def test_divide_by_zero(self):
        # arrange
        a = 4321
        b = 0
        cal = Calculator()
 
        with pytest.raises(ZeroDivisionError):
            cal.divide(a, b)