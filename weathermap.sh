#!/bin/bash

# download the latest data
python getWeather.py

# add control points to the image (as vrt for efficiency)
gdal_translate -of VRT -gcp 0 0 -1335833.89 8625823.20 0 -gcp 500 0 556597.45 8625823.20 0 -gcp 500 500 556597.45 6106854.83 0 -gcp 0 500 -1335833.89 6106854.83 0 in.png gcp.vrt > /dev/null 2>&1

# transform the image to the fit on the map - output to GeoTiff
gdalwarp -t_srs '+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +wktext  +no_defs' -overwrite gcp.vrt projected.tif > /dev/null 2>&1

# Optionally render onto a png map:
nik2img.py weather.xml weathermap.png --srs 900913 --dimensions 750 1000 --projected-extent -1335833.89 6106854.83 556597.45 8625823.20 -w pgw --no-open > /dev/null 2>&1
