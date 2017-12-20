# GW_from_GeogiaTech_catalog
A little module in Python to get a specific waveform from the entire GeorgiaTech catalog

The entire catalog can be download from:
http://www.einstein.gatech.edu/catalog/

The way to call this module is the following:

file = 1 #Choose which GW want to get
path = '/write the corresponding path in your computer/GT%04i.h5' % file
       Example: paht = '/home/user/Documents/Georgia_Tech_catalog/GT%04i.h5' % file
h_plus, h_cross, sampling = get_waveform(path)
