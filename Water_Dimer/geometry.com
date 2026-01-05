%chk=geometry.chk
%mem=29GB  
%nprocshared=36   
#P PBE1PBE/aug-cc-pVDZ EmpiricalDispersion=GD3 NoSymm  
#P TD=(singlets,nstates=551) IOp(6/8=3) IOp(9/40=4) IOp(8/10=90)

Title Card Required

0 1
O          0.00000        0.00000        0.00000
H          0.76050       -0.58750        0.00000
H         -0.76050       -0.58750        0.00000
O          0.00000        0.00000        25.96100
H          0.00000        0.00000        25.00000
H          0.00000        0.93039        26.20200



