import matplotlib.patheffects as pe
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset
import matplotlib.image as mpimg
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset
import matplotlib.colors as mcolors

refEn  = 1 
lo, hi = -1, 1
levels = np.linspace(lo, hi, 500)
norm = mcolors.TwoSlopeNorm(vmin=lo, vcenter=0.0, vmax=hi)

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
RDiff_CC_X   = np.loadtxt('./Data/R_Diff_CC_X.dat')
RDiff_CC_Y   = np.loadtxt('./Data/R_Diff_CC_Y.dat')
RDiff_CC_Z   = np.loadtxt('./Data/R_Diff_CC_Z.dat')

nEl_Con = np.loadtxt('./Data/nEl_Con.dat')
nF_Con  = np.loadtxt('./Data/nF_Con.dat')

refEn  = 1
fig, ax =  plt.subplots(3,2,figsize=(6,8),constrained_layout=True)
# ================================================================
# R COORDINATE DATA
# ================================================================
ax[0,0].axhline(0, ls = '-', lw = 1, c = 'black')
ax[0,0].plot(RScan_G[:,0], RScan_G[:,1],  lw = 2.4, ls = '-',  c = 'black')
ax[0,0].plot(RScan_G[:,0], RScan_X[:,1],  lw = 3.5, ls = '-', label = f"{direc[0]}", c = '#3498db')
ax[0,0].plot(RScan_G[:,0], RScan_Y[:,1],  lw = 2., ls = '--', label = f"{direc[1]}", c = '#2ecc71')
ax[0,0].plot(RScan_G[:,0], RScan_Z[:,1],  lw = 2.4, ls = '-',  label = f"{direc[2]}", c = '#e74c3c')
ax[0,0].set_xlabel(r'Bz$-$Ar Distance, R ($\AA$)')
ax[0,0].set_ylabel(r'$\Delta$E(R) (meV)')
ax[0,0].set_xlim(2.8,9)
ax[0,0].set_ylim(-80,20)
ax[0,0].legend(frameon = False, fontsize = 10, ncol = 3, title = r'Polarization', title_fontsize='11', handlelength=1.4, loc = 'lower right',handletextpad=0.5,columnspacing=0.5)
xcoor = 5.3
ycoor = -50
ax[0,0].annotate('', xy=(xcoor, ycoor), xycoords='data', xytext=(60, 60), textcoords='offset pixels',
                 arrowprops=dict(arrowstyle='<|-,head_width=0.16, head_length=0.35', lw=3.0, color='#2ecc71', joinstyle='miter', capstyle='butt', shrinkA=0, shrinkB=0, mutation_scale=10))
ax[0,0].annotate('', xy=(xcoor, ycoor), xycoords='data', xytext=(0,100), textcoords='offset pixels',
                 arrowprops=dict(arrowstyle='<|-,head_width=0.16, head_length=0.35', lw=3.0, color='#e74c3c', joinstyle='miter', capstyle='butt', shrinkA=0, shrinkB=0, mutation_scale=10))
ax[0,0].annotate('', xy=(xcoor, ycoor), xycoords='data', xytext=(100, 0), textcoords='offset pixels',
                 arrowprops=dict(arrowstyle='<|-,head_width=0.16, head_length=0.35', lw=3.0, color='#3498db', joinstyle='miter', capstyle='butt', shrinkA=0, shrinkB=0, mutation_scale=10))
ax[0,0].annotate('', xy=(6.7, 74), xycoords='data', xytext=(55, 0), textcoords='offset pixels',
                 arrowprops=dict(arrowstyle='<|-,head_width=0.15, head_length=0.3', lw=2.0, color='#3498db', joinstyle='miter', capstyle='butt', shrinkA=0, shrinkB=0, mutation_scale=10))
