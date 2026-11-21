import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource, LinearSegmentedColormap
import sys
out=sys.argv[1]
W,H=19.2,10.8
fig=plt.figure(figsize=(W,H),dpi=100)
# sky gradient
ax0=fig.add_axes([0,0,1,1]); ax0.axis("off")
g=np.linspace(0,1,512)[:,None]*np.ones((1,8))
sky=LinearSegmentedColormap.from_list("sky",["#e9c89a","#c98f63","#5b6f98","#1f3a68","#0b1730"])
ax0.imshow(g,cmap=sky,aspect="auto",extent=[0,1,0,1])
# monkey saddle terrain
ax=fig.add_axes([-0.35,-0.62,1.7,1.55],projection="3d")
n=500
x=np.linspace(-1.25,1.25,n); X,Y=np.meshgrid(x,x)
R=np.hypot(X,Y)
Z=(X**3-3*X*Y**2)*0.55
Z=Z*np.exp(-(R/1.6)**4)
ls=LightSource(azdeg=300,altdeg=25)
terr=LinearSegmentedColormap.from_list("t",["#10233f","#24497a","#3f6f95","#7a8f86","#c2a46f","#f0d9a8"])
rgb=ls.shade(Z,cmap=terr,blend_mode="soft",vert_exag=2)
ax.plot_surface(X,Y,Z,facecolors=rgb,rstride=2,cstride=2,linewidth=0,antialiased=False,shade=False)
ax.view_init(elev=16,azim=-62)
ax.set_box_aspect((1,1,0.42))
ax.set_zlim(-1.4,1.4)
ax.axis("off"); ax.patch.set_alpha(0)
fig.savefig(out,dpi=100)
