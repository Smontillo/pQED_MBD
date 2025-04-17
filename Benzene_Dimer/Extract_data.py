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
B0    = 0
Bf    = 8
dx    = 0.4
Nst   = int((Bf - B0)/dx)
steps = [B0 + dx * k for k in range(Nst)]
steps.append(25)
# ==========================================
λmin   = 0.0
λmax   = 0.05
dλ     = 0.05
nλ     = int((λmax - λmin)/dλ) + 1
λlist  = [λmin + x * dλ for x in range(nλ)]   # List of coupling strengths
# ========================================== 
En_X = np.zeros((len(steps),nλ))               # Polariton Energies
En_Y = np.zeros((len(steps),nλ))               # Polariton Energies
En_Z = np.zeros((len(steps),nλ))               # Polariton Energies
for k in range(len(steps)):
    En_X[k,:] = np.loadtxt(f"Calc_Res/Geom{k}/X_pol/Polariton_data.dat")[:,1]
    En_Y[k,:] = np.loadtxt(f"Calc_Res/Geom{k}/Y_pol/Polariton_data.dat")[:,1]
    En_Z[k,:] = np.loadtxt(f"Calc_Res/Geom{k}/Z_pol/Polariton_data.dat")[:,1]

fig, ax =  plt.subplots(figsize=(3,3))
ax.axhline(0, ls = '--', lw = 0.5, c = 'black')
ax.plot(steps[:-1], (En_X[:-1,0] - En_X[-1,0]) * 1,  lw = 2, ls = '-', marker = 'o', markersize = 3, c = 'black')
for t in range(nλ - 1):
    ax.plot(steps[:-1], (En_X[:-1,t+1] - En_X[-1,t+1]) * 1,  lw = 2, ls = '-', marker = 'o', markersize = 3, label = f"{direc[0]}", c = '#3498db')
    ax.plot(steps[:-1], (En_Y[:-1,t+1] - En_Y[-1,t+1]) * 1,  lw = 2, ls = '-', marker = 'o', markersize = 3, label = f"{direc[1]}", c = '#27ae60')
    ax.plot(steps[:-1], (En_Z[:-1,t+1] - En_Z[-1,t+1]) * 1,  lw = 2, ls = '-', marker = 'o', markersize = 3, label = f"{direc[2]}", c = '#e74c3c')
ax.set_xlabel(r'$Ar - Ar$ ($\AA$)')
ax.set_ylabel(r'E (eV)')
# ax.set_ylim(-25,3)
ax.set_xlim(0,8)
ax.legend(frameon = False, fontsize = 7, ncol = 3, title = r'Polarization', title_fontsize='7')
plt.savefig('./images/Pol_PES.png', dpi = 300, bbox_inches = 'tight')
plt.close()

np.savetxt(f'./{direc[0]}pol_data.dat', np.c_[steps[:-1],(En_X[:-1,:] - En_X[-1,:]) * 1000])
np.savetxt(f'./{direc[1]}pol_data.dat', np.c_[steps[:-1],(En_Z[:-1,:] - En_Z[-1,:]) * 1000])
