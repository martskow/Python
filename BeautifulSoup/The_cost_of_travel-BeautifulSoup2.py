
"""
Autor: Marta Skowron

The script contains the 'corrected' code from the previous version of the file - the exception mechanism has been added
checking whether the data has been entered correctly (if not, part
fixes, and displays information about the problem for the rest) and a function
checking internet access.

NOTE!: Tests in the testing function were performed on October 19, 2022. Prices
fuels may change and then the data for some cases should be corrected.
At the same time, I declare that on that day all tests passed.

Python Tutorial: Web Scraping with BeautifulSoup and Requests
https://www.youtube.com/watch?v=ng2o98k983k

Function "connected_to_internet" - user Def_Os from 
https://stackoverflow.com/questions/3764291/how-can-i-see-if-theres-an-available-and-active-network-connection-in-python
"""
from bs4 import BeautifulSoup
import requests


def connected_to_internet(url='http://www.google.com/', timeout=5):
    """
    The function checks the Internet connection status.
    Return:
        True/False (bool): there is/isn't an internet connection
    """
    try:
        _ = requests.head(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        return False


def fuel_prices(fuel_type):
    """
    The function for the given name of fuel returns its average price in Poland
    according to data from the website https://www.autocentrum.pl/paliwa/ceny-paliw/.
    
    Arg:
        fuel_type (str): type of the fuel ('95', '98', 'ON', 'ON+', 'LPG')
    Return:
        price (float): price of fuel in PLN per liter 
    """
    
    if fuel_type in ['95', '98', 'ON', 'ON+', 'LPG']:
        web = requests.get('https://www.autocentrum.pl/paliwa/ceny-paliw/').text
        soup = BeautifulSoup(web, 'lxml')
              
        fuel_prices = {}
        list_fuel = []
        i=0
        
        for fuel in soup.find_all('h3'):
            list_fuel.append([fuel.text,''])
        
        for price in soup.find_all('div', class_="price"):
            list_fuel[i][1] = price.text[53:57].replace(',','.')
            i+=1
        
        i=0
        for n in list_fuel:
            fuel_prices[str(list_fuel[i][0])]=float(list_fuel[i][1])
            i+=1
        
        price = fuel_prices[fuel_type]
        
        return price
    else:
        return None


def travel_cost(distance, consumption, fuel_type, number_of_people):
    """
    Calculates travel cost per passenger.
    Parameters:
        distance (float): distance in kilometers (km)
        consumption (float): average fuel consumption
        in liters per 100 kilometers (l/100km)
        fuel_type (str): type of the fuel ('95', '98', 'ON', 'ON+', 'LPG')
        number_of_people (int): number of people in the vehicle
    Returns:
        cost (float)/None: travel cost per person/if the user provided wrong data
    """
    if (type(distance) is float or int) and (type(consumption) is float or int)\
        and (type(number_of_people) is int):
        
        if fuel_type in ['95', '98', 'ON', 'ON+', 'LPG']:
        
                if distance>0 and consumption>0 and number_of_people in range (1,6):
                    cost = round((distance * consumption/100 * fuel_prices(fuel_type))/number_of_people,2) 
                    return cost
                else: 
                    raise ValueError
                
        else:
            raise KeyError
    else:
        raise TypeError


distance_1 = 100
consumption_1 = -10
fuel_type_1 = 'ON'
number_of_people_1 = 2


try: 
    cost = travel_cost(distance_1, consumption_1, fuel_type_1, number_of_people_1)
    print(cost)
except ValueError:
        print('Check if the entered data is correct: distance > 0, \
              consumption > 0 and number of people in range [1,5]')
except KeyError:
    try:
        print(travel_cost(distance_1, consumption_1, str(fuel_type_1), number_of_people_1))
    except KeyError:
        print('Check if the fuel has been selected among the given ones: 95, 98, ON, ON+, LPG')
except TypeError:
    try:
        print(travel_cost(float(distance_1), float(consumption_1), fuel_type_1, int(number_of_people_1)))
    except TypeError:
        print('Check if the entered data is correct: distance (float), \
              consumption (float)  and number of people (integer)')
              
distance_1 = '100'
consumption_1 = '10'
fuel_type_1 = 'ON'
number_of_people_1 = '2'

try: 
    cost = travel_cost(distance_1, consumption_1, fuel_type_1, number_of_people_1)
    print(cost)
except ValueError:
        print('Check if the entered data is correct: distance > 0, \
              consumption > 0 and number of people in range [1,5]')
except KeyError:
    try:
        print(travel_cost(distance_1, consumption_1, str(fuel_type_1), number_of_people_1))
    except KeyError:
        print('Check if the fuel has been selected among the given ones: 95, 98, ON, ON+, LPG')
except TypeError:
    try:
        print(travel_cost(float(distance_1), float(consumption_1), fuel_type_1, int(number_of_people_1)))
    except TypeError:
        print('Check if the entered data is correct: distance (float), \
              consumption (float)  and number of people (integer)')

distance_1 = 100
consumption_1 = 10
fuel_type_1 = 'on'
number_of_people_1 = 2

try: 
    cost = travel_cost(distance_1, consumption_1, fuel_type_1, number_of_people_1)
    print(cost)
except ValueError:
        print('Check if the entered data is correct: distance > 0, \
              consumption > 0 and number of people in range [1,5]')
except KeyError:
    try:
        print(travel_cost(distance_1, consumption_1, str(fuel_type_1).upper(), number_of_people_1))
    except KeyError:
        print('Check if the fuel has been selected among the given ones: 95, 98, ON, ON+, LPG')
except TypeError:
    try:
        print(travel_cost(float(distance_1), float(consumption_1), fuel_type_1, int(number_of_people_1)))
    except TypeError:
        print('Check if the entered data is correct: distance (float), \
              consumption (float)  and number of people (integer)')
              
distance_1 = 100
consumption_1 = 10
fuel_type_1 = 95
number_of_people_1 = 2

try: 
    cost = travel_cost(distance_1, consumption_1, fuel_type_1, number_of_people_1)
    print(cost)
except ValueError:
        print('Check if the entered data is correct: distance > 0, \
              consumption > 0 and number of people in range [1,5]')
except KeyError:
    try:
        print(travel_cost(distance_1, consumption_1, str(fuel_type_1).upper(), number_of_people_1))
    except KeyError:
        print('Check if the fuel has been selected among the given ones: 95, 98, ON, ON+, LPG')
except TypeError:
    try:
        print(travel_cost(float(distance_1), float(consumption_1), fuel_type_1, int(number_of_people_1)))
    except TypeError:
        print('Check if the entered data is correct: distance (float), \
              consumption (float)  and number of people (integer)')


def test_fuel_prices():
    """
    Test function for the function fuel_prices
    (The tests are valid on 19/10/2022, fuel prices can change over time.)
    """
    test = fuel_prices('ON')
    assert test == 8.03 , 'Incorrect result'
    print('Correct test. Fuel price: '+str(test)+" zł.")
    
    test = fuel_prices('LPG')
    assert test == 3.04 , 'Incorrect result'
    print('Correct test. Fuel price: '+str(test)+" zł.")
    
    test = fuel_prices('ksdfbie')
    assert test == None , 'Incorrect result'
    print('Correct test. Fuel price: '+str(test)+".")
    
    test = fuel_prices(5)
    assert test == None , 'Incorrect result'
    print('Correct test. Fuel price: '+str(test)+".")
    
test_fuel_prices()        
    
