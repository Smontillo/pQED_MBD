import numpy as np
import matplotlib.pyplot as plt
import subprocess as sp
# ================================================
Ha2eV  = 27
# ================================================
# SCAN INFORMATION
# ================================================
direc  = ['X', 'Y', 'Z']
B0     = 3.2
dx     = 0.05
Bf     = 8.02
steps  = int((Bf - B0)/dx)
Binf   = int((25 - B0)/dx)
# ==========================================
λmin   = 0.0
λmax   = 0.1
dλ     = 0.025
nλ     = int((λmax - λmin)/dλ) + 1
λlist  = [λmin + x * dλ for x in range(nλ)]   # COUPLING STRENGTH LIST
print(λlist)
# ========================================== 
Pos    = [B0 + x * dx for x in range(steps)]  # X COORDINATE DATA
En_X   = np.zeros(((steps),nλ))               # POLARITON ENERGY X POLARIZATION
En_Y   = np.zeros(((steps),nλ))               # POLARITON ENERGY Y POLARIZATION
En_Z   = np.zeros(((steps),nλ))               # POLARITON ENERGY Z POLARIZATION
for k in range((steps)):
    En_X[k,:] = np.loadtxt(f"Calc_Res/Geom{k}/X_pol/Polariton_data.dat")[:,1]
    En_Y[k,:] = np.loadtxt(f"Calc_Res/Geom{k}/Y_pol/Polariton_data.dat")[:,1]
    En_Z[k,:] = np.loadtxt(f"Calc_Res/Geom{k}/Z_pol/Polariton_data.dat")[:,1]
# ================================================================
# DIFFERENCE WITH RESPECT THE REFERENCE GEOMETRY
# ================================================================
DiffE_G = (En_X[:-1,0] - En_X[-1,0]) * 1000
DiffE_X = (En_X[:-1,:] - En_X[-1,:]) * 1000
DiffE_Y = (En_Y[:-1,:] - En_Y[-1,:]) * 1000
DiffE_Z = (En_Z[:-1,:] - En_Z[-1,:]) * 1000
# ================================================================
# LOAD REFERENCE DATA 
# ================================================================
data_CC     = np.loadtxt('./data_CC.dat')                       # COUPLED CLUSTERS QED DATA
data_pMBD   = np.loadtxt('./data_pMBD.dat')                     # PMBD DATA
# ================================================================
# DIFFERENCE WITH RESPECT THE REFERENCE GEOMETRY
# ================================================================
CC_Diff_G   = (data_CC[:-1,1] - data_CC[-1,1]) * 1000 * Ha2eV  
CC_Diff_X   = (data_CC[:-1,2] - data_CC[-1,2]) * 1000 * Ha2eV
CC_Diff_Y   = (data_CC[:-1,3] - data_CC[-1,3]) * 1000 * Ha2eV
CC_Diff_Z   = (data_CC[:-1,4] - data_CC[-1,4]) * 1000 * Ha2eV
pMBD_Diff_G = (data_pMBD[:-1,1] - data_pMBD[-1,1]) * 1000 * Ha2eV
pMBD_Diff_X = (data_pMBD[:-1,2] - data_pMBD[-1,2]) * 1000 * Ha2eV
pMBD_Diff_Y = (data_pMBD[:-1,3] - data_pMBD[-1,3]) * 1000 * Ha2eV
pMBD_Diff_Z = (data_pMBD[:-1,4] - data_pMBD[-1,4]) * 1000 * Ha2eV
# ================================================================
# PLOTTING (SIDE BY SIDE PLOT)
# ================================================================
print(f'Ground Energy Minima ->  {np.min(DiffE_G):.2f} meV at R = {Pos[np.argmin(DiffE_G)]:.2f} Å')
print(f'X Polariton Energy Minima ->  {np.min(DiffE_X[:,-1]):.2f} meV at R = {Pos[np.argmin(DiffE_X[:,-1])]:.2f} Å')
print(f'Z Polariton Energy Minima ->  {np.min(DiffE_Z[:,-1]):.2f} meV at R = {Pos[np.argmin(DiffE_Z[:,-1])]:.2f} Å')
# PES SCAN PLOT
fig, ax =  plt.subplots(1,2,figsize=(6,3))
ax[0].axhline(0, ls = '-', lw = 1, c = 'black')
ax[0].plot(Pos[:-1], DiffE_G,  lw = 2, ls = '-', c = 'black')
ax[0].plot(Pos[:-1], DiffE_X[:,2],  lw = 2, ls = '-', label = f"{direc[0]}", c = '#3498db')
ax[0].plot(Pos[:-1], DiffE_Y[:,2],  lw = 1, ls = '--', label = f"{direc[1]}", c = '#2ecc71')
ax[0].plot(Pos[:-1], DiffE_Z[:,2],  lw = 2, ls = '-', label = f"{direc[2]}", c = '#e74c3c')
for t in range(3,5):
    ax[0].plot(Pos[:-1], DiffE_X[:,t],  lw = 2, ls = '-', c = '#3498db')
    ax[0].plot(Pos[:-1], DiffE_Y[:,t],  lw = 1, ls = '--', c = '#2ecc71')
    ax[0].plot(Pos[:-1], DiffE_Z[:,t],  lw = 2, ls = '-', c = '#e74c3c')
