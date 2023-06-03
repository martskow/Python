"""
Autor: Marta Skowron

Plik zawiera testy jednostkowe funkcji znajdującej się w pliku Zad_2.py
"""
import pytest


def test_n_TypeIntPositive_d_TypeIntPositive_nGreaterThand_ReturnsTrue():
    """
    Function tests function is_divisible for cases when n and d are ints, they 
    are grater than 1 and value of n is greater than d value. 
    The function is_divisible returns True.
    """
    from Zad_2 import is_divisible
    test = is_divisible(10, 5)
    assert test
    
    
def test_n_TypeIntNegative_d_TypeIntNegative_nLessThand_ReturnsTrue():
    """
    Function tests function is_divisible for cases when n and d are ints, they 
    are negative and value of n is less than d value. 
    The function is_divisible returns True.
    """
    from Zad_2 import is_divisible
    test = is_divisible(-10, -5)
    assert test
    
    
def test_n_TypeIntPositive_d_TypeIntNegative_nGreaterThand_ReturnsTrue():
    """
    Function tests function is_divisible for cases when n and d are ints, n is
    positive and d is negative. The function is_divisible returns True.
    """
    from Zad_2 import is_divisible
    test = is_divisible(10, -5)
    assert test
    
    
def test_n_TypeIntNegative_d_TypeIntPositive_nAbsoluteGreaterThand_ReturnsTrue():
    """
    Function tests function is_divisible for cases when n and d are ints, d is
    positive, n is negative and the absolute value of n is greater than d. 
    The function is_divisible returns True.
    """
    from Zad_2 import is_divisible
    test = is_divisible(-10, 5)
    assert test
    

def test_n_TypeIntPositive_d_TypeIntPositive_nGreaterThand_ReturnsFalse():
    """
    Function tests function is_divisible for cases when n and d are ints, they 
    are grater than 1 and value of n is greater than d value. 
    The function is_divisible returns False.
    """
    from Zad_2 import is_divisible
    test = is_divisible(10, 3)
    assert not test
    
def test_n_TypeIntNegative_d_TypeIntNegative_nLessThand_ReturnsFalse():
    """
    Function tests function is_divisible for cases when n and d are ints, they 
    are negative and value of n is greater than d value. 
    The function is_divisible returns False.
    """
    from Zad_2 import is_divisible
    test = is_divisible(-10, -3)
    assert not test

def test_n_TypeIntPositive_d_TypeIntNegative_nAbsoluteGreaterThand_ReturnsFalse():
    """
    Function tests function is_divisible for cases when n and d are ints, n is
    positive and d is negative. The function is_divisible returns False.
    """
    from Zad_2 import is_divisible
    test = is_divisible(10, -3)
    assert not test
    
    
def test_n_TypeIntNegative_d_TypeIntPositive_nGreaterThand_ReturnsFlase():
    """
    Function tests function is_divisible for cases when n and d are ints, d is
    positive and n is negative. The function is_divisible returns False.
    """
    from Zad_2 import is_divisible
    test = is_divisible(-10, 3)
    assert not test

def test_n_TypeIntPositive_d_TypeIntPositive_nEuqald_ReturnsTrue():
    """
    Function tests function is_divisible for cases when n and d are ints, they
    are greater than 1 and they are equal. 
    The function is_divisible returns True.
    """
    from Zad_2 import is_divisible
    test = is_divisible(10, 10)
    assert test
    
def test_n_TypeIntPositive_d_TypeIntPositive_nLessThand_ReturnsFalse():
    """
    Function tests function is_divisible for cases when n and d are ints, they
    are greater than 1 and value of n is less than d value. 
    The function is_divisible returns False.
    """
    from Zad_2 import is_divisible
    test = is_divisible(10, 20)
    assert not test


def test_n_TypeIntPositive_d_Equal1_ReturnsTrue():
    """
    Function tests function is_divisible for cases when n is int grater than 1
    and d is equal 1. The function is_divisible returns True.
    """
    from Zad_2 import is_divisible
    test = is_divisible(10, 1)
    assert test

    
def test_n_TypeFloatPositive_d_TypeIntPositive_ReturnsFalse():
    """
    Function tests function is_divisible for cases when n is float grater than 1
    and d is int greater than 0. The function is_divisible returns False.
    """
    from Zad_2 import is_divisible
    test = is_divisible(10.5, 2)
    assert not test
    
def test_n_TypeIntPositive_d_TypeFloatPositive_ReturnsTrue():
    """
    Function tests function is_divisible for cases when n is int grater than 1
    and d is float greater than 1, but not grater than n. 
    The function is_divisible returns True.
    """
    from Zad_2 import is_divisible
    test = is_divisible(10, 2.5)
    assert test
    

def test_n_TypeIntPositive_d_TypeFloatPositive_ReturnsFalse():
    """
    Function tests function is_divisible for cases when n is int grater than 1
    and d is float greater than 1, but not grater than n. 
    The function is_divisible returns False.
    """
    from Zad_2 import is_divisible
    test = is_divisible(10, 1.5)
    assert not test
    
    
