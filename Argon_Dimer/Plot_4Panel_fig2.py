import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
import matplotlib.colors as mcolors
# ================================================
direc  = ['X', 'Y', 'Z']
# ================================================
RScan_X = np.loadtxt('./Data/R_Scan_X.dat')
RScan_Y = np.loadtxt('./Data/R_Scan_Y.dat')
RScan_Z = np.loadtxt('./Data/R_Scan_Z.dat')
RScan_G = np.loadtxt('./Data/R_Scan_G.dat')
RDiff_X = np.loadtxt('./Data/R_Diff_X.dat')
RDiff_Z = np.loadtxt('./Data/R_Diff_Z.dat')
RDiff_pMBD_Z = np.loadtxt('./Data/R_Diff_pMBD_Z.dat')
RDiff_pMBD_X = np.loadtxt('./Data/R_Diff_pMBD_X.dat')
RDiff_CC_X =np.loadtxt('./Data/R_Diff_CC_X.dat')
RDiff_CC_Z =np.loadtxt('./Data/R_Diff_CC_Z.dat')

nEl_Con = np.loadtxt('./Data/nEl_Con.dat')
nF_Con  = np.loadtxt('./Data/nF_Con.dat')

TD_X   = np.loadtxt('./Data/3D_Energy_X.dat')
TD_Z   = np.loadtxt('./Data/3D_Energy_Z.dat')
TD_Pos = np.loadtxt('./Data/3D_Pos.dat')
TD_Nel = np.loadtxt('./Data/3D_Nel.dat')

refEn  = 1
print(f'Min. Value → {np.min(RScan_G[:,1]):.2f}') 
print(f'1 percent → {refEn:.2f}') 
lo, hi = -1, 1
levels = np.linspace(lo, hi, 500)
zD0   = 3.85
norm = mcolors.TwoSlopeNorm(vmin=lo, vcenter=0.0, vmax=hi)
fig, ax =  plt.subplots(2,2,figsize=(6,6))
# ================================================================
# CONVERGENCE DATA
# ================================================================
ax[0,0].axhline(refEn, lw = 1, ls = '-', c = 'black')
ax[0,0].axhline(-refEn, lw = 1, ls = '-', c = 'black')
ax[0,0].plot(nEl_Con[:,0], nEl_Con[:,1] - nEl_Con[-1,1],  lw = 2, ls = '-', label = f"{direc[0]}", c = '#3498db')
ax[0,0].plot(nEl_Con[:,0], nEl_Con[:,2] - nEl_Con[-1,2],  lw = 0.7, ls = '-', label = f"{direc[1]}", c = '#2ecc71')
ax[0,0].plot(nEl_Con[:,0], nEl_Con[:,3] - nEl_Con[-1,3],  lw = 2, ls = '-', label = f"{direc[2]}", c = '#e74c3c')
ax[0,0].set_xlabel(r'Electronic States, N$_\mathrm{el}$', fontsize=12)
ax[0,0].set_ylabel(r'$\Delta$E(R) $-$ $\Delta$E(R)$_{N_\mathrm{el}=431}$ (meV)', fontsize=12)
ax[0,0].set_xlim(nEl_Con[0,0],nEl_Con[-1,0])
ax[0,0].set_ylim(-10,80)
sub_ax = inset_axes(ax[0,0], width="60%", height="40%", loc=1)
sub_ax.axhline(refEn, lw = 1, ls = '-', c = 'black')
sub_ax.axhline(-refEn, lw = 1, ls = '-', c = 'black')
sub_ax.plot(nEl_Con[:,0], nEl_Con[:,1] - nEl_Con[-1,1],  lw = 1.5, ls = '-', label = f"{direc[0]}", c = '#3498db')
sub_ax.plot(nEl_Con[:,0], nEl_Con[:,2] - nEl_Con[-1,2],  lw = 1.5, ls = '-', label = f"{direc[0]}", c = '#2ecc71')
sub_ax.plot(nEl_Con[:,0], nEl_Con[:,3] - nEl_Con[-1,3],  lw = 1.5, ls = '-', label = f"{direc[0]}", c = '#e74c3c')
sub_ax.set_xlim(200,428)
sub_ax.set_ylim(-2,2)
sub_ax.set_yticks([-1,1])
sub_ax.tick_params(axis='y', labelsize=7) 
sub_ax.xaxis.set_visible(False)
mark_inset(ax[0,0], sub_ax, loc1=4, loc2=3, fc='none', ec='black', ls='--', lw = 0.7)
ax[0,1].axhline(refEn, lw = 1, ls = '-', c = 'black')
ax[0,1].axhline(-refEn, lw = 1, ls = '-', c = 'black')
ax[0,1].plot(nF_Con[:,0], nF_Con[:,1], lw = 2, ls = '-', marker = 'o', markersize = 3, label = f"{direc[0]}", c = '#3498db')
ax[0,1].plot(nF_Con[:,0], nF_Con[:,2], lw = 0.5, ls = '-', marker = 'o', markersize = 2, label = f"{direc[1]}", c = '#2ecc71')
ax[0,1].plot(nF_Con[:,0], nF_Con[:,3], lw = 2, ls = '-', marker = 'o', markersize = 3, label = f"{direc[2]}", c = '#e74c3c')
ax[0,1].set_xlabel(r'Fock States, N$_\mathrm{F}$', fontsize=12)
ax[0,1].set_ylabel(r'$\Delta$E(R) $-$ $\Delta$E(R)$_{N_\mathrm{F}=8}$ (meV)', fontsize=12)
ax[0,1].set_xlim(nF_Con[0,0],8)
ax[0,1].set_ylim(-2,4)
ax[0,1].set_xticks([2,4,6,8])
ax[1,0].text(4.4, 3.9, 'X Polarization', fontsize=10)
# ================================================================
# CONVERGENCE DATA 3D
# ================================================================
# -------- First subplot (X) --------
norm_x = TwoSlopeNorm(vmin=TD_X.min()*1000,
                      vcenter=0,
                      vmax=TD_X.max()*1000)
