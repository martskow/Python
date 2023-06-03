"""
Autor: Marta Skowron
"""


def poprawnosc_sekwencji(alfabet):
    """
    Funkcja dla zadanego przez użytkownika alfabetu, składającego się wyłącznie
    z liter, zwraca funkcję walidator_DNA() lub wartość None przy nieprawidłowej
    formie/wartościach podanego alfabetu. #czy musi spr czy litery to 'ACGT'?
    Arg:
        alfabet(list/str): lista, zawierająca wyłącznie pojedyńcze znaki będące
        literami, bądź napis złożony z liter
    Return:
        walidator_DNA(function): jeżeli dane wejściowe zostały wprowadzone 
        poprawnie zwrócona zostaje funkcja walidator_DNA
    
    Rzuca wyjątek:
        TypeError, jeżeli użytkownik podana zły format alfabetu.
        ValueError, jeżeli użytkownik poda alfabet, który zawiera 
        znaki inne niż pojedyńcze litery.
        
    """
    if not (type(alfabet) is list or type(alfabet) is str):
        raise TypeError('Podano zły format alfabetu.')

    elif (any(type(element) is int for element in alfabet)
          or not (all(element.isalpha() for element in alfabet))):
        raise ValueError('Podany alfabet zawiera znaki inne niż litery.')

    elif (type(alfabet) is list
          and not all(len(element) == 1 for element in alfabet)):
        raise ValueError('Podano zły format tablicy zawierającej alfabet - ' + \
                         'sprawdź czy znaki zosały wprowadzone pojedyńczo')
    else:
        def walidator_DNA(sekwencja):
            """
            Funkcja dla zadanej sekwencji zwraca True jeżeli wszystkie jej 
            elementy znajdują się w alfabecie lub False w przeciwnym wypadku. 
            Jeżeli sekwencja nie zostanie poprawnie podana funkcja zwróci 
            wartość None.
            Arg:
                sekwencja(str): sprawdzany ciąg znaków
            Return:
                True/False(bool): True w przypadku, gdy wszystkie znaki w  
                sekwencji znajdują się w alfabecie lub False w przeciwnym 
                wypadku
                
            Rzuca wyjątek:
                TypeError: jeżeli sekwencja nie zostanie poprawnie podana
            """
            if type(sekwencja) is str:
                if sekwencja == '':
                    znacznik = False
                else:
                    znacznik = True
                for i in range(0, len(sekwencja)):
                    if not sekwencja[i] in alfabet:
                        znacznik = False
                        break
                return znacznik
            else:
                print('Podano zły format sekwencji.')
                raise TypeError

        return walidator_DNA
