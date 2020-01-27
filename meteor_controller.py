#!/usr/bin/env python3

# IMPORTS

import cherrypy
import re, json
from _natural_disasters_database import _natural_disasters_database

# CLASS

class MeteorController(object):

    def __init__(self, nddb):
        self.nddb = nddb

    def GET_ALL(self):

        output = dict()
        # Return json of all meteors in the natrual_disaster_database
        entries = [json.loads(self.GET_KEY(location)) for location in self.nddb.meteors.meteors.keys()]

        try:
            output['meteors'] = entries
            output['result'] = 'success'
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)

    def GET_KEY(self, key):

        output = dict()
        # return json of the meteor whose key matches the desired key from the GET
        try:
            value = self.nddb.meteors.get_meteor(key)
            if value is not None:
                output['name'] = value['name']
                output['nametype'] = value['nametype']
                output['recclass'] = value['recclass']
                output['mass'] = value['mass']
                output['fall'] = value['fall']
                output['year'] = value['year']
                output['latitude'] = value['latitude']
                output['longitude'] = value['longitude']
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

        output = dict()
        key = str(key)

        # Create a list of all of the meteors whose year attribute matches the desired year and return the json ot it
        entries = [entry for entry in json.loads(self.GET_ALL())['meteors'] if entry['year'] == key]

        try:
            output['meteors'] = entries
            output['result'] = 'success'
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)

    def GET_STATE(self, key):

        output = dict()
        key = str(key)

        # Create a list of all of the meteors whose state attribute matches the desired state and return the json of it
        entries = [entry for entry in json.loads(self.GET_ALL())['meteors'] if entry['state'] == key]

        try:
            output['meteors'] = entries
            output['result'] = 'success'
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)

    def POST(self):

        output = dict()

        data = cherrypy.request.body.read()
        print(data)
        value = json.loads(data)
        # Create and add a meteor with the data from the request body as the value, and the id as the key 
        # and store it in the natural_disasters_database data
        try:
            name = value['name']
            x_id = value['id']
            nametype = value['nametype']
            recclass = value['recclass']
            mass = value['mass']
            fall = value['fall']
            year = value['year']
            longitude = value['longitude']
            latitude = value['latitude']
            state = value['state']

            self.nddb.meteors.set_meteor(x_id, [name, nametype, recclass, mass, fall, year, latitude, longitude, state])
            output['id'] = x_id
            output['result'] = 'success'
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)
