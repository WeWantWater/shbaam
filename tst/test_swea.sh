#!/bin/sh
#*******************************************************************************
#test_swea.sh
#*******************************************************************************

#Purpose:
#This script reproduces all SHBAAM processing steps used in the writing of:
#David, Cédric H., et al. (201x)
#xxx
#DOI: xx.xxxx/xxxxxx
#The files used are available from:
#David, Cédric H., et al. (201x)
#xxx
#DOI: xx.xxxx/xxxxxx
#The following are the possible arguments:
# - No argument: all unit tests are run
# - One unique unit test number: this test is run
# - Two unit test numbers: all tests between those (included) are run
#The script returns the following exit codes
# - 0  if all experiments are successful 
# - 22 if some arguments are faulty 
# - 99 if a comparison failed 
#Author:
#Cedric H. David, 2018-2018


#*******************************************************************************
#Publication message
#*******************************************************************************
echo "********************"
echo "Reproducing files for: http://dx.doi.org/xx.xxxx/"
echo "********************"


#*******************************************************************************
#Select which unit tests to perform based on inputs to this shell script
#*******************************************************************************
if [ "$#" = "0" ]; then
     fst=1
     lst=99
     echo "Performing all unit tests: 1-99"
     echo "********************"
fi 
#Perform all unit tests if no options are given 

if [ "$#" = "1" ]; then
     fst=$1
     lst=$1
     echo "Performing one unit test: $1"
     echo "********************"
fi 
#Perform one single unit test if one option is given 

if [ "$#" = "2" ]; then
     fst=$1
     lst=$2
     echo "Performing unit tests: $1-$2"
     echo "********************"
fi 
#Perform all unit tests between first and second option given (both included) 

if [ "$#" -gt "2" ]; then
     echo "A maximum of two options can be used" 1>&2
     exit 22
fi 
#Exit if more than two options are given 


#*******************************************************************************
#Initialize count for unit tests
#*******************************************************************************
unt=0


#*******************************************************************************
#Ground water storage anomalies, Nepal
#*******************************************************************************
unt=$((unt+1))
if [ "$unt" -ge "$fst" ] && [ "$unt" -le "$lst" ] ; then
echo "Running unit test $unt/x"
run_file=tmp_run_$unt.txt
cmp_file=tmp_cmp_$unt.txt

echo "- Ground water storage anomalies, Nepal"
../src/shbaam_swea.py                                                          \
     ../input/GLDAS/GLDAS_VIC10_M/GLDAS_VIC10_M.A200204_200212.nc4\
     ../input/SERVIR_STK/Nepal.shp                                             \
     ../output/SERVIR_STK/GLDAS.VIC.Nepal.pnt_tst.shp                          \
     ../output/SERVIR_STK/timeseries_swea_Nepal_tst.csv                        \
     ../output/SERVIR_STK/map_swea_Nepal_tst.nc4                               \
     > $run_file
x=$? && if [ $x -gt 0 ] ; then echo "Failed run: $run_file" >&2 ; exit $x ; fi

echo "- Comparing shapefiles"
./test_cmp_shp.py                                                               \
     ../output/SERVIR_STK/GLDAS.VIC.Nepal.pnt_tst.shp                          \
     ../output/SERVIR_STK/GLDAS.VIC.Nepal.pnt.shp                              \
     > $cmp_file
x=$? && if [ $x -gt 0 ] ; then echo "Failed comparison: $cmp_file" >&2 ; exit $x ; fi

echo "- Comparing timeseries"
./test_cmp_csv.py                                                               \
     ../output/SERVIR_STK/timeseries_swea_Nepal_tst.csv                        \
     ../output/SERVIR_STK/timeseries_swea_Nepal.csv                            \
     1e-6                                                                      \
     1e-6                                                                      \
     > $cmp_file
x=$? && if [ $x -gt 0 ] ; then echo "Failed comparison: $cmp_file" >&2 ; exit $x ; fi

echo "- Comparing maps"
./test_cmp_nc4.py                                                               \
     ../output/SERVIR_STK/map_swea_Nepal_tst.nc4                               \
     ../output/SERVIR_STK/map_swea_Nepal.nc4                                   \
     1e-6                                                                      \
     1e-6                                                                      \
     > $cmp_file
x=$? && if [ $x -gt 0 ] ; then echo "Failed comparison: $cmp_file" >&2 ; exit $x ; fi

rm -f $run_file
rm -f $cmp_file
echo "Success"
echo "********************"
fi


#*******************************************************************************
#Ground water storage anomalies, FourDoabs
#*******************************************************************************
unt=$((unt+1))
if [ "$unt" -ge "$fst" ] && [ "$unt" -le "$lst" ] ; then
echo "Running unit test $unt/x"
run_file=tmp_run_$unt.txt
cmp_file=tmp_cmp_$unt.txt

