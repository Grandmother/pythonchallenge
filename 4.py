#!/usr/bin/env python3

import urllib.request as request
import re

url_base = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

nothing0 = "12345"
nothing1 = str(16044 / 2)

nothing = nothing1

while nothing is not None:
    page = request.urlopen(url_base + nothing).read().decode('UTF-8')
    nothing = re.search(r'\d+$', page)
    if nothing is not None:
        print(nothing)
        nothing = nothing.group(0)
    else:
        print(page)

