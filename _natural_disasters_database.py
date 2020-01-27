#!/usr/bin/env python3

import json
import pprint
from tornado_db import tornado_db
from meteor_db import meteor_db
from fires_db import FiresApi
from landslide_db import landslide_db

class _natural_disasters_database(object):

    def __init__(self):
        print("Loading database...")
        print("Loading tornadoes...")
        self.tornadoes = tornado_db()
        self.tornadoes.load_tornadoes('tornadoes/tornadoes_short.json')
        #self.tornadoes.load_tornadoes('tornadoes/tornadoes_2015.json')
        #self.tornadoes.load_tornadoes('tornadoes/tornadoes_2018.json')
        print("Loading meteors...")
        self.meteors = meteor_db()
        self.meteors.load_meteors('meteors/output.json')
        print("Loading fires...")
        self.fires = FiresApi()
        self.fires.load_fires('fires/fires3.csv')
        print("Loading landslides...")
        self.landslides = landslide_db()
        self.landslides.load_landslides('landslides/landslide_formatted.csv')


    def reset_data(self):
        self.tornadoes = tornado_db()
        self.tornadoes.load_tornadoes('tornadoes/tornadoes.json')
        self.meteors = meteor_db()
        self.meteors.load_meteors('meteors/meteor_data.json')
        self.fires = FiresApi()
        self.fires.load_fires('fires/fires2.csv')
        self.landslides = landslide_db()
        self.landslides.load_landslides('landslides/landslide_formatted.csv')

if __name__ == "__main__":
    nd_db = _natural_disasters_database()
