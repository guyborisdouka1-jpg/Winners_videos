"""Moteur de vidéos Winners' English Center (sans voix, musique jeu-concours).
Usage : python3 engine.py <nom_spec>   (spec dans specs.py)
"""
import subprocess, wave, os, math, sys, shutil
import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SR = 44100; S = 1.5; W, H = int(720 * S), int(1280 * S); FPS = 24

# ------------------------------------------------------------ timing
DUR = dict(quiz=10.6, order=9.5, vf=9.0, nedis=8.8, traduis=9.3)
def item_timing(kind, it, st):
    if kind == "quiz":
        return dict(st=st, app=[st + .8, st + 1.4, st + 2.0], cd=st + 2.8, rv=st + 7.8, end=st + 10.6)
    if kind == "order":
        n = len(it["words"]); return dict(st=st, app=[st + .5 + k * .15 for k in range(n)], cd=st + 1.6, rv=st + 6.6, end=st + 9.5)
    if kind == "vf":
        return dict(st=st, app=[st + .5, st + 1.2], cd=st + 2.0, rv=st + 6.0, end=st + 9.0)
    if kind == "nedis":
        return dict(st=st, app=[st + .4, st + 1.2], cd=st + 1.8, rv=st + 5.8, end=st + 8.8)
    if kind == "traduis":
        return dict(st=st, app=[st + .5], cd=st + 1.3, rv=st + 6.3, end=st + 9.3)
    if kind == "convo":
        n = len(it["lines"]); app = [st + .6 + k * 1.1 for k in range(n)]
        cd = app[-1] + .7; return dict(st=st, app=app, cd=cd, rv=cd + 4, end=cd + 7.5)

def build_timeline(spec):
    tl = []; t = 2.5
    for it in spec["items"]:
        tm = item_timing(spec["kind"], it, t); tl.append(tm); t = tm["end"]
    return tl, t, t + 4.5

# ------------------------------------------------------------ audio
MUSIC = {
 "classique": dict(bpm=120, prog=[(45, [69, 72, 76, 72]), (41, [65, 69, 72, 69]), (38, [62, 65, 69, 65]), (40, [64, 68, 71, 68])],
                   wave_type="sine", pattern="xxxxxxxxxxxxxxxx", kick=[0, 2], tick_fr=1800, jingle=[72, 76, 79, 84]),
 "suspense": dict(bpm=100, prog=[(50, [62, 65, 69, 65]), (46, [58, 62, 65, 62]), (48, [60, 64, 67, 64]), (45, [61, 64, 69, 64])],
                  wave_type="square", pattern="x.x.x.x.x.x.x.xx", kick=[0, 2], tick_fr=1600, jingle=[74, 78, 81, 86]),
 "energie": dict(bpm=132, prog=[(52, [64, 67, 71, 67]), (48, [60, 64, 67, 64]), (55, [67, 71, 74, 71]), (50, [62, 66, 69, 66])],
                 wave_type="saw", pattern="xxxxxxxxxxxxxxxx", kick=[0, 1, 2, 3], tick_fr=2000, jingle=[76, 79, 83, 88]),
 "mystere": dict(bpm=92, prog=[(48, [72, 75, 79, 75]), (44, [68, 72, 75, 72]), (41, [65, 68, 72, 68]), (43, [67, 71, 74, 71])],
                 wave_type="sine", pattern="x..xx..xx..x.x.x", kick=[0, 2], tick_fr=1300, jingle=[72, 76, 79, 84]),
}
def hz(m): return 440 * 2 ** ((m - 69) / 12)

