import sys; sys.path.insert(0,'/tmp/gen')
from b2 import *

# ---- B1 · 1,6 s · l'accroche ----
s = header(1.6)
s += '<div class="abs" style="left:560px;top:170px;font:900 1100px Inter;color:transparent;-webkit-text-stroke:4px rgba(12,127,143,.2);line-height:1">?</div>'
s += post(90,270,'createur.jpg','@createur','transform:rotate(-1.2deg)')
s += '''<div class="mini" style="left:560px;top:960px;width:430px;height:310px;transform:rotate(4deg);padding:20px"><svg width="390" height="270" viewBox="0 0 390 270">
<line x1="0" y1="250" x2="390" y2="250" stroke="#cfd8d8" stroke-width="3"/><path d="M0,30 C80,34 220,44 380,56" fill="none" stroke="#0C7F8F" stroke-width="9" stroke-linecap="round"/><circle cx="380" cy="56" r="13" fill="#0C7F8F"/>
<path d="M0,30 C80,40 120,150 190,200 S300,240 380,244" fill="none" stroke="#8aa0a4" stroke-width="6" stroke-linecap="round" stroke-dasharray="2 14"/>
<text x="150" y="112" font-family="JetBrains Mono" font-weight="800" font-size="19" fill="#0B5560">JUSQU'À LA FIN</text><text x="185" y="236" font-family="JetBrains Mono" font-weight="800" font-size="19" fill="#6c8387">LES AUTRES</text></svg></div>'''
s += '<div class="chip" style="left:90px;top:226px;display:none">x</div>'
s += peek('premiere.jpg','@autre.video')
s += sub(1420, "te gardent <span class='kw'>jusqu'à la fin</span> ?")
page('B1', s)

# ---- B2 · 4,9 s · le crush écrit ----
s = header(4.9)
s += post(90,330,'cinema.jpg','@video.en.cours','transform:rotate(1deg)')
s += video_bar(980, 55)
for dy,op,bl in [(-190,.12,14),(-100,.26,8)]:
    s += notif(60, 230+dy+110, -2, f'opacity:{op};filter:blur({bl}px)')
s += notif(70, 250, -2, 'transform:rotate(-2deg) scale(1.06);')
s += peek('createur.jpg','@suivant')
s += sub(1420, "ton crush <span class='kw'>t'écrit</span> enfin")
page('B2', s)

# ---- B3 · 6,9 s · ignoré ----
s = header(6.9)
s += post(90,330,'cinema.jpg','@video.en.cours','transform:rotate(1deg)')
s += video_bar(980, 92)
for dx,op,bl in [(-250,.13,13),(-130,.28,7)]:
    s += notif(75+dx, 230, -2, f'opacity:{op};filter:blur({bl}px)')
s += notif(75, 236, -2)
s += '<div class="chip" style="left:90px;top:470px;font-size:30px;padding:10px 20px">← IGNORER</div>'
s += peek('createur.jpg','@suivant')
s += sub(1420, "mais tu l'<span class='kw pk'>ignores</span>")
page('B3', s)

# ---- B4 · 9,6 s · le pivot (la question) ----
s = header(9.6)
s += '<div class="abs" style="left:180px;top:150px;font:900 1300px Inter;color:transparent;-webkit-text-stroke:5px rgba(12,127,143,.2);line-height:1;filter:blur(1px)">?</div>'
s += '<div class="mini" style="left:-120px;top:520px;width:420px;height:300px;transform:rotate(-7deg);filter:blur(9px);opacity:.6"><img src="a/createur.jpg"></div>'
s += '<div class="mini" style="left:800px;top:880px;width:420px;height:300px;transform:rotate(6deg);filter:blur(9px);opacity:.6"><img src="a/cadreur.jpg"></div>'
s += '<div class="mini" style="left:110px;top:520px;width:860px;height:484px;transform:rotate(-1.2deg);box-shadow:0 34px 80px rgba(11,34,41,.35),0 0 0 8px #0C7F8F"><img src="a/grading.jpg"></div>'
s += '<div class="chip" style="left:110px;top:1060px;font-size:28px">LOG  ▸  ÉTALONNÉ</div>'
s += sub(1420, "qu'est-ce qu'elles ont <span class='kw'>de plus</span> ?", 56)
page('B4', s)

