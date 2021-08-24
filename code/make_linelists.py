#Author: Shivani Shah
#Adapted from Alex's code to make linelists
#input: the wavelength, element, dwav, the super master list
#output: a master list, 
import numpy as np
import funcdef as fd
import utils
import sys
from pandas import Series as pdS

base_path  = "/home/shivani/rprocess/Linelists/myAll"
 
def main():
    
    ll = fd.read() #Roederer
    fp1 = open("../data/allMasterList.txt", "w")
    fp1.write("wavelength, species, expot, loggf, type, filename\n")
    fmt1 = "{:7.2f}, {:>5.1f}, {:>+6.2f}, {:>+6.2f}, syn, {}\n"
    fp2 = open("make_linelists.sh", "w")
    fp2.write(r"#!/bin/bash"+"\n")
    fmt2 = "./awk_print_range.sh {} {} {} > {}\n"
    dwave = 5
    wav = ll["wav"] #panda series
    elemAr = ll["elem"]
    expotAr = ll["expot"]
    loggfAr = ll["loggf"]

    ##I am sure there is a reason I am using pandas to read the file. Can't remember what it is.
    ##But here is a long-drawn-out way to append new elements to the Roederer list
    
    #Adding other molecular band and other elements
    #To do: Create a file for these
    wavExt = pdS(data = [4313.0, 4323.0, 3876.0, 4217.0, 4225.0, 4237.0, 4371.0, 5165.0, 4737.0, 4940.0, 4050., 4090.0, 3986.0])
    elemExt = pdS(data = ["C-H", "C-H", "C-N", "C-H", "C-H", "C-H", "C-H", "C-H", "C-H", "C-H", "UII", "UII", "UII"]) #check this
    exportExt = pdS( data = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.0, 0.217, 0.652])
    loggfExt = pdS( data = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,-0.713, -0.377, -0.165])

    wav = pdS.append(wav, wavExt).values
    elemAr = pdS.append(elemAr, elemExt).values
    expotAr = pdS.append(expotAr, exportExt).values
    loggfAr = pdS.append(loggfAr, loggfExt).values
    
    for row in range(len(wav)):
        wave = wav[row]
        intwave = int(wave)
        roundwave = int(np.round(wave))

        
        elem = elemAr[row]
        print(elem)
        '''
        elemName = elem[0:2]
        elemIon = elem[2:]
        elemNew = elemName + " " + elemIon
        print(elemNew)
        '''
        #elem = smhutils.species_to_elements(species).split()[0]
        species, elemName = utils.element_to_species_my(elem)
        print(species)
        name = "{}{}.moog".format(elemName,intwave)
        print(name)

        expot, loggf = expotAr[row], loggfAr[row]
        #writing to create the master list 
        fp1.write(fmt1.format(wave, species, expot, loggf, base_path + "/" + name))
        
        #comment = "\"{}{}\"".format(name, row["comments"].strip())
        
        #writing to the sh file to create the linelist
        comment = "None"
        fp2.write(fmt2.format(roundwave-dwave, roundwave+dwave, comment, base_path + "/" + name))
    
    
if __name__ == "__main__":
    main()
