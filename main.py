#Program is written and developed by Enoch Kan
#Kazlauskas Lab, Department of Biochemistry, Molecular Biology and Biophysics
#University of Minnesota, Twin Cities; Fall 2016
#Copyright (c) Enoch Kan 2016
#File OS
import os;import csv;import numpy as np;from Bio.PDB import PDBList;from Bio.PDB import PDBParser
filebase=os.path.dirname(os.path.realpath(__file__))
outfilebase=filebase+'/output'
if not os.path.exists(outfilebase):
    os.makedirs(outfilebase)
#Arrays
atr=[];val=[];csvlist=[];ares=[];resname=[];rescode=[];heteroname=[];heterocode=[];atomlist=[];atomnamelist=[];hitnum_list=[];hitting=[]
sort1=[];sort2=[];sort3=[];sort4=[];sort5=[]
#Reading info
with open('Input.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if len (row) != 0:
            csvlist = csvlist + [row]
csvfile.close()
##val[]
##0:PDB ID
##1:Chain (default A)r
##2: Residue
##3: Distance
select = csvlist[0][0];achn=csvlist[1][0];mk=csvlist[3][0]
for i in range(0, len(csvlist[2])):
    ares.append(csvlist[2][i])
#Opening the file
pdbl = PDBList()
pdbl.retrieve_pdb_file(select,pdir='pdb')
file_path=filebase+'/pdb/pdb'+select+'.ent'
#Read the file
parser=PDBParser(QUIET=1)
structure=parser.get_structure('test', file_path)
#Residue Info
rf = open(os.path.join(outfilebase, "residue_list"+'.csv'), 'wt')
reswriter = csv.writer(rf, lineterminator='\n')
reswriter.writerow(["-------------------------------------------------------------------"])
reswriter.writerow(["-------------------------------------------------------------------"])
model = structure[0];chain = model[achn]
for res in chain.get_residues():
    tags = res.get_full_id()
    if res.get_resname() != 'HOH' and tags[3][0] == " ":
        resname.append(res.get_resname())
        resid = res.get_id()
        rescode.append(resid[1])
reswriter.writerow(["A total of"+" "+str(len(resname))+" "+"residues in chain "+achn])
for i in range(0, len(resname), 10):
    reswriter.writerow(["["+str(rescode[i])+"]"+" "+" ".join([str(v) for v in resname[i:i+10]])])
reswriter.writerow(["-------------------------------------------------------------------"])
reswriter.writerow(["-------------------------------------------------------------------"])
reswriter.writerow(["List of Heteroatoms: "])
for res in chain.get_residues():
    tags = res.get_full_id()
    if res.get_resname() != 'HOH' and tags[3][0] != " ":
        heteroname.append(res.get_resname())
        resid = res.get_id()
        heterocode.append(resid[1])
for i in range(0, len(heteroname), 10):
    reswriter.writerow(["["+str(heterocode[i])+"]"+" "+ " ".join([str(v) for v in heteroname[i:i+10]])])
sf = open(os.path.join(outfilebase, "simple_output"+'.csv'), 'wt')
df = open(os.path.join(outfilebase, "detailed_output"+'.csv'), 'wt')
try:
    writer = csv.writer(sf, lineterminator='\n')
    writer2= csv.writer(df, lineterminator='\n')
    for i in range(0,len(ares)):
        a=int(ares[i])
        m=int(mk)
        #Search with active site residue
        model1 = structure [0]
        chain1 = model1 [achn]
        residue1 = chain1 [a]
        res1id=residue1.get_id()
        for atom in residue1:
            atomnamelist.append(atom.get_name())
        for atom in residue1:
            atomlist.append(atom.get_vector())
        for i in range(0, len(atomlist)):
            for model in structure:
                for chain in model:
                    for residue in chain:
                        for atom in residue:
                            dist = np.linalg.norm(atom.get_vector()-atomlist[i])
                            if dist <= m:
                                resid1=residue.get_id()
                                rdist=round(dist, 2)
                                if residue.get_resname() != 'HOH':
                                    if resid1[1] != a:
                                        sort1.append((residue.get_resname(), resid1[1], atom.get_name(), rdist, residue1.get_resname(), res1id[1], atomnamelist[i]))
                                        sort1=sorted(sort1, key=lambda e: (e[3]))
        for i in range(0, len(ares)):
            writer2.writerow(['Residue Number: '+ares[i]])
        writer2.writerow(['Residue','Distance','Origin'])
        for i in range(0, len(sort1)):
            writer2.writerow([sort1[i][0]+" "+str(sort1[i][1])+" "+sort1[i][2],sort1[i][3],sort1[i][4] + " " + str(sort1[i][5]) + " " + sort1[i][6]])
            if sort1[i][1] not in sort2:
                sort2.append(sort1[i][1])
                sort3.append(sort1[i])
            else:
                sort4.append(sort1[i])
                sort4=sorted(sort4, key=lambda e: (e[1]))
        writer.writerow(['Residue',' ',' ','Distance','Origin', ' ', ' ', 'Other Atoms'])
        for i in range(0, len(sort3)):
            num = sort3[i][1]
            for r in range(0, len(sort4)):
                if sort4[r][1] == num:
                    if sort4[r][2] not in sort5:
                        if sort4[r][2] != sort3[i][2]:
                            sort5.append(sort4[r][2])
            writer.writerow([sort3[i][0],str(sort3[i][1]),sort3[i][2],sort3[i][3],residue1.get_resname(),a,sort3[i][6],','.join(sort5)])
            del sort5[:]
finally:
    sf.close()
    df.close()

