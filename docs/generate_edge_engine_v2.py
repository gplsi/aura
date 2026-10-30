from PIL import Image, ImageDraw, ImageFont
import sys, os
OUT = sys.argv[1]
R = "/System/Library/Fonts/Supplemental/Arial.ttf"
B = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
def F(s, b=False): return ImageFont.truetype(B if b else R, s)

BG=(18,15,12); CARD=(28,22,16); GOLD=(245,197,115); TXT=(220,210,200); WHITE=(248,250,252)
DIM=(160,148,135); RED=(225,29,72); CLOUD=(56,189,248); CLOUD_BG=(14,30,42); CLOUD_D=(125,211,252)
STEPCOL=[(215,145,60),(225,125,85),(235,165,125),(245,197,115)]

def arrow_down(d, x, y1, y2, col, w=3):
    d.line([(x,y1),(x,y2-10)], fill=col, width=w)
    d.polygon([(x-8,y2-12),(x+8,y2-12),(x,y2)], fill=col)

def cloud_band(d, x1, y1, x2, y2, scale=1.0):
    d.rounded_rectangle((x1,y1,x2,y2), radius=12, fill=CLOUD_BG, outline=CLOUD, width=2)
    d.rounded_rectangle((x1+16,y1+14,x1+16+int(150*scale),y1+44), radius=6, fill=CLOUD)
    d.text((x1+16+int(75*scale), y1+29), "LAYERS A + B", fill=(8,20,30), font=F(int(13*scale),True), anchor="mm")
    d.text((x1+30+int(150*scale), y1+29), "FEDERATED SOVEREIGN CLOUD  ·  Gaia-X 24/7 + EuroHPC  (outside the plant)", fill=WHITE, font=F(int(16*scale),True), anchor="lm")
    items = [("Core Ontology ISA-95", "Layer 1 · shared data model", "INDElab / UvA"),
             ("Sector Oracles", "Layer 2 · HACCP/EFSA · REACH/CLP", "built by the competing teams"),
             ("Generic AI models", "LLM/SLM trained on MareNostrum 5", "BSC · EuroHPC"),
             ("MLOps pipeline", "signed, versioned knowledge packages", "ESTEN")]
    n=len(items); gap=14; iw=(x2-x1-32-gap*(n-1))/n
    cy1=y1+58; cy2=y2-14
    for i,(t,s,p) in enumerate(items):
        a=x1+16+i*(iw+gap); b=a+iw
        d.rounded_rectangle((a,cy1,b,cy2), radius=8, fill=(20,44,60), outline=(56,120,160), width=1)
        mx=(a+b)/2
        d.text((mx, cy1+20*scale), t, fill=WHITE, font=F(int(15*scale),True), anchor="mm")
        d.text((mx, cy1+42*scale), s, fill=CLOUD_D, font=F(int(12*scale)), anchor="mm")
        d.text((mx, cy1+60*scale), p, fill=DIM, font=F(int(11*scale)), anchor="mm")
    return [x1+16+i*(iw+gap)+iw/2 for i in range(n)]

def boundary(d, x1, x2, y, xs_down, label_x, top=None):
    # downward feeds
    for x in xs_down:
        arrow_down(d, int(x), (top if top else y-38), y+44, CLOUD, 3)
    d.line([(x1,y),(x2,y)], fill=RED, width=3)
    t="DATA SOVEREIGNTY BOUNDARY (pilot validation) — raw plant data never leaves the factory"
    f=F(13,True); w=d.textlength(t,font=f)
    d.rounded_rectangle((label_x-w/2-12,y-14,label_x+w/2+12,y+14), radius=6, fill=(20,10,12), outline=RED, width=1)
    d.text((label_x,y), t, fill=WHITE, font=f, anchor="mm")

