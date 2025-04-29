import numpy as np
import matplotlib.pyplot as plt
import subprocess as sp
import Parameters as par
# ================================================
nm2eV  = 1239.84193
Ha2eV  = 27
# ================================================
# SCAN INFORMATION
# ================================================
direc  = ['X', 'Y', 'Z']
steps  = int((par.Bf0 - par.B)/par.dx) 
Binf   = int((par.Bref - par.B)/par.dx)
nlist  = [steps, Binf]
nlist.append(Binf)
print(steps)
# ==========================================
nSt0   = par.nSt0
nStf   = par.nStf
dSt    = par.dSt
nSt    = int((nStf - nSt0)/dSt) + 1
Slist  = [nSt0 + x * dSt for x in range(nSt)] 
# ==========================================
λmin   = float(par.lam_MIN)
λmax   = float(par.lam_MAX)
dλ     = float(par.dlam)
nλ     = int((λmax - λmin)/dλ) + 1
λlist  = [λmin + x * dλ for x in range(nλ)]   # List of coupling strengths
# ========================================== 
Pos    = [par.B + x * par.dx for x in range(steps+1)]  # x-coordinate data
En_X = np.zeros(((2), nSt, nλ))               # Polariton Energies
En_Y = np.zeros(((2), nSt, nλ))               # Polariton Energies
En_Z = np.zeros(((2), nSt, nλ))               # Polariton Energies
for k in range((2)):
    for m in range(nSt):
        En_X[k,m,:] = np.loadtxt(f"Calc_Res/Geom{nlist[k]}/nSt_{m}/X_pol/Polariton_data.dat")[:,1]
        En_Y[k,m,:] = np.loadtxt(f"Calc_Res/Geom{nlist[k]}/nSt_{m}/Y_pol/Polariton_data.dat")[:,1]
        En_Z[k,m,:] = np.loadtxt(f"Calc_Res/Geom{nlist[k]}/nSt_{m}/Z_pol/Polariton_data.dat")[:,1]

fig, ax =  plt.subplots(2,1,figsize=(3,3), sharex = True)
# ax.axhline(0, ls = '--', lw = 0.5, c = 'black')
for t in range(1):
    ax[0].plot(Slist, (En_X[0,:,t+1] - En_X[0,0,t+1]) * 1000,  lw = 2, ls = '-', marker = 'o', markersize = 3, label = f"{direc[0]}", c = '#3498db')
    ax[0].plot(Slist, (En_Y[0,:,t+1] - En_Y[0,0,t+1]) * 1000,  lw = 0.5, ls = '-', marker = 'o', markersize = 1, label = f"{direc[1]}", c = '#27ae60')
    ax[0].plot(Slist, (En_Z[0,:,t+1] - En_Z[0,0,t+1]) * 1000,  lw = 2, ls = '-', marker = 'o', markersize = 3, label = f"{direc[2]}", c = '#e74c3c')
    ax[1].plot(Slist, (En_X[1,:,t+1] - En_X[1,0,t+1]) * 1000,  lw = 2, ls = '-', marker = 'o', markersize = 3, c = '#3498db')
    ax[1].plot(Slist, (En_Y[1,:,t+1] - En_Y[1,0,t+1]) * 1000,  lw = 0.5, ls = '-', marker = 'o', markersize = 1, c = '#27ae60')
    ax[1].plot(Slist, (En_Z[1,:,t+1] - En_Z[1,0,t+1]) * 1000,  lw = 2, ls = '-', marker = 'o', markersize = 3, c = '#e74c3c')
# ax.plot(Pos[:-1], (En_X[:-1,0,0] - En_X[-1,0,0]) * 1000,  lw = 2, ls = '-', marker = 'o', markersize = 3, c = 'black')
ax[1].set_xlabel(r'Electronic States')
ax[0].set_ylabel(r'E (meV)')
ax[1].set_ylabel(r'E (meV)')
ax[0].set_title('Eq. Geometry', fontsize = 6)
ax[1].set_title('Ref. Geometry', fontsize = 6)
# ax.set_ylim(-25,3)
# ax.set_xlim(3,7.8)
ax[0].legend(frameon = False, fontsize = 7, ncol = 1, title = r'Polarization', title_fontsize='7')
plt.savefig('./images/Pol_PES.png', dpi = 300, bbox_inches = 'tight')
plt.close()