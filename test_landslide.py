import unittest
import requests
import json

class TestLandslide(unittest.TestCase):

        SITE_URL = 'http://student04.cse.nd.edu:51092' 
        LANDSLIDE_URL = SITE_URL + '/landslides/'

        def reset_data(self):
            r = requests.delete(self.LANDSLIDE_URL)

        def is_json(self, resp):
            try:
                json.loads(resp)
                return True
            except ValueError:
                return False

        def test_landslide_get_year(self):
            self.reset_data()

            key = '2012'
            r = requests.get(self.LANDSLIDE_URL + 'year/' + key)

            self.assertTrue(self.is_json(r.content.decode('utf-8')))
            resp = json.loads(r.content.decode('utf-8'))
            self.assertEqual(resp['result'], 'success')

            landslides = resp['landslides']
            l = landslides[0]
            self.assertEqual(l['id'], '4344')
            self.assertEqual(l['date'], '5/1/2012')
            self.assertEqual(l['year'], '2012')
            self.assertEqual(l['category'], 'Medium')
            self.assertEqual(l['lat'], '39.1229')
            self.assertEqual(l['lon'], '-84.4481')
            self.assertEqual(l['state'], 'OH')

        def test_landslide_get_state(self):
            self.reset_data()

            key = 'OH'
            r = requests.get(self.LANDSLIDE_URL + 'state/' + key)

            self.assertTrue(self.is_json(r.content.decode('utf-8')))
            resp = json.loads(r.content.decode('utf-8'))
            self.assertEqual(resp['result'], 'success')

            landslides = resp['landslides']
            l = landslides[0]
            self.assertEqual(l['id'], '3409')
            self.assertEqual(l['date'], '4/25/2011')
            self.assertEqual(l['year'], '2011')
            self.assertEqual(l['category'], 'Small')
            self.assertEqual(l['lat'], '39.1369')
            self.assertEqual(l['lon'], '-84.7904')
            self.assertEqual(l['state'], 'OH')

        def test_landslide_get_all(self):
            self.reset_data()

            r = requests.get(self.LANDSLIDE_URL)

            self.assertTrue(self.is_json(r.content.decode('utf-8')))
            resp = json.loads(r.content.decode('utf-8'))
            self.assertEqual(resp['result'], 'success')

            landslides = resp['landslides']
            l = landslides[0]
            self.assertEqual(l['id'], '5510')
            self.assertEqual(l['date'], '9/12/2013')
            self.assertEqual(l['year'], '2013')
            self.assertEqual(l['category'], 'Medium')
            self.assertEqual(l['lat'], '39.8839')
            self.assertEqual(l['lon'], '-105.3033')
            self.assertEqual(l['state'], 'CO')

if __name__ == "__main__":
        unittest.main()

