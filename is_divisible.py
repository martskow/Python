"""
Autor: Dr inż. Agnieszka Kazimierska (function code)
Marta Skowron (comments)
"""

def is_divisible(n, d):
    """
    Function chcecks whether a given number is divisible by a given divisor.
    Parameters:
        n(float): number whose dicvisibility is checking
        d(float): divisor 
    Return:
        True/False(bool): function returns True when n is divisible by d and 
        false when isn't.
    
    Raises ZeroDivisionError when d is equal 0.
    """
    if d == 0:
        raise ZeroDivisionError('Divisor cannot be equal 0.')
    return n % d == 0