def steps(d, x0, y0, total_w, h, fed=True):
    data=[("STEP 1","1. PREDICT","Generic predictive models",["Real-time sensor log analysis","Anomaly detection on local GPU","Failure anticipation (>2 h)","Dough / enamel quality alerts"]),
          ("STEP 2","2. GUIDE","Ontology + sector oracles",["Dual Graph-RAG: oracles + private graph","Explainable step-by-step SOPs","Root-cause evidence","AI Act-aligned rationale"]),
          ("STEP 3","3. ACT","Updated SOPs & compliance rules",["Human-at-the-Edge decision","Operator executes or overrides","Plant line adjustment","Outcome logged locally"]),
          ("STEP 4","4. LEARN","New model versions (pull)",["Tacit experience capture","Judge Agent validation","Private Graph update","Knowledge stays in the plant"])]
    gap=22; cw=(total_w-3*gap)/4
    for i,(sn,st,feed,items) in enumerate(data):
        col=STEPCOL[i]; a=x0+i*(cw+gap); b=a+cw
        d.rounded_rectangle((a,y0,b,y0+h), radius=10, fill=CARD, outline=col, width=2)
        y=y0+14
        if fed:
            d.rounded_rectangle((a+10,y,b-10,y+44), radius=6, fill=(20,44,60), outline=(56,120,160), width=1)
            d.text((a+18,y+12), "▼ FED FROM CLOUD", fill=CLOUD, font=F(10,True), anchor="lm")
            d.text((a+18,y+30), feed, fill=WHITE, font=F(12), anchor="lm")
            y+=58
        d.rounded_rectangle((a+12,y,a+86,y+26), radius=6, fill=(45,32,22), outline=col, width=1)
        d.text((a+49,y+13), sn, fill=col, font=F(11,True), anchor="mm")
        d.text((a+14,y+46), st, fill=WHITE, font=F(17,True), anchor="lm")
        yy=y+80
        for it in items:
            words=it.split(); line=""; lines=[]
            for w_ in words:
                tst=(line+" "+w_).strip()
                if d.textlength("• "+tst, font=F(13))>cw-24: lines.append(line); line=w_
                else: line=tst
            lines.append(line)
            for k,l in enumerate(lines):
                d.text((a+12,yy), ("• " if k==0 else "   ")+l, fill=TXT, font=F(13), anchor="lm"); yy+=19
            yy+=12
        if i<3:
            ax=b+3; my=y0+h/2
            d.line([(ax,my),(ax+12,my)], fill=col, width=3)
            d.polygon([(ax+10,my-6),(ax+19,my),(ax+10,my+6)], fill=col)
    # feedback loop
    ly=y0+h+30; lx1=x0+cw/2; lx2=x0+3*(cw+gap)+cw/2
    d.line([(lx1,ly),(lx2,ly)], fill=RED, width=3); d.line([(lx2,y0+h),(lx2,ly)], fill=RED, width=3); d.line([(lx1,y0+h+8),(lx1,ly)], fill=RED, width=3)
    d.polygon([(lx1-7,y0+h+12),(lx1+7,y0+h+12),(lx1,y0+h+1)], fill=RED)
    t="CONTINUOUS TACIT-TO-EXPLICIT KNOWLEDGE LOOP — RUNS ENTIRELY INSIDE THE PLANT"
    f=F(12,True); w=d.textlength(t,font=f); mx=(lx1+lx2)/2
    d.rounded_rectangle((mx-w/2-12,ly-15,mx+w/2+12,ly+15), radius=6, fill=(20,16,12), outline=RED, width=1)
    d.text((mx,ly), t, fill=WHITE, font=f, anchor="mm")
    return ly+15

def plant_frame(d, x1, y1, x2, y2, title):
    d.rounded_rectangle((x1,y1,x2,y2), radius=12, fill=None, outline=(215,145,60), width=2)
    d.rounded_rectangle((x1+16,y1-14,x1+16+150,y1+14), radius=6, fill=(215,145,60))
    d.text((x1+16+75,y1), "LAYER C", fill=(30,18,8), font=F(13,True), anchor="mm")
    d.rounded_rectangle((x1+176,y1-14,x1+186+d.textlength(title,font=F(14,True))+10,y1+14), radius=6, fill=BG)
    d.text((x1+186,y1), title, fill=GOLD, font=F(14,True), anchor="lm")

def local_box(d, x1, y1, x2, f=13):
    items=[("Private Knowledge Graph (Layer 3)","SOPs, machinery manuals, operator logs and sensor data, stored only inside the factory"),
           ("4-agent cognitive engine","Router · Dual Graph-RAG · Explainable analyst (EU AI Act) · Judge evaluator"),
           ("Factory GPU edge server","Local inference with zero latency; runs the loop even without connectivity")]
    h=28+len(items)*40+8
    d.rounded_rectangle((x1,y1,x2,y1+h),radius=10,fill=CARD,outline=(110,80,50),width=1)
    d.text((x1+14,y1+16),"STAYS INSIDE THE PLANT",fill=GOLD,font=F(12,True),anchor="lm")
    y=y1+40
    for t,dsc in items:
        d.text((x1+14,y),"■ "+t,fill=WHITE,font=F(f,True),anchor="lm")
        d.text((x1+30,y+18),dsc,fill=TXT,font=F(f-1),anchor="lm")
        y+=40
    return y1+h

def no_outbound(d, x, y):
    # crossed upward arrow
    d.line([(x,y+38),(x,y-28)], fill=(120,40,50), width=3)
    d.polygon([(x-8,y-26),(x+8,y-26),(x,y-38)], fill=(120,40,50))
    d.line([(x-12,y-12),(x+12,y+12)], fill=RED, width=4); d.line([(x-12,y+12),(x+12,y-12)], fill=RED, width=4)

