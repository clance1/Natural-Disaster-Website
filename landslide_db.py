#!/usr/bin/env python3
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="landslide_database")

# This is the landslide database

class landslide_db:
    def __init__(self):
        self.landslides = {}
    
    def load_landslides(self, landslide_file):
        f = open(landslide_file, 'r')
        
        for line in f:
            entry = dict()
            
            line = (line.strip()).split(',')
            lat = line[3]
            lon = line[4]
            index = (lat, lon)
            entry['date'] = line[1]
            entry['year'] = line[1].split('/')[-1]
            entry['category'] = line[2]
            entry['lat'] = lat 
            entry['lon'] = lon 

            if len(line) == 6:
                entry['state'] = line[5]
            else:
                #state = geolocator.reverse("{}, {}".format(lat, lon)).raw['address']['state']
                entry['state'] = ''

            self.landslides[index] = entry
        
        f.close()
        
    def get_landslide(self, lat, lon):
        '''Get a specific landslide info by its id'''
        if (lat, lon) in self.landslides:
            return self.landslides[(lat, lon)]
        else:
            return None
    
    def get_landslide_state(self, state):
        return [landslide for landslide in self.landslides.values() if landslide['state'] == state]

    def get_landslide_year(self, year):
        return [landslide for landslide in self.landslides.values() if landslide['year'] == year]

    def get_landslides(self):
        '''return all the landslides in the database'''
        return self.landslides

    def set_landslide(self, lat, lon, landslide_info):
        self.landslides[(lat, lon)] = landslide_info
    
    def delete_landslide(self, lat, lon):
        if (lat, lon) in self.landslides:
            del self.landslides[(lat, lon)]

    def delete_landslides(self):
        self.landslides.clear()

    def reset_landslide(self):
        self.landslides.clear()
        self.load_landslides("../landslides/landslide_formatted.csv")
        

if __name__ == '__main__':
    ldb = landslide_db()

    ldb.load_landslides("landslides/landslide_formatted.csv")
    #print(ldb.get_landslide('41.9738', '-91.6056'))
    #print(ldb.get_landslide_state('IN'))
    print(ldb.get_landslide_year('2010'))
