#Author: Shivani Shah
#Adapted from Alex's code to make linelists
#input: the wavelength, element, dwav, the super master list
#output: a master list, 
import numpy as np
import funcdef as fd
import utils
import sys

base_path  = "/home/shivani/rprocess/lineLists/myAll"
 
def main():
    
    ll = fd.read() #Roederer
    fp1 = open("allMasterList.txt", "w")
    fp1.write("wavelength, species, expot, loggf, type, filename\n")
    fmt1 = "{:7.2f}, {:>5.1f}, {:>+6.2f}, {:>+6.2f}, syn, {}\n"
    fp2 = open("make_linelists.sh", "w")
    fp2.write(r"#!/bin/bash"+"\n")
    fmt2 = "./awk_print_range.sh {} {} {} > {}\n"
    dwave = 5
    wav = ll["wav"]
    elemAr = ll["elem"]
    expotAr = ll["expot"]
    loggfAr = ll["loggf"]
    
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
        name =  "{}{}.moog".format(elemName,intwave)
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
