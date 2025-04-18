import numpy as np
import matplotlib.pyplot as plt
import subprocess as sp
# ================================================
nm2eV  = 1239.84193
Ha2eV  = 27
# ================================================
# SCAN INFORMATION
# ================================================
direc  = ['X', 'Y', 'Z']
B0     = 3.2
dx     = 0.16
Bf     = 8.16
steps  = int((Bf - B0)/dx)
Binf   = int((25 - B0)/dx)
# ==========================================
λmin   = 0.0
λmax   = 0.05
dλ     = 0.05
nλ     = int((λmax - λmin)/dλ) + 1
λlist  = [λmin + x * dλ for x in range(nλ)]   # List of coupling strengths
# ========================================== 
Pos    = [B0 + x * dx for x in range(steps)]  # x-coordinate data
En_X = np.zeros(((steps),nλ))               # Polariton Energies
En_Y = np.zeros(((steps),nλ))               # Polariton Energies
En_Z = np.zeros(((steps),nλ))               # Polariton Energies
for k in range((steps)):
    En_X[k,:] = np.loadtxt(f"Calc_Res/Geom{k}/X_pol/Polariton_data.dat")[:,1]
    En_Y[k,:] = np.loadtxt(f"Calc_Res/Geom{k}/Y_pol/Polariton_data.dat")[:,1]
    En_Z[k,:] = np.loadtxt(f"Calc_Res/Geom{k}/Z_pol/Polariton_data.dat")[:,1]

fig, ax =  plt.subplots(figsize=(3,3))
ax.axhline(0, ls = '--', lw = 0.5, c = 'black')
ax.plot(Pos[:-1], (En_X[:-1,0] - En_X[-1,0]) * 1000,  lw = 2, ls = '-', marker = 'o', markersize = 3, c = 'black')
for t in range(nλ - 1):
    ax.plot(Pos[:-1], (En_X[:-1,t+1] - En_X[-1,t+1]) * 1000,  lw = 2, ls = '-', marker = 'o', markersize = 3, label = f"{direc[0]}", c = '#3498db')
    ax.plot(Pos[:-1], (En_Y[:-1,t+1] - En_Y[-1,t+1]) * 1000,  lw = 0.5, ls = '-', marker = 'o', markersize = 1, label = f"{direc[1]}", c = '#27ae60')
    ax.plot(Pos[:-1], (En_Z[:-1,t+1] - En_Z[-1,t+1]) * 1000,  lw = 2, ls = '-', marker = 'o', markersize = 3, label = f"{direc[2]}", c = '#e74c3c')
ax.set_xlabel(r'$Ar - Ar$ ($\AA$)')
ax.set_ylabel(r'E (meV)')
ax.set_ylim(-25,3)
ax.set_xlim(3,7.8)
ax.legend(frameon = False, fontsize = 7, ncol = 3, title = r'Polarization', title_fontsize='7')
plt.savefig('./images/Pol_PES.png', dpi = 300, bbox_inches = 'tight')
plt.close()