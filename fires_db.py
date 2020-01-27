#############################################
#               fires_db.py                #
#   This api allows access to the data      #
#   from all of the wildfires across the    #
#   United States from 2000 - 2017          #
#############################################

import pandas as pd
import pprint

class FiresApi:

    def __init__(self):
        self.fires = dict()

    # Fills the data
    def load_fires(self, file):
        # Create dictionary of fires
        df = pd.read_csv(file)
        for index, fire in df.iterrows():
            entry = dict()

            index = (str(fire[5]), str(fire[6]))
            entry['id'] = fire[0]
            entry['start_doy'] = str(fire[2])
            entry['end_doy'] = str(fire[3])
            entry['category'] = fire[4]
            entry['latitude'] = str(fire[5])
            entry['longitude'] = str(fire[6])
            entry['year'] = str(fire[1])
            entry['state'] = fire[7]

            self.fires[index] = entry
    # Returns all the data
    def get_all_fires(self):
        return self.fires

    # Returns a dictionary of all of the fire data for the inputted state
    def get_state_fires(self, state):
        return [fire for fire in self.fires.values() if fire['state'] == state]

    # Returns a dictionary of all of the data for a specific year
    def get_year_fires(self, year):
        return [fire for fire in self.fires.values() if fire['year'] == year]

    def get_category_fires(self, category):
        return [fire for fire in self.fires.values() if fire['category'] == category]

    # Get a fire by a specific latitude and longitude
    def get_lat_long_fire(self, latitude, longitude):
        latitude = str(latitude)
        longitude = str(longitude)
        pprint('({}, {})'.format(latitude, longitude))
        if (latitude, longitude) in self.fires:
            return self.fires[(latitude, longitude)]
        else:
            return None

    def set_fire(self, latitude, longitude, fire_info):
        try:
            self.fires[(latitude, longitude)] = fire_info
            return True
        except Exception:
            return False

    def delete_fire(self, lat, lon):
        if (lat, lon) in self.fires:
            del self.fires[(lat, lon)]

    def delete_fires(self):
        self.fires.clear()

    def reset_fire(self):
        self.fires.clear()
        self.load_fires("fires/fires3.csv")
