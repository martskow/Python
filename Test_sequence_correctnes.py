"""
Autor: Marta Skowron

Ten moduł zawiera funkcję testującą dla domknięcia zawartego w pliku 'Zad_1.py'.
"""
from Zad_1 import poprawnosc_sekwencji


def poprawnosc_sekwencji_test():
    """
    Funkcja testująca dla funkcji poprawnosc_sekwencji.
    Testy zostały przeprowadzone jedynie dla przypadków, gdzie funkcja zwraca
    wartość None. Przypadki, dla których funkcja zwraca funkcję walidator_DNA
    zotstały przeprowadzone poza funkcją testującą.
    """
    try:
        poprawnosc_sekwencji(123)
        assert False, 'Niepoprawny test dla funkcji poprawnosc_sekwencji.'
    except TypeError:
        assert True
        print('Poprawny test dla funkcji poprawnosc_sekwencji.')

    try:
        poprawnosc_sekwencji('    ')
        assert False, 'Niepoprawny test dla funkcji poprawnosc_sekwencji.'
    except ValueError:
        assert True
        print('Poprawny test dla funkcji poprawnosc_sekwencji.')

    try:
        poprawnosc_sekwencji(['a', 2, 'b', 7])
        assert False, 'Niepoprawny test dla funkcji poprawnosc_sekwencji.'
    except ValueError:
        assert True
        print('Poprawny test dla funkcji poprawnosc_sekwencji.')

    try:
        poprawnosc_sekwencji(['a', '2', 'b', '7'])
        assert False, 'Niepoprawny test dla funkcji poprawnosc_sekwencji.'
    except ValueError:
        assert True
        print('Poprawny test dla funkcji poprawnosc_sekwencji.')

    try:
        poprawnosc_sekwencji(['a', '-', 'b', '#'])
        assert False, 'Niepoprawny test dla funkcji poprawnosc_sekwencji.'
    except ValueError:
        assert True
        print('Poprawny test dla funkcji poprawnosc_sekwencji.')

    try:
        poprawnosc_sekwencji(['abc', 'b', 'c'])
        assert False, 'Niepoprawny test dla funkcji poprawnosc_sekwencji.'
    except ValueError:
        assert True
        print('Poprawny test dla funkcji poprawnosc_sekwencji.')


def walidator_DNA_test():
    """
    Funkcja testująca dla funkcji walidator_DNA.
    """
    alfabet = ['A', 'C', 'G', 'T']
    zmienna = poprawnosc_sekwencji(alfabet)

    test = zmienna('ACGT')
    assert test, 'Niepoprawny test dla funkcji walidator_DNA.'
    print('Poprawny test dla funkcji walidator_DNA.')

    test = zmienna('AAGG')
    assert test, 'Niepoprawny test dla funkcji walidator_DNA.'
    print('Poprawny test dla funkcji walidator_DNA.')

    test = zmienna('')
    assert not test, 'Niepoprawny test dla funkcji walidator_DNA.'
    print('Poprawny test dla funkcji walidator_DNA.')

    test = zmienna('     ')
    assert not test, 'Niepoprawny test dla funkcji walidator_DNA.'
    print('Poprawny test dla funkcji walidator_DNA.')

    test = zmienna('AAXGG')
    assert not test, 'Niepoprawny test dla funkcji walidator_DNA.'
    print('Poprawny test dla funkcji walidator_DNA.')

    try:
        zmienna([])
        assert False, 'Niepoprawny test dla funkcji walidator_DNA.'
    except TypeError:
        assert True
        print('Poprawny test dla funkcji walidator_DNA.')

    try:
        zmienna(123)
        assert False, 'Niepoprawny test dla funkcji walidator_DNA.'
    except TypeError:
        assert True
        print('Poprawny test dla funkcji walidator_DNA.')

    alfabet = 'ACGT'
    zmienna = poprawnosc_sekwencji(alfabet)

    test = zmienna('ACGT')
    assert test, 'Niepoprawny test dla funkcji walidator_DNA.'
    print('Poprawny test dla funkcji walidator_DNA.')

    test = zmienna('AAGG')
    assert test, 'Niepoprawny test dla funkcji walidator_DNA.'
    print('Poprawny test dla funkcji walidator_DNA.')

    test = zmienna('')
    assert not test, 'Niepoprawny test dla funkcji walidator_DNA.'
    print('Poprawny test dla funkcji walidator_DNA.')

    test = zmienna('     ')
    assert not test, 'Niepoprawny test dla funkcji walidator_DNA.'
    print('Poprawny test dla funkcji walidator_DNA.')

    test = zmienna('AAXGG')
    assert not test, 'Niepoprawny test dla funkcji walidator_DNA.'
    print('Poprawny test dla funkcji walidator_DNA.')

    try:
        zmienna([])
        assert False, 'Niepoprawny test dla funkcji walidator_DNA.'
    except TypeError:
        assert True
        print('Poprawny test dla funkcji walidator_DNA.')

    try:
        zmienna(123)
        assert False, 'Niepoprawny test dla funkcji walidator_DNA.'
    except TypeError:
        assert True
        print('Poprawny test dla funkcji walidator_DNA.')

    alfabet = []
    zmienna = poprawnosc_sekwencji(alfabet)

    test = zmienna('')
    assert not test, 'Niepoprawny test dla funkcji walidator_DNA.'
    print('Poprawny test dla funkcji walidator_DNA.')

    test = zmienna('AAXGG')
    assert not test, 'Niepoprawny test dla funkcji walidator_DNA.'
    print('Poprawny test dla funkcji walidator_DNA.')

    alfabet = ''
    zmienna = poprawnosc_sekwencji(alfabet)

    test = zmienna('')
    assert not test, 'Niepoprawny test dla funkcji walidator_DNA.'
    print('Poprawny test dla funkcji walidator_DNA.')

    test = zmienna('AAXGG')
    assert not test, 'Niepoprawny test dla funkcji walidator_DNA.'
    print('Poprawny test dla funkcji walidator_DNA.')


poprawnosc_sekwencji_test()
walidator_DNA_test()
