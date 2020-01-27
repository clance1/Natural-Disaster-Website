#!/usr/bin/env python3

import json

class tornado_db(object):

    def __init__(self):
        self.tornadoes = dict()

    def load_tornadoes(self, tornado_file):
        with open(tornado_file, "r") as f:
            tornadoes = json.load(f)

            for tornado in tornadoes:
                tornado_dict = dict()

                begin_lat = str(tornado["BEGIN_LAT"])
                begin_lon = str(tornado["BEGIN_LON"])

                index = (begin_lat, begin_lon)

                begin_yearmonth = tornado["BEGIN_YEARMONTH"]
                tornado_dict["begin_year"] = str(int( begin_yearmonth / 100) )     # removes last two digits of integer representing the month
                tornado_dict["begin_month"] = str(begin_yearmonth % 100 )    # stores last two digits of integer representing the month
                tornado_dict["begin_day"] = str(tornado["BEGIN_DAY"])
                tornado_dict["begin_time"] = str(tornado["BEGIN_TIME"])
                
                end_yearmonth = tornado["END_YEARMONTH"]
                tornado_dict["end_year"] = str(int ( end_yearmonth / 100 )  )   # removes last two digits of integer representing the month
                tornado_dict["end_month"] = str(end_yearmonth % 100)     # stores last two digits of integer representing the month
                tornado_dict["end_day"] = str(tornado["END_DAY"])
                tornado_dict["end_time"] = str(tornado["END_TIME"])

                tornado_dict["state"] = str(tornado["STATE"])
                tornado_dict["event_id"] = str(tornado["EVENT_ID"])
                tornado_dict["cz_name"] = str(tornado["CZ_NAME"])

                tornado_dict["begin_lat"] = begin_lat
                tornado_dict["begin_lon"] = begin_lon
                tornado_dict["end_lat"] = str(tornado["END_LAT"])
                tornado_dict["end_lon"] = str(tornado["END_LON"])

                tornado_dict["tor_F_scale"] = str(tornado["TOR_F_SCALE"])

                self.tornadoes[index] = tornado_dict

    def get_all_tornadoes(self):
        return self.tornadoes

    def get_tornado(self, lat, lon):
        if (lat, lon) in self.tornadoes:
            return self.tornadoes[(lat, lon)]

    def get_tornadoes_year(self, year):
        tornado_list = list()
        for location, details in self.tornadoes.items():
            if details["begin_year"] == year:
                tornado_list.append(details)
        return json.dumps(tornado_list)

    def get_tornadoes_state(self, state):
        tornado_list = list()
        for location, details in self.tornadoes.items():
            if details["state"] == state:
                tornado_list.append(details)
        return json.dumps(tornado_list)

    def get_tornadoes_year_state(self, year, state):
        tornado_list = list()
        for location, details in self.tornadoes.items():
            if (details["state"] == state) and (details["begin_year"] == year):
                tornado_list.append(details)
        return json.dumps(tornado_list)

    def set_tornado(self, begin_lat, begin_lon, end_lat, end_lon, begin_year, begin_month, \
                    begin_day,begin_time, end_year, end_month, end_day, end_time, state, event_id,\
                    cz_name, tor_F_scale):
        tornado_dict = dict()
        index = (begin_lat, begin_lon)
        tornado_dict["begin_year"] = begin_year
        tornado_dict["begin_month"] = begin_month
        tornado_dict["begin_day"] = begin_day
        tornado_dict["begin_time"] = begin_time
                
        tornado_dict["end_year"] = end_year
        tornado_dict["end_month"] = end_month
        tornado_dict["end_day"] = end_day
        tornado_dict["end_time"] = end_time

        tornado_dict["state"] = state
        tornado_dict["event_id"] = event_id
        tornado_dict["cz_name"] = cz_name

        tornado_dict["begin_lat"] = begin_lat
        tornado_dict["begin_lon"] = begin_lon
        tornado_dict["end_lat"] = end_lat
        tornado_dict["end_lon"] = end_lon

        tornado_dict["tor_F_scale"] = tor_F_scale

        self.tornadoes[index] = tornado_dict

    def delete_tornado(self, lat, lon):
        if (lat, lon) in self.tornadoes:
            return self.tornadoes[(lat, lon)]
        return None

    def delete_all_tornadoes(self):
        self.tornadoes.clear()

    def reset_tornadoes(self):
        self.tornadoes.clear()
        self.load_tornadoes("tornadoes/tornadoes_short.json")

    def print_all_tornadoes(self):
        for location, details in self.tornadoes.items():
            print("Location: {} \nDetails: {}".format(location, details))

if __name__ == "__main__":
    
    tdb = tornado_db()
    tdb.load_tornadoes("tornadoes/tornadoes_short.json")
    #print(tdb.get_tornado(30.3375,-98.4931))
    #all = tdb.get_tornadoes_year(2015)
    #all = tdb.get_tornadoes_state("TEXAS")
    all = tdb.get_tornadoes_year_state(2019, "TEXAS")
    print(all)
    #tdb.print_all_tornadoes()
