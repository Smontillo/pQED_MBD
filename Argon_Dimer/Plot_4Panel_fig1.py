import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
import matplotlib.colors as mcolors
from matplotlib.patches import Ellipse
import matplotlib.patheffects as pe
# ================================================
direc  = ['X', 'Y', 'Z']
# ================================================
RScan_X      = np.loadtxt('./Data/R_Scan_X.dat')
RScan_Y      = np.loadtxt('./Data/R_Scan_Y.dat')
RScan_Z      = np.loadtxt('./Data/R_Scan_Z.dat')
RScan_G      = np.loadtxt('./Data/R_Scan_G.dat')
RDiff_X      = np.loadtxt('./Data/R_Diff_X.dat')
RDiff_Z      = np.loadtxt('./Data/R_Diff_Z.dat')
RDiff_pMBD_Z = np.loadtxt('./Data/R_Diff_pMBD_Z.dat')
RDiff_pMBD_X = np.loadtxt('./Data/R_Diff_pMBD_X.dat')
RDiff_CC_X   = np.loadtxt('./Data/R_Diff_CC_X.dat')
RDiff_CC_Z   = np.loadtxt('./Data/R_Diff_CC_Z.dat')
Den_X        = np.loadtxt('./Data/Density3D_X.dat')
Den_Z        = np.loadtxt('./Data/Density3D_Z.dat')
Den_Pos      = np.loadtxt('./Data/Density3D_Pos.dat')

nEl_Con = np.loadtxt('./Data/nEl_Con.dat')
nF_Con  = np.loadtxt('./Data/nF_Con.dat')

TD_X   = np.loadtxt('./Data/3D_Energy_X.dat')
TD_Z   = np.loadtxt('./Data/3D_Energy_Z.dat')
TD_Pos = np.loadtxt('./Data/3D_Pos.dat')
TD_Nel = np.loadtxt('./Data/3D_Nel.dat')

refEn  = 1 
lo, hi = -1, 1
levels = np.linspace(lo, hi, 500)
zD0   = 3.85
norm = mcolors.TwoSlopeNorm(vmin=lo, vcenter=0.0, vmax=hi)

fig, ax =  plt.subplots(2,2,figsize=(6,6))
# ================================================================
# R COORDINATE DATA
# ================================================================
ax[0,0].axhline(0, ls = '-', lw = 1, c = 'black')
ax[0,0].plot(RScan_G[:,0], RScan_G[:,1],  lw = 2, ls = '-', c = 'black')
ax[0,0].plot(RScan_G[:,0], RScan_X[:,1],  lw = 2, ls = '-', label = f"{direc[0]}", c = '#3498db')
ax[0,0].plot(RScan_G[:,0], RScan_Y[:,1],  lw = 1, ls = '--', label = f"{direc[1]}", c = '#2ecc71')
ax[0,0].plot(RScan_G[:,0], RScan_Z[:,1],  lw = 2, ls = '-', label = f"{direc[2]}", c = '#e74c3c')
for t in range(2,4):
    ax[0,0].plot(RScan_G[:,0], RScan_X[:,t],  lw = 2, ls = '-', c = '#3498db')
    ax[0,0].plot(RScan_G[:,0], RScan_Y[:,t],  lw = 1, ls = '--', c = '#2ecc71')
    ax[0,0].plot(RScan_G[:,0], RScan_Z[:,t],  lw = 2, ls = '-', c = '#e74c3c')
ax[0,0].set_xlabel(r'Ar$-$Ar Distance, R ($\AA$)', fontsize=10)
ax[0,0].set_ylabel(r'$\Delta$E(R) (meV)', fontsize=10)
ax[0,0].set_ylim(-25,10)
ax[0,0].set_xlim(3.2,7.8)
ax[0,0].set_xticks([4,5,6,7])
ax[0,0].legend(frameon = False, fontsize = 10, ncol = 3, title = r'Polarization', title_fontsize='10', handlelength=1.4, handletextpad=0.5,columnspacing=0.5, loc='lower right')
ax[0,0].annotate('', xy=(5.5, -13), xycoords='data', xytext=(0,100), textcoords='offset pixels',
                 arrowprops=dict(arrowstyle='<|-,head_width=0.18, head_length=0.37', lw=3.0, color='#e74c3c', joinstyle='miter', capstyle='butt', shrinkA=0, shrinkB=0, mutation_scale=10))
ax[0,0].annotate('', xy=(5.5, -13), xycoords='data', xytext=(100, 0), textcoords='offset pixels',
                 arrowprops=dict(arrowstyle='<|-,head_width=0.18, head_length=0.37', lw=3.0, color='#2ecc71', joinstyle='miter', capstyle='butt', shrinkA=0, shrinkB=0, mutation_scale=10))
