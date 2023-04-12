from ligotools import readligo as rl

fn_H1 = 'data/H-H1_LOSC_4_V2-1126259446-32.hdf5'
fn_L1 = 'data/L-L1_LOSC_4_V2-1126259446-32.hdf5'

def loaddata_test():
    assert len(rl.loaddata(fn_H1, 'H1')) == 3

def dq_channel_to_seglist_test():
    strain, time, chan_dict = rl.loaddata(fn_L1, 'H1')
    DQflag = 'CBC_CAT3'
    segment_list = rl.dq_channel_to_seglist(chan_dict[DQflag])
    assert type(segment_list[0]) == 'slice'
    