def make_audio(path, tl, outro_t, TOTAL, bpm, prog, wave_type, pattern, kick, tick_fr, jingle):
    N = int(TOTAL * SR) + SR; mix = np.zeros(N, np.float32)
    noise = np.random.default_rng(1).standard_normal(2 * SR).astype(np.float32)
    def add(st, a, g=1.0):
        k = int(st * SR); e = min(N, k + len(a))
        if 0 <= k < N: mix[k:e] += a[:e - k] * g
    def osc(fr, dur, kind):
        n = np.arange(int(dur * SR)) / SR
        if kind == "saw": return sum(np.sin(2 * np.pi * fr * k * n) / k for k in range(1, 8)) * .64
        if kind == "square": return sum(np.sin(2 * np.pi * fr * k * n) / k for k in range(1, 9, 2)) * .8
        return np.sin(2 * np.pi * fr * n) + .3 * np.sin(4 * np.pi * fr * n)
    def env(a, att, dec):
        n = np.arange(len(a)) / SR; return a * np.minimum(1, n / att) * np.exp(-n * dec)
    B = 60 / bpm
    for bar in range(int(TOTAL / (4 * B)) + 1):
        t0 = bar * 4 * B; root, chord = prog[bar % len(prog)]
        for e8 in range(8): add(t0 + e8 * B / 2, env(osc(hz(root), B / 2 * .9, "saw"), .003, 9) * .10)
        for s in range(16):
            if pattern[s] == "x": add(t0 + s * B / 4, env(osc(hz(chord[s % 4]), .15, wave_type), .002, 25) * .05)
            add(t0 + s * B / 4, env(noise[:int(.03 * SR)], .001, 120) * (.03 if s % 2 else .012))
        for b in kick:
            n = np.arange(int(.25 * SR)) / SR
            add(t0 + b * B, np.sin(2 * np.pi * (55 + 90 * np.exp(-n * 30)) * n) * np.exp(-n * 12) * .3)
        if len(kick) < 4:
            for b in (1, 3): add(t0 + b * B, env(noise[:int(.15 * SR)], .001, 25) * .06)
        n = np.arange(int(4 * B * SR)) / SR
        add(t0, (np.sin(2 * np.pi * hz(root - 12) * n) + .4 * np.sin(2 * np.pi * hz(root + 7) * n))
            * np.minimum(1, n / .3) * np.minimum(1, (4 * B - n) / .3) * .05)
    tt = np.arange(N) / SR; mix *= np.minimum(1, tt) * np.clip((TOTAL - tt) / 2, 0, 1)
    def hit(st, g):
        n = np.arange(int(1.2 * SR)) / SR
        add(st, np.sin(2 * np.pi * (45 + 120 * np.exp(-n * 20)) * n) * np.exp(-n * 4) + .5 * noise[:len(n)] * np.exp(-n * 10), g)
    def whoosh(st):
        n = np.arange(int(.5 * SR)) / SR
        add(st, np.sin(2 * np.pi * np.cumsum(300 + 2500 * n) / SR) * np.sin(np.pi * n / .5) * .08)
        add(st, noise[:len(n)] * np.sin(np.pi * n / .5) * .05)
    def correct(st):
        for k, m in enumerate(jingle):
            n = np.arange(int(.6 * SR)) / SR; fr = hz(m)
            add(st + k * .09, (np.sin(2 * np.pi * fr * n) + .3 * np.sin(4 * np.pi * fr * n)) * np.exp(-n * 5) * .16)
    hit(.15, .6)
    for tm in tl:
        whoosh(tm["st"] + .1)
        for o in tm["app"]: add(o, env(np.sin(2 * np.pi * 1200 * np.arange(int(.05 * SR)) / SR), .001, 60) * .1)
        nt = int(round((tm["rv"] - tm["cd"]) / .5))
        for k in range(nt):
            n = np.arange(int(.04 * SR)) / SR
            add(tm["cd"] + k * .5, np.sin(2 * np.pi * (tick_fr if k % 2 == 0 else tick_fr * .78) * n) * np.exp(-n * 90) * (.18 + .025 * k))
        n = np.arange(int(1.5 * SR)) / SR
        add(tm["rv"] - 1.5, np.sin(2 * np.pi * np.cumsum(200 + 600 * n / 1.5) / SR) * (n / 1.5) ** 2 * .08)
        hit(tm["rv"], .45); correct(tm["rv"] + .05)
    hit(outro_t, .5); correct(outro_t + .1)
    mix = mix / np.abs(mix).max() * .9
    with wave.open(path, "w") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((mix[:int(TOTAL * SR)] * 32767).astype(np.int16).tobytes())

# ------------------------------------------------------------ visuals
FP = "/usr/share/fonts/truetype/google-fonts/Poppins-"
_fc = {}
def f(wt, s):
    k = (wt, int(s * S))
    if k not in _fc: _fc[k] = ImageFont.truetype(FP + wt + ".ttf", k[1])
    return _fc[k]
SYM = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
NAVY = (30, 34, 110); NAVY2 = (46, 49, 146); RED = (190, 45, 45); GOLD = (245, 190, 70); WHITE = (255, 255, 255)
GREEN = (40, 170, 90); GREY = (95, 100, 155); SOFT = (205, 205, 235); DIM = (130, 135, 180)
LOGO = Image.open(os.path.join(HERE, "logo_rond.png")).convert("RGBA").resize((int(110 * S),) * 2, Image.LANCZOS)
def ease(x): x = max(0, min(1, x)); return 1 - (1 - x) ** 3
def P(*v): return tuple(int(x * S) for x in v)
def sym(s): return ImageFont.truetype(SYM, int(s * S))