# ---- B5 · 12,3 s · « Moi, c'est James » ----
s = header(12.3)
s += '<div class="abs" style="left:300px;top:230px;width:480px;height:480px;border-radius:50%;background:conic-gradient(from 210deg,#0C7F8F,#9fdde5,#0C7F8F);padding:12px;box-shadow:0 36px 80px rgba(11,34,41,.3)"><div style="width:100%;height:100%;border-radius:50%;overflow:hidden;border:10px solid #F1EEE7"><img src="a/portrait.jpg" style="width:100%;height:100%;object-fit:cover;object-position:50% 22%"></div></div>'
s += '<div class="abs" style="left:300px;top:230px;width:480px;height:480px;border-radius:50%;border:3px solid rgba(12,127,143,.35);transform:scale(1.22)"></div>'
s += '<div class="abs wm-top" style="left:0;right:0;top:780px">JAMES</div>'
s += '<div class="abs" style="left:0;right:0;top:842px;display:flex;justify-content:center">'+ledword(128)+'</div>'
s += '<div class="abs handle" style="left:0;right:0;top:996px;text-align:center">@jamesframotion</div>'
s += '<div class="mini" style="left:70px;top:1110px;width:270px;height:190px;transform:rotate(-4deg)"><img src="a/timeline.jpg"></div><div class="mini" style="left:405px;top:1130px;width:270px;height:190px"><img src="a/grading.jpg"></div><div class="mini" style="left:740px;top:1110px;width:270px;height:190px;transform:rotate(4deg)"><img src="a/cinema.jpg"></div>'
s += sub(1420, "Moi, c'est <span class='kw'>James</span>")
page('B5', s)

# ---- B6 · 15,6 s · les compétences sur la timeline ----
s = header(15.6)
s += '<div class="post" style="left:90px;top:260px;height:560px;padding:30px;transform:rotate(-.8deg)">'
s += '<div style="height:60px"><span class="pill">Premiere Pro</span><span class="pill">CapCut</span><span class="pill">DaVinci</span></div>'
s += '<div class="abs" style="left:30px;top:100px;width:840px;height:400px;border-radius:20px;background:#0B2229"></div>'
clips = [(30,128,260,'HOOK VISUEL','#0C7F8F'),(330,128,210,'TRANSITION','#12A3B5'),(590,128,150,'MASK','#0C7F8F'),
         (110,206,330,'ÉTALONNAGE','#14909F'),(500,206,170,'VFX','#0C7F8F'),
         (160,284,520,'SOUND DESIGN','#1c6f77')]
for x,y,w,l,c in clips:
    s += f'<div class="clipb" style="left:{30+x}px;top:{y+30}px;width:{w}px;background:{c}">{l}</div>'
# forme d'onde dans la piste son
wave = ''.join(f'<i style="position:absolute;left:{400+i*9}px;top:{372-int(8+22*abs(__import__("math").sin(i*.7)))}px;width:4px;height:{int(16+44*abs(__import__("math").sin(i*.7)))}px;background:rgba(255,255,255,.55);border-radius:3px"></i>' for i in range(40))
s += f'<div class="abs" style="left:0;top:0">{wave}</div>'
s += '<div class="abs" style="left:358px;top:112px;width:5px;height:300px;background:#9fdde5;box-shadow:0 0 16px rgba(159,221,229,.8)"></div>'
s += '</div>'
s += '<div class="mini" style="left:200px;top:880px;width:600px;height:420px;transform:rotate(1.6deg)"><img src="a/premiere.jpg"></div>'
s += '<div class="mini" style="left:690px;top:1060px;width:420px;height:300px;transform:rotate(-5deg);filter:blur(8px);opacity:.6"><img src="a/pc.jpg"></div>'
s += sub(1420, "<span class='kw'>sound design</span>")
page('B6', s)

# ---- B7 · 20 s · chaque détail ----
s = header(20.0)
s += '<div class="mini" style="left:90px;top:300px;width:780px;height:455px;transform:rotate(-2deg)"><img src="a/timeline.jpg"></div>'
s += '<div class="abs" style="left:430px;top:690px;width:2px;height:240px;background:#0C7F8F;transform:rotate(18deg);transform-origin:top"></div>'
s += '<div class="abs" style="left:330px;top:760px;width:560px;height:560px;border-radius:50%;box-shadow:0 30px 70px rgba(11,34,41,.35);border:12px solid #0C7F8F;background:#0B2229 url(a/timeline.jpg) -980px -390px/2400px auto"></div>'
s += '<div class="abs" style="left:300px;top:1180px;width:150px;height:30px;background:#0C7F8F;border-radius:16px;transform:rotate(-38deg)"></div>'
s += '<div class="mini" style="left:760px;top:420px;width:420px;height:300px;transform:rotate(6deg);filter:blur(9px);opacity:.5"><img src="a/cadreur.jpg"></div>'
s += sub(1420, "Chaque <span class='kw'>détail</span> est pensé")
page('B7', s)

# ---- B8 · 25,2 s · les services ----
s = header(25.2)
s += '<div class="post" style="left:70px;top:270px;width:940px;height:830px;padding:34px;transform:rotate(-.6deg)">'
s += '<div class="hd"><div class="av"><i></i></div><div class="nm">@jamesframotion<small>monteur vidéo</small></div></div></div>'
tiles=[('cadreur.jpg','PUBLICITÉ'),('timeline.jpg','VIDÉO MARKETING'),('cinema.jpg','DOCUMENTAIRE'),('pc.jpg','CLIP MUSICAL'),
       ('createur.jpg','PODCAST'),('premiere.jpg','SKETCH'),(None,'SOUS-TITRES ANIMÉS'),('portrait.jpg','')]
