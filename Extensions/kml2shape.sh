#!/bin/bash
echo "start converting"
kml=$1
shape=$2'output.shp'
dir=$2
d=$2'output*'
ogr2ogr -f 'ESRI Shapefile' $shape $kml
echo "zip the result"
zip $dir'/EsriShapeFile.zip' $d
echo "done converting"
