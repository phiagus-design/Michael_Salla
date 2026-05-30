#!/usr/bin/env python3
"""Timeline & connection map of human/ET interaction events as claimed across
Michael Salla's nine project books (exopolitics literature) -- structural
analysis of the books' assertions, not verified fact."""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from matplotlib.lines import Line2D

# CATEGORIES: id -> (lane_y, color, label)
CATS = {
    "nazi":   (11.6, "#8c6d3f", "Nazi / Antarctic\nsecret programs"),
    "mj12":   (8.4, "#c0392b", "Crashes, MJ-12 &\ncover-up politics"),
    "contact":(5.2, "#2c6fbb", "Presidential & private\nET contact / treaties"),
    "modern": (2.0, "#1f9c8a", "Modern SSP, space\narks & disclosure"),
}
# EVENTS: id -> (decimal_year, label, category, actor)  actor H/E/B
E = {
 "byrd33":(1933.5,"Byrd aerial survey\nof Antarctica","nazi","H"),
 "schwab":(1938.96,"Schwabenland claims\nNeuschwabenland","nazi","H"),
 "relocate":(1939.05,"Programs move\nto Antarctica","nazi","H"),
 "haunebu":(1939.3,"Nazi SS 'Haunebu 1'\nfirst saucer","nazi","B"),
 "fdr_byrd":(1939.52,"FDR orders Byrd to\nchallenge Nazi bases","nazi","H"),
 "fdr_memo":(1944.14,"FDR memo: Non-\nTerrestrial Science","nazi","H"),
 "kugel":(1945.15,"Kugelblitz tested;\ncraft sent south","nazi","B"),
 "byrdneg":(1946.3,"Byrd flown to Antarctica;\ntalks fail","nazi","H"),
 "highjump":(1947.08,"Op. Highjump fleet\n'hit by UFO force'","nazi","E"),
 "paperclip":(1945.7,"Truman approves\nOp. Paperclip","mj12","H"),
 "roswell":(1947.5,"Roswell crash\n& retraction","mj12","E"),
 "ike_brief":(1947.6,"Eisenhower & JFK\nbriefed on Roswell","mj12","H"),
 "mj12":(1947.73,"Truman authorizes\nMajestic-12","mj12","H"),
 "forrestal":(1949.4,"Forrestal death:\n1st cover-up killing","mj12","H"),
 "adamski":(1952.9,"Adamski 'Desert Center'\ncontact (Orthon)","contact","E"),
 "edwards":(1954.14,"First Contact, Edwards\nAFB: Nordics spurned","contact","E"),
 "bravo":(1954.22,"Bravo H-bomb test\n(9 days later)","mj12","H"),
 "holloman":(1955.11,"Holloman AFB meeting\n-> 'Greada Treaty'","contact","B"),
 "s4":(1955.6,"S-4 facility opens\nat Area 51","mj12","B"),
 "jfk_req":(1961.49,"JFK requests MJ-12\nbriefing from Dulles","mj12","H"),
 "adam_jfk":(1961.8,"Adamski allegedly\nmeets Kennedy","contact","E"),
 "directive":(1961.9,"Dulles drafts 'Project\nEnvironment' kill order","mj12","H"),
 "halltw":(1965.0,"C. Hall: 'Tall Whites'\nat Nellis (1963-67)","contact","E"),
 "nsam271":(1963.7,"NSAM 271: JFK shares\nUFO files w/ USSR","mj12","H"),
 "jfk_kill":(1963.9,"JFK assassinated\n(Nov 22 1963)","mj12","H"),
 "solar":(1980.0,"'Solar Warden' Navy\nfleet operational","modern","B"),
 "ebd":(1984.0,"Eisenhower Briefing\nDocument surfaces","mj12","H"),
 "coalition":(1994.0,"Multinational Antarctic\nSSP coalition forms","modern","B"),
 "mckinnon":(1999.0,"McKinnon hack: 'Non-\nTerrestrial Officers'","modern","H"),
 "excavate":(2002.0,"Antarctic excavation\nof ruins begins","modern","B"),
 "vips":(2016.5,"VIPs visit Antarctica\n(Kerry, Aldrin)","modern","H"),
 "spartan":(2019.1,"'Spartan 1 & 2' reveal\nAntarctic fleet","modern","E"),
 "spaceforce":(2019.96,"U.S. Space Force\nestablished","modern","H"),
 "ganymede":(2021.78,"Fleet near Ganymede;\narks activate","modern","E"),
 "ark":(2022.05,"US-China mission to\nAtlantic space ark","modern","B"),
 "congress":(2022.45,"First Congress UFO\nhearing in 50 yrs","modern","H"),
 "rv":(2023.3,"Remote-viewing of\nAtlantic ark","modern","E"),
}
LINKS = [
 ("schwab","relocate"),("relocate","haunebu"),("schwab","fdr_byrd"),
 ("fdr_byrd","byrdneg"),("byrdneg","highjump"),("kugel","highjump"),
 ("highjump","solar"),("haunebu","s4"),("paperclip","s4"),
 ("roswell","ike_brief"),("ike_brief","mj12"),("mj12","forrestal"),
 ("mj12","jfk_req"),("jfk_req","directive"),("directive","jfk_kill"),
 ("nsam271","jfk_kill"),("mj12","ebd"),
 ("edwards","holloman"),("holloman","halltw"),("bravo","edwards"),
 ("adamski","adam_jfk"),("adam_jfk","nsam271"),("ike_brief","edwards"),
 ("coalition","mckinnon"),("excavate","vips"),("vips","spartan"),
 ("spartan","spaceforce"),("ganymede","ark"),("ark","rv"),
 ("ark","congress"),("solar","coalition"),
]
MARK = {"H":"o","E":"^","B":"s"}