img = mpimg.imread('./Images/Bz-Ar-img.png')
ax_inset = ax[0,0].inset_axes([0.57, 0.25, 0.38, 0.38])
ax_inset.imshow(img)
ax_inset.axis('off')
# DIFFERENCE WITH RESPECT TO λ = 0 PLOT
ax[0,1].axhline(0, ls = '-', lw = 1, c = 'black')
ax[0,1].plot(RScan_G[:,0], RDiff_X[:,1], lw = 3.5,  ls = '-', label = f"{direc[0]}", c = '#3498db')
ax[0,1].plot(RScan_G[:,0], RDiff_Z[:,1], lw = 2.4,  ls = '-', label = f"{direc[2]}", c = '#e74c3c')
ax[0,1].plot(RScan_G[:,0], RDiff_Y[:,1], lw = 1.5,  ls = '-', label = f"{direc[2]}", c = '#2ecc71')
ax[0,1].plot(RDiff_pMBD_X[:,0], RDiff_pMBD_X[:,1], ls = '--', lw = 3.5, c = '#3498db' )
ax[0,1].plot(RDiff_pMBD_X[:,0], RDiff_pMBD_Z[:,1], ls = '--', lw = 2, c = '#e74c3c' )
ax[0,1].plot(RDiff_pMBD_X[:,0], RDiff_pMBD_Y[:,1], ls = '--',  lw = 2, c = '#2ecc71' )
ax[0,1].plot(RDiff_CC_X[:,0],   RDiff_CC_X[:,1], ls = ' ', marker = 'o', markevery=2, markersize=4, markeredgecolor='black', markeredgewidth=0.35, c = '#3498db', alpha = 0.9 )
ax[0,1].plot(RDiff_CC_X[:,0],   RDiff_CC_Z[:,1], ls = ' ', marker = 'o', markevery=2, markersize=3, markeredgecolor='black', markeredgewidth=0.5, c = '#e74c3c', alpha = 0.7 )
ax[0,1].plot(RDiff_CC_X[:,0],   RDiff_CC_Y[:,1], ls = ' ', marker = 'o', markevery=4, markersize=3, markeredgecolor='black', markeredgewidth=0.5, c = '#2ecc71', alpha = 0.7 )
ax[0,1].set_xlabel(r'Bz$-$Ar Distance, R ($\AA$)')
ax[0,1].set_ylabel(r'$\Delta$E(R) - $\Delta$E(R)$_{\lambda=0}$ (meV)')
ax[0,1].set_xlim(2,8)
ax[0,1].set_ylim(-30,25)
ax[0,1].set_yticks(np.arange(-30,25,20))
ax2 = ax[0,1].twinx()
ax2.plot(np.NaN, np.NaN, ls= '-', lw=1, label='pQED', c='black')
ax2.plot(np.NaN, np.NaN, ls= '--', lw = 1,label='pMBD', c='black')
ax2.plot(np.NaN, np.NaN, marker= 'o', markersize= 2, ls=' ',lw = 1,label='QED-CC', c='black')
ax2.get_yaxis().set_visible(False)
ax2.legend(loc=0, frameon = False, ncol=1, fontsize = 8, title='Method', title_fontsize='10', handlelength=1.7, handletextpad=0.5,columnspacing=0.5)
ax[0,1].text(6,-27.5, r'$\lambda = 0.05$', fontsize=12)
# ================================================================
# CONVERGENCE DATA
# ================================================================
ax[2,0].axhline(refEn, lw = 1, ls = '-', c = 'black')
ax[2,0].axhline(-refEn, lw = 1, ls = '-', c = 'black')
ax[2,0].plot(nEl_Con[:,0], nEl_Con[:,1],  lw = 2, ls = '-', label = f"{direc[0]}", c = '#3498db')
ax[2,0].plot(nEl_Con[:,0], nEl_Con[:,2],  lw = 0.7, ls = '-', label = f"{direc[1]}", c = '#2ecc71')
ax[2,0].plot(nEl_Con[:,0], nEl_Con[:,3],  lw = 2, ls = '-', label = f"{direc[2]}", c = '#e74c3c')
ax[2,0].set_xlabel(r'Electronic States, N$_\mathrm{el}$ (x 10$^{3}$)')
ax[2,0].set_ylabel(r'$\Delta$E(R) - $\Delta$E(R)$_{N_{el}=10^3}$ (meV)')
ax[2,0].set_xlim(nEl_Con[0,0],nEl_Con[-1,0])
ax[2,0].set_ylim(-80,40)
ax[2,0].set_yticks(np.arange(-80,80,40))
sub_ax = inset_axes(ax[2,0], width="55%", height="35%", loc=4)
sub_ax.axhline(refEn, lw = 1, ls = '-', c = 'black')
sub_ax.axhline(-refEn, lw = 1, ls = '-', c = 'black')
sub_ax.plot(nEl_Con[:,0], nEl_Con[:,1] - nEl_Con[-1,1],  lw = 1.5, ls = '-', label = f"{direc[0]}", c = '#3498db')
sub_ax.plot(nEl_Con[:,0], nEl_Con[:,2] - nEl_Con[-1,2],  lw = 1.5, ls = '-', label = f"{direc[0]}", c = '#2ecc71')
sub_ax.plot(nEl_Con[:,0], nEl_Con[:,3] - nEl_Con[-1,3],  lw = 1.5, ls = '-', label = f"{direc[0]}", c = '#e74c3c')
sub_ax.set_xlim(3, 5.5)
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
ax[2,1].set_ylim(-4,5)
ax[2,1].set_yticks(np.arange(-4,5,2))

fsize = 13
fig.text(0, 0.97, f'(a)', fontsize=fsize)
fig.text(0, 0.64, f'(c)', fontsize=fsize)
fig.text(0.51, 0.97, f'(b)', fontsize=fsize)
fig.text(0.51, 0.64, f'(d)', fontsize=fsize)
fig.text(0, 0.31, f'(e)', fontsize=fsize)
fig.text(0.51, 0.31, f'(f)', fontsize=fsize)

