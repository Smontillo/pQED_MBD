import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset
import matplotlib.image as mpimg
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset
import matplotlib.colors as mcolors
import matplotlib.patheffects as pe
# ================================================
direc  = ['X', 'Y', 'Z']
# ================================================
RScan_X = np.loadtxt('./Data/R_Scan_X.dat')
RScan_Y = np.loadtxt('./Data/R_Scan_Y.dat')
RScan_Z = np.loadtxt('./Data/R_Scan_Z.dat')
RScan_G = np.loadtxt('./Data/R_Scan_G.dat')
RDiff_X = np.loadtxt('./Data/R_Diff_X.dat')
RDiff_Y = np.loadtxt('./Data/R_Diff_Y.dat')
RDiff_Z = np.loadtxt('./Data/R_Diff_Z.dat')
RDiff_pMBD_Z = np.loadtxt('./Data/R_Diff_pMBD_Z.dat')
RDiff_pMBD_X = np.loadtxt('./Data/R_Diff_pMBD_X.dat')
RDiff_pMBD_Y = np.loadtxt('./Data/R_Diff_pMBD_Y.dat')
pMBD         = np.loadtxt('./Data/pMBD_Data.dat')

Den_X        = np.loadtxt('./Data/Density3D_X.dat')
Den_Z        = np.loadtxt('./Data/Density3D_Z.dat')
Den_Pos      = np.loadtxt('./Data/Density3D_Pos.dat')

nEl_Con = np.loadtxt('./Data/nEl_Con.dat')
nF_Con  = np.loadtxt('./Data/nF_Con.dat')

refEn  = 1 
lo, hi = - 1, 1
levels = np.linspace(lo, hi, 500)
norm = mcolors.TwoSlopeNorm(vmin=lo, vcenter=0.0, vmax=hi)
fig, ax =  plt.subplots(3,2,figsize=(6,8),constrained_layout=True)
# ================================================================
# R COORDINATE DATA
# ================================================================
ax[0,0].axhline(0, ls = '-', lw = 1, c = 'black')
ax[0,0].plot(RScan_G[:,0], RScan_G[:,1],  lw = 2, ls = '-', marker = 'o', markersize = 3, c = 'black')
ax[0,0].plot(RScan_G[:,0], RScan_X[:,1],  lw = 2, ls = '-', marker = 'o', markersize = 3, label = f"{direc[0]}", c = '#3498db')
ax[0,0].plot(RScan_G[:,0], RScan_Y[:,1],  lw = 2, ls = '-', marker = 'o', markersize = 3, label = f"{direc[1]}", c = '#2ecc71')
ax[0,0].plot(RScan_G[:,0], RScan_Z[:,1],  lw = 2, ls = '-', marker = 'o', markersize = 3, label = f"{direc[2]}", c = '#e74c3c')
ax[0,0].set_xlabel(r'Bz$-$Bz Slip Coordinate, R ($\AA$)')
ax[0,0].set_ylabel(r'$\Delta$E(R) (meV)')
ax[0,0].set_xlim(0,8)
ax[0,0].set_ylim(-200,100)
ax[0,0].legend(frameon = False, fontsize = 10, ncol = 3, title = r'Polarization', title_fontsize='11', handlelength=1.4, loc = 'lower right',handletextpad=0.5,columnspacing=0.5)
xcoor = 1.5
ycoor = 35
ax[0,0].annotate('', xy=(xcoor, ycoor), xycoords='data', xytext=(60, 60), textcoords='offset pixels',
                 arrowprops=dict(arrowstyle='<|-,head_width=0.16, head_length=0.35', lw=3.0, color='#2ecc71', joinstyle='miter', capstyle='butt', shrinkA=0, shrinkB=0, mutation_scale=10))
ax[0,0].annotate('', xy=(xcoor, ycoor), xycoords='data', xytext=(0,100), textcoords='offset pixels',
                 arrowprops=dict(arrowstyle='<|-,head_width=0.16, head_length=0.35', lw=3.0, color='#e74c3c', joinstyle='miter', capstyle='butt', shrinkA=0, shrinkB=0, mutation_scale=10))
