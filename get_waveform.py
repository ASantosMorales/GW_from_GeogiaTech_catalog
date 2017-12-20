#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 12:46:25 2017

@author: a_santos

Module to generate an especific waveform from the Georgia Tech waveform catalog.
This module was prefixed to get only the l:2 and m:2 radiated mode.
The entire catalog has to be stored in the computer

The way to use this module is the following:
    
    file = 3 # I want to get the GT0003.h5 waveform
    path = '/Write here the path where the entire catalog is store/GT%04i.h5' % file 
    
    h_plus, h_cross, sampling = get_waveform(path)

"""

def get_waveform (path):
    import numpy as np
    import h5py
    from scipy.interpolate import interp1d
    # Call the h5 file
    f = h5py.File(path, 'r')
    
    # Get parameters and interpolation
    amp = interp1d(list(f["amp_l2_m2/knots"]), list(f["amp_l2_m2/data"]))
    phase = interp1d(list(f["phase_l2_m2/knots"]), list(f["phase_l2_m2/data"]))
    sampling = np.arange(min(list(f["amp_l2_m2/knots"])), max(list(f["amp_l2_m2/knots"])), 0.1)
    
    # Weyl scalar
    h = amp(sampling)*np.exp(-phase(sampling)*1j)
    
    # Splitting h_+ and h_x
    h_plus = h.real
    h_cross = h.imag
    return (h_plus, h_cross, sampling)