# ---------- 1) standalone technical panel ----------
W,H=1024,1180
img=Image.new("RGBA",(W,H),BG); d=ImageDraw.Draw(img)
d.text((W/2,42),"EDGE ENGINE: EMPOWERING THE HUMAN OPERATOR",fill=GOLD,font=F(28,True),anchor="mm")
d.text((W/2,76),"The 4-step loop runs in the plant and is fed by federated cloud services and knowledge",fill=(210,195,180),font=F(16),anchor="mm")
xs=cloud_band(d,40,105,984,265)
by=318
d.text((512,280),"▼ Plant-initiated pull of signed, versioned packages (or mirror repository) · during development the pilots share cleaned, anonymised datasets",fill=CLOUD_D,font=F(12),anchor="mm")
by=322
boundary(d,24,1000,by,xs,470,top=292)
no_outbound(d,985,by+2); d.text((985,by+50),"no data out",fill=RED,font=F(11,True),anchor="mm")
plant_frame(d,24,392,1000,H-24,"FACTORY PLANT · on-premise GPU edge node + Private Knowledge Graph (Layer 3)")
end=steps(d,48,422,928,385,fed=True)
end=local_box(d,48,end+24,976)
d.rounded_rectangle((48,end+16,976,end+80),radius=10,fill=CARD,outline=(215,145,60),width=1)
end-=6
d.text((W/2,end+42),"Validated at TRL 5 in on-premise industrial edge pilots",fill=GOLD,font=F(16,True),anchor="mm")
d.text((W/2,end+66),"Vicky Foods (continuous bakery dough telemetry)   |   AKCOAT (chemical rheology & thermal curing)",fill=WHITE,font=F(13),anchor="mm")
img=img.crop((0,0,W,end+104)); d=ImageDraw.Draw(img)
d.rectangle((0,end+84,W,end+104),fill=BG)
d.rounded_rectangle((24,392,1000,end+92),radius=12,outline=(215,145,60),width=2)
plant_frame(d,24,392,1000,end+92,"FACTORY PLANT · on-premise GPU edge node + Private Knowledge Graph (Layer 3)")
img.save(os.path.join(OUT,"aura_edge_engine_4steps_dark_v2.png"))

# ---------- 2) dual projection ----------
W,H=2048,1400
dual=Image.new("RGBA",(W,H),(12,10,8)); d=ImageDraw.Draw(dual)
d.text((W/2,36),"THE AURA EDGE ENGINE — DUAL OPERATIONAL PROJECTION",fill=GOLD,font=F(26,True),anchor="mm")
d.text((W/2,66),"The closed loop runs inside the plant (Layer C) and is fed from the federated cloud (Layers A + B)  ·  Technical loop (left) | Executive flow (right)",fill=(210,195,180),font=F(16),anchor="mm")
xs=cloud_band(d,40,95,2008,250,scale=1.15)
d.text((W/2,266),"▼ Plant-initiated pull of signed, versioned knowledge packages (models · ontology · oracles · SOP rules) — or via a mirror repository · during development (Stages 1–2) the pilots share cleaned, anonymised datasets with the sandbox",fill=CLOUD_D,font=F(14),anchor="mm")
by=312
boundary(d,20,2028,by,[xs[0],xs[1],xs[2],xs[3]],W/2,top=280)
no_outbound(d,1990,by+2); d.text((1972,by+30),"no telemetry / raw data out",fill=RED,font=F(12,True),anchor="rm")
plant_frame(d,20,380,2028,H-20,"FACTORY PLANT · the 4-step loop runs here, on the on-premise edge node, with full human agency")
# left: loop cards without own cloud band
left=Image.new("RGBA",(1000,980),BG); dl=ImageDraw.Draw(left)
dl.text((500,34),"TECHNICAL 4-STEP CLOSED LOOP",fill=GOLD,font=F(22,True),anchor="mm")
dl.text((500,62),"What each step receives from the cloud, and what stays in the plant",fill=(210,195,180),font=F(14),anchor="mm")
e=steps(dl,24,95,952,400,fed=True)
e=local_box(dl,24,e+26,976,14)-4
dl.rounded_rectangle((24,e+24,976,e+92),radius=10,fill=CARD,outline=(215,145,60),width=1)
dl.text((500,e+46),"Validated at TRL 5 in on-premise industrial edge pilots",fill=GOLD,font=F(16,True),anchor="mm")
dl.text((500,e+72),"Vicky Foods (continuous bakery dough telemetry)   |   AKCOAT (chemical rheology & thermal curing)",fill=WHITE,font=F(13),anchor="mm")
left=left.crop((0,0,1000,e+110))
right=Image.open("aura_bucle_4_etapas.png").convert("RGBA")
ph=H-20-400-20
lh=min(ph, left.size[1]); 
dual.paste(left,(34,410))
rs=min(ph,980); right=right.resize((rs,rs),Image.Resampling.LANCZOS)
dual.paste(right,(1044+(980-rs)//2,410))
d.rounded_rectangle((30,406,1034,410+left.size[1]+4),radius=10,outline=(110,80,50),width=1)
H2=max(410+left.size[1],410+rs)+30
dual=dual.crop((0,0,W,H2)); d=ImageDraw.Draw(dual)
d.rounded_rectangle((20,380,2028,H2-10),radius=12,outline=(215,145,60),width=2)
plant_frame(d,20,380,2028,H2-10,"FACTORY PLANT · the 4-step loop runs here, on the on-premise edge node, with full human agency")
dual.save(os.path.join(OUT,"aura_edge_engine_dual_projection_v2.png"))
print("ok", dual.size, img.size)
