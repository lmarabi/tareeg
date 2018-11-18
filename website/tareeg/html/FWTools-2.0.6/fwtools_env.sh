#
# Bourne style shell environment initialization.
#

FWTOOLS_HOME=/home/yackel/public_html/app/webroot/osme/FWTools-2.0.6

# Check that the location is correct.

if test \! -d $FWTOOLS_HOME/pymod ; then
  echo 
  echo FWTOOLS_HOME=$FWTOOLS_HOME, but this does not seem to be correct.
  echo
else

# Setup Environment Variables for FWTools 

  PROJ_LIB=$FWTOOLS_HOME/share/proj
  GEOTIFF_CSV=$FWTOOLS_HOME/share/gdal
  GDAL_DATA=$FWTOOLS_HOME/share/gdal
  OPENEV_HOME=$FWTOOLS_HOME
  PYTHONHOME=${FWTOOLS_HOME}
  PYTHONPATH=${FWTOOLS_HOME}/pymod:${FWTOOLS_HOME}/lib/python2.2/site-packages:${PYTHONPATH}
  LD_LIBRARY_PATH=${FWTOOLS_HOME}/lib:${LD_LIBRARY_PATH}:/lib:${FWTOOLS_HOME}/lib/fallback
  PATH=${FWTOOLS_HOME}/bin:$PATH
  LC_NUMERIC=C

  export PYTHONHOME PYTHONPATH LD_LIBRARY_PATH PATH PROJ_LIB GEOTIFF_CSV LC_NUMERIC GDAL_DATA FWTOOLS_HOME
fi

