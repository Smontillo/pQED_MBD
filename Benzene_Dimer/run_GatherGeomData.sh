mkdir Geom_data

grep -A 24 '0 1' geometry.com | tail -24 | awk {'print $1'} > Geom_data/atoms.dat  # Atomic symbols
grep -A 24 '0 1' geometry.com | tail -24 | awk {'print $2'} > Geom_data/Xcoor.dat  # X coordinate
grep -A 24 '0 1' geometry.com | tail -24 | awk {'print $3'} > Geom_data/Ycoor.dat  # Y coordinate
grep -A 24 '0 1' geometry.com | tail -24 | awk {'print $4'} > Geom_data/Zcoor.dat  # Z coordinate