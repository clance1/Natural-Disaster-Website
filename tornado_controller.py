# Aemile Donoghue
# tornado_controller.py

import cherrypy
import re, json
from _natural_disasters_database import _natural_disasters_database

class TornadoController(object):

    def __init__(self, nddb=None):
        if nddb is None:
            self.nddb = _natural_disasters_database()
        else:
            self.nddb = nddb

        self.nddb.tornadoes.load_tornadoes('tornadoes/tornadoes.json')

    def GET_ALL(self):
        try:
            tornado_list = self.nddb.tornadoes.get_all_tornadoes()
            # return the stringified dictionary of all tornadoes as the value of 'tornadoes' and a success message
            output = {"tornadoes" : str(tornado_list)}
            output["result"] = "success"
        except Exception as ex:
            output = {"result" : "error", "message" : str(ex)}
        return json.dumps(output)

    def GET_YEAR(self, year):
        output = dict()
        try:
            # return the stringified dictionary of all tornadoes as the value of 'tornadoes' and a success message
            data = self.nddb.tornadoes.get_tornadoes_year(year)
            output["tornadoes"] = str(data)
            output["result"] = "success"
        except Exception as ex:
            output["result"] = "error"
            output["message"] = str(ex)
        return json.dumps(output)

    def GET_STATE(self, state):
        output = dict()
        try:
            # return the stringified dictionary of all tornadoes as the value of 'tornadoes' and a success message
            data = self.nddb.tornadoes.get_tornadoes_state(state)
            output["tornadoes"] = str(data)
            output["result"] = "success"
        except Exception as ex:
            output["result"] = "error"
            output["message"] = str(ex)
        return json.dumps(output)

    def POST_TORNADO(self):
        output = {"result": "success"}

        try:
            data = cherrypy.request.body.read()
            tornado_dict = json.loads(data.decode('utf-8'))
            
            # Create a tornado using the data from the request body as the value of the new tornado to add
            # to the natural_disaster_database 
            begin_year = tornado_dict["begin_year"]
            begin_month = tornado_dict["begin_month"]
            begin_day = tornado_dict["begin_day"]
            begin_time = tornado_dict["begin_time"]
            end_year = tornado_dict["end_year"]
            end_month = tornado_dict["end_month"]
            end_day = tornado_dict["end_day"]
            end_time = tornado_dict["end_time"]
            state = tornado_dict["state"]
            event_id = tornado_dict["event_id"]
            cz_name = tornado_dict["cz_name"]
            begin_lat = tornado_dict["begin_lat"]
            begin_lon = tornado_dict["begin_lon"]
            end_lat = tornado_dict["end_lat"]
            end_lon = tornado_dict["end_lon"]
            tor_F_scale = tornado_dict["tor_F_scale"]

            self.nddb.tornadoes.set_tornado(begin_lat, begin_lon, end_lat, end_lon, begin_year, begin_month, \
                    begin_day,begin_time, end_year, end_month, end_day, end_time, state, event_id,\
                    cz_name, tor_F_scale)
            #output['key'] = str((begin_key, end_key))

            
        except Exception as ex:
            output["result"] = "error"
            output["message"] = str(ex)
        return json.dumps(output)


