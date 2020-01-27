#!/usr/bin/env python3

# IMPORTS

import cherrypy
from _natural_disasters_database import _natural_disasters_database
from meteor_controller import MeteorController
from tornado_controller import TornadoController
from fires_controller import FiresController
from landslide_controller import LandslideController
from geopy.geocoders import Nominatim

# CORS
class OptionsController:
	def OPTIONS(self, *args, **kwargs):
		return ""

# FUNCTIONS
def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
    cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE, OPTIONS"
    cherrypy.response.headers["Access-Control-Allow-Credentials"] = "true"

def start_service():

    # Database loading

    nddb = _natural_disasters_database() # should load automatically

    # Controller Specifications

    m_con = MeteorController(nddb)
    t_con = TornadoController(nddb)
    f_con = FiresController(nddb)
    l_con = LandslideController(nddb)
    o_con = OptionsController()

    dispatcher = cherrypy.dispatch.RoutesDispatcher()

    # Dispatcher Connections

    # Meteors
    dispatcher.connect('meteor_get_all', '/meteors/', controller=m_con, action = 'GET_ALL', conditions=dict(method=['GET']))
    dispatcher.connect('meteor_get_year', '/meteors/year/:key', controller=m_con, action = 'GET_YEAR', conditions=dict(method=['GET']))
    dispatcher.connect('meteor_get_year_options', '/meteors/year/:key', controller=o_con, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('meteor_get_state', '/meteors/state/:key', controller=m_con, action = 'GET_STATE', conditions=dict(method=['GET']))
    dispatcher.connect('meteor_get_state_options', '/meteors/state/:key', controller=o_con, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('meteor_post', '/meteors/', controller=m_con, action = 'POST', conditions=dict(method=['POST']))
    dispatcher.connect('meteor_options', '/meteors/', controller=o_con, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))

    # Tornadoes
    dispatcher.connect('tornado_get_all', '/tornadoes/', controller=t_con, action = 'GET_ALL', conditions=dict(method=['GET']))
    dispatcher.connect('tornado_post', '/tornadoes/', controller=t_con, action = 'POST_TORNADO', conditions=dict(method=['POST']))
    dispatcher.connect('tornado_options', '/tornadoes/', controller=o_con, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('tornado_get_year', '/tornadoes/year/:year', controller=t_con, action = 'GET_YEAR', conditions=dict(method=['GET']))
    dispatcher.connect('tornado_get_state_options', '/tornadoes/state/:year', controller=o_con, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('tornado_get_state', '/tornadoes/state/:state', controller=t_con, action = 'GET_STATE', conditions=dict(method=['GET']))
    dispatcher.connect('tornado_get_state_options', '/tornadoes/state/:state', controller=o_con, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    # Fires
    dispatcher.connect('fires_get_all', '/fires/', controller=f_con, action='GET_ALL', conditions=dict(method=['GET']))
    dispatcher.connect('fires_options', '/fires/', controller=o_con, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('fires_get_year', '/fires/year/:key', controller=f_con, action = 'GET_YEAR', conditions=dict(method=['GET']))
    dispatcher.connect('fires_get_year_options', '/fires/year/:key', controller=o_con, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('fires_get_state', '/fires/state/:key', controller=f_con, action = 'GET_STATE', conditions=dict(method=['GET']))
    dispatcher.connect('fires_get_state_options', '/fires/state/:key', controller=o_con, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('fires_post', '/fires/', controller=f_con, action='POST_FIRE', conditions=dict(method=['POST']))

    # Landslides
    dispatcher.connect('landslides_get_all', '/landslides/', controller=l_con, action='GET_ALL', conditions=dict(method=['GET']))
    dispatcher.connect('landslides_options', '/landslides/', controller=o_con, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('landslides_get_year', '/landslides/year/:key', controller=l_con, action = 'GET_YEAR', conditions=dict(method=['GET']))
    dispatcher.connect('landslides_get_year_options', '/landslides/year/:key', controller=o_con, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('landslides_get_state', '/landslides/state/:key', controller=l_con, action = 'GET_STATE', conditions=dict(method=['GET']))
    dispatcher.connect('landslides_get_state_options', '/landslides/state/:key', controller=o_con, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('landslides_post', '/landslides/', controller=l_con, action='POST', conditions=dict(method=['POST']))

    # Configuration
    conf = {
            'global' : {
                'server.socket_host': 'student04.cse.nd.edu',
                'server.socket_port': 51092, # change this later
                },

            '/' : {'request.dispatch': dispatcher,
                   'tools.CORS.on': True,}
            }

    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)


# DRIVER

if __name__ == '__main__':
    cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
    start_service()