plt.rcParams["font.family"]="DejaVu Sans"
fig,(axL,axR)=plt.subplots(1,2,figsize=(23,13.7),sharey=True,
    gridspec_kw={"width_ratios":[37,46],"wspace":0.035})
fig.patch.set_facecolor("#f7f5f0")
LO_MAX,HI_MIN=1969,1979
axL.set_xlim(1932,LO_MAX); axR.set_xlim(HI_MIN,2025.8)
for ax in (axL,axR):
    ax.set_ylim(0.0,13.7); ax.set_facecolor("#f7f5f0")
    for s in ["top","right","left"]: ax.spines[s].set_visible(False)
    ax.tick_params(left=False); ax.set_yticks([])

for k,(y,c,lab) in CATS.items():
    for ax in (axL,axR):
        ax.axhspan(y-0.30,y+0.30,color=c,alpha=0.08,zorder=0)
        ax.axhline(y,color=c,alpha=0.16,lw=1,zorder=0)
    axL.text(1931.2,y,lab,ha="right",va="center",fontsize=10.5,
             fontweight="bold",color=c,linespacing=0.95)

panel=lambda eid: axL if E[eid][0]<=LO_MAX else axR

# connection arrows (behind)
for a,b in LINKS:
    if panel(a) is not panel(b): continue
    ax=panel(a); ya,yb=CATS[E[a][2]][0],CATS[E[b][2]][0]
    xa,xb=E[a][0],E[b][0]
    rad=0.22 if ya!=yb else (0.0 if abs(xb-xa)<3 else 0.14)
    ax.add_patch(FancyArrowPatch((xa,ya),(xb,yb),
        connectionstyle=f"arc3,rad={rad}",arrowstyle="-|>",
        mutation_scale=11,lw=1.1,color="#555",alpha=0.42,zorder=1))

# events + de-conflicted labels with leader lines
TIERS=[(+0.50,1),(-0.50,-1),(+1.12,1),(-1.12,-1)]   # offset, sign
GAP={axL:2.6, axR:3.6}
placed={}  # (ax,tier_idx)->last_label_x
order={}   # (ax,cat)->counter
for eid,(yr,lab,cat,actor) in sorted(E.items(),key=lambda kv:kv[1][0]):
    ax=panel(eid); y,c,_=CATS[cat]
    ax.scatter(yr,y,s=185,marker=MARK[actor],color=c,
               edgecolor="white",linewidth=1.5,zorder=5)
    i=order.get((ax,cat),0); order[(ax,cat)]=i+1
    off,sign=TIERS[i%4]
    lx=yr; key=(ax,i%4)
    if key in placed and lx-placed[key]<GAP[ax]:
        lx=placed[key]+GAP[ax]
    placed[key]=lx
    ax.plot([yr,lx],[y+sign*0.30, y+off-sign*0.16],
            color="#999",lw=0.7,alpha=0.7,zorder=3)
    ax.annotate(lab,(lx,y+off),ha="center",
                va="bottom" if sign>0 else "top",
                fontsize=8.2,color="#1f1f1f",zorder=6,linespacing=0.95)

axL.set_xticks(range(1935,1970,5)); axR.set_xticks(range(1980,2025,5))
for ax in (axL,axR): ax.tick_params(axis="x",labelsize=10.5)

# broken-axis marks
fig.text(0.508,0.066,"//",ha="center",fontsize=15,color="#888")
axR.annotate("origin programs\nfeed modern SSP",xy=(1980.1,2.0),
    xytext=(1983.2,4.6),fontsize=8.4,style="italic",color="#777",
    arrowprops=dict(arrowstyle="-|>",color="#999",lw=1,
                    connectionstyle="arc3,rad=-0.3"))

handles=[Line2D([],[],marker="o",color="w",markerfacecolor="#444",markersize=11,label="Human-only event"),
         Line2D([],[],marker="^",color="w",markerfacecolor="#444",markersize=12,label="ET contact / sighting"),
         Line2D([],[],marker="s",color="w",markerfacecolor="#444",markersize=11,label="Tech exchange / both"),
         Line2D([],[],color="#555",lw=1.4,alpha=0.6,label="Claimed causal link")]
lg=axR.legend(handles=handles,loc="upper right",fontsize=9.8,frameon=True,
              framealpha=0.92,title="Event type",title_fontsize=10.5)
lg.get_frame().set_edgecolor("#ccc")

fig.suptitle("Human–Extraterrestrial Interaction: A Classified Timeline & Connection Map",
             fontsize=20.5,fontweight="bold",y=0.975)
fig.text(0.5,0.937,"Key events as claimed across Michael Salla's nine 'Exopolitics' / "
         "Secret Space Program books   ·   1933–2023   ·   colour = theme, shape = actor, arrows = narrative causation",
         ha="center",fontsize=11,color="#555")
fig.text(0.5,0.02,"Source: the project's books only (Salla, 2013–2023). These are the books' "
         "assertions, shown for structural analysis — not historically verified facts.",
         ha="center",fontsize=8.6,style="italic",color="#8a8a8a")
plt.subplots_adjust(left=0.10,right=0.99,top=0.915,bottom=0.075)
plt.savefig("/mnt/user-data/outputs/et_human_timeline.png",dpi=170,facecolor=fig.get_facecolor())
print("saved. events:",len(E),"links:",len(LINKS))
