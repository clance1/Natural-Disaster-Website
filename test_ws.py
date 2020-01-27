import unittest
import requests
import json

class TestLandslide(unittest.TestCase):

        # I Changed this to test locally and dont remember which port we were using
        SITE_URL = "http://student04.cse.nd.edu:51034"

        LANDSLIDE_URL = SITE_URL + "/landslides/"
        TORNADO_URL = SITE_URL + "/tornadoes/"
        FIRE_URL = SITE_URL + "/fires/"

        def reset_landslide_data(self):
            r = requests.delete(self.LANDSLIDE_URL)

        def reset_tornado_data(self):
            r = requests.delete(self.TORNADO_URL)

        def reset_fire_data(self):
            r = requests.delete(self.FIRE_URL)

        def is_json(self, resp):
            try:
                json.loads(resp)
                return True
            except ValueError:
                return False

        # Landslide tests

        def test_landslide_post(self):
            self.reset_landslide_data()

            ls = {}
            ls["date"] = "6/20/2015"
            ls["year"] = "2015"
            ls["category"] = "Small"
            ls["lat"] = "39.6423"
            ls["lon"] = "-86.1234"
            ls["state"] = "IN"

            r = requests.post(self.LANDSLIDE_URL, data = json.dumps(ls))
            self.assertTrue(self.is_json(r.content.decode()))
            resp = json.loads(r.content.decode())
            self.assertEqual(resp["result"], "success")

            r = requests.get(self.LANDSLIDE_URL + "state/IN")

            self.assertTrue(self.is_json(r.content.decode("utf-8")))
            resp = json.loads(r.content.decode("utf-8"))
            self.assertEqual(resp["result"], "success")

            landslides = resp["landslides"]
            l = landslides[-1]
            self.assertEqual(l["date"], ls["date"])
            self.assertEqual(l["year"], ls["year"])
            self.assertEqual(l["category"], ls["category"])
            self.assertEqual(l["lat"], ls["lat"])
            self.assertEqual(l["lon"], ls["lon"])
            self.assertEqual(l["state"], ls["state"])

        def test_landslide_get_year(self):
            self.reset_landslide_data()

            key = "2012"
            r = requests.get(self.LANDSLIDE_URL + "year/" + key)

            self.assertTrue(self.is_json(r.content.decode("utf-8")))
            resp = json.loads(r.content.decode("utf-8"))
            self.assertEqual(resp["result"], "success")

            landslides = resp["landslides"]
            l = landslides[0]
            self.assertEqual(l["date"], "5/1/2012")
            self.assertEqual(l["year"], "2012")
            self.assertEqual(l["category"], "Medium")
            self.assertEqual(l["lat"], "39.1229")
            self.assertEqual(l["lon"], "-84.4481")
            self.assertEqual(l["state"], "OH")

        def test_landslide_get_state(self):
            self.reset_landslide_data()

            key = "OH"
            r = requests.get(self.LANDSLIDE_URL + "state/" + key)

            self.assertTrue(self.is_json(r.content.decode("utf-8")))
            resp = json.loads(r.content.decode("utf-8"))
            self.assertEqual(resp["result"], "success")

            landslides = resp["landslides"]
            l = landslides[0]
            self.assertEqual(l["date"], "4/25/2011")
            self.assertEqual(l["year"], "2011")
            self.assertEqual(l["category"], "Small")
            self.assertEqual(l["lat"], "39.1369")
            self.assertEqual(l["lon"], "-84.7904")
            self.assertEqual(l["state"], "OH")

        def test_landslide_get_all(self):
            #self.reset_landslide_data()

            r = requests.get(self.LANDSLIDE_URL)

            self.assertTrue(self.is_json(r.content.decode("utf-8")))
            resp = json.loads(r.content.decode("utf-8"))
            self.assertEqual(resp["result"], "success")

            landslides = resp["landslides"]
            l = landslides[0]
            self.assertEqual(l["date"], "9/12/2013")
            self.assertEqual(l["year"], "2013")
            self.assertEqual(l["category"], "Medium")
            self.assertEqual(l["lat"], "39.8839")
            self.assertEqual(l["lon"], "-105.3033")
            self.assertEqual(l["state"], "CO")

        def test_tornado_get_year(self):
            #self.reset_tornado_data()

            year = 2019
            r = requests.get(self.TORNADO_URL + "year/" + year)

            self.assertTrue(self.is_json(r.content.decode("utf-8")))
            resp = json.loads(r.content.decode("utf-8"))
            self.assertEqual(resp["result"], "success")

            tornadoes = resp["tornadoes"]
            t = tornadoes[0]
            self.assertEqual(t["begin_year"], "2019")
            self.assertEqual(t["begin_month"], "4")
            self.assertEqual(t["begin_day"], "19")
            self.assertEqual(t["begin_time"], "1631")
            self.assertEqual(t["end_year"], "2019")
            self.assertEqual(t["end_month"], "4")
            self.assertEqual(t["end_day"], "19")
            self.assertEqual(t["end_time"], "1633")
            self.assertEqual(t["state"], "VIRGINIA")
            self.assertEqual(t["event_id"], "817339")
            self.assertEqual(t["cz_name"], "NELSON")
            self.assertEqual(t["begin_lat"], "37.699")
            self.assertEqual(t["begin_lon"], "-78.789")
            self.assertEqual(t["end_lat"], "37.72")
            self.assertEqual(t["end_lon"], "-78.781")
            self.assertEqual(t["tor_F_scale"], "EF1")

                # Tornadoes tests

        def test_tornado_get_year(self):
            #self.reset_tornado_data()

            year = "2019"
            r = requests.get(self.TORNADO_URL + "year/" + year)

            self.assertTrue(self.is_json(r.content.decode("utf-8")))
            resp = json.loads(r.content.decode("utf-8"))
            self.assertEqual(resp["result"], "success")

            tornadoes = resp["tornadoes"]
            self.assertEqual(len(tornadoes), 462292)

        def test_tornado_get_state(self):
            #self.reset_tornado_data()

            key = "VIRGINIA"
            r = requests.get(self.TORNADO_URL + "state/" + key)

            self.assertTrue(self.is_json(r.content.decode("utf-8")))
            resp = json.loads(r.content.decode("utf-8"))
            self.assertEqual(resp["result"], "success")

            tornadoes = resp["tornadoes"]
            self.assertEqual(len(tornadoes), 7096)

        def test_tornado_get_all(self):
            #self.reset_tornado_data()

            r = requests.get(self.TORNADO_URL)

            self.assertTrue(self.is_json(r.content.decode("utf-8")))
            resp = json.loads(r.content.decode("utf-8"))
            self.assertEqual(resp["result"], "success")

            tornadoes = resp["tornadoes"]
            self.assertEqual(len(tornadoes), 495454)

        def test_tornado_post(self):
            #self.reset_tornado_data()

            t = dict()
            t["begin_year"] = "2000"
            t["begin_month"]= "3"
            t["begin_day"]= "19"
            t["begin_time"]= "1631"
            t["end_year"]= "2000"
            t["end_month"]= "4"
            t["end_day"]= "19"
            t["end_time"]= "1633"
            t["state"]= "TEXAS"
            t["event_id"]= "000000"
            t["cz_name"]= "TEST"
            t["begin_lat"]= "10.000"
            t["begin_lon"]= "11.000"
            t["end_lat"]= "10.00"
            t["end_lon"]= "11.000"
            t["tor_F_scale"]= "EF1"

            r = requests.post(self.TORNADO_URL, data = json.dumps(t))

            self.assertTrue(self.is_json(r.content.decode()))
            resp = json.loads(r.content.decode())
            self.assertEqual(resp["result"], "success")

            # check that the number of tornadoes has increased by 1
            r = requests.get(self.TORNADO_URL + "/year/2000")
            self.assertTrue(self.is_json(r.content.decode("utf-8")))
            resp = json.loads(r.content.decode("utf-8"))
            self.assertEqual(resp["result"], "success")

            tornadoes = resp["tornadoes"]

            self.assertEqual(328, len(tornadoes))

        # FIRE TESTS
        def test_fire_get_state(self):
            #self.reset_fire_data()

            key = "CA"
            url = self.FIRE_URL + "state/" + key
            r = requests.get(url)

            self.assertTrue(self.is_json(r.content.decode("utf-8")))
            resp = json.loads(r.content.decode("utf-8"))
            self.assertEqual(resp["result"], "success")

            fires = resp["fires"]
            f = fires[0]
            self.assertEqual(f["id"], 1)
            self.assertEqual(f["year"], 2004)
            self.assertEqual(f["start_doy"],  133)
            self.assertEqual(f["end_doy"],  133.0)
            self.assertEqual(f["category"], "A")
            self.assertEqual(f["latitude"], 38.93305556)
            self.assertEqual(f["longitude"], -120.40444444)
            self.assertEqual(f["state"], "CA")

        def test_fire_get_year(self):
            #self.reset_fire_data()

            key = "2005"
            url = self.FIRE_URL + "year/" + key
            r = requests.get(url)

            self.assertTrue(self.is_json(r.content.decode("utf-8")))
            resp = json.loads(r.content.decode("utf-8"))
            self.assertEqual(resp["result"], "success")

            fires = resp["fires"]
            f = fires[0]
            self.assertEqual(f["id"], 7)
            self.assertEqual(f["start_doy"],  67)
            self.assertEqual(f["end_doy"],  67.0)
            self.assertEqual(f["year"], 2005)
            self.assertEqual(f["category"], "B")
            self.assertEqual(f["latitude"], 40.96805556)
            self.assertEqual(f["longitude"], -122.43388889)
            self.assertEqual(f["state"], "CA")
    
if __name__ == "__main__":
        unittest.main()
