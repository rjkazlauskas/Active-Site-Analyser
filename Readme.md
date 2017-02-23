##CONTENTS OF THIS FILE
-----------------------------
 
 * [Quickstart](##QUICKSTART)
 * Introduction
 * Requirements 
 * Configuration
 * Output
 * [TROUBLESHOOTING](##troubleshooting)

##QUICKSTART
----------------------------
This program reads through pdb files and returns atoms that are close to a
predifined active site residue specified by the user.  
To set up please follow the steps below:

* make sure Input.csv, which contains all the parameters is in the working directory

* using terminal, change directed (cd) into the folder that contains main.py and run the command "python main.py"
 
##INTRODUCTION
----------------------------
The goal of this program is to provide an extension of a current web-based consensus finder program (originally written by Bryan Jones) by identifying the regions near the active site using protein database (PDB) files.  
The current consensus finder returns substitutions throughout the amino acid sequence. To change the susbstrate specificity, researchers focus primarily on only the active site and in order to stabilize . 
The consensus finder is written in Python and protein database files can be read using the molecular visualization system PyMOL.

 * For a full description of the module, visit the project page:
	kazlab@umn.edu

 * For more information regarding Biopython modules, visit biopython's page:
	biopython.org

 * To submit bug reports and feature suggestions, or to track changes, email:
	kanxx030@umn.edu

##REQUIREMENTS
----------------------------
The current program can only be run locally on Windows or Mac OSX.  The program will later be added to web server so it will be accessible on any other systems such as Mac and Linux.
Python modules needed: {os, csv, numpy} (default, installed with Python 2.7 or 3.4) and Biopython (download available at biopython.org)
Package used: Anaconda

##CONFIGURATION
----------------------------
1.  Open terminal, change directory to where main.py is located using "cd" command 
2.  Make sure there is a file named "Input.csv" in the working directory by typing "ls" in terminal
3.  Make sure your "Input.csv" is formatted correctly, for example:

``` 
4EB0
A
84
3
```

specifies using PDB file with four-digit code 4EB0, chain A, residue 84 and 3 angstroms as search parameters.  Open program in an advanced text editor (BBEdit), or IDLE such as Pycharm and run the program.  The output of the program should be displayed and stored in a new folder named "Output"

##OUTPUT
----------------------------
A total of three output files should be found in the "output" folder.

```
simple_output.csv
residue_list.csv
detailed_output.csv
```

I suggest opening each of the files in Excel, as using normal text editors might cause the document to look a bit chaotic with all the commas that csv's have.  The contents of the csv's are described by their respective titles.  
**residue_list.csv** contains a list of residues in the structure.  Note that water is excluded and other substrates are listed at the bottom.
**simple_output and detailed_output** are the standard output files containing the closest atoms to the user-defined active site residue.  The simple output only shows the closest atoms from each residue, and other atoms are compiled as a list.  

## TROUBLESHOOTING
----------------------------
* "I can't run the program.  It's giving me some sort of error code."

First thing I would check is the if all the required folders and files are present.  An input.csv file is required to feed the program our search criteria.  I would also check if all the required Python libraries and modules are installed, since this program mainly relies on Bio.PDB.  

* "I am running this program but it is looping infinitely, what do I do?"

A simple "Ctrl+F" will break the infinite loop.  And please copy and paste the error message and send it to kanxx030@umn.edu.

* "How do I check my computer's python version?"

Go to terminal, type "Python -V" on a mac or type "python --version" on windows cmd

For other questions, please email rjk@umn.edu or kanxx030@umn.edu.  Thank you.  


