# GW_from_GeogiaTech_catalog
A little module in Python to get a specific waveform from the entire GeorgiaTech catalog

The entire catalog can be download here:
http://www.einstein.gatech.edu/catalog/

The way to call this module is the following:

file = 1 #Choose which GW want to get
path = '/home/user/.../GT%04i.h5' % file

h_plus, h_cross, sampling = get_waveform(path)

Having as result, by example, the following plot (GT0586)
![alt text](https://github.com/ASantosMorales/GW_from_GeogiaTech_catalog/blob/master/GT0582.png)
