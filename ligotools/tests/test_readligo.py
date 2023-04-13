from ligotools import readligo as rl
import pytest
import numpy as np

fn_H1 = 'data/H-H1_LOSC_4_V2-1126259446-32.hdf5'
fn_L1 = 'data/L-L1_LOSC_4_V2-1126259446-32.hdf5'

def test_loaddata():
    assert len(rl.loaddata(fn_H1, 'H1')) == 3
    
def test_loaddata_type1():
    assert type(rl.loaddata(fn_H1, 'H1')[0]).__module__ == np.__name__
    
def test_loaddata_type2():
    assert type(rl.loaddata(fn_H1, 'H1')[2]) == dict
    

def test_dq_channel_to_seglist():
    strain, time, chan_dict = rl.loaddata(fn_L1, 'H1')
    DQflag = 'CBC_CAT3'
    segment_list = rl.dq_channel_to_seglist(chan_dict[DQflag])
    assert type(segment_list[0]) == slice
    