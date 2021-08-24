# Linelists

IMP: See notes on super_master_list.moog

Description of the contents of the folder:
Code:
Adapted from Alex's code (https://www.dropbox.com/sh/6ffhe6uowd1qhmj/AAB3z2YCJrmr_iHykl4rQuoQa?dl=0) 
Steps: (1) run make_linelists.py (2) run make_linelists.sh (3) copy over content of myAll to myAllULines and make the required changes in the linelist		


    read function in funcdef.py reads in the Roederer file (used by make_linelist.py)
    utils.py from SMHr folder adapted (added a new function) to convert element to species (used by make_linelist.py). 		
    make_linelist.py: Creates the master list (using Roederer as the reference + additional molecular bands and UII lines that I have added manually in the script) called allMasterList.txt, which					will be compatible with SMHr
    		      Creates the make_linelist.sh file that can be implemented to create the linelists, which are stored in myAll folder
    super_master_list.moog: it is all synthesis lists created by linemake concatenated  to make one big list. Used by awk_print_range.sh. This is imported from linemake folder, forked from APJ's.
    			    Confirm that you have either the latest or the most stable version.
    awk_print_range.sh used by make_linelists.sh for obtaining the lines in specified wavelength ranges
    run_synthesis: performs automated synthetic fits (created by APJ, edited by S.S) given a ordered list of lines for e.g., s5_master_list.txt in data folder.

   

myAll folder: consists of all the linelists (following Roederer n-cap) 
myAllULines folder: Should be same as myAll folder except for following changes:
	    Change made to the logg value of La line at 4050. Value changed to 0.428 following this source: https://ui.adsabs.harvard.edu/abs/1996MNRAS.278..997B/abstract 

data:
one place for all the data

    Roederer-HD222925-ncap-linelist.txt: all n-cap transitions that are important
    myLInelist.txt: an on going compilation of lines not in Roederer (either found in Cain or found by me)
    allMasterList.txt: master transition list following Roederer's list compatible with SMHr (consists of elements that can be measured using EW -- need to fix this)
    RPA-lightelement-linelist-v5-20200831-moog.txt - light element linlist being used for U Lines project and RPA analysis
    s5_sorted_master_list.txt - an ordered list of lines to be fit using Alex's automated synthesis fit code (run_synthesis.py). Can use this as a reference to fit the lines. 
    s5_sorted_master_list_extra.txt - as above, but with extra lines. 
    C/* - different regions of C band -- this folder needs some cleaning
    N/* - N linelist -- this folder needs cleaning
    masseronDownloaded/*: CH masseron linelist downloaded from http://www.astro.ulb.ac.be/~spectrotools/. However, apparently, the corrected version is here http://cdsarc.u-strasbg.fr/viz-bin/qcat?J/A+A/571/A47
    chmasseron_fixed.moog: Masseron CH lines fixed by APJ in the MOOG format
    chmasseron_fixed_edited.moog: Masseron CH lines fixed by APJ, wavelength region trimmed by SS
    synthesisInfo.txt: Info on elements to synthesis, recommended steps, isotopic ratios to include/remove etc.,