#Author: Shivani Shah
#Adapted from Alex's code to make linelists
#input: the wavelength, element, dwav, the super master list
#output: a master list, 
import numpy as np
import funcdef as fd
import utils
import sys
from pandas import Series as pdS


base_path  = "/home/shivani/rprocess/Linelists/synULines"
 
def main():
    
    iur = fd.read() #Roederer
    wav = iur["wav"] #panda series
    elemAr = iur["elem"]
    expotAr = iur["expot"]
    loggfAr = iur["loggf"]

    #s5 master and s5 extra master list
    #hack:some of the elements from s5 master and s5 master extra will be the same as in roederer.
    #but don't care about that since they will just be rewritten, just need to include the extra
    #lines for now
    #maybe fix this in future
    wavs5, speciess5, expots5, loggfs5 = fd.reads5()
    elems5 = [utils.species_to_element_my(spe) for spe in speciess5]
  
    
    fp1 = open("../data/allMasterList.txt", "w")
    fp1.write("wavelength, species, expot, loggf, type, filename\n")
    fmt1 = "{:7.2f}, {:>5.1f}, {:>+6.2f}, {:>+6.2f}, syn, {}\n"
    fp2 = open("make_linelists.sh", "w")
    fp2.write(r"#!/bin/bash"+"\n")
    fmt2 = "./awk_print_range.sh {} {} {} > {}\n"
    dwave = 5
   

    ##I am sure there is a reason I am using pandas to read the file. Can't remember what it is.
    ##But here is a long-drawn-out way to append new elements to the Roederer list
    
    #Adding other molecular band and other elements
    #To do: Create a file for these
    wavExt = pdS(data = [ 4050., 4090.0, 3986.0])
    elemExt = pdS(data = ["UII", "UII", "UII"]) #check this
    expotExt = pdS( data = [ 0.0, 0.217, 0.652])
    loggfExt = pdS( data = [-0.713, -0.377, -0.165])

    wav = pdS.append(wav, wavExt).values
    wav = np.concatenate((wav, wavs5))
    elemAr = pdS.append(elemAr, elemExt).values
    elemAr = np.concatenate((elemAr, elems5))
    expotAr = pdS.append(expotAr, expotExt).values
    expotAr = np.concatenate((expotAr, expots5))
    loggfAr = pdS.append(loggfAr, loggfExt).values
    loggfAr = np.concatenate((loggfAr, loggfs5))

    
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

    #write out some of the CH bands if they require a different range of wavelengths
    fp1.write(fmt1.format(4313, 106.0, np.nan, np.nan, base_path + "/CH4313.moog"))
    fp2.write(fmt2.format(4305, 4317, "None", base_path + "/CH4313.moog"))
    fp1.write(fmt1.format(5165, 106.0, np.nan, np.nan, base_path + "/CH5165.moog"))
    fp2.write(fmt2.format(5160, 5170, "None", base_path + "/CH5165.moog"))
    fp1.write(fmt1.format(4737, 106.0, np.nan, np.nan, base_path + "/CH4737.moog"))
    fp2.write(fmt2.format(4732, 4782, "None", base_path + "/CH4737.moog"))
    fp1.write(fmt1.format(4940, 106.0, np.nan, np.nan, base_path + "/CH4940.moog"))
    fp2.write(fmt2.format(4935, 4945, "None", base_path + "/CH4940.moog"))
    fp1.write(fmt1.format(4280, 106.0, np.nan, np.nan, base_path + "/CH4280.moog")) #not sure if this is supposed to be CH or C.
    fp2.write(fmt2.format(4275, 4285, "None", base_path + "/CH4280.moog")) #writing it out as CH for now cross check
   


    
if __name__ == "__main__":
    main()
