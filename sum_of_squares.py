"""
Autor: Dr inż. Agnieszka Kazimierska (function code)
Marta Skowron (comments)
"""

def sum_of_squares(n):
    """
    Function for a given number n returns the sum of squres of the 
    numbers from 1 to n.
    Parameter:
        n(int): number equal or greater than 1
    Return:
        sum_sq(float): sum of the squres of the numbers from 1 to n
        
    Raises TypeError when given n value ins't an integer.
    Raises ValueError when geiven n value is less than 1.
    """
    if not isinstance(n, int):
        raise TypeError('Given value has to be an integer.')
    if n <= 0:
        raise ValueError('Given value has to be greater than 0.')
    sum_sq = 0
    for ii in range(1, n+1):
        sum_sq += ii**2
    return sum_sq
