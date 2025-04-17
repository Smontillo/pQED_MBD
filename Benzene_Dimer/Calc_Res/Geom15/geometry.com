%chk=geometry.chk 
%mem=8GB 
%nprocshared=24 
#P PBE1PBE/aug-cc-pVDZ EmpiricalDispersion=GD3 NoSymm 
#P TD=(singlets,nstates=250) IOp(6/8=3) IOp(9/40=4) 

Geom 15

0 1
C    -1.2131    -0.6884    0.0
C    -1.2028    0.7064    0.0001
C    -0.0103    -1.3948    0.0
C    0.0104    1.3948    -0.0001
C    1.2028    -0.7063    0.0
C    1.2131    0.6884    0.0
H    -2.1577    -1.2244    0.0
H    -2.1393    1.2564    0.0001
H    -0.0184    -2.4809    -0.0001
H    0.0184    2.4808    0.0
H    2.1394    -1.2563    0.0001
H    2.1577    1.2245    0.0
C    4.8101    -0.69053    3.3
C    4.8204    0.70427    3.3
C    6.0129    -1.39693    3.3
C    6.0336    1.39267    3.3
C    7.226    -0.70843    3.3
C    7.2363    0.68627    3.3
H    3.8655    -1.22653    3.3
H    3.8839    1.25427    3.3
H    6.0048    -2.48303    3.3
H    6.0416    2.47867    3.3
H    8.1626    -1.25843    3.3
H    8.1809    1.22237    3.3



