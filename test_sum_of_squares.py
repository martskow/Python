"""
Autor: Marta Skowron

Plik zawiera testy jednostkowe funkcji znajdującej się w pliku Zad_1.py

Testy nazwane uwzględniając wyskazówki ze stron podanych poniżej:
https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-best-practices
https://dev.to/n_develop/how-do-you-name-your-tests-108c
"""
import pytest


def test_n_GreatterThan1_RetrunsSumOfSquares():
    """
    Function tests function sum_of_sqares for typical cases - n type is int and 
    n is greater or equal 1.
    """
    from Zad_1 import sum_of_squares
    test1 = sum_of_squares(10)
    assert test1 == 385
    
    test2 = sum_of_squares(2)
    assert test2 == 5
    
    
def test_n_Equal1_Returns1():
    from Zad_1 import sum_of_squares
    test2 = sum_of_squares(1)
    assert test2 == 1
 
       
def test_n_LessThan1_ThrowsValueError():
    """
    Function tests function sum_of_squares for cases when n type is int and n 
    is less than 1.
    """
    from Zad_1 import sum_of_squares
    with pytest.raises(ValueError):
        return sum_of_squares(0)
    
    with pytest.raises(ValueError):
        return sum_of_squares(-1)
    
    with pytest.raises(ValueError):
        return sum_of_squares(-100)


def test_n_TypeIsNotInt_ThrowsTypeError():
    """
    Function tests function sum_of_squares for cases when n type isn't int .
    """
    from Zad_1 import sum_of_squares
    with pytest.raises(TypeError):
        return sum_of_squares(1.5)
    
    with pytest.raises(TypeError):
        return sum_of_squares('1')


#pytest.main(["--cov=Zad_1", "--cov-report=term-missing"])