ax[0].set_xlabel(r'Ar - Ar ($\AA$)')
ax[0].set_ylabel(r'$\Delta$E(R) (meV)')
ax[0].set_ylim(-25,10)
ax[0].set_xlim(3.2,7.8)
ax[0].legend(frameon = False, fontsize = 7, ncol = 3, title = r'Polarization', title_fontsize='7', handlelength=1.4)
# DIFFERENCE WITH RESPECT TO λ = 0 PLOT
ax[1].axhline(0, ls = '-', lw = 1, c = 'black')
ax[1].plot(Pos[:-1], DiffE_X[:,2] - DiffE_G,  lw = 2, ls = '-', label = f"{direc[0]}", c = '#3498db')
ax[1].plot(Pos[:-1], DiffE_Z[:,2] - DiffE_G,  lw = 2, ls = '-', label = f"{direc[2]}", c = '#e74c3c')
ax[1].plot(data_CC[:-1,0], CC_Diff_X - CC_Diff_G, ls = '--', lw = 2, c = '#3498db' )
ax[1].plot(data_CC[:-1,0], CC_Diff_Z - CC_Diff_G, ls = '--', lw = 2, c = '#e74c3c' )
ax[1].plot(data_pMBD[:-1,0], pMBD_Diff_X - pMBD_Diff_G, ls = ' ', marker = 'o', markevery=4, markersize=3, markeredgecolor='black', markeredgewidth=0.5, c = '#3498db', alpha = 0.7)
ax[1].plot(data_pMBD[:-1,0], pMBD_Diff_Z - pMBD_Diff_G, ls = ' ', marker = 'o', markevery=4, markersize=3, markeredgecolor='black', markeredgewidth=0.3, c = '#e74c3c', alpha = 0.7)
ax[1].set_xlabel(r'Ar - Ar ($\AA$)')
ax[1].set_ylabel(r'$\Delta$E(R) - $\Delta$E(R)$_{\lambda=0}$ (meV)')
ax[1].set_ylim(-5,10)
ax[1].set_yticks([-5,0,5,10])
ax[1].set_xlim(3.2,7.8)
ax2 = ax[1].twinx()
ax2.plot(np.NaN, np.NaN, ls= '-', lw=1, label='pQED', c='black')
ax2.plot(np.NaN, np.NaN, ls= '--', lw = 1,label='QED-CC', c='black')
ax2.plot(np.NaN, np.NaN, ls= ' ', marker = 'o', markersize=2,label='pMBD', c='black')
ax2.get_yaxis().set_visible(False)
ax2.legend(loc=0, frameon = False, ncol=1, fontsize = 7, title='Method', title_fontsize='7', handlelength=1.4)
ax[0].grid()
ax[1].grid()
plt.tight_layout()
plt.savefig('./Images/Position_Scan.png', dpi = 300, bbox_inches = 'tight')
plt.close()


np.savetxt('../Data/R_Scan_X.dat', np.c_[Pos[:-1],DiffE_X[:,2:]])
np.savetxt('../Data/R_Scan_Y.dat', np.c_[Pos[:-1],DiffE_Y[:,2:]])
np.savetxt('../Data/R_Scan_Z.dat', np.c_[Pos[:-1],DiffE_Z[:,2:]])
np.savetxt('../Data/R_Scan_G.dat', np.c_[Pos[:-1],DiffE_G])
np.savetxt('../Data/R_Diff_X.dat', np.c_[Pos[:-1], DiffE_X[:,2] - DiffE_G])
np.savetxt('../Data/R_Diff_Z.dat', np.c_[Pos[:-1], DiffE_Z[:,2] - DiffE_G])
np.savetxt('../Data/R_Diff_pMBD_Z.dat', np.c_[data_pMBD[:-1,0], pMBD_Diff_Z - pMBD_Diff_G])
np.savetxt('../Data/R_Diff_pMBD_X.dat', np.c_[data_pMBD[:-1,0], pMBD_Diff_X - pMBD_Diff_G])
np.savetxt('../Data/R_Diff_CC_X.dat', np.c_[data_CC[:-1,0], CC_Diff_X - CC_Diff_G])
np.savetxt('../Data/R_Diff_CC_Z.dat', np.c_[data_CC[:-1,0], CC_Diff_Z - CC_Diff_G])
