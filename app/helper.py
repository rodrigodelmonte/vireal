import json
from schema import Schema, And, Use


province_json = open('provinces.json').read()
provinces = json.loads(province_json)

def discover_province(x,y):

    for province in provinces:
        ax = provinces[province]['boundaries']['upperLeft']['x']
        ay = provinces[province]['boundaries']['upperLeft']['y']
        bx = provinces[province]['boundaries']['bottomRight']['x']
        by = provinces[province]['boundaries']['bottomRight']['y']

        if x >= ax and x <= bx and y <= ay and y >= by:
            return province


#Schema validator for request body.
schema = Schema([{
                'x': And(Use(int), lambda x: 0 <= x <= 1400, error='Valor de x invalido.'),
                'y': And(Use(int), lambda y: 0 <= y <= 1000, error='Valor de y invalido.'),
                'title': Use(str, error='Valor de title invalido.'),
                'price': Use(int, error='Valor de price invalido.'),
                'description': Use(str, error='Valor de description invalido.'),
                'beds': And(Use(int), lambda n: 1 <= n <= 5, error='Valor de beds invalido.'),
                'baths': And(Use(int), lambda n: 1 <= n <= 4, error='Valor de baths invalido.'),
                'squareMeters': And(Use(int), lambda n: 20 <= n <= 240, error='Valor de squareMeters invalido.')
                }])