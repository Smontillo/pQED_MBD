import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
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
RDiff_pMBD_Y = np.loadtxt('./Data/R_Diff_pMBD_Y.dat')
RDiff_pMBD_X = np.loadtxt('./Data/R_Diff_pMBD_X.dat')
RDiff_CC_X =np.loadtxt('./Data/R_Diff_CC_X.dat')
RDiff_CC_Z =np.loadtxt('./Data/R_Diff_CC_Z.dat')
RDiff_CC_Y =np.loadtxt('./Data/R_Diff_CC_Y.dat')
Den_X        = np.loadtxt('./Data/Density3D_X.dat')
Den_Z        = np.loadtxt('./Data/Density3D_Z.dat')
Den_Pos      = np.loadtxt('./Data/Density3D_Pos.dat')

refEn  = 1 
lo, hi = -0.5, 0.5
levels = np.linspace(lo, hi, 500)
zD0   = 3.85
norm = mcolors.TwoSlopeNorm(vmin=lo, vcenter=0.0, vmax=hi)
colors = ["#700321", "white", "#0a3d73"]
my_cmap = mcolors.LinearSegmentedColormap.from_list("my_div", colors, N=256)


fig, ax =  plt.subplots(2,2,figsize=(6,6))
# ================================================================
# R COORDINATE DATA
# ================================================================
ax[0,0].axhline(0, ls = '-', lw = 1, c = 'black')
ax[0,0].plot(RScan_G[:,0], RScan_G[:,1],  lw = 2, ls = '-', c = 'black')
ax[0,0].plot(RScan_G[:,0], RScan_X[:,1],  lw = 2, ls = '-', label = f"{direc[0]}", c = '#3498db')
ax[0,0].plot(RScan_G[:,0], RScan_Y[:,1],  lw = 1, ls = '--', label = f"{direc[1]}", c = '#2ecc71')
ax[0,0].plot(RScan_G[:,0], RScan_Z[:,1],  lw = 2, ls = '-', label = f"{direc[2]}", c = '#e74c3c')
ax[0,0].set_xlabel(r'O$-$H Distance, R ($\AA$)', fontsize=12)
ax[0,0].set_ylabel(r'$\Delta$E(R) (meV)', fontsize=12)
ax[0,0].set_ylim(-250,5)
ax[0,0].set_xlim(1.4,6)
ax[0,0].set_xticks([2,4,6])
ax[0,0].legend(frameon = False, fontsize = 10, ncol = 3, title = r'Polarization', title_fontsize=10, handlelength=1.4, handletextpad=0.5,columnspacing=0.5, loc='lower right')
ax[0,0].annotate('', xy=(3.5, -150), xycoords='data', xytext=(0,100), textcoords='offset pixels',
                 arrowprops=dict(arrowstyle='<|-,head_width=0.18, head_length=0.37', lw=3.0, color='#e74c3c', joinstyle='miter', capstyle='butt', shrinkA=0, shrinkB=0, mutation_scale=10))
ax[0,0].annotate('', xy=(3.5, -150), xycoords='data', xytext=(100, 0), textcoords='offset pixels',
                 arrowprops=dict(arrowstyle='<|-,head_width=0.18, head_length=0.37', lw=3.0, color='#2ecc71', joinstyle='miter', capstyle='butt', shrinkA=0, shrinkB=0, mutation_scale=10))
ax[0,0].annotate('', xy=(3.5, -150), xycoords='data', xytext=(-60, -60), textcoords='offset pixels',
                 arrowprops=dict(arrowstyle='<|-,head_width=0.18, head_length=0.37', lw=3.0, color='#3498db', joinstyle='miter', capstyle='butt', shrinkA=0, shrinkB=0, mutation_scale=10))
