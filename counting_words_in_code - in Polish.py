"""
Author: Marta Skowron

Funkcja string.find() odpowiedź użytkownika Tomerikoo
https://stackoverflow.com/questions/2294493/how-to-get-the-position-of-a-character-in-python
"""


def likwidacja_znakow(tekst):
    """
    Funkcja dla podanego przez użytkownika tekstu zamienia znaki: ',', '.', 
    ':', ';', '(', ')', '[', ']' na znak spacji.
    Args:
        tekst(string): zmienna typu string zawierająca dowolny tekst
    Return:
        tekst(string): zmieniony tekst wejściowy na tekst bez wymienonych wyżej
        znaków
    """
    tekst = tekst.replace(",", ' ')
    tekst = tekst.replace(".", ' ')
    tekst = tekst.replace(":", ' ')
    tekst = tekst.replace(";", ' ')
    tekst = tekst.replace("(", ' ')
    tekst = tekst.replace(")", ' ')
    tekst = tekst.replace("[", ' ')
    tekst = tekst.replace("]", ' ')

    return tekst


def licz(tablica, slownik):
    """
    Funkacja dla zadanej tablicy i słownika zwraca nową wartość słownika, 
    zliczającego wystąpienie wyrazów 'if', 'elif', 'else', 'for' i 'while' 
    (z wyłączeniem komentarzy dokumentujących - pod warunkiem, że kod jest
    zgodny z zasadami PEP-8).
    Args:
        tablica(list): tablica zawirająca elementy typu string
        slownik(dict): słownik zawierający nstępujące klucze: 'if', 'elif',
        'else', 'for', 'while', a odpowiadające im wartości to liczby typu int
    Return:
        slownik(dict): słownik zaktualizowany pod kątem elementów tablicy 
    """
    for i in range(0, len(tablica)):
        try:
            if tablica[i] == 'if':
                slownik['if'] += 1
            if tablica[i] == 'elif':
                slownik['elif'] += 1
            if tablica[i] == 'else':
                slownik['else'] += 1
            if tablica[i] == 'for':
                slownik['for'] += 1
            if tablica[i] == 'while':
                slownik['while'] += 1
        except KeyError:
            print('Podany słownik zawiera błędne klucze.')

    return slownik


def zliczanie_slowa():
    """
    Funkacja dla wpisanej przez użytkownika w konsoli linijki kodu lub 
    wprowadzenie pliku typu py poprzez potoki zliczy wystąpienia wyrazów 'if', 
    'elif', 'else', 'for' i 'while' (wszystkie wystąpienia tzn. także w 
    komentarzach dokumentacyjnych)
    Args:
    Return:
        zliczanie(dict): słownik którego kluczami są wyrazy  'if', 'elif', 
        'else', 'for' i 'while', a wartościami odpowiadająca liczba wystąpień
        danego wyrazu we wprowadzonej linijce kodu lub całym pliku
    """
    zliczanie = {'if': 0, 'elif': 0, 'else': 0, 'for': 0, 'while': 0}
    znacznik = False
    while True:
        try:
            tekst = input('Wprowadź kod:')
            linijki = tekst.split('\n')
            for linijka in linijki:
                if not znacznik:
                    if linijka.find('#') == -1 and linijka.find('"""') == -1:
                        licz(likwidacja_znakow(linijka).split(), zliczanie)
                    elif linijka.find('"""') != -1 or linijka.find("'''") != -1:
                        znacznik = True
                    elif linijka.find('#') != -1:
                        for n in range(linijka.find('#'), len(linijka)):
                            linijka = linijka[:n:]
                        licz(likwidacja_znakow(linijka).split(), zliczanie)

                else:
                    if linijka.find('"""') != -1 or linijka.find("'''") != -1:
                        znacznik = False

        except EOFError:
            return zliczanie
            break


print(zliczanie_slowa())


def test_likwidacja_znakow():
    """
    Funkacja testująca dla funkcji likwidacja_znakow
    """
    test = likwidacja_znakow('')
    assert test == '', 'Incorrect result'
    print('Correct test for function likwidacja_znakow')

    test = likwidacja_znakow('(tekst)')
    assert test == ' tekst ', 'Incorrect result'
    print('Correct test for function likwidacja_znakow')

    test = likwidacja_znakow('(),;:[]')
    assert test == '       ', 'Incorrect result'
    print('Correct test for function likwidacja_znakow')

    test = likwidacja_znakow('test:test')
    assert test == 'test test', 'Incorrect result'
    print('Correct test for function likwidacja_znakow')


test_likwidacja_znakow()    

def test_licz():
    """
    Funkacja testująca dla funkcji likwidacja_znakow
    """
    test = licz([], {})
    assert test == {}, 'Incorrect result'
    print('Correct test for function licz')

    test = licz(['if'], {'if': 0})
    assert test == {'if': 1}, 'Incorrect result'
    print('Correct test for function licz')

    test = licz(['else'], {'if': 0})
    assert test == {'if': 0}, 'Incorrect result'
    print('Correct test for function licz')

    test = licz([1, 2, 'kot', 'if'], {'if': 0})
    assert test == {'if': 1}, 'Incorrect result'
    print('Correct test for function licz')

    test = licz(['if', 'while', 'for'], {'if': 100, 'while': 101, 'for': 102})
    assert test == {'if': 101, 'while': 102, 'for': 103}, 'Incorrect result'
    print('Correct test for function licz')


test_licz()