_BASE = None
def base():
    global _BASE
    if _BASE is None:
        im = Image.new("RGB", (W, H), NAVY); d = ImageDraw.Draw(im)
        d.ellipse(P(440, -200, 1000, 330), fill=NAVY2); d.ellipse(P(-280, 960, 280, 1500), fill=NAVY2)
        d.text(P(360, 110), "I speak English, and you ?", font=f("Italic", 30), fill=SOFT, anchor="mm")
        d.text(P(360, 1170), "Abonne-toi pour plus de vidéos", font=f("Medium", 28), fill=SOFT, anchor="mm")
        im.paste(LOGO, P(30, 195), LOGO)
        d.text(P(155, 225), "WINNERS'", font=f("Bold", 28), fill=GOLD, anchor="lm")
        d.text(P(155, 262), "ENGLISH CENTER", font=f("Bold", 28), fill=WHITE, anchor="lm")
        d.rectangle(P(0, 1020, 720, 1090), fill=RED)
        d.text(P(360, 1055), "0767037284  •  Cocody Riviera Palmeraie", font=f("Bold", 26), fill=WHITE, anchor="mm")
        _BASE = im
    im = _BASE.copy(); return im, ImageDraw.Draw(im)

def wrap(d, text, font, maxw):
    out = []
    for para in text.split("\n"):
        line = ""
        for w_ in para.split(" "):
            test = (line + " " + w_).strip()
            if d.textlength(test, font=font) <= maxw * S or not line: line = test
            else: out.append(line); line = w_
        out.append(line)
    return out
