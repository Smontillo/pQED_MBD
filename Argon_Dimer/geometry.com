%chk=geometry.chk
%mem=10GB
%nprocshared=12

#p PBE1PBE/aug-cc-pVDZ EmpiricalDispersion=GD3
#p TD=(singlets,nstates=432) IOp(6/8=3, 9/40=4, 8/10=90)

Title Card Required

0 1
Ar         0.00000        0.00000       0.00000         
Ar         0.00000        0.00000       4.00000      



