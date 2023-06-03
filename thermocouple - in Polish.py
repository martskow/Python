"""
Autor: Marta Skowron

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats



def skalowanie_termopary(plik):
    '''
    Funkcja dla zmierzonego napięcia i temperatury w doswiadczeniu skalowania 
    termopary zwaranca wartosc współczynnika alfa oraz rysuje wykres zależnosci
    tych wartosci wraz z regrasją liniową.
    Funkcja nie została przetestowana dla innych danych, ale jest zgodna z
    obliczeniami wykonanymi w sprawozdaniu na te zajęcia.
    Args:
        plik(file): plik z danymi w formacie csv rozdzielany znakiem ';'
    Return:
        alfa(float): wspołczynnik termoelektryczny termopary
    '''
    dane = pd.read_csv(plik, delimiter=';')
    U = dane['U [mV]'].to_list()
    T= np.array(dane['T [st C]']).reshape(1,-1)

    for i in range(0,len(U)):
        U[i]=float(dane['U [mV]'][i].replace(',','.'))

    U1 = U
    T = np.array(dane['T [st C]']).reshape(1,-1)
    U = np.array(U).reshape(1,-1)
    alfa = stats.linregress(T,U)[0]
    a = [T[0][0], T[0][-1]]
    b = [T[0][0]*alfa + stats.linregress(T,U)[1], 
         T[0][-1]*alfa+ stats.linregress(T,U)[1]]
    plt.plot(dane['T [st C]'], U1, '.', label='U(T)')
    plt.plot(a, b, 'r-', label='Regresja liniowa')
    plt.xlabel('Temperatura [stopnie Celsjusza]')
    plt.ylabel('Napięcie [mV]')
    plt.title('U(T)')
    plt.legend(loc="upper left")
    plt.savefig('skalowanie_termopary', bbox_inches='tight')
    plt.show()
    
    return alfa


def temperatura_krzepniecia(plik, alfa):
    '''
    Funkcja dla zmierzonego napięcia w czasie i dla wyliczonego współczynnika 
    termoelektrycznego w doswiadczeniu wyznaczania temperatury krzepnięcia wody 
    zwaranca wartosc temperatury krzepnięcia, współczynnika alfa oraz rysuje 
    wykres zależnosci napięcia od czasu.
    Funkcja nie została przetestowana dla innych danych, ale jest zgodna z
    obliczeniami wykonanymi w sprawozdaniu na te zajęcia.
    Args:
        plik(file): plik z danymi w formacie csv rozdzielany znakiem ';'
        alfa(float): wspołczynnik termoelektryczny termopary
    Return:
        T_k(float): temperatura krzepnięcia wody
        alfa(float): wspołczynnik termoelektryczny termopary
    '''
    
    dane = pd.read_csv(plik, delimiter=';')
    U = dane['U [mV]']
    t = dane['t [s]']
    for i in range(0,len(U)):
        U[i]=float(dane['U [mV]'][i].replace(',','.'))
        
    plt.plot(t, U, '.')
    plt.xlabel('Czas [s]')
    plt.ylabel('Napięcie [mV]')
    plt.title('U(t)')
    plt.savefig('temperatura_krzepniecia', bbox_inches='tight')
    plt.show()
    
    U_k = (U[54]+U[57])/2 #zakres w którym napięcie jest najbardziej wyrównane
    T_k = U_k/alfa
    
    return T_k, alfa
    
print(temperatura_krzepniecia('dane_temp_krzepniecia.csv', 
                        skalowanie_termopary('dane_skalowanie.csv')))