ax[0,0].annotate('', xy=(xcoor, ycoor), xycoords='data', xytext=(100, 0), textcoords='offset pixels',
                 arrowprops=dict(arrowstyle='<|-,head_width=0.16, head_length=0.35', lw=3.0, color='#3498db', joinstyle='miter', capstyle='butt', shrinkA=0, shrinkB=0, mutation_scale=10))
ax[0,0].annotate('', xy=(6.7, 74), xycoords='data', xytext=(55, 0), textcoords='offset pixels',
                 arrowprops=dict(arrowstyle='<|-,head_width=0.15, head_length=0.3', lw=2.0, color='#3498db', joinstyle='miter', capstyle='butt', shrinkA=0, shrinkB=0, mutation_scale=10))
img = mpimg.imread('./Images/Benzene3.png')
ax_inset = ax[0,0].inset_axes([0.38, 0.60, 0.44, 0.44])
ax_inset.imshow(img)
ax_inset.axis('off')
# DIFFERENCE WITH RESPECT TO λ = 0 PLOT
ax[0,1].axhline(0, ls = '-', lw = 1, c = 'black')
ax[0,1].plot(RScan_G[:,0], RDiff_X[:,1], lw = 2, marker = 'o', markersize = 3, ls = '-', label = f"{direc[0]}", c = '#3498db')
ax[0,1].plot(RScan_G[:,0], RDiff_Z[:,1], lw = 2, marker = 'o', markersize = 3, ls = '-', label = f"{direc[2]}", c = '#e74c3c')
ax[0,1].plot(RScan_G[:,0], RDiff_Y[:,1], lw = 2, marker = 'o', markersize = 3, ls = '-', label = f"{direc[2]}", c = '#2ecc71')
ax[0,1].plot(pMBD[:,0], pMBD[:,2] - pMBD[:,1], ls = '--', lw = 2, c = '#3498db' )
ax[0,1].plot(pMBD[:,0], pMBD[:,-1] - pMBD[:,1], ls = '--', lw = 2, c = '#e74c3c' )
ax[0,1].plot(pMBD[:,0], pMBD[:,3] - pMBD[:,1], ls = '--', lw = 2, c = '#2ecc71' )
ax[0,1].set_xlabel(r'Bz$-$Bz Slip Coordinate, R ($\AA$)')
ax[0,1].set_ylabel(r'$\Delta$E(R) - $\Delta$E(R)$_{\lambda=0}$ (meV)')
ax[0,1].set_xlim(0,8)
ax[0,1].set_ylim(-50,70)
ax[0,1].set_yticks(np.arange(-50,90,20))
ax2 = ax[0,1].twinx()
ax2.plot(np.NaN, np.NaN, ls= '-', lw=1, marker='o', markersize=3,label='pQED', c='black')
ax2.plot(np.NaN, np.NaN, ls= '--', lw = 1,label='pMBD', c='black')
ax2.get_yaxis().set_visible(False)
ax2.legend(loc=0, frameon = False, ncol=2, fontsize = 10, title='Method', title_fontsize='11', handlelength=1.4, handletextpad=0.5,columnspacing=0.5)

X,Y = np.meshgrid( Den_Pos[:,0], Den_Pos[:,1] )
from mpl_toolkits.axes_grid1 import make_axes_locatable

ann = ax[1,0].annotate('', xy=(-3.2, -1.6), xycoords='data', xytext=(0,100), textcoords='offset pixels',
                 arrowprops=dict(arrowstyle='<|-,head_width=0.18, head_length=0.37', lw=3.0, color='#e74c3c', joinstyle='miter', capstyle='butt', shrinkA=0, shrinkB=0, mutation_scale=10))
ann2 = ax[1,0].annotate('', xy=(-3.2, -1.6), xycoords='data', xytext=(100, 0), textcoords='offset pixels',
                 arrowprops=dict(arrowstyle='<|-,head_width=0.18, head_length=0.37', lw=3.0, color='#3498db', joinstyle='miter', capstyle='butt', shrinkA=0, shrinkB=0, mutation_scale=10))

ann.arrow_patch.set_path_effects([
    pe.Stroke(linewidth=4, foreground='black'),
    pe.Normal()
])
ann2.arrow_patch.set_path_effects([
    pe.Stroke(linewidth=4, foreground='black'),
    pe.Normal()
])

