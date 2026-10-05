import sys, engine as E, specs
from PIL import Image
SP="/tmp/claude-0/-home-claude-winners-videos/17a547c7-039c-55d4-9536-c0d414251b3e/scratchpad"
for nm in sys.argv[1:]:
    sp=specs.SPECS[nm]; tl,ot,T=E.build_timeline(sp); n=len(sp["items"])
    times=[2.0, tl[0]["cd"]+1, tl[0]["rv"]+1.5, tl[1]["rv"]+1.5, tl[-1]["rv"]+1.5, T-0.5]
    ims=[]
    for t in times:
        im,d=E.base()
        if t<2.5:
            E.centered(d,560,sp["title"],E.f("Bold",56),E.GOLD); E.centered(d,690,sp["sub"],E.f("Medium",32),E.SOFT)
        elif t<ot:
            i=next(k for k,tm in enumerate(tl) if t<tm["end"]); E.draw_item(d,sp["kind"],sp["items"][i],tl[i],t,i,n)
        else:
            E.centered(d,400,sp["outro1"],E.f("Bold",58),E.GOLD); E.centered(d,560,sp["outro2"],E.f("Bold",40),E.WHITE)
        ims.append(im.resize((270,480)))
    g=Image.new("RGB",(280*6,480),"white")
    for k,im in enumerate(ims): g.paste(im,(k*280,0))
    g.save(f"{SP}/pv_{nm}.png"); print(nm, round(T,1))
