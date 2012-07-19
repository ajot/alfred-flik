#! /usr/bin/python

from encodings import hex_codec
from encodings import ascii
import httplib
import urllib2
import json
import sys
import datetime
import time
import rovi_search

# getting user input
if len(sys.argv) < 2:
    sys.exit(2)


##### Use this when running from the commmand line #####
# search = sys.argv[1]
# contact = sys.argv[2]

##### Use this when running from Alfred #####
search = sys.argv[1].split ('\ ')[0]
contact = sys.argv[1].split ('\ ')[1]


rovi_search.get_relatedMovies(search, contact)