ann = ax[1,1].annotate('', xy=(-3.2, -1.6), xycoords='data', xytext=(0,100), textcoords='offset pixels',
                 arrowprops=dict(arrowstyle='<|-,head_width=0.18, head_length=0.37', lw=3.0, color='#e74c3c', joinstyle='miter', capstyle='butt', shrinkA=0, shrinkB=0, mutation_scale=10))
ann2 = ax[1,1].annotate('', xy=(-3.2, -1.6), xycoords='data', xytext=(100, 0), textcoords='offset pixels',
                 arrowprops=dict(arrowstyle='<|-,head_width=0.18, head_length=0.37', lw=3.0, color='#3498db', joinstyle='miter', capstyle='butt', shrinkA=0, shrinkB=0, mutation_scale=10))

ann.arrow_patch.set_path_effects([
    pe.Stroke(linewidth=4, foreground='black'),
    pe.Normal()
])
ann2.arrow_patch.set_path_effects([
    pe.Stroke(linewidth=4, foreground='black'),
    pe.Normal()
])

# --- your two contourf calls (left and right) ---
cntr_left  = ax[1,0].contourf(X, Y, np.clip(Den_X, lo,hi), levels=levels, cmap='seismic', norm=norm, extend='neither')
cntr_right = ax[1,1].contourf(X, Y, np.clip(Den_Z, lo,hi), levels=levels, cmap='seismic', norm=norm, extend='neither')
ax[1,0].set_ylabel("Z Coordinate, R ($\AA$)")
ax[1,0].set_xlabel("Bz$-$Bz Slip Coordinate, R ($\\AA$)")
ax[1,1].set_xlabel("Bz$-$Bz Slip Coordinate, R ($\\AA$)")
ax[1,0].set_ylim(-2,6)
ax[1,1].set_ylim(-2,6)
ax[1,0].set_xlim(-3.6,4.4)
ax[1,1].set_xlim(-3.6,4.4)
ax[1,0].set_yticks([-2,0,2,4])
ax[1,1].set_yticks([-2,0,2,4])
ax[1,0].text(-2, 5.3, f'X Polarization', fontsize=12)
ax[1,1].text(-2, 5.3, f'Z Polarization', fontsize=12)
# --- make a colorbar axis to the RIGHT of ax[1,1] ---
div1 = make_axes_locatable(ax[1,1])
cax  = div1.append_axes("right", size="3.5%", pad=0.03)

# (important) add an invisible spacer of the SAME size to ax[1,0]
# so both bottom subplots keep equal widths
# div0 = make_axes_locatable(ax[1,0])
# _    = div0.append_axes("right", size="3.5%", pad=0.04, visible=False)

# --- single colorbar shared by the two bottom plots (mappable can be either contour) ---
cbar = fig.colorbar(cntr_right, cax=cax, ticks=[lo, 0, hi])
cbar.set_label(r"$\Delta\rho_{00}(\mathrm{x,z})$ (m|e|/Å²)", fontsize=10)
cbar.ax.tick_params(labelsize=8)   # tick labels size = 10

zD0  = 1.94
rO   = 1.9166 - 0.9618
rH   = 2.2909 - 0.9618

