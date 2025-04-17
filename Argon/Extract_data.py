import numpy as np
import matplotlib.pyplot as plt
import subprocess as sp
# ================================================
nm2eV  = 1239.84193
Ha2eV  = 27
# ================================================
# SCAN INFORMATION
# ================================================
direc  = 'X'
B0     = 3.2
dx     = 0.16
Bf     = 8.0
steps  = int((Bf - B0)/dx)
Binf   = int((25 - B0)/dx)
states = 10
# ==========================================
λmin   = 0.0
λmax   = 0.1
dλ     = 0.05
nλ     = int((λmax - λmin)/dλ) + 1
λlist  = [λmin + x * dλ for x in range(nλ)]   # List of coupling strengths
# ========================================== 
Pos    = [B0 + x * dx for x in range(steps)]  # x-coordinate data
En_Cav = np.zeros((steps+1,nλ))               # Polariton Energies
for k in range(steps):
    En_Cav[k,:] = np.loadtxt(f"Calc_Res/Geom{k}/PF_run/Polariton_data.dat")[:,1]
En_Cav[-1,:] = np.loadtxt(f"Calc_Res/Geom{Binf}/PF_run/Polariton_data.dat")[:,1]  # Energy reference point

fig, ax =  plt.subplots(figsize=(3,3))
for t in range(nλ):
    ax.plot(Pos, (En_Cav[:-1,t] - En_Cav[-1,t]) * 1000,  lw = 1, ls = '-', marker = 'o', markersize = 2, label = f"{np.round(λlist[t],2)}")
ax.set_xlabel(r'$Ar - Ar$ ($\AA$)')
ax.set_ylabel(r'E (meV)')
ax.set_ylim(-25,3)
ax.set_xlim(3.3,8)
ax.set_title(f'{direc} polarization', fontsize = 11)
ax.legend(frameon = False, fontsize = 7, ncol = 2, title = r'$\lambda$ (a.u.)', title_fontsize='7')
plt.savefig('./images/Pol_PES.png', dpi = 300, bbox_inches = 'tight')
plt.close()

np.savetxt(f'./{direc}pol_data.dat', np.c_[Pos,(En_Cav[:-1,:] - En_Cav[-1,:]) * 1000])