#===Density Plots===#
Den_X        = np.loadtxt('./Data/Density3D_X.dat')
Den_Z        = np.loadtxt('./Data/Density3D_Z.dat')
Den_Pos      = np.loadtxt('./Data/Density3D_Pos.dat')
X,Y = np.meshgrid( Den_Pos[:,0], Den_Pos[:,1] )
from mpl_toolkits.axes_grid1 import make_axes_locatable

ann = ax[1,0].annotate('', xy=(-3.2, -1.6), xycoords='data', xytext=(0,100), textcoords='offset pixels',
                 arrowprops=dict(arrowstyle='<|-,head_width=0.18, head_length=0.37', lw=3.0, color='#e74c3c', joinstyle='miter', capstyle='butt', shrinkA=0, shrinkB=0, mutation_scale=10))
ann2 = ax[1,0].annotate('', xy=(-3.28, -1.6), xycoords='data', xytext=(100, 0), textcoords='offset pixels',
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
ann2 = ax[1,1].annotate('', xy=(-3.28, -1.6), xycoords='data', xytext=(100, 0), textcoords='offset pixels',
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
ax[1,0].set_ylim(-2,5.1)
ax[1,1].set_ylim(-2,5.1)
ax[1,0].set_xlim(-3.5,3.5)
ax[1,1].set_xlim(-3.5,3.5)
ax[1,0].set_yticks([-2,0,2,4])
ax[1,1].set_yticks([-2,0,2,4])
ax[1,0].text(-1.7, 4.5, f'X Polarization', fontsize=12)
ax[1,1].text(-1.7, 4.5, f'Z Polarization', fontsize=12)
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
MS_H = 8

ax[1,0].plot(-0.006, -0.1,marker='o', markersize=MS+TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(-0.006, -0.1,marker='o', markersize=MS-TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(-0.006, -0.1,marker='o', markersize=MS, color='black', fillstyle='none', markeredgewidth=MW)

ax[1,0].plot(1.21, -0.1,marker='o', markersize=MS+TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(1.21, -0.1,marker='o', markersize=MS-TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(1.21, -0.1,marker='o', markersize=MS, color='black', fillstyle='none', markeredgewidth=MW)

ax[1,0].plot(-1.21, -0.1,marker='o', markersize=MS+TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(-1.21, -0.1,marker='o', markersize=MS-TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(-1.21, -0.1,marker='o', markersize=MS, color='black', fillstyle='none', markeredgewidth=MW)

ax[1,0].plot(0.006, -0.1,marker='o', markersize=MS_H+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(0.006, -0.1,marker='o', markersize=MS_H-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(0.006, -0.1,marker='o', markersize=MS_H, color='white', fillstyle='none', markeredgewidth=MW)

ax[1,0].plot(2.16, -0.1,marker='o', markersize=MS_H+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(2.16, -0.1,marker='o', markersize=MS_H-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(2.16, -0.1,marker='o', markersize=MS_H, color='white', fillstyle='none', markeredgewidth=MW)

ax[1,0].plot(-2.16, -0.1,marker='o', markersize=MS_H+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(-2.16, -0.1,marker='o', markersize=MS_H-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(-2.16, -0.1,marker='o', markersize=MS_H, color='white', fillstyle='none', markeredgewidth=MW)

ax[1,0].plot(0, 3.45,marker='o', markersize=MS+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(0, 3.45,marker='o', markersize=MS-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(0, 3.45,marker='o', markersize=MS, color='#92c6c9', fillstyle='none', markeredgewidth=MW)

#==right panel===#
ax[1,1].plot(-0.006, -0.1,marker='o', markersize=MS+TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(-0.006, -0.1,marker='o', markersize=MS-TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(-0.006, -0.1,marker='o', markersize=MS, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(1.21, -0.1,marker='o', markersize=MS+TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(1.21, -0.1,marker='o', markersize=MS-TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(1.21, -0.1,marker='o', markersize=MS, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(-1.21, -0.1,marker='o', markersize=MS+TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(-1.21, -0.1,marker='o', markersize=MS-TO, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(-1.21, -0.1,marker='o', markersize=MS, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(0.006, -0.1,marker='o', markersize=MS_H+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(0.006, -0.1,marker='o', markersize=MS_H-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(0.006, -0.1,marker='o', markersize=MS_H, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(2.16, -0.1,marker='o', markersize=MS_H+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(2.16, -0.1,marker='o', markersize=MS_H-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(2.16, -0.1,marker='o', markersize=MS_H, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(-2.16, -0.1,marker='o', markersize=MS_H+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(-2.16, -0.1,marker='o', markersize=MS_H-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(-2.16, -0.1,marker='o', markersize=MS_H, color='white', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(0, 3.45,marker='o', markersize=MS+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(0, 3.45,marker='o', markersize=MS-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(0, 3.45,marker='o', markersize=MS, color='#92c6c9', fillstyle='none', markeredgewidth=MW)

plt.savefig('./Images/Benzene-Ar_6panel.pdf', dpi = 300, bbox_inches = 'tight')
