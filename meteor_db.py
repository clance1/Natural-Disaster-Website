#!/usr/bin/env python3

import json
import certifi
import ssl
import geopy.geocoders
from geopy.geocoders import Nominatim

class meteor_db(object):

    ctx = ssl.create_default_context(cafile=certifi.where())
    geopy.geocoders.options.default_ssl_context = ctx

    def __init__(self):
        self.meteors   = dict()

    def load_meteors(self, meteor_file):
        f = open(meteor_file)
        meteor_data = json.load(f)
        
        for meteor in meteor_data:
            
            meteor_dict = dict()
            meteor_dict['name'] = meteor['name']
            meteor_dict['nametype'] = meteor['nametype']
            meteor_dict['recclass'] = meteor['recclass']
            meteor_dict['mass'] = meteor['mass']
            meteor_dict['fall'] = meteor['fall']
            meteor_dict['year'] = meteor['year'][0:4] # relevant year digits
            meteor_dict['latitude'] = meteor['latitude']
            meteor_dict['longitude'] = meteor['longitude']
            meteor_dict['state'] = meteor['state']
            self.meteors[meteor['id']] = meteor_dict
        
        f.close()

    def get_meteor(self, x_id):
        if x_id in self.meteors:
            return self.meteors[x_id]

        return None

    def get_meteor_name(self, name):
        return [(location, meteor) for location, meteor in self.meteors.items() if meteor['name'] == name]

    def get_meteors_y(self, year):
        return [meteor for meteor in self.meteors.values() if meteor['year'] == year]

    def get_meteors_s(self, state):
        return [meteor for meteor in self.meteors.values() if meteor['state'] == state]

    def set_meteor(self, key, data):
        entry_dict = dict()
        entry_dict['name'] = data[0]
        entry_dict['nametype'] = data[1]
        entry_dict['recclass'] = data[2]
        entry_dict['mass'] = data[3]
        entry_dict['fall'] = data[4]
        entry_dict['year'] = data[5]
        entry_dict['latitude'] = data[6]
        entry_dict['longitude'] = data[7]
        entry_dict['state'] = data[8]

        self.meteors[key] = entry_dict

    def delete_meteor(self, x_id):
        if x_id in self.meteors:
            del self.meteors[x_id]

    def print_meteors(self):
        for location, details in self.meteors.items():
            print("ID: {} \nDetails: {}".format(location, details))

if __name__ == "__main__":
    mdb = meteor_db()
    
    mdb.load_meteors('meteors/meteor_data.json')
    #mdb.print_meteors()
    print(mdb.get_meteors_s('California'))
