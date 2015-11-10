#!/usr/bin/env python

###
# This downloads the latest imagery from Met Office Datapoint and stores it in the current directory as in.png
# Currently, it gets the isobars layer, but you can change this to Rainfall etc simply by editing the URL.
###

import urllib
import subprocess
import datetime
from PIL import Image

# USER NEEDS TO FILL IN THEIR DATAPOINT API KEY HERE
USER_KEY = ""

# set working directory
wd = "./"

#get the current date
date = datetime.datetime.now().strftime('%Y-%m-%d')

# get the latest data (gives data for noon today)
urllib.urlretrieve("http://datapoint.metoffice.gov.uk/public/data/layer/wxfcs/Atlantic/png?RUN=" \
+date+"T00:00:00Z&FORECAST=12&key="+USER_KEY+", wd+"in.png")