for i,(img,lab) in enumerate(tiles):
    col, row = i%4, i//4
    x = 108 + col*226; y = 440 + row*330
    hot = (i==3)
    ring = 'box-shadow:0 0 0 8px #0C7F8F,0 24px 50px rgba(12,127,143,.5);transform:scale(1.07)' if hot else ''
    if img: s += f'<div class="tile" style="left:{x}px;top:{y}px;{ring}"><img src="a/{img}"></div>'
    else: s += f'<div class="tile" style="left:{x}px;top:{y}px;background:#0C7F8F;display:flex;align-items:center;justify-content:center;color:#fff;font:900 40px Inter;text-align:center;line-height:1.05;padding:16px">Aa<br>…</div>'
    if lab: s += f'<div class="tl" style="left:{x}px;top:{y+222}px;{"color:#0C7F8F;font-weight:800" if hot else ""}">{lab}</div>'
s += '<div class="mini" style="left:760px;top:1220px;width:420px;height:300px;transform:rotate(5deg);filter:blur(9px);opacity:.45"><img src="a/grading.jpg"></div>'
s += sub(1420, "documentaire, <span class='kw'>clip musical</span>")
page('B8', s)

# ---- B9 · 34,7 s · fin : DM + abonne-toi ----
SOC = {'tt':'<svg width="46" height="46" viewBox="0 0 24 24" fill="#fff"><path d="M16 3c.3 2.3 1.7 3.9 4 4.1v3.2c-1.5 0-2.9-.5-4-1.3v6.2a5.6 5.6 0 1 1-5.6-5.6c.3 0 .6 0 .9.1v3.3a2.4 2.4 0 1 0 1.5 2.2V3H16z"/></svg>',
       'ig':'<svg width="46" height="46" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.3" cy="6.7" r="1" fill="#fff"/></svg>',
       'fb':'<svg width="46" height="46" viewBox="0 0 24 24" fill="#fff"><path d="M13.5 21v-8h2.7l.4-3.2h-3.1V7.8c0-.9.3-1.5 1.6-1.5h1.6V3.4c-.3 0-1.2-.1-2.3-.1-2.3 0-3.9 1.4-3.9 4v2.5H7.8V13h2.7v8h3z"/></svg>',
       'yt':'<svg width="50" height="50" viewBox="0 0 24 24" fill="#fff"><path d="M21.6 7.2a2.5 2.5 0 0 0-1.8-1.8C18.2 5 12 5 12 5s-6.2 0-7.8.4A2.5 2.5 0 0 0 2.4 7.2C2 8.8 2 12 2 12s0 3.2.4 4.8a2.5 2.5 0 0 0 1.8 1.8C5.8 19 12 19 12 19s6.2 0 7.8-.4a2.5 2.5 0 0 0 1.8-1.8c.4-1.6.4-4.8.4-4.8s0-3.2-.4-4.8zM10 15V9l5.2 3L10 15z"/></svg>'}
s = header(34.7)
s += '<div class="abs" style="left:420px;top:230px;width:240px;height:240px;border-radius:50%;background:conic-gradient(from 210deg,#0C7F8F,#9fdde5,#0C7F8F);padding:9px;box-shadow:0 24px 60px rgba(11,34,41,.28)"><div style="width:100%;height:100%;border-radius:50%;overflow:hidden;border:7px solid #F1EEE7"><img src="a/portrait.jpg" style="width:100%;height:100%;object-fit:cover;object-position:50% 22%"></div></div>'
s += '<div class="abs" style="left:0;right:0;top:488px;display:flex;justify-content:center">'+ledword(92)+'</div>'
s += '<div class="abs handle" style="left:0;right:0;top:590px;text-align:center">@jamesframotion</div>'
s += '<div class="post" style="left:90px;top:680px;height:420px;padding:34px;transform:rotate(-1deg)">'
s += '<div style="width:640px;padding:22px 28px;border-radius:30px;background:#EEF3F3;font:500 36px Inter;color:#243f46">Hey 😍 tu fais quoi ce soir ?</div>'
s += '<div style="position:absolute;left:34px;right:34px;bottom:34px;height:112px;border-radius:60px;border:4px solid #0C7F8F;display:flex;align-items:center;padding:0 38px;font:600 40px Inter;color:#0B2229">Écris-moi…<span style="margin-left:auto;width:78px;height:78px;border-radius:50%;background:#0C7F8F;display:flex;align-items:center;justify-content:center"><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.4" stroke-linejoin="round"><path d="M22 2 11 13M22 2l-7 20-4-9-9-4 20-7z"/></svg></span></div></div>'
s += '<div class="abs" style="left:240px;top:1160px;width:600px;height:110px;border-radius:60px;background:#0C7F8F;color:#fff;font:800 44px Inter;display:flex;align-items:center;justify-content:center;gap:18px;box-shadow:0 22px 50px rgba(12,127,143,.5)">🔔 S\'abonner</div>'
s += ''.join(f'<div class="abs soc" style="left:{300+i*122}px;top:1290px;width:84px;height:84px;margin-left:-24px">{SOC[k]}</div>' for i,k in enumerate(['tt','ig','fb','yt']))
s += sub(1450, "Écris-moi en <span class='kw'>DM</span> et <span class='pk'>abonne-toi</span> !", 58)
page('B9', s)