echo "- Ground water storage anomalies, FourDoabs"
../src/shbaam_swea.py                                                          \
     ../input/GLDAS/GLDAS_VIC10_M/GLDAS_VIC10_M.A200204_200212.nc4\
     ../input/SERVIR_STK/FourDoabs.shp                                             \
     ../output/SERVIR_STK/GLDAS.VIC.FourDoabs.pnt_tst.shp                          \
     ../output/SERVIR_STK/timeseries_swea_FourDoabs_tst.csv                        \
     ../output/SERVIR_STK/map_swea_FourDoabs_tst.nc4                               \
     > $run_file
x=$? && if [ $x -gt 0 ] ; then echo "Failed run: $run_file" >&2 ; exit $x ; fi

echo "- Comparing shapefiles"
./test_cmp_shp.py                                                               \
     ../output/SERVIR_STK/GLDAS.VIC.FourDoabs.pnt_tst.shp                          \
     ../output/SERVIR_STK/GLDAS.VIC.FourDoabs.pnt.shp                              \
     > $cmp_file
x=$? && if [ $x -gt 0 ] ; then echo "Failed comparison: $cmp_file" >&2 ; exit $x ; fi

echo "- Comparing timeseries"
./test_cmp_csv.py                                                               \
     ../output/SERVIR_STK/timeseries_swea_FourDoabs_tst.csv                        \
     ../output/SERVIR_STK/timeseries_swea_FourDoabs.csv                            \
     1e-6                                                                      \
     1e-6                                                                      \
     > $cmp_file
x=$? && if [ $x -gt 0 ] ; then echo "Failed comparison: $cmp_file" >&2 ; exit $x ; fi

echo "- Comparing maps"
./test_cmp_nc4.py                                                               \
     ../output/SERVIR_STK/map_swea_FourDoabs_tst.nc4                               \
     ../output/SERVIR_STK/map_swea_FourDoabs.nc4                                   \
     1e-6                                                                      \
     1e-6                                                                      \
     > $cmp_file
x=$? && if [ $x -gt 0 ] ; then echo "Failed comparison: $cmp_file" >&2 ; exit $x ; fi

rm -f $run_file
rm -f $cmp_file
echo "Success"
echo "********************"
fi


#*******************************************************************************
#Ground water storage anomalies, NorthWestBD
#*******************************************************************************
unt=$((unt+1))
if [ "$unt" -ge "$fst" ] && [ "$unt" -le "$lst" ] ; then
echo "Running unit test $unt/x"
run_file=tmp_run_$unt.txt
cmp_file=tmp_cmp_$unt.txt

echo "- Ground water storage anomalies, NorthWestBD"
../src/shbaam_swea.py                                                          \
     ../input/GLDAS/GLDAS_VIC10_M/GLDAS_VIC10_M.A200204_200212.nc4\
     ../input/SERVIR_STK/NorthWestBD.shp                                             \
     ../output/SERVIR_STK/GLDAS.VIC.NorthWestBD.pnt_tst.shp                          \
     ../output/SERVIR_STK/timeseries_swea_NorthWestBD_tst.csv                        \
     ../output/SERVIR_STK/map_swea_NorthWestBD_tst.nc4                               \
     > $run_file
x=$? && if [ $x -gt 0 ] ; then echo "Failed run: $run_file" >&2 ; exit $x ; fi

echo "- Comparing shapefiles"
./test_cmp_shp.py                                                               \
     ../output/SERVIR_STK/GLDAS.VIC.NorthWestBD.pnt_tst.shp                          \
     ../output/SERVIR_STK/GLDAS.VIC.NorthWestBD.pnt.shp                              \
     > $cmp_file
x=$? && if [ $x -gt 0 ] ; then echo "Failed comparison: $cmp_file" >&2 ; exit $x ; fi

echo "- Comparing timeseries"
./test_cmp_csv.py                                                               \
     ../output/SERVIR_STK/timeseries_swea_NorthWestBD_tst.csv                        \
     ../output/SERVIR_STK/timeseries_swea_NorthWestBD.csv                            \
     1e-6                                                                      \
     1e-6                                                                      \
     > $cmp_file
x=$? && if [ $x -gt 0 ] ; then echo "Failed comparison: $cmp_file" >&2 ; exit $x ; fi

echo "- Comparing maps"
./test_cmp_nc4.py                                                               \
     ../output/SERVIR_STK/map_swea_NorthWestBD_tst.nc4                               \
     ../output/SERVIR_STK/map_swea_NorthWestBD.nc4                                   \
     1e-6                                                                      \
     1e-6                                                                      \
     > $cmp_file
x=$? && if [ $x -gt 0 ] ; then echo "Failed comparison: $cmp_file" >&2 ; exit $x ; fi

rm -f $run_file
rm -f $cmp_file
echo "Success"
echo "********************"
fi


#*******************************************************************************
#Clean up
#*******************************************************************************
rm -f ../output/SERVIR_STK/*_tst.*


#*******************************************************************************
#End
#*******************************************************************************
echo "Passed all tests!!!"
echo "********************"
