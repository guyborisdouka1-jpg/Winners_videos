import os, sys, subprocess, shutil
from PIL import Image
import engine as E
SLIDES = {"C1_presenter":"classique","C2_make_do":"energie","C3_faux_amis":"mystere","C4_restaurant":"suspense",
          "C5_in_on_at":"energie","C6_travail":"classique","C7_test_niveau":"suspense"}
DUR = [3.0, 5.0, 5.0, 6.5, 5.5, 4.0]   # couverture, contenu, contenu, quiz, réponses, fin
FPS = 24; W, H = 1080, 1920; FADE = 0.4
os.makedirs("diapos", exist_ok=True)
for name, mus in SLIDES.items():
    ims = []
    for k in range(1, 7):
        bg = Image.new("RGB", (W, H), (30, 34, 110))
        im = Image.open(f"images/{name}_{k}.png").convert("RGB")
        bg.paste(im, (0, (H - 1350) // 2)); ims.append(bg)
    total = sum(DUR); fd = f"/tmp/diapo_{name}"; shutil.rmtree(fd, ignore_errors=True); os.makedirs(fd)
    starts = [sum(DUR[:i]) for i in range(6)]
    for fi in range(int(total * FPS)):
        t = fi / FPS; i = max(j for j in range(6) if starts[j] <= t)
        fr = ims[i]
        if i > 0 and t - starts[i] < FADE:
            fr = Image.blend(ims[i - 1], ims[i], (t - starts[i]) / FADE)
        fr.save(f"{fd}/{fi:05d}.png")
    wav = f"{fd}/a.wav"
    E.make_audio(wav, [], total + 5, total, **E.MUSIC[mus])
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", f"{fd}/%05d.png", "-i", wav,
                    "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k",
                    "-shortest", "-movflags", "+faststart", f"diapos/{name}_video.mp4"], check=True)
    shutil.rmtree(fd); print(name)
