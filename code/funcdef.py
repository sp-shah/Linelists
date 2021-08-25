import numpy as np
import pandas
import sys



def read():
    f = pandas.read_table('/home/shivani/rprocess/lineLists/Roederer-HD222925-ncap-linelist.txt', delim_whitespace=True, 
                          header=None,
                          skiprows = 22,
                          usecols = range(4),
                          engine='python',
                          names = ["elem", "wav", "expot", "loggf"])

    return f

def reads5():
    filePaths5 = "/home/shivani/rprocess/Linelists/data/s5_sorted_master_list.txt"
    dats5 = np.genfromtxt(filePaths5, usecols = (0,1,2,3), names = ["wav","species", "expot", "loggf"], delimiter = ",", skip_header = True)
    filePaths5Ext = "/home/shivani/rprocess/Linelists/data/s5_sorted_master_list_extra.txt"
    dats5Ext = np.genfromtxt(filePaths5Ext, usecols = (0,1,2,3), names = ["wav","species", "expot", "loggf"], delimiter = ",", skip_header = True)

    wav = np.concatenate((dats5["wav"], dats5Ext["wav"]))
    species = np.concatenate((dats5["species"], dats5Ext["species"]))
    expot = np.concatenate((dats5["expot"], dats5Ext["expot"]))
    loggf = np.concatenate((dats5["loggf"], dats5Ext["loggf"]))

    
    return wav, species, expot, loggf

if __name__ == "__main__":
    read()
