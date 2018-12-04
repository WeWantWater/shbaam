#!/usr/bin/env python
#*******************************************************************************
#tst_cmp_n3d.py
#*******************************************************************************

#Purpose:
#Compare netCDF files.
#Author:
#Cedric H. David, 2018-2018


#*******************************************************************************
#Prerequisites
#*******************************************************************************
import sys
import netCDF4
import math
import numpy


#*******************************************************************************
#Declaration of variables (given as command line arguments)
#*******************************************************************************
# 1 - correct_nc4_file
# 2 - test_nc4_file
#(3)- relative tolerance 
#(4)- absolute tolerance 


#*******************************************************************************
#Get command line arguments
#*******************************************************************************
num_args=len(sys.argv)
if num_args < 3 or num_args > 5:
     print('ERROR - A minimum of 2 and a maximum of 4 arguments can be used')
     raise SystemExit(22) 

correct_nc4_file=sys.argv[1]
test_nc4_file=sys.argv[2]
if num_args > 3:
     rel_tol=float(sys.argv[3])
else:
     rel_tol=float(0)
if num_args > 4:
     abs_tol=float(sys.argv[4])
else:
     abs_tol=float(0)
     

#*******************************************************************************
#Print current variables
#*******************************************************************************
print('Comparing netCDF files')
print('1st netCDF file               :'+correct_nc4_file)
print('2nd netCDF file               :'+test_nc4_file)
print('Relative tolerance            :'+str(rel_tol))
print('Absolute tolerance            :'+str(abs_tol))
print('-------------------------------')


#*******************************************************************************
#Test if input files exist
#*******************************************************************************
try:
     with open(correct_nc4_file) as file:
          pass
except IOError as e:
     print('Unable to open '+correct_nc4_file)
     raise SystemExit(22) 

try:
     with open(test_nc4_file) as file:
          pass
except IOError as e:
     print('Unable to open '+test_nc4_file)
     raise SystemExit(22) 


#*******************************************************************************
#Read and compare netCDF files
#*******************************************************************************

#-------------------------------------------------------------------------------
#Open files and get dimensions
#-------------------------------------------------------------------------------
correct_data = netCDF4.Dataset(correct_nc4_file, "r")

if 'lon' in correct_data.dimensions:
     correct_num_lons=len(correct_data.dimensions['lon'])
elif 'Lon' in correct_data.dimensions:
     correct_num_lons=len(correct_data.dimensions['Lon'])
else:
     print('ERROR - Neither lon nor Lon are dimensions in: '+correct_nc4_file) 
     raise SystemExit(99) 

if 'lat' in correct_data.dimensions:
     correct_num_lats=len(correct_data.dimensions['lat'])
elif 'Lat' in correct_data.dimensions:
     correct_num_lats=len(correct_data.dimensions['Lat'])
else:
     print('ERROR - Neither lat nor Lat are dimensions in: '+correct_nc4_file) 
     raise SystemExit(99) 

if 'time' in correct_data.dimensions:
     correct_num_times=len(correct_data.dimensions['time'])
elif 'Time' in correct_data.dimensions:
     correct_num_times=len(correct_data.dimensions['Time'])
else:
     print('ERROR - Neither time nor Time are dimensions in: '+correct_nc4_file) 
     raise SystemExit(99) 

# Dimensional establishes the dimensional variables expected to be present in the
# nc4 file. All other variables, those regarding water storage anomalies, are 
# added to the avail_vars list so that we check every potential WSA variable.
# This works perfectly fine if there is only one WSA variable as well. 
dimensional = ["lon", "lat", "time"]
correct_avail_vars = []
for var in correct_data.variables.keys():
     if var.lower() not in dimensional:
          correct_avail_vars.append(var)
if not correct_avail_vars:
     print('ERROR - no water anomaly variables available in: '+correct_nc4_file) 
     raise SystemExit(99) 

test_data = netCDF4.Dataset(test_nc4_file, "r")

if 'lon' in test_data.dimensions:
     test_num_lons=len(test_data.dimensions['lon'])
elif 'Lon' in test_data.dimensions:
     test_num_lons=len(test_data.dimensions['Lon'])
else:
     print('ERROR - Neither lon nor Lon are dimensions in: '+test_nc4_file) 
     raise SystemExit(99) 

if 'lat' in test_data.dimensions:
     test_num_lats=len(test_data.dimensions['lat'])
elif 'Lat' in test_data.dimensions:
     test_num_lats=len(test_data.dimensions['Lat'])
else:
     print('ERROR - Neither lat nor Lat are dimensions in: '+test_nc4_file) 
     raise SystemExit(99) 

if 'time' in test_data.dimensions:
     test_num_times=len(test_data.dimensions['time'])
elif 'Time' in test_data.dimensions:
     test_num_times=len(test_data.dimensions['Time'])
else:
     print('ERROR - Neither time nor Time are dimensions in: '+test_nc4_file) 
     raise SystemExit(99) 


test_avail_vars = []
for var in test_data.variables.keys():
     if var.lower() not in dimensional:
          test_avail_vars.append(var)
