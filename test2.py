#!/usr/bin/env python3

import sys
from geopy.geocoders import Nominatim

location = Nominatim(user_agent="paradigms_project").reverse("37.85, -90.255")
print(location.address)
