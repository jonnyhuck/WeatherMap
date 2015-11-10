#!/usr/bin/env python

import urllib
import subprocess
import datetime
from PIL import Image

# set working directory
wd = "./"

#get the current date
date = datetime.datetime.now().strftime('%Y-%m-%d')

# get the latest data (gives data for noon today)
urllib.urlretrieve("http://datapoint.metoffice.gov.uk/public/data/layer/wxfcs/Atlantic/png?RUN=" \
+date+"T00:00:00Z&FORECAST=12&key=ba6a2766-d970-4993-90bd-ce6cdf74c77e", wd+"in.png")