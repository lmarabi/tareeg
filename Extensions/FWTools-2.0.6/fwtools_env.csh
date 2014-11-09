#
# C Shell style shell environment initialization.
#

setenv FWTOOLS_HOME /home/turtle/NetBeansProjects/OSMExtractor/Extensions/FWTools-2.0.6

# Check that the location is correct.

if ! -d $FWTOOLS_HOME/pymod then 

  echo 
  echo FWTOOLS_HOME=$FWTOOLS_HOME, but this does not seem to be correct.
  echo

else

# Setup Environment Variables for FWTools 

  setenv PROJ_LIB $FWTOOLS_HOME/share/proj
  setenv GEOTIFF_CSV $FWTOOLS_HOME/share/gdal
  setenv GDAL_DATA $FWTOOLS_HOME/share/gdal
  setenv OPENEV_HOME $FWTOOLS_HOME
  setenv PYTHONHOME $FWTOOLS_HOME
  setenv LC_NUMERIC C
  setenv PATH $FWTOOLS_HOME/bin:$PATH

  if $?PYTHONPATH then
    setenv PYTHONPATH $FWTOOLS_HOME/pymod:$FWTOOLS_HOME/lib/python2.2/site-packages:$PYTHONPATH
  else
    setenv PYTHONPATH $FWTOOLS_HOME/pymod:$FWTOOLS_HOME/lib/python2.2/site-packages
  endif

  if $?LD_LIBRARY_PATH then
    setenv LD_LIBRARY_PATH $FWTOOLS_HOME/lib:${LD_LIBRARY_PATH}:/lib:$FWTOOLS_HOME/lib/fallback
  else
    setenv LD_LIBRARY_PATH $FWTOOLS_HOME/lib:/lib:$FWTOOLS_HOME/lib/fallback
  endif

endif
