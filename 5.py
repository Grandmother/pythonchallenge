#!/usr/bin/env python3

import pickle
import urllib.request

base_url = "http://www.pythonchallenge.com/pc/def/"
filename = "banner.p"

with urllib.request.urlopen(base_url + filename) as response:
    data = pickle.load(response)
    for d in data:
        for c in d:
            print(c[0]*c[1], end='')
        print()
