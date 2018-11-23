import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

u   =20.   #m/s
v   =20.   #m/s
wmin=-25.    #m/s
wmax=25    #m/s 
w   =np.arange(wmin,wmax+1,1) #m/s

theta= 0.      # deg (90 = North; 180 = West)
alphamax=20.    # deg
alphamin=0.0    # deg
alpha = np.arange(alphamin,alphamax+0.5,0.5) # deg


# By default, the np trig library assumes radians. Convert degrees to radians.
alpha=np.radians(alpha)
theta=np.radians(theta)

# Define the trig parameters.
costilt = np.zeros(len(alpha))   # initialize to zeros. 
sintilt = np.zeros(len(alpha))   # initialize to zeros. 
cosanzm = np.cos(theta)
sinanzm = np.sin(theta)

for a in range(len(alpha)):
    costilt[a]= np.cos(alpha[a])
    sintilt[a]= np.sin(alpha[a])

Vr  = np.zeros(shape=(len(w),len(alpha)))   # initialize to zeros.
Vrw = np.zeros(shape=(len(w),len(alpha)))   # initialize to zeros.

for j in range(len(alpha)):
    for i in range(len(w)):
# Ob operators.
        Vr[i,j]  = u*cosanzm*costilt[j] + v*sinanzm*costilt[j] 
        Vrw[i,j] = u*cosanzm*costilt[j] + v*sinanzm*costilt[j] + (w[i]        )*sintilt[j]

# Make the plot.
diff=Vr  -Vrw

#plt.figure(figsize=(13.125*1.5,10.5/2.3))
#plt.figure(figsize=(13.125*1.5*0.85,10.5/2.3))
plt.figure(figsize=(15,11))
#plt.figure(figsize=(10,20))

inc=1.
lev=15.
clevs=np.arange(-1*lev,lev+inc,inc)
inc=0.5;lev=5.
clevsdiff=np.arange(-1*lev,lev+inc,inc)

fig_title_fontsize=28
title_fontsize=22
clabel_fontsize=16
xy_label_fontsize=20

#Plot 3
ax3=plt.subplot(1,1,1)
plt.title(r'$Vr (u,v) - Vr (u,v,w) = -w sin(\alpha)$',fontsize=title_fontsize)
cs1=plt.contourf(np.degrees(alpha),w,diff,clevsdiff,cmap='coolwarm',extend='both')
plt.xlabel('Radar Tilt Angle',fontsize=xy_label_fontsize)
plt.ylabel('Vertical Velocity (w)',fontsize=xy_label_fontsize)
cs2=plt.contour(np.degrees(alpha),w,diff,colors='k')
cbar = plt.colorbar(cs1,ticks=clevsdiff)
cbar.add_lines(cs2)
#cbar.tick_params(labelsize=clabel_fontsize)
cbar.set_label('$m/s$')
plt.clabel(cs2, inline=1, fontsize=clabel_fontsize, colors='k')
plt.setp(ax3.get_xticklabels(), visible=True, fontsize=clabel_fontsize)
plt.setp(ax3.get_yticklabels(), visible=True, fontsize=clabel_fontsize)

plt.tight_layout()
plt.subplots_adjust(top=0.93)
plt.suptitle("Doppler Radial Wind Observation Operator Differences",fontsize=fig_title_fontsize,x=0.5, y=1.00)
plt.savefig('./ObsOpDiff_2.png',bbox_inches='tight')
#plt.show()
   




