import numpy as np, wave, sys, json
WORDS=json.loads(sys.argv[1]); OUT=sys.argv[2]; END=float(sys.argv[3]); T=float(sys.argv[4])
SR=44100; N=int(T*SR); mix=np.zeros(N)
hz=lambda m:440*2**((m-69)/12)
noise=np.random.default_rng(7).standard_normal(3*SR)
def add(st,a,g=1):
    k=int(st*SR); e=min(N,k+len(a))
    if 0<=k<N: mix[k:e]+=a[:e-k]*g
def osc(fr,dur,kind):
    n=np.arange(int(dur*SR))/SR
    if kind=="saw": return sum(np.sin(2*np.pi*fr*k*n)/k for k in range(1,8))*.6
    if kind=="sq": return sum(np.sin(2*np.pi*fr*k*n)/k for k in range(1,9,2))*.8
    return np.sin(2*np.pi*fr*n)
def env(a,att,dec):
    n=np.arange(len(a))/SR; return a*np.minimum(1,n/att)*np.exp(-n*dec)
B=60/128; prog=[(45,[69,72,76]),(41,[65,69,72]),(43,[67,71,74]),(40,[64,68,71])]
t=0;bar=0
while t<T:
    root,ch=prog[bar%4]
    for e8 in range(8): add(t+e8*B/2,env(osc(hz(root),B/2*.9,"saw"),.003,8),.11)
    for s in range(16):
        if s in (0,3,6,8,11,14):
            for m in ch: add(t+s*B/4,env(osc(hz(m),.14,"sq"),.002,22),.025)
        add(t+s*B/4,env(noise[:int(.03*SR)],.001,140),.03 if s%2 else .012)
    for b in range(4):
        n=np.arange(int(.25*SR))/SR; add(t+b*B,np.sin(2*np.pi*(55+90*np.exp(-n*30))*n)*np.exp(-n*12),.32)
    for b in (1,3): add(t+b*B,env(noise[:int(.15*SR)],.001,25),.07)
    for k in range(8):
        n=np.arange(int(.04*SR))/SR; add(t+k*B/2,np.sin(2*np.pi*(1800 if k%2==0 else 1400)*n)*np.exp(-n*90),.05)
    t+=4*B; bar+=1
tt=np.arange(N)/SR; mix*=np.minimum(1,tt/.3)
def hit(st,g):
    n=np.arange(int(1.0*SR))/SR
    add(st,np.sin(2*np.pi*(45+120*np.exp(-n*20))*n)*np.exp(-n*4)+.5*noise[:len(n)]*np.exp(-n*10),g)
def roll(st,dur):
    k=0
    while k*.035<dur:
        n=np.arange(int(.03*SR))/SR; add(st+k*.035,noise[:len(n)]*np.exp(-n*80),.05+.12*(k*.035/dur)); k+=1
def ding(st):
    for k,m in enumerate([84,88,91]):
        n=np.arange(int(.7*SR))/SR; fr=hz(m); add(st+k*.06,(np.sin(2*np.pi*fr*n)+.3*np.sin(4*np.pi*fr*n))*np.exp(-n*5),.14)
hit(.1,.55)
for st in WORDS: roll(st-.55,.5); ding(st)
hit(END+.02,.6)
for k,m in enumerate([72,76,79,84,88]):
    n=np.arange(int(1.0*SR))/SR; add(END+.1+k*.11,(np.sin(2*np.pi*hz(m)*n)+.3*np.sin(4*np.pi*hz(m)*n))*np.exp(-n*3.5),.16)
mix*=np.clip((T-tt)/1.2,0,1); mix=mix/np.abs(mix).max()*.9
with wave.open(OUT,'w') as w:
    w.setnchannels(1);w.setsampwidth(2);w.setframerate(SR);w.writeframes((mix*32767).astype(np.int16).tobytes())
