import numpy as np
import json
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from ligotools import readligo as rl
from ligotools.utils import *


# data for testing the whiten function:

fn_H1 = 'data/H-H1_LOSC_4_V2-1126259446-32.hdf5'
fn_L1 = 'data/L-L1_LOSC_4_V2-1126259446-32.hdf5'

# Read the event properties from a local json file
fnjson = "data/BBH_events_v3.json"
events = json.load(open(fnjson,"r"))
eventname = 'GW150914'
event = events[eventname]
fs = event['fs']

try:
    events = json.load(open(fnjson,"r"))
except IOError:
    print("Cannot find resource file "+fnjson)
    print("You can download it from https://www.gwosc.org/s/events/"+fnjson)
    print("Quitting.")
    quit()


try:
    # read in data from H1 and L1, if available:
    strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_H1, 'H1')
    strain_L1, time_L1, chan_dict_L1 = rl.loaddata(fn_L1, 'L1')
except:
    print("Cannot find data files!")
    print("You can download them from https://www.gwosc.org/s/events/"+eventname)
    print("Quitting.")
    quit()

# number of sample for the fast fourier transform:
NFFT = 4*fs
Pxx_H1, freqs = mlab.psd(strain_H1, Fs = fs, NFFT = NFFT)
Pxx_L1, freqs = mlab.psd(strain_L1, Fs = fs, NFFT = NFFT)

# We will use interpolations of the ASDs computed above for whitening:
psd_H1 = interp1d(freqs, Pxx_H1)
psd_L1 = interp1d(freqs, Pxx_L1)

# both H1 and L1 will have the same time vector, so:
time = time_H1
# the time sample interval (uniformly sampled!)
dt = time[1] - time[0]


# TEST 1
def test_whiten():
	output = whiten(strain_H1,psd_H1,dt)
	assert len(strain_H1) == len(output), "length of the output array does not match the original one"
	
	
