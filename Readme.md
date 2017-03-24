##CONTENTS OF THIS FILE
-----------------------------
 
 * [Quickstart](##Quickstart)
 * [Introduction](##Introduction)
 * [Requirements](#Requirements) 
 * [Configuration](#Configuration)
 * [Output](#Output)
 * [Troubleshooting](#Troubleshooting)

## <a name="Quickstart"></a>Quickstart
----------------------------
This program reads through pdb files and returns atoms that are close to a
a residue specified by the user.  
To run:

* input parameters should be in a file named input.csv in the working directory _input is capitalized below; does this matter?_
* _needs more about the results of consensus finder needed_
* using terminal, change the working directory to the directory that contains main.py and run the command "python main.py"
 
## <a name="Introduction"></a>Introduction
----------------------------
This program extends the program consensus finder program (written by Bryan Jones) by identifying the regions near the active site.  Consensus finder identifies allowed amino acid substitutions throughout a given amino acid sequence. Sometimes one would like to avoid changes in the substrate binding region (goal is protein stabilization); other times one would prefer changes in the substrate binding region (goal is changing substrate specificity). Active site finder allows users to choose the subset of the consensus finder results that are most appropriate.  
Active site finder is written in Python. Protein database files can be read using the molecular visualization program PyMOL.

 * For a full description of the module, visit the project page:
	kazlab@umn.edu

 * For more information regarding Biopython modules, visit biopython's page:
	biopython.org

 * To submit bug reports and feature suggestions, or to track changes, email:
	kanxx030@umn.edu

## <a name="Requirements"></a>Requirements
----------------------------
The current program runs locally on Windows or Mac OSX. A web-based version is planned.
The program uses Python modules: {os, csv, numpy}, which are installed by default with Python 2.7 or 3.4, and Biopython (download available at biopython.org)
Package used: Anaconda _not clear if this is relevant_

## <a name="Configuration"></a>Configuration
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

specifies using PDB file with four-digit code 4EB0, chain A, residue 84 and 3 angstroms as search parameters.  
4. Open program in an advanced text editor (BBEdit), or IDLE such as Pycharm and run the program.  The output of the program should be displayed and stored in a new folder named "Output"

## <a name="Output"></a>Output
----------------------------
A total of three output files should be found in the "output" folder.

```
simple_output.csv
residue_list.csv
detailed_output.csv
```

Open the files in Excel. (cvs files can look chaotic in a text editor.)
**residue_list.csv** lists all residues in the structure, including substrates or heteroatoms.  Water is excluded.
**simple_output** lists the closest atoms from each residue, and other atoms are compiled as a list. _need clearer explanation of the simple and detailed output._
**detailed_output** list the standard output files containing the closest atoms to the user-defined active site residue.   

## <a name="Troubleshooting"></a>Troubleshooting
----------------------------
* "I can't run the program.  It's giving me some sort of error code."

Check that all the required folders and files are present.  An input.csv file is required to feed the program our search criteria. _confusing - required file in mentioned, but what folders are required?_  
Check if all the required Python libraries and modules are installed, since this program mainly relies on Bio.PDB _Bio.PDB is never mentioned above; above modules are mentioned, but libraries are not_.  

* "I am running this program but it is looping infinitely, what do I do?"

"Ctrl+F" will break the infinite loop.  Please copy and paste the error message and send it to kanxx030@umn.edu.

* "How do I check my computer's python version?"  _why would I need to do this?_

On a mac:
```
Python -V
```
On Windows cmd:
```
python --version
```

For other questions, please email rjk@umn.edu or kanxx030@umn.edu.  Thank you.  
