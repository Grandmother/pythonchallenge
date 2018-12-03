#!/usr/bin/env python3

import re
import zipfile

import os
import pathlib
import shutil

import urllib.request
import sys
import atexit

tmp_dir = "channel/"

def cleanup():
    tmp_dir_path = pathlib.Path(tmp_dir)
    if tmp_dir_path.is_dir():
        shutil.rmtree(tmp_dir)

atexit.register(cleanup)

try:
    os.mkdir(tmp_dir)
except FileExistsError:
    pass
except Exception as e:
    print(str(e))
    sys.exit(1)

zip_url = "http://www.pythonchallenge.com/pc/def/channel.zip"
channel_zip = urllib.request.urlretrieve(zip_url, tmp_dir + "channel.zip")

zipfile = zipfile.ZipFile(tmp_dir + "channel.zip")
zipfile.extractall(tmp_dir)

nothing = "90052"
while nothing is not None:
    filename = "channel/" + nothing + ".txt"
    f_data = open(filename).read()
    nothing = re.search(r'\d+$', f_data)
    if nothing is not None:
        nothing = nothing.group(0)
        zipinfo = zipfile.getinfo(nothing + '.txt')
        print(zipinfo.comment.decode('UTF-8'), end='')

