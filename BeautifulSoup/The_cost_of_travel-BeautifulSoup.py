"""
Autor: Marta Skowron

NOTE!: Tests in the testing function were performed on October 15, 2022. Prices
fuels may change and then the data for some cases should be corrected.
At the same time, I declare that on that day all tests passed.

Python Tutorial: Web Scraping with BeautifulSoup and Requests
https://www.youtube.com/watch?v=ng2o98k983k
"""
from bs4 import BeautifulSoup
import requests

def fuel_prices(fuel_type):
    """
    The function for the given name of fuel returns its average price in Poland
    according to data from the website https://www.autocentrum.pl/paliwa/ceny-paliw/.
    
    Arg:
        fuel_type (str): type of the fuel ('95', '98', 'ON', 'ON+', 'LPG')
    Return:
        price (float)/None: price of fuel in PLN per liter or None if the user 
                            provided wrong data
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
        and (type(number_of_people) is int) and \
        fuel_type in ['95', '98', 'ON', 'ON+', 'LPG']:
        
            if distance>0 and consumption>0 and number_of_people in range (1,6):
                cost = round((distance * consumption/100 * fuel_prices(fuel_type))/number_of_people,2) 
                return cost
            else: 
                return None
    else:
        return None


def test_fuel_prices():
    """
    Test function for the function fuel_prices
    (The tests are valid on 15/10/2022, fuel prices can change over time.)
    """
    test = fuel_prices('ON')
    assert test == 7.98 , 'Incorrect result'
    print('Correct test. Fuel price: '+str(test)+" zł.")
    
    test = fuel_prices('LPG')
    assert test == 3.11 , 'Incorrect result'
    print('Correct test. Fuel price: '+str(test)+" zł.")
    
    test = fuel_prices('ksdfbie')
    assert test == None , 'Incorrect result'
    print('Correct test. Fuel price: '+str(test)+".")
    
    test = fuel_prices(5)
    assert test == None , 'Incorrect result'
    print('Correct test. Fuel price: '+str(test)+".")
    
test_fuel_prices()
    
def test_travel_cost():
    
    """
    Test function for the function travel_cost
    (The tests are valid on 15/10/2022, fuel prices can change over time.)
    """
    test = travel_cost(100, 5, 'ON', 2)
    assert test == 19.95 , 'Incorrect result'
    print('Correct test. Fuel price per person: '+str(test)+" zł.")
    
    test = travel_cost(-100, 5, 'ON', 2)
    assert test == None , 'Incorrect result'
    print('Correct test. Fuel price per person: '+str(test)+".")
    
    test = travel_cost(150, 5.5, '95', 5)
    assert test == 11.20 , 'Incorrect result'
    print('Correct test. Fuel price per person: '+str(test)+" zł.")
    
    test = travel_cost(150, 5, '95', 0)
    assert test == None , 'Incorrect result'
    print('Correct test. Fuel price per person: '+str(test)+".")
    
    test = travel_cost(150, 5, '95', 2.5)
    assert test == None , 'Incorrect result'
    print('Correct test. Fuel price per person: '+str(test)+".")
    
    test = travel_cost(150, 5, 'jwkndiwu', 2)
    assert test == None , 'Incorrect result'
    print('Correct test. Fuel price per person: '+str(test)+".")
    
test_travel_cost()
    
    
    
    
    
    
    
    
    
    