MW = 2
MS = 12
TO = 2
MS_H = 8
ax[1,0].plot(-1.2028, 0, marker='o', markersize=MS-TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(-1.2028, 0, marker='o', markersize=MS+TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(-1.2028, 0, marker='o', markersize=MS, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(0.0104,0, marker='o', markersize=MS-TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(0.0104,0, marker='o', markersize=MS+TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(0.0104,0, marker='o', markersize=MS, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(1.2131,0, marker='o', markersize=MS+TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(1.2131,0, marker='o', markersize=MS-TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(1.2131,0, marker='o', markersize=MS, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(-2.1393,0, marker='o', markersize=MS_H+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(-2.1393,0, marker='o', markersize=MS_H-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(-2.1393,0, marker='o', markersize=MS_H, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(0.0184,0,marker='o', markersize=MS_H+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(0.0184,0,marker='o', markersize=MS_H-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(0.0184,0,marker='o', markersize=MS_H, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(2.1577,0,marker='o', markersize=MS_H+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(2.1577,0,marker='o', markersize=MS_H-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(2.1577,0,marker='o', markersize=MS_H, color='white', fillstyle='none', markeredgewidth=MW)

ax[1,0].plot(0.5972, 3.3, marker='o', markersize=MS-TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(0.5972, 3.3, marker='o', markersize=MS+TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(0.5972, 3.3, marker='o', markersize=MS, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(1.8104,3.3, marker='o', markersize=MS-TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(1.8104,3.3, marker='o', markersize=MS+TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(1.8104,3.3, marker='o', markersize=MS, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(3.0131,3.3, marker='o', markersize=MS+TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(3.0131,3.3, marker='o', markersize=MS-TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(3.0131,3.3, marker='o', markersize=MS, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(-0.3393,3.3, marker='o', markersize=MS_H+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(-0.3393,3.3, marker='o', markersize=MS_H-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(-0.3393,3.3, marker='o', markersize=MS_H, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(1.8184,3.3,marker='o', markersize=MS_H+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(1.8184,3.3,marker='o', markersize=MS_H-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(1.8184,3.3,marker='o', markersize=MS_H, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(3.9577,3.3,marker='o', markersize=MS_H+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(3.9577,3.3,marker='o', markersize=MS_H-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(3.9577,3.3,marker='o', markersize=MS_H, color='white', fillstyle='none', markeredgewidth=MW)

ax[1,1].plot(-1.2028, 0, marker='o', markersize=MS-TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(-1.2028, 0, marker='o', markersize=MS+TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(-1.2028, 0, marker='o', markersize=MS, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(0.0104,0, marker='o', markersize=MS-TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(0.0104,0, marker='o', markersize=MS+TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(0.0104,0, marker='o', markersize=MS, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(1.2131,0, marker='o', markersize=MS+TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(1.2131,0, marker='o', markersize=MS-TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(1.2131,0, marker='o', markersize=MS, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(-2.1393,0, marker='o', markersize=MS_H+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(-2.1393,0, marker='o', markersize=MS_H-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(-2.1393,0, marker='o', markersize=MS_H, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(0.0184,0,marker='o', markersize=MS_H+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(0.0184,0,marker='o', markersize=MS_H-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(0.0184,0,marker='o', markersize=MS_H, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(2.1577,0,marker='o', markersize=MS_H+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(2.1577,0,marker='o', markersize=MS_H-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(2.1577,0,marker='o', markersize=MS_H, color='white', fillstyle='none', markeredgewidth=MW)

ax[1,1].plot(0.5972, 3.3, marker='o', markersize=MS-TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(0.5972, 3.3, marker='o', markersize=MS+TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(0.5972, 3.3, marker='o', markersize=MS, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(1.8104,3.3, marker='o', markersize=MS-TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(1.8104,3.3, marker='o', markersize=MS+TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(1.8104,3.3, marker='o', markersize=MS, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(3.0131,3.3, marker='o', markersize=MS+TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(3.0131,3.3, marker='o', markersize=MS-TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(3.0131,3.3, marker='o', markersize=MS, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(-0.3393,3.3, marker='o', markersize=MS_H+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(-0.3393,3.3, marker='o', markersize=MS_H-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(-0.3393,3.3, marker='o', markersize=MS_H, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(1.8184,3.3,marker='o', markersize=MS_H+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(1.8184,3.3,marker='o', markersize=MS_H-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(1.8184,3.3,marker='o', markersize=MS_H, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(3.9577,3.3,marker='o', markersize=MS_H+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(3.9577,3.3,marker='o', markersize=MS_H-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(3.9577,3.3,marker='o', markersize=MS_H, color='white', fillstyle='none', markeredgewidth=MW)

ax[0,1].text(5, -45, f'$\lambda=0.05$', fontsize=12)

# ================================================================
# CONVERGENCE DATA
# ================================================================
ax[2,0].axhline(refEn, lw = 1, ls = '-', c = 'black')
ax[2,0].axhline(-refEn, lw = 1, ls = '-', c = 'black')
ax[2,0].plot(nEl_Con[:,0], nEl_Con[:,1] - nEl_Con[-1,1],  lw = 2, ls = '-', label = f"{direc[0]}", c = '#3498db')
ax[2,0].plot(nEl_Con[:,0], nEl_Con[:,2] - nEl_Con[-1,2],  lw = 0.7, ls = '-', label = f"{direc[1]}", c = '#2ecc71')
ax[2,0].plot(nEl_Con[:,0], nEl_Con[:,3] - nEl_Con[-1,3],  lw = 2, ls = '-', label = f"{direc[2]}", c = '#e74c3c')
ax[2,0].set_xlabel(r'Electronic States, N$_\mathrm{el}$ (x 10$^{3}$)')
ax[2,0].set_ylabel(r'$\Delta$E(R) - $\Delta$E(R)$_{N_{el}=10^3}$ (meV)')
ax[2,0].set_xlim(nEl_Con[0,0],nEl_Con[-1,0])
ax[2,0].set_ylim(-80,80)
# ax[2,0].set_xticks([100,200,300,400])
ax[2,0].set_yticks(np.arange(-80,100,40))
sub_ax = inset_axes(ax[2,0], width="55%", height="35%", loc=4)
sub_ax.axhline(refEn, lw = 1, ls = '-', c = 'black')
sub_ax.axhline(-refEn, lw = 1, ls = '-', c = 'black')
sub_ax.plot(nEl_Con[:,0], nEl_Con[:,1] - nEl_Con[-1,1],  lw = 1.5, ls = '-', label = f"{direc[0]}", c = '#3498db')
sub_ax.plot(nEl_Con[:,0], nEl_Con[:,2] - nEl_Con[-1,2],  lw = 1.5, ls = '-', label = f"{direc[0]}", c = '#2ecc71')
sub_ax.plot(nEl_Con[:,0], nEl_Con[:,3] - nEl_Con[-1,3],  lw = 1.5, ls = '-', label = f"{direc[0]}", c = '#e74c3c')
sub_ax.set_xlim(6,9.95)
sub_ax.set_ylim(-2,2)
sub_ax.set_yticks([-1,0,1])
sub_ax.tick_params(axis='y', labelsize=7) 
sub_ax.xaxis.set_visible(False)
mark_inset(ax[2,0], sub_ax, loc1=1, loc2=2, fc='none', ec='black', ls='--', lw = 0.7)
ax[2,1].axhline(refEn, lw = 1, ls = '-', c = 'black')
ax[2,1].axhline(-refEn, lw = 1, ls = '-', c = 'black')
ax[2,1].plot(nF_Con[:,0], nF_Con[:,1], lw = 2, ls = '-', marker = 'o', markersize = 3, label = f"{direc[0]}", c = '#3498db')
ax[2,1].plot(nF_Con[:,0], nF_Con[:,2], lw = 2, ls = '-', marker = 'o', markersize = 2, label = f"{direc[1]}", c = '#2ecc71')
ax[2,1].plot(nF_Con[:,0], nF_Con[:,3], lw = 2, ls = '-', marker = 'o', markersize = 3, label = f"{direc[2]}", c = '#e74c3c')
ax[2,1].set_xlabel(r'Fock States, N$_\mathrm{F}$')
ax[2,1].set_ylabel(r'$\Delta$E(R) - $\Delta$E(R)$_{N_F=6}$ (meV)')
ax[2,1].set_xlim(nF_Con[0,0],6)
ax[2,1].set_ylim(-18,12)
ax[2,1].set_yticks(np.arange(-18,14,6))

fsize = 13
fig.text(0, 0.97, f'(a)', fontsize=fsize)
fig.text(0, 0.64, f'(c)', fontsize=fsize)
fig.text(0.51, 0.97, f'(b)', fontsize=fsize)
fig.text(0.51, 0.64, f'(d)', fontsize=fsize)
fig.text(0, 0.32, f'(e)', fontsize=fsize)
fig.text(0.51, 0.31, f'(f)', fontsize=fsize)
# plt.tight_layout(pad=0.1)
plt.savefig('./Images/BenzeneDimerData.pdf', dpi = 300, bbox_inches = 'tight')