import numpy as np
import subprocess as sp
import os
# ===========================================
Atoms = np.loadtxt('./Geom_data/atoms.dat', dtype = str)
Xcoor = np.loadtxt('./Geom_data/Xcoor.dat')
Ycoor = np.loadtxt('./Geom_data/Ycoor.dat')
Zcoor = np.loadtxt('./Geom_data/Zcoor.dat')

X0    = 0
Xf    = 8
dx    = 0.4
Nst   = int((Xf - X0)/dx)
point = [X0 + dx * k for k in range(Nst)]
point.append(25)
print(len(point)-1)
try:
    os.makedirs(f"./Calc_Res")
except: 
    pass# print('Geometry Folder exist')
os.chdir(f"./Calc_Res")

for geom in range( Nst+1 ):
    try:
        os.makedirs(f"./Geom{geom}")
    except : pass
    os.chdir(f"./Geom{geom}")
    FILE01 = open("geometry.com","w")
    FILE01.write( "%chk=geometry.chk "+ "\n" )
    FILE01.write( "%mem=8GB "+ "\n" )
    FILE01.write( "%nprocshared=24 "+ "\n" )
    FILE01.write( "#P PBE1PBE/aug-cc-pVDZ EmpiricalDispersion=GD3 NoSymm "+ "\n" )
    FILE01.write( "#P TD=(singlets,nstates=250) IOp(6/8=3) IOp(9/40=4) "+ "\n" )
    FILE01.write( "\n" )
    FILE01.write(f"Geom {geom}"+ "\n" )
    FILE01.write( "\n" )
    FILE01.write( "0 1" + "\n" )
    for at in range( len(Atoms) ):
        print
        if at < 12:
            FILE01.write( Atoms[at] + "    " + np.round(Xcoor[at],4).astype(str) + "    " + (Ycoor[at]).astype(str) + "    " + (Zcoor[at]).astype(str) + "\n" )
        else:
            FILE01.write( Atoms[at] + "    " + np.round(Xcoor[at] + point[geom],4).astype(str) + "    " + (Ycoor[at]).astype(str) + "    " + (Zcoor[at]).astype(str) + "\n" )
    FILE01.write( "\n" )
    FILE01.write( "\n" )
    FILE01.write( "\n" )
    
    FILE01.close()
    os.chdir(f"../")