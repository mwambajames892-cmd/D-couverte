import pathlib
OUT = pathlib.Path.home()/'motion-design-claude-code/presentation/styleframes'

CSS = r"""
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1920px;overflow:hidden;background:#000}
:root{--accent:#F89018;--bg:#030B10;--teal:#06222a;--ink:#EAF4F4;--paper:#F1EEE7;--deep:#0B2229}
body{font-family:'Inter',sans-serif}
#stage{position:relative;width:1080px;height:1920px;overflow:hidden;background:var(--bg);color:var(--ink)}
.abs{position:absolute}
.grain{position:absolute;inset:0;pointer-events:none;opacity:.17;mix-blend-mode:overlay;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/></filter><rect width='300' height='300' filter='url(%23n)'/></svg>")}
.vig{position:absolute;inset:0;pointer-events:none;background:radial-gradient(ellipse at 50% 42%,transparent 48%,rgba(0,0,0,.6) 100%)}
.card{position:absolute;border-radius:22px;overflow:hidden;box-shadow:0 34px 90px rgba(0,0,0,.6),0 0 0 6px rgba(234,244,244,.92)}
.card img{width:100%;height:100%;object-fit:cover;display:block}
.card.acc{box-shadow:0 34px 90px rgba(0,0,0,.6),0 0 0 8px var(--accent)}
.tag{position:absolute;font:700 24px 'JetBrains Mono',monospace;letter-spacing:2px;padding:7px 14px;border-radius:9px;background:rgba(3,11,16,.88);color:var(--ink)}
.tag .rec{display:inline-block;width:16px;height:16px;border-radius:50%;background:#ff3b30;margin-right:10px;vertical-align:-1px}
.sub{position:absolute;left:70px;width:940px;text-align:center;font-weight:800;font-size:64px;line-height:1.2;letter-spacing:-.5px;color:#fff;text-shadow:0 4px 24px rgba(0,0,0,.65)}
.sub .kw{background:var(--accent);color:#04141a;padding:0 16px;border-radius:12px;box-decoration-break:clone;-webkit-box-decoration-break:clone;text-shadow:none}
.sub .pk{position:relative;white-space:nowrap}
.sub .pk::after{content:'';position:absolute;left:-6px;right:-6px;bottom:-14px;height:9px;background:var(--accent);border-radius:9px;transform:rotate(-1.4deg)}
.light .sub{color:var(--deep);text-shadow:none}
.led{font-family:'JetBrains Mono',monospace;font-weight:800;color:transparent;-webkit-background-clip:text;background-clip:text;background-image:radial-gradient(circle at 50% 50%,var(--dot,#fff) 0 2.3px,transparent 2.9px);background-size:6.4px 6.4px;line-height:1;white-space:nowrap;position:relative;display:inline-block}
.led .o{position:relative;display:inline-block}
.led .o::after{content:'';position:absolute;left:50%;top:-4%;width:.1em;height:1.12em;margin-left:-.05em;background:var(--accent);transform:rotate(28deg);border-radius:4px;box-shadow:0 0 22px rgba(248,144,24,.7)}
.wm-top{font:700 38px 'Inter';letter-spacing:.62em;margin-right:-.62em;text-align:center;color:var(--ink)}
.handle{font:500 32px 'JetBrains Mono',monospace;color:#7fa3a8;letter-spacing:1px}
.rule{position:absolute;left:0;right:0;height:2px;background:linear-gradient(90deg,transparent,rgba(31,150,170,.9),transparent)}
.ph{position:absolute;top:150px;bottom:570px;width:4px;background:var(--accent);box-shadow:0 0 24px rgba(248,144,24,.8)}
.ph::before{content:'';position:absolute;top:-22px;left:-14px;border-left:16px solid transparent;border-right:16px solid transparent;border-top:24px solid var(--accent)}
.tick{position:absolute;width:2px;background:rgba(160,200,205,.35)}
.tlab{position:absolute;font:600 20px 'JetBrains Mono',monospace;color:rgba(160,200,205,.6)}
.clip{position:absolute;height:62px;border-radius:10px;border:2px solid rgba(255,255,255,.25)}
.notif{position:absolute;width:900px;height:190px;border-radius:40px;background:rgba(244,250,250,.97);color:#0B2229;box-shadow:0 30px 70px rgba(0,0,0,.45);display:flex;align-items:center;padding:0 36px;gap:30px}
.notif .av{width:116px;height:116px;border-radius:50%;background:linear-gradient(135deg,#ff9a56,#ff4f81);display:flex;align-items:center;justify-content:center;font-size:62px;flex:none}
.notif .t1{font:800 42px 'Inter'}
.notif .t1 small{font:500 28px 'Inter';color:#6b8288;margin-left:10px}
.notif .t2{font:500 38px 'Inter';margin-top:6px;color:#243f46}
.notif .dot{width:26px;height:26px;border-radius:50%;background:#0a84ff;margin-left:auto;flex:none}
"""

def page(name, body, theme='', extra_css=''):
    html = ('<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=1080,height=1920">'
            f'<title>{name}</title><style>{CSS}{extra_css}</style></head><body><div id="stage" class="{theme}">{body}'
            '<div class="grain"></div></div></body></html>')
    (OUT/f'{name}.html').write_text(html, encoding='utf-8')

def ruler(x0=0, x1=1080, y=190, step=36, start=0):
    s = ''
    for i, x in enumerate(range(x0, x1, step)):
        big = i % 5 == 0
        s += f'<div class="tick" style="left:{x}px;top:{y-(30 if big else 16)}px;height:{30 if big else 16}px"></div>'
        if big:
            s += f'<div class="tlab" style="left:{x+8}px;top:{y-34}px">00:{(start+i//5)*1:02d}</div>'
    return s

def ledword(size=128, dot='#EAF4F4'):
    return f'<div class="led" style="font-size:{size}px;--dot:{dot}">FRAM<span class="o">O</span>TION</div>'

def sub(top, html, extra=''):
    return f'<div class="sub" style="top:{top}px;{extra}">{html}</div>'