im1 = ax[1,0].imshow(TD_X.T * 1000, cmap='seismic', origin='lower',
                     extent=[TD_Pos[0], TD_Pos[-1], TD_Nel[0]/100, TD_Nel[-1]/100],
                     aspect='auto', norm=norm_x)
cbar1 = fig.colorbar(im1, ax=ax[1,0])
cbar1.ax.tick_params(labelsize=8)
ax[1,0].set_ylabel(r'Electronic States (x $10^2$)', fontsize=12)
ax[1,0].set_xlabel(r'Ar$-$Ar Distance, R ($\AA$)', fontsize=12)
ax[1,0].set_xticks([4,5,6,7])
# -------- Second subplot (Z) --------
norm_z = TwoSlopeNorm(vmin=TD_Z.min()*1000,
                      vcenter=0,
                      vmax=TD_Z.max()*1000)
im2 = ax[1,1].imshow(TD_Z.T * 1000, cmap='seismic', origin='lower',
                     extent=[TD_Pos[0], TD_Pos[-1], TD_Nel[0]/100, TD_Nel[-1]/100],
                     aspect='auto', norm=norm_z)
cbar2 = fig.colorbar(im2, ax=ax[1,1])
cbar2.set_label(r'$\Delta$E(R) $-$ $\Delta$E(R)$_{N_\mathrm{el}=431}$ (meV)', fontsize=10)
cbar2.ax.tick_params(labelsize=8)
ax[1,1].set_xlabel(r'Ar$-$Ar Distance, R ($\AA$)', fontsize=12)
ax[1,1].tick_params(axis='x')
ax[1,1].tick_params( axis='y')
ax[1,1].set_xticks([4,5,6,7])

ax[1,1].text(4.4, 3.9, 'Z Polarization', fontsize=10)

fsize = 13
fig.text(0, 0.99, f'(a)', fontsize=fsize)
fig.text(0, 0.48, f'(c)', fontsize=fsize)
fig.text(0.48, 0.99, f'(b)', fontsize=fsize)
fig.text(0.48, 0.48, f'(d)', fontsize=fsize)

plt.tight_layout(pad=0.1)
plt.savefig('./Images/ArgonData_fig2.png', dpi = 300, bbox_inches = 'tight')
