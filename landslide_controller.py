#!/usr/bin/env python3

import cherrypy
import json
from _natural_disasters_database import _natural_disasters_database

class LandslideController(object):

    def __init__(self, nddb = None):
        if nddb is None:
            self.nddb = _natural_disasters_database
        else:
            self.nddb = nddb
        
        self.nddb.landslides.load_landslides('landslides/landslide_formatted.csv');

    def POST(self):
        '''Add new landslide into database'''
        # Default Outut
        output = {'result': 'success'}

        # extract msg from body
        data = cherrypy.request.body.read()
        data = json.loads(data)

        # Try - except
        try:
            date = data['date']
            year = data['year']
            category = data['category']
            lat = data['lat']
            lon = data['lon']
            state = data['state']
            self.nddb.landslides.set_landslide(lat, lon, 
                {'date': date, 
                 'year': year,
                 'category': category,
                 'lat': lat,
                 'lon': lon,
                 'state': state})

        except Exception as ex:
            output['result']        = 'error'
            output['message']       = str(ex)

        return json.dumps(output)

    def GET_YEAR(self, key):
        '''Get the landslides that happened in the given year'''
        # Default Outut
        output = {'result': 'success'}

        # Try - except
        try:
            landslides = self.nddb.landslides.get_landslide_year(key)
            output['landslides'] = landslides
        except Exception as ex:
            output['result']        = 'error'
            output['message']       = str(ex)

        return json.dumps(output)

    def GET_STATE(self, key):
        '''Get the landslides that happened in the given state'''
        # Default Outut
        output = {'result': 'success'}

        # Try - except
        try:
            landslides = self.nddb.landslides.get_landslide_state(key)
            output['landslides'] = landslides
        except Exception as ex:
            output['result']        = 'error'
            output['message']       = str(ex)

        return json.dumps(output)

    def GET_ALL(self):
        '''Get all the landslides in the database'''
        # Default Outut
        output = {'result': 'success'}

        # Try - except
        try:
            ans = []
            for key in self.nddb.landslides.landslides:
                ans.append(self.nddb.landslides.landslides[key])
            output['landslides'] = ans

        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)
