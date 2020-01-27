#!/usr/bin/env python3

from _natural_disasters_database import _natural_disasters_database
import unittest

class TestNDDatabase(unittest.TestCase):
    ''' Unit tests for Paradigms OO API '''

    nd_db = _natural_disasters_database()

    def reset_data(self):
        
        self.nd_db.reset_data()

    def test_landslides(self):
        print("\nTesting landslide database...")

        self.reset_data()

        # Test getter
        landslide = self.nd_db.landslides.get_landslide(44.1547, -93.9816)
        self.assertEqual(landslide['id'], '6066')
        self.assertEqual(landslide['date'], '6/18/2014')
        self.assertEqual(landslide['category'], 'Small')

        # Test delete
        self.nd_db.landslides.delete_landslide(44.1547, -93.9816)
        landslide = self.nd_db.landslides.get_landslide(44.1547, -93.9816)
        self.assertEqual(landslide, None)

        # Test setter
        landslide_info = {
            'id': '6066',
            'date': '6/18/2014',
            'category': 'Small',
            'lat': 44.1547,
            'lon': -93.9816
        }
        self.nd_db.landslides.set_landslide(44.1547, -93.9816, landslide_info)
        landslide = self.nd_db.landslides.get_landslide(44.1547, -93.9816)
        self.assertEqual(landslide['id'], '6066')
        self.assertEqual(landslide['date'], '6/18/2014')
        self.assertEqual(landslide['category'], 'Small')

        # Test deleting the entire db
        self.nd_db.landslides.delete_landslides()
        self.assertEqual(self.nd_db.landslides.landslides, {})
    
    def test_meteors(self):
        print("\nTesting metoer database...")
        
        self.reset_data()

        meteors = self.nd_db.meteors.get_meteors_y('2001')
        self.assertEqual(meteors[1]['name'], 'Beni M\'hira')

        meteor = self.nd_db.meteors.get_meteor('34.45', '132.38333')
        self.assertEqual(meteor['name'], 'Hiroshima')
        self.assertEqual(meteor['mass'], '414')

        self.nd_db.meteors.delete_meteor('34.45', '132.38333')
        meteor = self.nd_db.meteors.get_meteor('34.45', '132.38333')
        self.assertEqual(meteor, None)

        self.reset_data()
        
    def test_fires(self):
        print("\nTesting fire database...")
        self.reset_data()

        fires = self.nd_db.fires.get_state_category_data('CA', 'D')
        self.assertEqual(fires[2006][0]['latitude'], 2453911.5)

        fires = self.nd_db.fires.get_year_data(2006)
        self.assertEqual(fires['AZ'][60]['longitude'], 2453786.5)

        fires = self.nd_db.fires.get_state_data('OH')
        self.assertEqual(fires[2005][0]['category'],  'E')

        fires = self.nd_db.fires.get_year_state_data('TX', 2006)
        self.assertEqual(fires[41]['longitude'],  2453830.5)

        self.reset_data()
        
    def test_tornadoes(self):
        print("\nTesting tornado database...")

        self.reset_data()
        
        tornado = self.nd_db.tornadoes.get_tornado(37.699,-78.789)
        self.assertEqual(tornado['begin_year'], 2019.04)
        self.assertEqual(tornado['begin_month'], 4)

        self.nd_db.tornadoes.set_tornado('35.6000', '-100.000', '35.0000', '-100.000', '2019.04', '1', '1', '2019.04', \
                                        '1', '1', '1800', '1820', 'TEXAS', '000000', 'TEST', 'EF3')
        tornado = self.nd_db.tornadoes.get_tornado('35.6000', '-100.000')
        self.assertEqual(tornado['cz_name'], 'TEST')

        tornadoes_2015 = self.nd_db.tornadoes.get_tornadoes_year(2019.04)
        texas_tornadoes = self.nd_db.tornadoes.get_tornadoes_state('TEXAS')
        texas_2015_tornadoes = self.nd_db.tornadoes.get_tornadoes_year_state(2019.04, 'TEXAS')
        self.assertEqual(len(tornadoes_2015), 325)
        self.assertEqual(len(texas_tornadoes), 168)
        self.assertEqual(len(texas_2015_tornadoes), 39)


        self.nd_db.tornadoes.delete_tornado('34.89', '-98.3159')
        tornado = self.nd_db.tornadoes.get_tornado('34.89', '-98.3159')
        self.assertEqual(tornado,None)

if __name__ == '__main__':
    unittest.main()
