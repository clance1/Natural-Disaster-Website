# Carson Lance
# fires_controller.py

import cherrypy
import re, json
from _natural_disasters_database import _natural_disasters_database
import pprint

class FiresController(object):
    def __init__(self, nddb=None):
        # Make sure that there is an instance of natural_disasters_database
        if nddb is None:
            self.nddb = _natural_disasters_database()
        else:
            self.nddb = nddb

        self.nddb.fires.load_fires('fires/fires3.csv')

    def GET_FIRES(self):
        output = dict()
        # Return ALL fires for every key in the natural_disasters_database_fires
        entries = [json.loads(self.GET_KEY(location)) for location in self.nddb.fires.fires.keys()]
        try:
            output['fires'] = entries
            output['result'] = 'success'
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)

    def GET_KEY(self, key):
        # Get the specific fire for that lat,lon key and return its json
        output = dict()
        try:
            value = self.nddb.fires.get_lat_long_fire(key[0], key[1])
            if value is not None:
                output['name'] = value['name']
                output['id'] = value['id']
                output['year'] = value['year']
                output['latitude'] = key[0]
                output['longitude'] = key[1]
                output['state'] = value['state']
                output['result'] = 'success'
            else:
                output['result'] = 'error'
                output['message'] = 'None type value associated with requested key'
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = 'Key not found'
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)

    def GET_YEAR(self, key):
        # Default Outut
        output = {'result': 'success'}
        key = int(key)

        entries = self.nddb.fires.get_year_fires(key)
        try:
            output['fires'] = entries
            output['result'] = 'success'

        except Exception as ex:
            output['result']        = 'error'
            output['message']       = str(ex)
        return json.dumps(output)

    def GET_STATE(self, key):
        output = {'result': 'success'}
        entries = self.nddb.fires.get_state_fires(key)
        # Try - except
        try:
            output['fires'] = entries
            output['result'] = 'success'
        except Exception as ex:
            output['result']        = 'error'
            output['message']       = str(ex)

        return json.dumps(output)

    def POST_FIRE(self):
        data = cherrypy.request.body.read()
        data = json.loads(data)
        print('DATA POSTING')
        print(data)
        # Create a fire whose key is the lat, lon and whose value is the fire's data from the request
        if self.nddb.fires.set_fire(data['latitude'], data['longitude'], data):
            output = {'result': 'success'}
        else:
            output = {'result': 'failure'}
        return json.dumps(output)
