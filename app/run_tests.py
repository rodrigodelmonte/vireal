from app import app, db
import json
import unittest

class SpotipposTestCase(unittest.TestCase):

    global body
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

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        pass

    def test_create_propertie(self):

        result = self.app.post('/properties',
                                data=json.dumps(body),
                                content_type='application/json')
        self.assertEqual(result.data, '{\n  "message": "Propertie success created! Id: 1"\n}\n')
        self.assertEqual(result.status_code, 200)

    def test_create_propertie_empty_data(self):

        result = self.app.post('/properties',
                                content_type='application/json')
        self.assertEqual(result.data, '{\n  "message": "Please send a json body!?"\n}\n')
        self.assertEqual(result.status_code, 200)

    def test_find_propertie(self):

        self.app.post('/properties',
                                data=json.dumps(body),
                                content_type='application/json')
        result = self.app.get('/properties/1',
                                content_type='application/json')
        data = json.loads(result.get_data(as_text=True))
        self.assertEqual(data['x'], 222)
        self.assertEqual(data['y'], 444)
        self.assertEqual(data['title'], "Imovel codigo 1, com 5 quartos e 4 banheiros")
        self.assertEqual(data['price'], 1250000)
        self.assertEqual(data['description'], "Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
        self.assertEqual(data['beds'], 4)
        self.assertEqual(data['baths'], 3)
        self.assertEqual(data['squareMeters'], 210)
        self.assertEqual(data['province'], "Scavy")
        self.assertEqual(result.status_code, 200)


if __name__  == '__main__':
    unittest.main()
