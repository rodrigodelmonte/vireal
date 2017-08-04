from app import app, db
import json
import unittest

class SpotipposTestCase(unittest.TestCase):


    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

        body = [
                   {
                       "baths": 4,
                       "beds": 5,
                       "description": "Ut officia elit laboris nostrud exercitation deserunt velit. Ullamco duis sint anim non fugiat esse cillum commodo mollit sit minim ex.",
                       "price": 1684000,
                       "squareMeters": 166,
                       "title": "Imovel codigo 4, com 5 quartos e 4 banheiros.",
                       "x": 252,
                       "y": 868
                   },
                   {
                       "baths": 1,
                       "beds": 2,
                       "description": "Incididunt dolor ad proident incididunt culpa nostrud ea deserunt dolor. Tempor eiusmod elit esse adipisicing reprehenderit eiusmod mollit ex velit sunt dolor sunt.",
                       "price": 560000,
                       "squareMeters": 54,
                       "title": "Imovel codigo 5, com 2 quartos e 1 banheiros.",
                       "x": 34,
                       "y": 660
                   },
                   {
                       "baths": 4,
                       "beds": 5,
                       "description": "Enim amet Lorem exercitation consectetur sunt nulla incididunt aliqua nisi do voluptate laborum. Est mollit consectetur qui velit consequat reprehenderit et adipisicing occaecat labore labore ipsum do aliquip.",
                       "price": 1354000,
                       "squareMeters": 131,
                       "title": "Imovel codigo 7, com 5 quartos e 4 banheiros.",
                       "x": 38,
                       "y": 664
                   }
            ]

        for b in body:
            self.app.post('/properties', data=json.dumps(b), content_type='application/json')

    def tearDown(self):
        pass

    def test_create_propertie(self):

        body = {
                "x": 222,
                "y": 444,
                "title": "Imovel codigo 1, com 5 quartos e 4 banheiros",
                "price": 1250000,
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                "beds": 4,
                "baths": 3,
                "squareMeters": 210
            }

        result = self.app.post('/properties', data=json.dumps(body), content_type='application/json')
        self.assertEqual(result.data, '{\n  "message": "Propertie success created! Id: 4"\n}\n')
        self.assertEqual(result.status_code, 200)

    def test_create_propertie_empty_data(self):

        result = self.app.post('/properties', content_type='application/json')
        self.assertEqual(result.data, '{\n  "message": "Please send a json body!?"\n}\n')
        self.assertEqual(result.status_code, 200)

    def test_find_propertie(self):

        result = self.app.get('/properties/1', content_type='application/json')
        data = json.loads(result.get_data(as_text=True))
        self.assertEqual(data['x'], 252)
        self.assertEqual(data['y'], 868)
        self.assertEqual(data['title'], "Imovel codigo 4, com 5 quartos e 4 banheiros.")
        self.assertEqual(data['price'], 1684000)
        self.assertEqual(data['description'], "Ut officia elit laboris nostrud exercitation deserunt velit. Ullamco duis sint anim non fugiat esse cillum commodo mollit sit minim ex.")
        self.assertEqual(data['beds'], 5)
        self.assertEqual(data['baths'], 4)
        self.assertEqual(data['squareMeters'], 166)
        self.assertEqual(data['province'], "Gode")
        self.assertEqual(result.status_code, 200)

    def test_find_propertie_not_exists(self):
        result = self.app.get('/properties/100', content_type='application/json')
        self.assertEqual(result.data, '{\n  "message": "id not exists!"\n}\n')
        self.assertEqual(result.status_code, 200)

    def test_find_properties_by_query_string(self):

        result = self.app.get('/properties?ax=0&ay=1000&bx=600&by=500', content_type='application/json')
        data = json.loads(result.get_data(as_text=True))
        self.assertEqual(data['foundProperties'], 3)
        self.assertEqual(result.status_code, 200)

    def test_x_invalid(self):

        body = {
                "x": 2000,
                "y": 444,
                "title": "Imovel codigo 1, com 5 quartos e 4 banheiros",
                "price": 1250000,
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                "beds": 4,
                "baths": 3,
                "squareMeters": 210
            }
        result = self.app.post('/properties', data=json.dumps(body), content_type='application/json')
        self.assertEqual(result.data, '{\n  "message": "Valor de x invalido."\n}\n')
        self.assertEqual(result.status_code, 200)

    def test_y_invalid(self):

        body = {
                "x": 222,
                "y": 4440,
                "title": "Imovel codigo 1, com 5 quartos e 4 banheiros",
                "price": 1250000,
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                "beds": 4,
                "baths": 3,
                "squareMeters": 210
            }
        result = self.app.post('/properties', data=json.dumps(body), content_type='application/json')
        self.assertEqual(result.data, '{\n  "message": "Valor de y invalido."\n}\n')
        self.assertEqual(result.status_code, 200)

    def test_debs_invalid(self):

        body = {
                "x": 222,
                "y": 444,
                "title": 0,
                "price": 1250000,
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                "beds": 10,
                "baths": 3,
                "squareMeters": 210
            }
        result = self.app.post('/properties', data=json.dumps(body), content_type='application/json')
        self.assertEqual(result.data, '{\n  "message": "Valor de beds invalido."\n}\n')
        self.assertEqual(result.status_code, 200)

    def test_baths_invalid(self):

        body = {
                "x": 222,
                "y": 444,
                "title": 0,
                "price": 1250000,
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                "beds": 4,
                "baths": 30,
                "squareMeters": 210
            }
        result = self.app.post('/properties', data=json.dumps(body), content_type='application/json')
        self.assertEqual(result.data, '{\n  "message": "Valor de baths invalido."\n}\n')
        self.assertEqual(result.status_code, 200)

    def test_squareMeters_invalid(self):

        body = {
                "x": 222,
                "y": 444,
                "title": 0,
                "price": 1250000,
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                "beds": 4,
                "baths": 3,
                "squareMeters": 2100
            }
        result = self.app.post('/properties', data=json.dumps(body), content_type='application/json')
        self.assertEqual(result.data, '{\n  "message": "Valor de squareMeters invalido."\n}\n')
        self.assertEqual(result.status_code, 200)

if __name__  == '__main__':
    unittest.main()
