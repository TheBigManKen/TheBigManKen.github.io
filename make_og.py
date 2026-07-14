import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
W,H=1200,630
fig=plt.figure(figsize=(W/100,H/100),dpi=100); ax=fig.add_axes([0,0,1,1]); ax.axis("off")
ax.set_xlim(0,W); ax.set_ylim(0,H)
grad=np.zeros((H,W,3)); c1=np.array([15,23,42]); c2=np.array([28,51,94])
for x in range(W): grad[:,x,:]=(c1*(1-x/W)+c2*(x/W))/255
ax.imshow(grad,extent=[0,W,0,H],aspect="auto",zorder=0)
acc="#4f9cf9"; acc2="#38bdf8"
for gx in range(0,W,50): ax.plot([gx,gx],[0,H],color="#fff",alpha=0.03,lw=1)
rng=np.random.default_rng(5); xs=np.linspace(560,1150,24)
base=np.maximum.accumulate(np.linspace(120,360,24)+rng.normal(0,16,24))
ax.plot(xs,base,color=acc2,lw=3,alpha=.9); ax.fill_between(xs,base,0,color=acc,alpha=.12)
ax.scatter(xs[::3],base[::3],s=30,color="#fff",zorder=4,alpha=.9)
ax.text(70,430,"Kenechukwu Ven-Anyanwuocha",color="#fff",fontsize=33,fontweight="bold")
ax.text(72,375,"Data Analyst",color=acc2,fontsize=24,fontweight="bold")
ax.text(74,335,"Python · SQL · Power BI · Tableau  ·  Portfolio",color="#cdd8ee",fontsize=15)
x0=74
for c in ["Churn model","A/B testing","Dashboards","SQL"]:
    w=24+len(c)*10
    ax.add_patch(FancyBboxPatch((x0,270),w,38,boxstyle="round,pad=2,rounding_size=18",lw=1,ec="#33456b",fc="#16213c"))
    ax.text(x0+w/2,289,c,color="#e8eefc",fontsize=12.5,ha="center",va="center"); x0+=w+16
fig.savefig("portfolio/assets/og-preview.png",dpi=100); print("saved og-preview.png")
