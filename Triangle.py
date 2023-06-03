"""
Autor: Dr inż. Agnieszka Kazimierska (function code)
Marta Skowron (comments)


+ poprawka w linijce 27 - źle został wprowadzony warunek utworzenia trójkąta
if a > b + c or b > a + c or c > a + b powinno być 
if a >= b + c or b >= a + c or c >= a + b:
    
Nie wiem także, czy funckcja scale nie powinna rzucać wyjątku przy próbie 
skalowania przez liczbę ujemną, ale nie zmieniałam nic w kodzie i po 
przeskalowaniu przez k <= 0 sprawdzam rzucany wyjątek w funkcji __init__ 
"""
import math

class Triangle:
    
    def __init__(self, a, b, c):
        """
        Create a triangle's features if a triangle with given sides can exist.
        
        Args:
            a(int/float):
            b(int/float):
            c(int/float):
                
        Raises TypeError when a, b or c has wrong type.
        Raises ValueError when triangle with given side length cannot exist.
        """
        if not isinstance(a, (float, int)) \
            or not isinstance(b, (float, int)) \
            or not isinstance(c, (float, int)):
            raise TypeError('Side lengths have to be numbers.')
        if a >= b + c or b >= a + c or c >= a + b:
            raise ValueError('Triangle with given side length cannot exist.')
        self.a = a
        self.b = b
        self.c = c
    
    
    def calculate_area(self):
        """
        Calculate triangle area.
                
        Rerturn:
            Triangle area(float/int)
        """
        p = 0.5 * (self.a + self.b + self.c)
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    

    def is_right_angled(self):
        """
        Checks whether the given triangle is a right triangle
                
        Rerturn:
            True/False(bool): True when triangle is a right triangle and False
            when triangle isn't a right triangle
        """
        sides = [self.a, self.b, self.c]
        sides.sort()
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2
    

    def scale(self, k):
        """
        Scales the sides of a triangle by the given factor k
          
        Arg:
            k(int/float): factor 
        Rerturn:
            Triangle(object): class Triangle object.
            
        Raises TypeError when k has wrong type.
        """
        if not isinstance(k, (float, int)):
            raise TypeError('Scale factor has to be a number.')
        return Triangle(self.a * k, self.b * k, self.c * k)
