import pathlib
OUT = pathlib.Path.home()/'motion-design-claude-code/presentation/styleframes'
T='#0C7F8F'      # vert-bleu (remplace tout l'orange)
TD='#0B5560'; TL='#CFE7EA'; INK='#0B2229'; PAPER='#F1EEE7'
CSS = r"""
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1920px;overflow:hidden;background:#F1EEE7}
body{font-family:'Inter',sans-serif}
#stage{position:relative;width:1080px;height:1920px;overflow:hidden;background:radial-gradient(ellipse at 50% 30%,#FBF9F4 0%,#F1EEE7 55%,#E4DFD3 100%);color:#0B2229}
.abs{position:absolute}
.grain{position:absolute;inset:0;pointer-events:none;opacity:.14;mix-blend-mode:multiply;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/></filter><rect width='300' height='300' filter='url(%23n)'/></svg>")}
.vig{position:absolute;inset:0;pointer-events:none;background:radial-gradient(ellipse at 50% 42%,transparent 55%,rgba(11,34,41,.14) 100%)}
.sub{position:absolute;left:60px;width:960px;text-align:center;font-weight:800;font-size:64px;line-height:1.2;letter-spacing:-.5px;color:#0B2229}
.sub .kw{background:#0C7F8F;color:#fff;padding:0 16px;border-radius:12px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.sub .pk{position:relative;white-space:nowrap}
.sub .pk::after{content:'';position:absolute;left:-6px;right:-6px;bottom:-14px;height:9px;background:#0C7F8F;border-radius:9px;transform:rotate(-1.4deg)}
/* règle de temps = barres de story : la tête de lecture avance avec la voix */
.tick{position:absolute;width:2px;background:rgba(11,34,41,.28)}
.tlab{position:absolute;font:600 19px 'JetBrains Mono',monospace;color:rgba(11,34,41,.5)}
.trk{position:absolute;left:70px;width:940px;top:176px;height:8px;border-radius:5px;background:#D9E4E4}
.trf{position:absolute;left:70px;top:176px;height:8px;border-radius:5px;background:#0C7F8F}
.ph{position:absolute;top:96px;height:104px;width:4px;background:#0C7F8F;margin-left:-2px;box-shadow:0 0 18px rgba(12,127,143,.6)}
.ph::before{content:'';position:absolute;top:-6px;left:-12px;border-left:14px solid transparent;border-right:14px solid transparent;border-top:20px solid #0C7F8F}
.tc{position:absolute;top:56px;font:800 24px 'JetBrains Mono',monospace;color:#fff;background:#0C7F8F;padding:5px 12px;border-radius:8px;transform:translateX(-50%)}
.post{position:absolute;width:900px;background:#fff;border-radius:44px;box-shadow:0 40px 90px rgba(11,34,41,.22),0 0 0 2px rgba(11,34,41,.06);padding:34px}
.post .hd{display:flex;align-items:center;gap:22px;height:92px}
.post .av{width:84px;height:84px;border-radius:50%;background:conic-gradient(from 200deg,#0C7F8F,#7fd0da,#0C7F8F);padding:5px;flex:none}
.post .av i{display:block;width:100%;height:100%;border-radius:50%;background:#0B2229}
.post .nm{font:800 34px Inter;color:#0B2229}.post .nm small{display:block;font:500 26px Inter;color:#78898d;margin-top:2px}
.post .media{position:relative;height:560px;border-radius:28px;overflow:hidden;margin-top:6px}
.post .media img{width:100%;height:100%;object-fit:cover;display:block}
.post .acts{display:flex;gap:34px;margin-top:26px;align-items:center}
.post .bar{height:22px;border-radius:12px;background:#E8E4DA;margin-top:16px}
.chip{position:absolute;font:700 24px 'JetBrains Mono',monospace;letter-spacing:2px;color:#fff;background:#0C7F8F;padding:7px 14px;border-radius:9px;white-space:nowrap}
.mini{position:absolute;border-radius:26px;overflow:hidden;background:#fff;box-shadow:0 26px 60px rgba(11,34,41,.28),0 0 0 6px #fff}
.mini img{width:100%;height:100%;object-fit:cover;display:block}
.notif{position:absolute;width:930px;height:200px;border-radius:44px;background:#0B2229;color:#fff;box-shadow:0 34px 80px rgba(11,34,41,.45);display:flex;align-items:center;padding:0 38px;gap:30px}
.notif .av{width:124px;height:124px;border-radius:50%;background:linear-gradient(135deg,#27b2c4,#0B5560);display:flex;align-items:center;justify-content:center;font-size:66px;flex:none}
.notif .t1{font:800 44px Inter}.notif .t1 small{font:500 28px Inter;color:#9fb6ba;margin-left:10px}
.notif .t2{font:500 40px Inter;margin-top:6px;color:#dfeced}.notif .dot{width:28px;height:28px;border-radius:50%;background:#27b2c4;margin-left:auto;flex:none}
.led{font-family:'JetBrains Mono',monospace;font-weight:800;color:transparent;-webkit-background-clip:text;background-clip:text;background-image:radial-gradient(circle at 50% 50%,#0B2229 0 2.3px,transparent 2.9px);background-size:6.4px 6.4px;line-height:1;white-space:nowrap;position:relative;display:inline-block}
.led .o{position:relative;display:inline-block}
.led .o::after{content:'';position:absolute;left:50%;top:-4%;width:.1em;height:1.12em;margin-left:-.05em;background:#0C7F8F;transform:rotate(28deg);border-radius:4px;box-shadow:0 0 22px rgba(12,127,143,.55)}
.wm-top{font:700 38px 'Inter';letter-spacing:.62em;margin-right:-.62em;text-align:center;color:#0B2229}
.handle{font:500 32px 'JetBrains Mono',monospace;color:#4f7077;letter-spacing:1px}
.ico{display:inline-block}
.clipb{position:absolute;height:56px;border-radius:10px;color:#fff;font:700 20px 'JetBrains Mono',monospace;letter-spacing:1px;display:flex;align-items:center;padding:0 14px;white-space:nowrap;box-shadow:inset 0 0 0 2px rgba(255,255,255,.25)}
.pill{display:inline-block;font:800 26px Inter;padding:9px 20px;border-radius:30px;background:#E7F1F2;color:#0B5560;margin-right:12px}
.tile{position:absolute;width:205px;height:205px;border-radius:22px;overflow:hidden;box-shadow:0 0 0 4px #fff,0 14px 30px rgba(11,34,41,.2)}
.tile img{width:100%;height:100%;object-fit:cover;display:block}
.tl{position:absolute;width:205px;text-align:center;font:700 21px 'JetBrains Mono',monospace;letter-spacing:.5px;color:#0B2229}
.soc{width:96px;height:96px;border-radius:50%;background:#0B2229;display:flex;align-items:center;justify-content:center}
"""
def page(name, body):
    (OUT/f'{name}.html').write_text('<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=1080,height=1920">'
        f'<title>{name}</title><style>{CSS}</style></head><body><div id="stage">{body}<div class="vig"></div><div class="grain"></div></div></body></html>', encoding='utf-8')

