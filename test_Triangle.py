"""
Autor: Marta Skowron

Plik zawiera testy jednostkowe funkcji znajdującej się w pliku Zad_3.py
"""
import pytest

def test__init__abc_AreInts_GreatestThan0_TringleCanBeConstructed():
    """
    Function tests function __init__ in class triangle when a,b,c are ints
    greatest than 0 and tringle can be constructed from them.
    """
    from Zad_3 import Triangle
    
    test_a = Triangle(3, 4, 5).a
    assert test_a == 3
    
    test_b = Triangle(3, 4, 5).b
    assert test_b == 4
    
    test_c = Triangle(3, 4, 5).c
    assert test_c == 5
    

def test__init__abc_AreFloats_GreatestThan0_TringleCanBeConstructed():
    """
    Function tests function __init__ in class triangle when a,b,c are floats
    greatest than 0 and tringle can be constructed from them.
    """
    from Zad_3 import Triangle
    
    test_a = Triangle(3.5, 4.5, 5.5).a
    assert test_a == 3.5
    
    test_b = Triangle(3.5, 4.5, 5.5).b
    assert test_b == 4.5
    
    test_c = Triangle(3.5, 4.5, 5.5).c
    assert test_c == 5.5


def test__init__abc_AreInts_LessThan0_ThrowsValueError():
    """
    Function tests function __init__ in class triangle when a,b,c are ints
    less than 0 so tringle can't be constructed from them.
    """
    from Zad_3 import Triangle
    
    with pytest.raises(ValueError):
        Triangle(-3, -4, -5)
        
    with pytest.raises(ValueError):
        Triangle(-3, 4, 5)
        
    with pytest.raises(ValueError):
        Triangle(3, -4, 5)
        
    with pytest.raises(ValueError):
        Triangle(3, 4, -5)


def test__init__abc_AreIntsOrFloats_GreaterThan0_ThrowsValueError():
    """
    Function tests function __init__ in class triangle when a,b,c are floats
    less than 0 so tringle can't be constructed from them.
    """
    from Zad_3 import Triangle
    
    with pytest.raises(ValueError):
        Triangle(1, 2, 3)
        
    with pytest.raises(ValueError):
        Triangle(1.5, 11.5, 21.5)
        

def test__init__abc_WrongType_ThrowsTypeError():
    """
    Function tests function __init__ in class triangle when a,b,c have wrong
    types.
    """
    from Zad_3 import Triangle
    
    with pytest.raises(TypeError):
        Triangle('3', '4', '5')
        
    with pytest.raises(TypeError):
        Triangle('3', 4, 5)
        
    with pytest.raises(TypeError):
        Triangle(3, '4', 5)
        
    with pytest.raises(TypeError):
        Triangle(3, 4, '5')
        
        
@pytest.fixture
def Triangle1():
    from Zad_3 import Triangle
    return Triangle(3, 6, 8)
        

@pytest.fixture
def Triangle2():
    from Zad_3 import Triangle
    return Triangle(3, 4, 5)


def test_calculate_area(Triangle1, Triangle2):
    """
    Function tests function calculate_area in class triangle.
    """
    test = Triangle1.calculate_area()
    assert test == 7.644442425710328
    
    test = Triangle2.calculate_area()
    assert test == 6


@pytest.fixture
def Triangle3():
    from Zad_3 import Triangle
    return Triangle(12, 16, 20)


def test_scale_k_IsInt_GreaterThan1(Triangle2, Triangle3):
    """
    Function tests function scale when k is int greater than 1.
    """
    test = Triangle2.scale(4)
    assert test.a == Triangle3.a and test.b == Triangle3.b \
        and test.c == Triangle3.c
    

@pytest.fixture
def Triangle4():
    from Zad_3 import Triangle
    return Triangle(4.5, 6, 7.5)


def test_scale_k_IsFloat_GreaterThan1(Triangle2, Triangle4):
    """
    Function tests function scale when k is float greater than 1.
    """
    test = Triangle2.scale(1.5)
    assert test.a == Triangle4.a and test.b == Triangle4.b \
        and test.c == Triangle4.c
    

def test_scale_k_IsEqual1(Triangle2):
    """
    Function tests function scale when k is equal 1.
    """
    test = Triangle2.scale(1)
    assert test.a == Triangle2.a and test.b == Triangle2.b \
        and test.c == Triangle2.c
    

@pytest.fixture
def Triangle5():
    from Zad_3 import Triangle
    return Triangle(0.3, 0.4, 0.5)


def test_scale_k_IsFloat_LessThan1ButGreaterThan0(Triangle2, Triangle5):
    """
    Function tests function scale when k is float greater than 0 and less 
    than 1.
    """
    test = Triangle2.scale(0.1)
    assert round(test.a, 1) == Triangle5.a and round(test.b, 1) == Triangle5.b \
        and round(test.c, 1) == Triangle5.c
    

def test_scale_k_IsInt_LessThan0_ThrowsValueError(Triangle2):
    """
    Function tests function scale when k is int less than 0.
    """
    with pytest.raises(ValueError):
        Triangle2.scale(-1)
        
        
def test_scale_k_IsFloat_LessThan0_ThrowsValueError(Triangle2):
    """
    Function tests function scale when k is float less than 0.
    """
    with pytest.raises(ValueError):
        Triangle2.scale(-1.5)
        

def test_scale_k_WrongType_ThrowsTypeError(Triangle2):
    """
    Function tests function scale when k has wrong type.
    """
    with pytest.raises(TypeError):
        Triangle2.scale('2')


def test_is_right_angled_ReturnsTrue(Triangle2):
    """
    Function tests function is_right_angled for trinagle right angled.
    """
    test = Triangle2.is_right_angled()
    assert test


def test_is_right_angled_ReturnsFalse(Triangle1):
    """
    Function tests function is_right_angled for trinagle not right angled.
    """
    test = Triangle1.is_right_angled()
    assert not test
    
    
#pytest.main(["--cov=Zad_3", "--cov-report=term-missing"])        