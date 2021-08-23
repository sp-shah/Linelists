# Linelists
Description of the contents of the folder:
Code:
Adapted from Alex's code (https://www.dropbox.com/sh/6ffhe6uowd1qhmj/AAB3z2YCJrmr_iHykl4rQuoQa?dl=0) 

    read function in funcdef.py reads in the Roederer file
    Creates the master list (using Roederer as the reference) (make_linelist.py). master list called allMasterList.txt
    Creates the make_linelist.sh file that can be implemented to create the linelists, which are stored in myAll folder
    super_master_list.moog used in step 3. it is all synthesis lists created by linemake concatenated  to make one big list
    awk_print_range.sh used in step 3 for obtaining the lines in specified wavelength ranges
    utils.py from SMHr folder adapted to convert element to species 

myAll folder:
consists of all the linelists (following Roederer n-cap) - decided not to add this since it is very large. create using the code
data:
one place for all the data

    Roederer-HD222925-ncap-linelist.txt: all n-cap transitions that are imp
    super_master_list.moog
    myLInelist.txt: an on going compilation of lines not in Roederer (either found in Cain or found by me)
    allMasterList.txt: master transition list following Roederer's list compatible with SMHr (consists of elements that can be measured using EW -- need to fix this)