def test_n_TypeFloatPositive_d_Equal1_ReturnsFalse():
    """
    Function tests function is_divisible for cases when n is float grater than 1
    and d is equal 1. The function is_divisible returns False.
    """
    from Zad_2 import is_divisible
    test = is_divisible(10.5, 1)
    assert not test
    
    
def test_n_TypeFloatPositive_d_TypeFloatPositive_ReturnsTrue():
    """
    Function tests function is_divisible for cases when n and d are floats 
    greater than 1, but d is not grater than n. 
    The function is_divisible returns True.
    """
    from Zad_2 import is_divisible
    test = is_divisible(10.5, 1.5)
    assert test
    
    
def test_n_TypeFloatNegative_d_TypeFloatNegative_ReturnsTrue():
    """
    Function tests function is_divisible for cases when n and d are floats 
    negative, but d is not less than n. 
    The function is_divisible returns True.
    """
    from Zad_2 import is_divisible
    test = is_divisible(-10.5, -1.5)
    assert test
    
    
def test_n_TypeFloatPositive_d_TypeFloatNegative_ReturnsTrue():
    """
    Function tests function is_divisible for cases when n and d are floats 
    negative, but d absolute is less than n. 
    The function is_divisible returns True.
    """
    from Zad_2 import is_divisible
    test = is_divisible(10.5, -1.5)
    assert test
    
    
def test_n_TypeFloatNegative_d_TypeFloatPositive_ReturnsTrue():
    """
    Function tests function is_divisible for cases when n and d are floats 
    negative, but d is less than n absolute. 
    The function is_divisible returns True.
    """
    from Zad_2 import is_divisible
    test = is_divisible(-10.5, 1.5)
    assert test
    
    
def test_n_TypeFloatPositive_d_TypeFloatPositive_ReturnsFalse():
    """
    Function tests function is_divisible for cases when n and d are floats 
    greater than 1, but d is not grater than n. 
    The function is_divisible returns False.
    """
    from Zad_2 import is_divisible
    test = is_divisible(10.25, 1.65)
    assert not test
    
    
def test_n_TypeFloatNegative_d_TypeFloatNegative_ReturnsFalse():
    """
    Function tests function is_divisible for cases when n and d are floats 
    negative, but d is not less than n. 
    The function is_divisible returns False.
    """
    from Zad_2 import is_divisible
    test = is_divisible(-10.25, -1.5)
    assert not test
    
    
def test_n_TypeFloatPositive_d_TypeFloatNegative_ReturnsFalse():
    """
    Function tests function is_divisible for cases when n and d are floats 
    negative, but d absolute is less than n. 
    The function is_divisible returns True.
    """
    from Zad_2 import is_divisible
    test = is_divisible(10.25, -1.5)
    assert not test
    
    
def test_n_TypeFloatNegative_d_TypeFloatPositive_ReturnsFalse():
    """
    Function tests function is_divisible for cases when n and d are floats 
    negative, but d is less than n absolute. 
    The function is_divisible returns True.
    """
    from Zad_2 import is_divisible
    test = is_divisible(-10.25, 1.5)
    assert not test
    
    
def test_n_TypeFloatPositive_d_TypeFloatPositive_nEuqald_ReturnsTrue():
    """
    Function tests function is_divisible for cases when n and d are floats, they
    are greater than 1 and they are equal. 
    The function is_divisible returns True.
    """
    from Zad_2 import is_divisible
    test = is_divisible(10.5, 10.5)
    assert test
    
    
def test_n_Equal0_d_AnyValueOtherThan0_ReturnsTrue():
    """
    Function tests function is_divisible for cases when n is equal 0 and d 
    takes any value other than 0.
    The function is_divisible returns True.
    """
    from Zad_2 import is_divisible
    test = is_divisible(0, 1)
    assert test
    
    test = is_divisible(0, -1)
    assert test
    
    test = is_divisible(0, 10)
    assert test
    
    test = is_divisible(0, -10)
    assert test
    
    test = is_divisible(0, 1.5)
    assert test
    
    test = is_divisible(0, -1.5)
    assert test
    
    
def test_n_AnyValueOtherThan0_d_Equal0_ThrowsZeroDivisionError():
    """
    Function tests function is_divisible for cases when n takes any value other
    than 0 and d is equal 0. The function is_divisible throws ZeroDivisionError.
    """
    from Zad_2 import is_divisible
    with pytest.raises(ZeroDivisionError):
        is_divisible(1, 0)
        
    with pytest.raises(ZeroDivisionError):
        is_divisible(10, 0)
        
    with pytest.raises(ZeroDivisionError):
        is_divisible(-10, 0)
        
    with pytest.raises(ZeroDivisionError):
        is_divisible(1.5, 0)
        
    with pytest.raises(ZeroDivisionError):
        is_divisible(-1.5, 0)
        

def test_n_Equal0_d_Equal0_ThrowsZeroDivisionError():
    """
    Function tests function is_divisible for cases when n and d are equal 0. 
    The function is_divisible throws ZeroDivisionError.
    """
    from Zad_2 import is_divisible
    with pytest.raises(ZeroDivisionError):
        is_divisible(0, 0)
    
#pytest.main(["--cov=Zad_2", "--cov-report=term-missing"])