def header(t, total=36.7, ruler_label=True):
    x = 70 + 940*t/total
    s = f'<div class="trk"></div><div class="trf" style="width:{x-70:.0f}px"></div>'
    for sec in range(0, 37):
        px = 70 + 940*sec/total
        big = sec % 5 == 0
        s += f'<div class="tick" style="left:{px:.0f}px;top:{176-(26 if big else 14)}px;height:{26 if big else 14}px"></div>'
        if big and sec: s += f'<div class="tlab" style="left:{px+6:.0f}px;top:{118}px">00:{sec:02d}</div>'
    s += f'<div class="ph" style="left:{x:.0f}px"></div><div class="tc" style="left:{x:.0f}px">00:{int(t):02d}</div>'
    return s

def sub(top, html, size=64): return f'<div class="sub" style="top:{top}px;font-size:{size}px;white-space:nowrap">{html}</div>'
def ledword(size=128): return f'<div class="led" style="font-size:{size}px">FRAM<span class="o">O</span>TION</div>'
HEART='<svg class="ico" width="58" height="58" viewBox="0 0 24 24" fill="none" stroke="#0B2229" stroke-width="2" stroke-linejoin="round"><path d="M12 21s-7.5-4.6-9.6-9.2C.9 8.4 2.6 4.5 6.4 4.5c2.2 0 3.7 1.2 5.6 3.3 1.9-2.1 3.4-3.3 5.6-3.3 3.8 0 5.5 3.9 4 7.3C19.5 16.4 12 21 12 21z"/></svg>'
COMM='<svg class="ico" width="58" height="58" viewBox="0 0 24 24" fill="none" stroke="#0B2229" stroke-width="2" stroke-linejoin="round"><path d="M21 11.5a8.5 8.5 0 0 1-12.4 7.5L3 20.5l1.6-5.2A8.5 8.5 0 1 1 21 11.5z"/></svg>'
SEND='<svg class="ico" width="58" height="58" viewBox="0 0 24 24" fill="none" stroke="#0B2229" stroke-width="2" stroke-linejoin="round"><path d="M22 2 11 13M22 2l-7 20-4-9-9-4 20-7z"/></svg>'

def post(left, top, img, name, style='', bars=True):
    b = '<div class="bar" style="width:92%"></div><div class="bar" style="width:62%"></div>' if bars else ''
    return (f'<div class="post" style="left:{left}px;top:{top}px;{style}"><div class="hd"><div class="av"><i></i></div><div class="nm">{name}<small>à l\'instant</small></div></div>'
            f'<div class="media"><img src="a/{img}"></div><div class="acts">{HEART}{COMM}{SEND}</div>{b}</div>')
def video_bar(top, pct, rot=1):
    return (f'<div class="abs" style="left:150px;top:{top}px;width:780px;height:12px;border-radius:7px;background:rgba(255,255,255,.55);transform:rotate({rot}deg)"></div>'
            f'<div class="abs" style="left:150px;top:{top}px;width:{780*pct/100:.0f}px;height:12px;border-radius:7px;background:#0C7F8F;transform:rotate({rot}deg);box-shadow:0 0 14px rgba(12,127,143,.7)"></div>')
def notif(left, top, rot=-2, extra='', msg='Hey 😍 tu fais quoi ce soir ?'):
    return f'<div class="notif" style="left:{left}px;top:{top}px;transform:rotate({rot}deg);{extra}"><div class="av">❤️</div><div><div class="t1">Crush<small>à l\'instant</small></div><div class="t2">{msg}</div></div><div class="dot"></div></div>'
def peek(img, name): return post(150, 1640, img, name, 'transform:scale(.9);filter:blur(7px);opacity:.75')