ax[0,0].annotate('', xy=(5.5, -13), xycoords='data', xytext=(-60, -60), textcoords='offset pixels',
                 arrowprops=dict(arrowstyle='<|-,head_width=0.18, head_length=0.37', lw=3.0, color='#3498db', joinstyle='miter', capstyle='butt', shrinkA=0, shrinkB=0, mutation_scale=10))
# ax[0,0].plot(5.5, -13, 'o', c='black')
img = mpimg.imread('./Images/ArgonDimer.png')
ax_inset = ax[0,0].inset_axes([0.75, 0.49, 0.16, 0.16])
ax_inset.imshow(img)
ax_inset.axis('off')
ax_inset.text(0.5, 0.5, 'Ar',color='black', fontsize=9,
              ha='center', va='center',
              transform=ax_inset.transAxes)  # 
ax_inset = ax[0,0].inset_axes([0.75, 0.25, 0.16, 0.16])
ax_inset.imshow(img)
ax_inset.axis('off')
ax_inset.text(0.5, 0.5, 'Ar', color='black', fontsize=9,
              ha='center', va='center',
              transform=ax_inset.transAxes)  # (0–1) coordinates of the inset
ax[0,0].text(4.2, -16, r'$\lambda = 0.1$', transform=ax[0,0].transData,
             rotation=64, ha='left', va='center', fontsize=9)
ax[0,0].text(4.0, -8.6, r'$\lambda = 0$', transform=ax[0,0].transData,
             rotation=53, ha='left', va='center', fontsize=9)
ax[0,0].text(4.8, 5, r'$\lambda = 0.1$', transform=ax[0,0].transData,
             rotation=-13, ha='left', va='center', fontsize=9)
# DIFFERENCE WITH RESPECT TO λ = 0 PLOT
ax[0,1].axhline(0, ls = '-', lw = 1, c = 'black')
ax[0,1].plot(RScan_G[:,0], RDiff_X[:,1],  lw = 2, ls = '-', label = f"{direc[0]}", c = '#3498db')
ax[0,1].plot(RScan_G[:,0], RDiff_Z[:,1],  lw = 2, ls = '-', label = f"{direc[2]}", c = '#e74c3c')
ax[0,1].plot(RDiff_pMBD_X[:,0], RDiff_pMBD_X[:,1], ls = '--', lw = 2, c = '#3498db' )
ax[0,1].plot(RDiff_pMBD_X[:,0], RDiff_pMBD_Z[:,1], ls = '--', lw = 2, c = '#e74c3c' )
ax[0,1].plot(RDiff_CC_X[:,0], RDiff_CC_X[:,1], ls = ' ', marker = 'o', markevery=2, markersize=3, markeredgecolor='black', markeredgewidth=0.5, c = '#3498db', alpha = 0.7)
ax[0,1].plot(RDiff_CC_X[:,0], RDiff_CC_Z[:,1], ls = ' ', marker = 'o', markevery=2, markersize=3, markeredgecolor='black', markeredgewidth=0.5, c = '#e74c3c', alpha = 0.7)
ax[0,1].set_xlabel(r'Ar$-$Ar Distance, R ($\AA$)', fontsize=10)
ax[0,1].set_ylabel(r'$\Delta$E(R) $-$ $\Delta$E(R)$_{\lambda=0}$ (meV)', fontsize=10)
ax[0,1].set_ylim(-5,10)
ax[0,1].set_yticks([-5,0,5,10])
ax[0,1].set_xticks([4,5,6,7])
ax[0,1].set_xlim(3.2,7.8)
ax[0,1].text(6.2,-4.5, r'$\lambda = 0.05$', fontsize=10)
ax2 = ax[0,1].twinx()
ax2.plot(np.NaN, np.NaN, ls= '-', lw=2, label='pQED', c='black')
ax2.plot(np.NaN, np.NaN, ls= '--', lw = 2,label='pMBD', c='black')
ax2.plot(np.NaN, np.NaN, ls= ' ', marker = 'o', markersize=2,label='QED-CC', c='black')
ax2.get_yaxis().set_visible(False)
ax2.legend(loc=0, frameon = False, ncol=1, fontsize = 10, title='Method', title_fontsize=10, handlelength=1.4, handletextpad=0.5,columnspacing=0.5)
# ================================================================
# CONVERGENCE DATA 3D
# ================================================================
X,Y = np.meshgrid( Den_Pos[:,0], Den_Pos[:,1] )
from mpl_toolkits.axes_grid1 import make_axes_locatable

ann = ax[1,0].annotate('', xy=(-1.8, -1.6), xycoords='data', xytext=(0,100), textcoords='offset pixels',
                 arrowprops=dict(arrowstyle='<|-,head_width=0.18, head_length=0.37', lw=3.0, color='#e74c3c', joinstyle='miter', capstyle='butt', shrinkA=0, shrinkB=0, mutation_scale=10))