img = mpimg.imread('./Images/WaterDimer_Render.png')
ax_inset = ax[0,0].inset_axes([0.55, 0.26, 0.5, 0.5])
ax_inset.imshow(img)
ax_inset.axis('off')
# DIFFERENCE WITH RESPECT TO λ = 0 PLOT
ax[0,1].axhline(0, ls = '-', lw = 1, c = 'black')
ax[0,1].plot(RScan_G[:,0], RDiff_X[:,1],  lw = 2, ls = '-', label = f"{direc[0]}", c = '#3498db')
ax[0,1].plot(RScan_G[:,0], RDiff_Y[:,1],  lw = 1, ls = '-', label = f"{direc[1]}", c = '#2ecc71')
ax[0,1].plot(RScan_G[:,0], RDiff_Z[:,1],  lw = 2, ls = '-', label = f"{direc[2]}", c = '#e74c3c')
ax[0,1].plot(RDiff_pMBD_X[:,0], RDiff_pMBD_X[:,1], ls = '--', lw = 2, c = '#3498db' )
ax[0,1].plot(RDiff_pMBD_X[:,0], RDiff_pMBD_Y[:,1], ls = '--', lw = 1, c = '#2ecc71' )
ax[0,1].plot(RDiff_pMBD_X[:,0], RDiff_pMBD_Z[:,1], ls = '--', lw = 2, c = '#e74c3c' )
ax[0,1].plot(RDiff_CC_X[:,0], RDiff_CC_X[:,1], ls = ' ', marker = 'o', markevery=2, markersize=3, markeredgecolor='black', markeredgewidth=0.5, c = '#3498db', alpha = 0.7)
ax[0,1].plot(RDiff_CC_X[:,0], RDiff_CC_Y[:,1], ls = ' ', marker = 'o', markevery=4, markersize=3, markeredgecolor='black', markeredgewidth=0.5, c = '#2ecc71', alpha = 0.7)
ax[0,1].plot(RDiff_CC_X[:,0], RDiff_CC_Z[:,1], ls = ' ', marker = 'o', markevery=3, markersize=3, markeredgecolor='black', markeredgewidth=0.5, c = '#e74c3c', alpha = 0.7)
ax[0,1].set_xlabel(r'O$-$H Distance, R ($\AA$)', fontsize=12)
ax[0,1].set_ylabel(r'$\Delta$E(R) $-$ $\Delta$E(R)$_{\lambda=0}$ (meV)', fontsize=12)
ax[0,1].set_ylim(-10,20)
ax[0,1].set_xlim(1.2,6)
ax2 = ax[0,1].twinx()
ax2.plot(np.NaN, np.NaN, ls= '-', lw=1, label='pQED', c='black')
ax2.plot(np.NaN, np.NaN, ls= '--', lw = 1,label='pMBD', c='black')
ax2.plot(np.NaN, np.NaN, ls= ' ', marker = 'o', markersize=2,label='QED-CC', c='black')
ax2.get_yaxis().set_visible(False)
ax2.legend(loc=0, frameon = False, ncol=1, fontsize = 10, title='Method', title_fontsize=10, handlelength=1.4, handletextpad=0.5,columnspacing=0.5)
# ax[0,0].grid()
# ax[0,1].grid()
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
cntr_left  = ax[1,0].contourf(X, Y, np.clip(Den_X, lo,hi), levels=levels, cmap='seismic', norm=norm, extend='neither')
cntr_right = ax[1,1].contourf(X, Y, np.clip(Den_Z, lo,hi), levels=levels, cmap='seismic', norm=norm, extend='neither')
ax[1,0].set_ylabel("O$-$H Distance, R ($\AA$)", fontsize=12)
ax[1,0].set_xlabel("X Coordinate ($\\AA$)", fontsize=12)
ax[1,1].set_xlabel("X Coordinate ($\\AA$)", fontsize=12)
ax[1,0].set_ylim(-2,5)
ax[1,1].set_ylim(-2,5)
ax[1,0].set_xlim(-2,2)
ax[1,1].set_xlim(-2,2)
ax[1,0].set_yticks([-2,0,2,4])
ax[1,1].set_yticks([-2,0,2,4])
ax[1,0].text(-1, 4.5, f'X Polarization', fontsize=12)
ax[1,1].text(-1, 4.5, f'Z Polarization', fontsize=12)
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
ax[1,0].plot(0.742609750467, rH + zD0, marker='o', markersize=MS-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(0.742609750467, rH + zD0, marker='o', markersize=MS+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(0.742609750467, rH + zD0, marker='o', markersize=MS, color='#fafafa', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(-0.138924647189, rO + zD0, marker='o', markersize=MS-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(-0.138924647189, rO + zD0, marker='o', markersize=MS+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(-0.138924647189, rO + zD0, marker='o', markersize=MS, color='#f2031a', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(0, zD0, marker='o', markersize=MS+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(0, zD0, marker='o', markersize=MS-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(0, zD0, marker='o', markersize=MS, color='#fafafa', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(0,0, marker='o', markersize=MS+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(0,0, marker='o', markersize=MS-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(0,0, marker='o', markersize=MS, color='#f2031a', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(-0.4684, -0.35062015096,marker='o', markersize=MS+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(-0.4684, -0.35062015096,marker='o', markersize=MS-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,0].plot(-0.4684, -0.35062015096,marker='o', markersize=MS, color='#fafafa', fillstyle='none', markeredgewidth=MW)

ax[1,1].plot(0.742609750467, rH + zD0, marker='o', markersize=MS-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(0.742609750467, rH + zD0, marker='o', markersize=MS+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(0.742609750467, rH + zD0, marker='o', markersize=MS, color='#fafafa', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(-0.138924647189, rO + zD0, marker='o', markersize=MS-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(-0.138924647189, rO + zD0, marker='o', markersize=MS+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(-0.138924647189, rO + zD0, marker='o', markersize=MS, color='#f2031a', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(0, zD0, marker='o', markersize=MS+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(0, zD0, marker='o', markersize=MS-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(0, zD0, marker='o', markersize=MS, color='#fafafa', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(0,0, marker='o', markersize=MS+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(0,0, marker='o', markersize=MS-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(0,0, marker='o', markersize=MS, color='#f2031a', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(-0.4684, -0.35062015096,marker='o', markersize=MS+TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(-0.4684, -0.35062015096,marker='o', markersize=MS-TO, color='black', fillstyle='none', markeredgewidth=MW)
ax[1,1].plot(-0.4684, -0.35062015096,marker='o', markersize=MS, color='#fafafa', fillstyle='none', markeredgewidth=MW)

ax[0,1].text(4.1, -9.4, f'$\lambda=0.05$', fontsize=12)

fsize = 13
fig.text(0, 0.98, f'(a)', fontsize=fsize)
fig.text(0, 0.47, f'(c)', fontsize=fsize)
fig.text(0.47, 0.98, f'(b)', fontsize=fsize)
fig.text(0.47, 0.47, f'(d)', fontsize=fsize)

plt.tight_layout(pad=0.1)
plt.savefig('./Images/WaterData_fig1.pdf', dpi = 300, bbox_inches = 'tight')