if not test_avail_vars:
     print('ERROR - no water anomaly variables available in: '+test_nc4_file) 
     raise SystemExit(99) 


#-------------------------------------------------------------------------------
#Compare file sizes and variable names
#-------------------------------------------------------------------------------
if correct_num_lons==test_num_lons:
     print('Common number of longitudes   :'+str(correct_num_lons))
else:
     print('ERROR - The number of longitudes differs: '                        \
           +str(correct_num_lons)+' <> '+str(test_num_lons))
     raise SystemExit(99) 

if correct_num_lats==test_num_lats:
     print('Common number of latitudes    :'+str(correct_num_lats))
else:
     print('ERROR - The number of latitudes differs: '                         \
           +str(correct_num_lats)+' <> '+str(test_num_lats))
     raise SystemExit(99) 

if correct_num_times==test_num_times:
     print('Common number of time steps   :'+str(correct_num_times))
else:
     print('ERROR - The number of time steps differs: '                        \
           +str(correct_num_times)+' <> '+str(test_num_times))
     raise SystemExit(99) 

if correct_avail_vars==test_avail_vars:
     print('Common variable names          :'+str(correct_avail_vars))
else:
     print('ERROR - The variable names differ: '                               \
           +str(correct_avail_vars)+' <> '+str(test_avail_vars))
     raise SystemExit(99) 

print('-------------------------------')

#-------------------------------------------------------------------------------
#Compare coordinate values if they exist in both files
#-------------------------------------------------------------------------------
if 'lon' in correct_data.variables:
     correct_lons=correct_data.variables['lon']
elif 'Lon' in correct_data.variables:
     correct_lons=correct_data.variables['Lon']

if 'lon' in test_data.variables:
     test_lons=test_data.variables['lon']
elif 'Lon' in test_data.variables:
     test_lons=test_data.variables['Lon']

if 'correct_lons' in locals() and 'test_lons' in locals():
     #This makes sure that both variables actually exist before comparing them
     if numpy.array_equal(correct_lons[:],test_lons[:]):
          print('The longitudes are the same')
     else:
          print('ERROR: The longitudes differ')
          raise SystemExit(99) 

if 'lat' in correct_data.variables:
     correct_lats=correct_data.variables['lat']
elif 'Lat' in correct_data.variables:
     correct_lats=correct_data.variables['Lat']

if 'lat' in test_data.variables:
     test_lats=test_data.variables['lat']
elif 'Lat' in test_data.variables:
     test_lats=test_data.variables['Lat']

if 'correct_lats' in locals() and 'test_lats' in locals():
     #This makes sure that both variables actually exist before comparing them
     if numpy.array_equal(correct_lats[:],test_lats[:]):
          print('The latitudes are the same')
     else:
          print('ERROR: The latitudes differ')
          raise SystemExit(99) 

print('-------------------------------')

#-------------------------------------------------------------------------------
#Compute differences 
#-------------------------------------------------------------------------------
rel_diff_max=0
abs_diff_max=0

for water_anomaly_var in correct_avail_vars:
     for time_step in range(correct_num_times):
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#Reading values
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
          correct_values=correct_data.variables[water_anomaly_var][time_step,:]
          test_values=test_data.variables[water_anomaly_var][time_step,:]

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#Checking that the locations of NoData are the same
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
          correct_masks=numpy.logical_not(numpy.ma.getmaskarray(correct_values))
          test_masks=numpy.logical_not(numpy.ma.getmaskarray(test_values))
          if not numpy.array_equal(correct_masks,test_masks):
               print('ERROR - The locations of NoData differ')
               raise SystemExit(99) 

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#Comparing difference values
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
     #Tried computations with regular Python lists but this makes is very slow.
     #Also tried using map(operator.sub,V,W) or [x-y for x,y in zip(V,W)]
     #But this still results in slow computations.
     #The best performance seems to be with Numpy.
          abs_diff=numpy.absolute(correct_values-test_values)
          abs_diff_max=max(numpy.max(abs_diff),abs_diff_max)

          rel_diff=numpy.sum(numpy.multiply(abs_diff,abs_diff,where=correct_masks))  \
                 /numpy.sum(numpy.multiply(correct_values,correct_values,where=correct_masks))
          #Using the mask helps avoid the 'overflow' warning at runtime by performing
          #operations only for values that are not masked
          rel_diff=math.sqrt(rel_diff)
          rel_diff_max=max(rel_diff,rel_diff_max)


#*******************************************************************************
#Print difference values and comparing values to tolerance
#*******************************************************************************
print('Max relative difference       :'+'{0:.2e}'.format(rel_diff_max))
print('Max absolute difference       :'+'{0:.2e}'.format(abs_diff_max))
print('-------------------------------')

if rel_diff_max > rel_tol:
     print('Unacceptable rel. difference!!!')
     print('-------------------------------')
     raise SystemExit(99) 

if abs_diff_max > abs_tol:
     print('Unacceptable abs. difference!!!')
     print('-------------------------------')
     raise SystemExit(99) 

print('netCDF files similar!!!')
print('-------------------------------')


#*******************************************************************************
#End
#*******************************************************************************