ann2 = ax[1,0].annotate('', xy=(-1.8, -1.6), xycoords='data', xytext=(100, 0), textcoords='offset pixels',
                 arrowprops=dict(arrowstyle='<|-,head_width=0.18, head_length=0.37', lw=3.0, color='#3498db', joinstyle='miter', capstyle='butt', shrinkA=0, shrinkB=0, mutation_scale=10))

ann.arrow_patch.set_path_effects([
    pe.Stroke(linewidth=4, foreground='black'),
    pe.Normal()
])
ann2.arrow_patch.set_path_effects([
    pe.Stroke(linewidth=4, foreground='black'),
    pe.Normal()
])

ann = ax[1,1].annotate('', xy=(-1.8, -1.6), xycoords='data', xytext=(0,100), textcoords='offset pixels',
                 arrowprops=dict(arrowstyle='<|-,head_width=0.18, head_length=0.37', lw=3.0, color='#e74c3c', joinstyle='miter', capstyle='butt', shrinkA=0, shrinkB=0, mutation_scale=10))
ann2 = ax[1,1].annotate('', xy=(-1.8, -1.6), xycoords='data', xytext=(100, 0), textcoords='offset pixels',
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
cntr_left  = ax[1,0].contourf(X, Y, np.clip(Den_X, -1, 1), levels=levels, cmap="seismic", norm=norm, extend='neither')
cntr_right = ax[1,1].contourf(X, Y, np.clip(Den_Z, -1, 1), levels=levels, cmap="seismic", norm=norm, extend='neither')
ax[1,0].set_ylabel("Ar$-$Ar Distance, R ($\AA$)", fontsize=10)
ax[1,0].set_xlabel("X Coordinate ($\\AA$)", fontsize=10)
ax[1,1].set_xlabel("X Coordinate ($\\AA$)", fontsize=10)
ax[1,0].set_ylim(-2,6.3)
ax[1,1].set_ylim(-2,6.3)
ax[1,0].set_xlim(-2,2)
ax[1,1].set_xlim(-2,2)
ax[1,0].set_yticks([-2,0,2,4,6])
ax[1,1].set_yticks([-2,0,2,4,6])
ax[1,0].text(-1, 5.7, f'X Polarization', fontsize=10)
ax[1,1].text(-1, 5.7, f'Z Polarization', fontsize=10)
# --- make a colorbar axis to the RIGHT of ax[1,1] ---
div1 = make_axes_locatable(ax[1,1])
cax  = div1.append_axes("right", size="3.5%", pad=0.03)

# (important) add an invisible spacer of the SAME size to ax[1,0]
# so both bottom subplots keep equal widths
# div0 = make_axes_locatable(ax[1,0])
# _    = div0.append_axes("right", size="3.5%", pad=0.04, visible=False)

# --- single colorbar shared by the two bottom plots (mappable can be either contour) ---
cbar = fig.colorbar(cntr_right, cax=cax, ticks=[-1, 0, 1])
cbar.set_label(r"$\Delta\rho_{00}(\mathrm{x,z})$ (m|e|/Å²)", fontsize=9)
cbar.ax.tick_params(labelsize=8)   # tick labels size = 10

MW = 2
MS = 12
TO = 2

ax[1,0].plot(0, 0,marker='o', markersize=MS+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(0, 0,marker='o', markersize=MS-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(0, 0,marker='o', markersize=MS, color='#92c6c9', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(0, 3.85,marker='o', markersize=MS+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(0, 3.85,marker='o', markersize=MS-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(0, 3.85,marker='o', markersize=MS, color='#92c6c9', fillstyle='none', markeredgewidth=MW)

ax[1,1].plot(0, 0, marker='o', markersize=MS-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(0, 0, marker='o', markersize=MS+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(0, 0, marker='o', markersize=MS, color='#92c6c9', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(0, 3.85,marker='o', markersize=MS+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(0, 3.85,marker='o', markersize=MS-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(0, 3.85,marker='o', markersize=MS, color='#92c6c9', fillstyle='none', markeredgewidth=MW)

ax[1,0].text(0.8,-1.7, r'$\lambda = 0.1$', fontsize=10)
ax[1,1].text(0.8,-1.7, r'$\lambda = 0.1$', fontsize=10)

fsize = 13
fig.text(0, 0.978, f'(a)', fontsize=fsize)
fig.text(0, 0.47, f'(c)', fontsize=fsize)
fig.text(0.47, 0.978, f'(b)', fontsize=fsize)
fig.text(0.47, 0.47, f'(d)', fontsize=fsize)

plt.tight_layout(pad=0.1)
plt.subplots_adjust(wspace=0.3)
plt.savefig('./Images/ArgonData_fig1.png', dpi = 300, bbox_inches = 'tight')
