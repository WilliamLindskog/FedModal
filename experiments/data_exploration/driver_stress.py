
from os import listdir
from wfdb import rdsamp
from pandas import read_csv
from os.path import splitext

# Get path name
folder_name = './data/driver_stress/physionet.org/files/drivedb/1.0.0/'

# Read the data
all_signal=[]
meta_data=[]
for f in sorted(listdir(folder_name)):
    if f.endswith(".dat"):
        signals, fields = rdsamp(folder_name + splitext(f)[0])
        all_signal.append(signals)
        meta_data.append(fields)

print("Signal 1: ", all_signal[0])