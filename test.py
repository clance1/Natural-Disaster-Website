#!/usr/bin/env python3

import requests
import json

r = requests.get('http://student04.cse.nd.edu:51034/meteors/')
response = json.loads(r.content.decode())

print(response)