def centered(d, y, text, font, fill, maxw=640):
    lines = wrap(d, text, font, maxw); lh = int(font.size * 1.2)
    y0 = int(y * S) - (len(lines) - 1) * lh // 2
    for j, l in enumerate(lines): d.text((W // 2, y0 + j * lh), l, font=font, fill=fill, anchor="mm")
    return len(lines)

def countdown(d, t, tm, y=940):
    if tm["cd"] <= t < tm["rv"]:
        n = max(1, math.ceil(tm["rv"] - t)); rr = int(48 * (1 + .08 * max(0, 1 - ((tm["rv"] - t) % 1) * 4)))
        d.ellipse(P(360 - rr, y - rr, 360 + rr, y + rr), fill=RED)
        d.text(P(360, y), str(n), font=f("Bold", 56), fill=WHITE, anchor="mm")
def note_box(d, text, y=940, col=RED):
    d.rounded_rectangle(P(40, y - 50, 680, y + 50), 24, fill=WHITE)
    centered(d, y, text, f("Bold", 27), col, 600)
def badge(d, txt):
    d.rounded_rectangle(P(560, 215, 690, 265), 25, fill=RED)
    d.text(P(625, 240), txt, font=f("Bold", 26), fill=WHITE, anchor="mm")

def option_rows(d, t, tm, opts, ok, y0=440, letters="ABC"):
    rev = t >= tm["rv"]; fs = 30 if max(map(len, opts)) < 24 else 25
    for k, o in enumerate(opts):
        p = ease((t - tm["app"][k]) / .35)
        if p <= 0: continue
        y = y0 + k * 112; x = 40 + int((1 - p) * 700); good = k == ok
        col = GREEN if (rev and good) else (GREY if rev else WHITE); tc = WHITE if rev else NAVY
        d.rounded_rectangle(P(x, y, x + 640, y + 95), 26, fill=col)
        d.ellipse(P(x + 15, y + 20, x + 70, y + 75), fill=GOLD if not (rev and not good) else DIM)
        d.text(P(x + 42, y + 48), letters[k], font=f("Bold", 30), fill=NAVY, anchor="mm")
        d.text(P(x + 90, y + 48), o, font=f("Bold", fs), fill=tc, anchor="lm")
        if rev: d.text(P(x + 605, y + 48), "✓" if good else "✗", font=sym(40), fill=WHITE, anchor="mm")

def chips(d, words, y, fill, tc, alpha_list=None, size=32):
    font = f("Bold", size); pad = 22; gap = 14
    widths = [d.textlength(w_, font=font) / S + 2 * pad for w_ in words]
    rows, cur, cw = [], [], 0
    for w_, wd in zip(words, widths):
        if cur and cw + wd + gap > 640: rows.append(cur); cur, cw = [], 0
        cur.append((w_, wd)); cw += wd + gap
    rows.append(cur); idx = 0
    for r, row in enumerate(rows):
        tw = sum(wd for _, wd in row) + gap * (len(row) - 1); x = 360 - tw / 2; yy = y + r * 80
        for w_, wd in row:
            p = 1 if alpha_list is None else alpha_list[idx]
            if p > 0:
                dy = (1 - p) * 40
                d.rounded_rectangle(P(x, yy + dy, x + wd, yy + 62 + dy), 18, fill=fill)
                d.text(P(x + wd / 2, yy + 31 + dy), w_, font=font, fill=tc, anchor="mm")
            x += wd + gap; idx += 1

def bubble(d, x_right, y, text, who, color, tc, maxw=470):
    font = f("Bold", 28); lines = wrap(d, text, font, maxw)
    tw = max(d.textlength(l, font=font) for l in lines) / S; h = 30 + len(lines) * 40
    bw = tw + 40
    x0 = 40 if not x_right else 680 - bw
    d.rounded_rectangle(P(x0, y, x0 + bw, y + h), 22, fill=color)
    d.text(P(x0 + (14 if not x_right else bw - 14), y - 16), who, font=f("Bold", 20), fill=GOLD, anchor="lm" if not x_right else "rm")
    for j, l in enumerate(lines): d.text(P(x0 + 20, y + 15 + j * 40 + 20), l, font=font, fill=tc, anchor="lm")
    return h

def draw_item(d, kind, it, tm, t, i, n):
    rev = t >= tm["rv"]
    badge(d, f"{i + 1}/{n}")
    if kind == "quiz":
        centered(d, 360, it["q"], f("Bold", 38), WHITE)
        option_rows(d, t, tm, it["opts"], it["ok"])
        countdown(d, t, tm)
        if rev: note_box(d, it["note"])
    elif kind == "order":
        centered(d, 330, "Remets les mots dans l'ordre :", f("Medium", 30), SOFT)
        al = [ease((t - a) / .3) for a in tm["app"]]
        chips(d, it["words"], 390, WHITE if not rev else DIM, NAVY, al)
        if rev:
            p = ease((t - tm["rv"]) / .5)
            sol = it["answer"].split(" ")
            chips(d, sol, 600, GREEN, WHITE, [ease((t - tm["rv"] - k * .12) / .3) for k in range(len(sol))])
            if t > tm["rv"] + .6: centered(d, 800, "« " + it["fr"] + " »", f("Medium", 28), SOFT)
        countdown(d, t, tm)
        if rev: note_box(d, "Tu l'avais ? Note ton point !", 940, NAVY)
    elif kind == "vf":
        centered(d, 330, "Cette phrase est-elle correcte ?", f("Medium", 30), SOFT)
        p = ease((t - tm["app"][0]) / .4)
        if p > 0:
            d.rounded_rectangle(P(40, 380, 680, 560), 30, fill=WHITE)
            col = NAVY if not rev else (GREEN if it["vrai"] else RED)
            centered(d, 470, "« " + it["s"] + " »", f("Bold", 36 if len(it["s"]) < 26 else 30), col, 600)
        p2 = ease((t - tm["app"][1]) / .35)
        if p2 > 0:
            for k, (lab, isv) in enumerate([("VRAI", True), ("FAUX", False)]):
                x = 60 + k * 320; good = isv == it["vrai"]
                fill = (GREEN if good else DIM) if rev else (GREEN if isv else RED)
                yy = 600 + (1 - p2) * 60
                d.rounded_rectangle(P(x, yy, x + 280, yy + 100), 30, fill=fill)
                d.text(P(x + 140, yy + 50), lab, font=f("Bold", 40), fill=WHITE, anchor="mm")
                if rev and good: d.text(P(x + 245, yy + 50), "✓", font=sym(36), fill=WHITE, anchor="mm")
        if rev and t > tm["rv"] + .3:
            centered(d, 780, it["note"], f("Bold", 30), GOLD)
        countdown(d, t, tm)
        if rev: note_box(d, "Vrai : " + it["fix"] if not it["vrai"] else "Bravo si tu as dit VRAI !", 940, GREEN)
    elif kind == "nedis":
        p = ease((t - tm["app"][0]) / .4)
        d.text(P(360, 345), "NE DIS PLUS", font=f("Bold", 34), fill=RED if p > 0 else NAVY, anchor="mm")
        if p > 0:
            d.rounded_rectangle(P(40, 385, 680, 545), 30, fill=WHITE)
            n_ = centered(d, 465, it["wrong"], f("Bold", 40), RED, 580)
            if t >= tm["app"][1]:
                q = ease((t - tm["app"][1]) / .4)
                d.line(P(80, 465, 80 + 560 * q, 465), fill=RED, width=int(6 * S))
                d.text(P(640, 400), "✗", font=sym(40), fill=RED, anchor="mm")
        if tm["cd"] <= t < tm["rv"]: centered(d, 640, "Comment on dit alors ?", f("Bold", 34), GOLD)
        if rev:
            q = ease((t - tm["rv"]) / .4)
            d.text(P(360, 610), "DIS PLUTÔT", font=f("Bold", 34), fill=GREEN, anchor="mm")
            yy = 650 + (1 - q) * 50
            d.rounded_rectangle(P(40, yy, 680, yy + 160), 30, fill=GREEN)
            centered(d, yy + 80, it["right"], f("Bold", 40), WHITE, 580)
            note_box(d, it["note"], 940, NAVY)
        countdown(d, t, tm)
    elif kind == "traduis":
        centered(d, 330, "Comment dit-on en anglais :", f("Medium", 30), SOFT)
        p = ease((t - tm["app"][0]) / .4)
        if p > 0:
            d.rounded_rectangle(P(40, 380, 680, 560), 30, fill=WHITE)
            centered(d, 470, "« " + it["fr"] + " »", f("Bold", 42), NAVY, 580)
        if rev:
            q = ease((t - tm["rv"]) / .4); yy = 600 + (1 - q) * 50
            d.rounded_rectangle(P(40, yy, 680, yy + 170), 30, fill=GREEN)
            centered(d, yy + 85, it["en"], f("Bold", 46), WHITE, 580)
            note_box(d, it["note"], 940, NAVY)
        countdown(d, t, tm)
    elif kind == "convo":
        centered(d, 325, "Trouve la faute !", f("Bold", 34), GOLD)
        y = 400
        for k, (who, txt) in enumerate(it["lines"]):
            if t < tm["app"][k]: break
            right = k % 2 == 1; bad = k == it["bad"]
            show = it["fix"] if (rev and bad) else txt
            col = (GREEN if rev and bad else WHITE); tc = WHITE if rev and bad else NAVY
            h = bubble(d, right, y, show, who, col, tc)
            if rev and bad:
                d.text(P(680 if not right else 40, y + h / 2), "✓", font=sym(36), fill=GREEN, anchor="rm" if not right else "lm")
            y += h + 40
        countdown(d, t, tm)
        if rev: note_box(d, "Correct : « " + it["ok"] + " »", 940, GREEN)

def render(name, spec, outdir):
    tl, outro_t, TOTAL = build_timeline(spec)
    fdir = f"/tmp/frames_{name}"; shutil.rmtree(fdir, ignore_errors=True); os.makedirs(fdir)
    wav = f"{fdir}/a.wav"; make_audio(wav, tl, outro_t, TOTAL, **MUSIC[spec["music"]])
    n = len(spec["items"])
    for fi in range(int(TOTAL * FPS)):
        t = fi / FPS; im, d = base()
        if t < 2.5:
            p = ease((t - .15) / .6)
            centered(d, 560, spec["title"], f("Bold", 30 + 26 * p), GOLD)
            if t > 1.0: centered(d, 690, spec["sub"], f("Medium", 32), SOFT)
        elif t < outro_t:
            i = next(k for k, tm in enumerate(tl) if t < tm["end"])
            draw_item(d, spec["kind"], spec["items"][i], tl[i], t, i, n)
        else:
            p = ease((t - outro_t) / .6)
            centered(d, 400, spec["outro1"], f("Bold", 34 + 24 * p), GOLD)
            centered(d, 560, spec["outro2"], f("Bold", 40), WHITE)
            if t > outro_t + 1.5:
                d.rounded_rectangle(P(80, 760, 640, 960), 30, fill=WHITE)
                centered(d, 820, "Cours d'anglais • Inscriptions", f("Bold", 30), NAVY)
                centered(d, 895, "0767037284", f("Bold", 54), RED)
        im.save(f"{fdir}/{fi:05d}.png")
    out = os.path.join(outdir, name + ".mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", f"{fdir}/%05d.png", "-i", wav,
                    "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k",
                    "-shortest", "-movflags", "+faststart", out], check=True)
    shutil.rmtree(fdir)
    print(name, round(TOTAL, 1), "s")

if __name__ == "__main__":
    import specs
    outdir = os.path.join(HERE, "videos"); os.makedirs(outdir, exist_ok=True)
    for nm in sys.argv[1:]: render(nm, specs.SPECS[nm], outdir)
